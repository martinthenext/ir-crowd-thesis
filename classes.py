from data import texts_vote_lists_truths_by_topic_id
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from itertools import ifilter, izip
from plots import plot_hist_combined

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
  irrelevant_vectors = vectorizer.transform(irrelevant_texts)

  inner_similarity = cosine_similarity(relevant_vectors).flatten()
  outer_similarity = cosine_similarity(relevant_vectors, irrelevant_vectors).flatten()

  # We are not interested in similarities of a document with itself
  inner_similarity_non_reflexive = inner_similarity[inner_similarity < 1.0]
  return inner_similarity_non_reflexive, outer_similarity

inner_outer_tuples_accross_topics = [get_inner_and_outer_similarities(topic) for topic 
  in texts_vote_lists_truths_by_topic_id.keys()]
inner_sets_by_topic, outer_sets_by_topic = zip(*inner_outer_tuples_accross_topics)

inner_all, outer_all = np.concatenate(inner_sets_by_topic), np.concatenate(outer_sets_by_topic)

np.savetxt("inner.csv", inner_all, fmt="%0.4f", delimiter=",")
np.savetxt("outer.csv", outer_all, fmt="%0.4f", delimiter=",")
