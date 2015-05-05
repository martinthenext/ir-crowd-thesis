"""

Run one accuracy sequence to a certain point, then run an estimator

"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from oneaccuracy import get_last_accuracy_in_sequence
from experiments import est_gp
from data import texts_vote_lists_truths_by_topic_id

def run_estimator_once(estimator, args, topic_id, max_votes_per_doc):
  texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[topic_id]
  n_documents = len(texts)

  vectorizer = TfidfVectorizer()
  X = vectorizer.fit_transform(texts)
  text_similarity = cosine_similarity(X)

  sequence_length = int(max_votes_per_doc * n_documents)

  get_last_accuracy_in_sequence(estimator, sequence_length, texts, vote_lists, truths, X, text_similarity, None, False, *args)

run_estimator_once(est_gp, [ None ], '20910', 1)

