from itertools import izip, imap, chain
from collections import defaultdict
import operator
import numpy as np
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib

JUDGEMENT_FILE = '/local/martin/data/all_judgements.txt'
FULLTEXT_FOLDER = '/local/martin/data/url-header-html-txt'
GROUND_TRUTH_FILE = '/local/martin/data/task1_unlabeled_g_truth_cons_public.csv'

class JudgementRecord(object):
  def __init__(self, table_row):
    attributes = table_row.split('\t')
    team_id, worker_id, _, topic_id, doc_id, _, relevance, _, _, _, label_type = attributes
    self.team_id = team_id
    self.worker_id = worker_id
    self.label_type = int(label_type)
    self.topic_id = topic_id
    self.doc_id = doc_id
    if not relevance=='na':
      self.is_relevant = (float(relevance) >= 0.5) 
    else:
      self.is_relevant = None
    

# First read off ground truth so we can look it up afterwards
truth_by_topic_id_and_doc_id = {}

with io.open(GROUND_TRUTH_FILE, 'r', encoding='utf-8') as f:
  headers = f.readline()
  for line in f:
    cols = line[:-1].split("\t")
    topic_id = cols[1]
    doc_id = cols[2]
    truth = float(cols[3]) / 2
    if truth < 0:
      truth = None
    truth_by_topic_id_and_doc_id[(topic_id, doc_id)] = truth


with io.open(JUDGEMENT_FILE, 'r', encoding='utf-8') as f:
  judgement_records = [JudgementRecord(line[:-1]) for line in f]
  is_useful = lambda j: (j.label_type == 0) and (j.is_relevant is not None)
  judgements = filter(is_useful, judgement_records)

# Grouping judgements by topic
judgements_by_topic_id = defaultdict(list)
for judgement in judgements:
  judgements_by_topic_id[judgement.topic_id].append(judgement)


# For every topic get: list of document texts, list of their mean relevances
topic_texts_relevances_variances_truths = []
min_judgements_per_document = []

for topic_id, judgements in judgements_by_topic_id.iteritems():
  # Grouping judgements by document inside a topic

  judgements_by_doc_id = defaultdict(list)
  for judgement in judgements:
    judgements_by_doc_id[judgement.doc_id].append(judgement)

  # We now have a particular indexing of documents: judgements_by_doc_id.keys()

  # Get full texts of documents
  document_texts = []
  for doc_id in judgements_by_doc_id.keys():
    # this doc is in <topic_id>/<doc_id>.txt file
    filename = "%s/%s/%s.txt" % (FULLTEXT_FOLDER, topic_id, doc_id)

    with io.open(filename, 'r', encoding='utf-8') as f:
      document_texts.append(f.read())

  # For every document compute the relevance
  mean_relevances = np.zeros(len(judgements_by_doc_id))
  var_relevances = np.zeros(len(judgements_by_doc_id))
  count_relevances = np.zeros(len(judgements_by_doc_id))


  for index, doc_id in enumerate(judgements_by_doc_id.keys()):
    doc_relevances = [j.is_relevant for j in judgements_by_doc_id[doc_id]]
    mean_relevances[index] = np.mean(doc_relevances)
    var_relevances[index] = np.var(doc_relevances)
    count_relevances[index] = len(judgements_by_doc_id[doc_id])

  # Computing pooled variance
  weigted_sum = sum([(n - 1) * s for n, s in izip(count_relevances, var_relevances)])
  denominator = sum(count_relevances) - len(count_relevances)
  pooled_variance = float(weigted_sum) / float(denominator)

  # Computing minimum amount of relevance judgements per document
  min_judgements_per_document.append(min(count_relevances))

  # Gettings ground truth for all the documents
  truths = np.array([truth_by_topic_id_and_doc_id[(topic_id, doc_id)] \
    for doc_id in judgements_by_doc_id.keys()])

  # DATA
  topic_texts_relevances_variances_truths.append(
   (topic_id, document_texts, mean_relevances, pooled_variance, truths) 
  )

# Get a list of all texts
all_texts_iter = imap(operator.itemgetter(1), topic_texts_relevances_variances_truths)
all_texts_iter = chain.from_iterable(all_texts_iter)

# Get a TF-IDF dictionary from all the documents across different topics
vectorizer = TfidfVectorizer()
vectorizer.fit(all_texts_iter)

# Printing the min judgements per document statistic
print "topic|min judgements per document"
print "-----|------"
for topic_id_count_pair in izip(judgements_by_topic_id.keys(), min_judgements_per_document):
  print "%s|%s" % topic_id_count_pair
print "global|%s" % min(min_judgements_per_document)
