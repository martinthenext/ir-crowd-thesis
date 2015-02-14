""" This script writes one random accuracy sequence for an estimator to standard output
    in a string form delimited by commas
"""
from experiments import get_accuracy_sequence, est_gp, est_merge_enough_votes, est_majority_vote
from data import texts_vote_lists_truths_by_topic_id
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import codecs
import sys


if __name__ == "__main__":
  sys.stdout = codecs.getwriter('utf-8')(sys.__stdout__)

  # Parameters
  topic_id = '20780'
  estimator, args = est_gp, [ 1 ]
#  estimator, args = est_majority_vote, []
  votes_per_doc = (1, 5)


  # Loading and processing input data
  # TODO unify this part with experiments.py and get rid of imports
  texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[topic_id]
  n_documents = len(texts)

  vectorizer = TfidfVectorizer()
  X = vectorizer.fit_transform(texts)
  text_similarity = cosine_similarity(X)

  min_votes_per_doc, max_votes_per_doc = votes_per_doc
  start_idx, stop_idx = min_votes_per_doc * n_documents, max_votes_per_doc * n_documents

  sequence = get_accuracy_sequence(estimator, stop_idx, texts, vote_lists, truths,
    X, text_similarity, *args)

  if sequence:
    sys.stdout.write(",".join([str(x) for x in sequence]) + '\n')
