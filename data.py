from itertools import izip, imap, chain
from collections import defaultdict
import operator
import numpy as np
import io
from sklearn.externals import joblib
import os


DATA_ROOT = os.getenv("HOME") + '/data/'
JUDGEMENT_FILE = DATA_ROOT + 'all_judgements.txt'
FULLTEXT_FOLDER = DATA_ROOT + 'url-header-html-txt'
GROUND_TRUTH_FILE = DATA_ROOT + 'task1_unlabeled_g_truth_cons_public.csv'


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
    else:
      truth = bool(truth)
    truth_by_topic_id_and_doc_id[(topic_id, doc_id)] = truth


with io.open(JUDGEMENT_FILE, 'r', encoding='utf-8') as f:
  judgement_records = [JudgementRecord(line[:-1]) for line in f]
  is_useful = lambda j: (j.label_type == 0) and (j.is_relevant is not None)
  judgements = filter(is_useful, judgement_records)

# Grouping judgements by topic
judgements_by_topic_id = defaultdict(list)
for judgement in judgements:
  judgements_by_topic_id[judgement.topic_id].append(judgement)

texts_vote_lists_truths_by_topic_id = {}

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

  vote_lists = [ [j.is_relevant for j in judgements_by_doc_id[doc_id]]
    for doc_id in judgements_by_doc_id.keys() ]

  # Gettings ground truth for all the documents
  truths = [truth_by_topic_id_and_doc_id[(topic_id, doc_id)] \
    for doc_id in judgements_by_doc_id.keys()]

  texts_vote_lists_truths_by_topic_id[topic_id] = (document_texts, vote_lists, truths)
  

if __name__ == "__main__":
  # Print a list of topic ids
  topic_id_list = '(' + ' '.join(texts_vote_lists_truths_by_topic_id.keys()) + ')'
  print topic_id_list

