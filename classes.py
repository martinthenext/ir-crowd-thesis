from data import texts_vote_lists_truths_by_topic_id
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from itertools import ifilter, izip, product
from plots import plot_hist
import codecs
import sys

sys.stdout = codecs.getwriter('utf-8')(sys.__stdout__)

def get_inner_and_outer_similarities(topic_id):
  texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[topic_id]
  vectorizer = TfidfVectorizer()
  vectorizer.fit(texts)

  # Take only documents with ground truth
  golden_texts_truths = ifilter(lambda (t, r): r is not None, izip(texts, truths) )
  # Split them into sets of relevant and irrelevant documents
  relevant_texts, irrelevant_texts = [], []
  for text, is_relevant in golden_texts_truths:
    if is_relevant:
      relevant_texts.append(text)
    else:
      irrelevant_texts.append(text)

  relevant_vectors = vectorizer.transform(relevant_texts)
  inner_similarity = cosine_similarity(relevant_vectors)

  # Go through the similarities and print pairs of text who are between 0.95 and 1 in similarity
  # In relevant texts
  sys.stdout.write('%s\n' % topic_id)
  n_documents = len(relevant_texts)
  for i in xrange(n_documents):
    for j in xrange(n_documents):
      sim = inner_similarity[i, j]
      print sim
      print sim != 1
      if (sim > 0.95):
        if not np.isclose(sim, 1.0):
          print 'SIMILARITY NOT 1'
          print sim
          sys.stdout.write('\n\nSIMILARITY - %0.32f\n' % sim)
          sys.stdout.write('=========TEXT1==========\n')
          sys.stdout.write(relevant_texts[i])
          sys.stdout.write('=========TEXT2==========\n')
          sys.stdout.write(relevant_texts[j])
          sys.stdout.write('EQUAL\n')
          sys.stdout.write(str(relevant_texts[j]==relevant_texts[i]))

  return 

inner_outer_tuples_accross_topics = [get_inner_and_outer_similarities(topic) for topic 
  in texts_vote_lists_truths_by_topic_id.keys()]
