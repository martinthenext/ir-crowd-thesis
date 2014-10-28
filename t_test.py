from data import topic_texts_relevances_variances, vectorizer
from itertools import izip
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import ttest_ind
import numpy as np

# Separate relevant documents from irrelevant
for topic_id, texts, relevances, pooled_variance in topic_texts_relevances_variances:
  relevant_texts = []
  irrelevant_texts = []
  for text, relevance in izip(texts, relevances):
    if relevance > 0.5:
      relevant_texts.append(text)
    else:
      irrelevant_texts.append(text)

  relevant_vectorized = vectorizer.transform(relevant_texts)
  irrelevant_vectorized = vectorizer.transform(irrelevant_texts)

  inner_similarity = cosine_similarity(relevant_vectorized)
  outer_similarity = cosine_similarity(relevant_vectorized, irrelevant_vectorized)

  t_test_p_value = ttest_ind(inner_similarity.flatten(), outer_similarity.flatten(), equal_var=False)[1]

  print "%s|%0.2f|%0.2f|%0.2f|%0.2f|%s|%0.e|%0.3f|" % (
    topic_id,
    np.mean(inner_similarity.flatten()),
    np.mean(outer_similarity.flatten()),
    np.std(inner_similarity.flatten()),
    np.std(outer_similarity.flatten()),
    len(texts),
    t_test_p_value,
    pooled_variance,
  )
