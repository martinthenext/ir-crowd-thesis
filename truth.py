"""

Compare people's votes with ground truth

"""

from data import topic_texts_relevances_variances_truths, vectorizer
import numpy as np
from itertools import izip, ifilter

def get_differences(list, list_with_Nones):
  pairs = izip(list, list_with_Nones)
  pairs_without_Nones = ifilter(lambda x: x[1] is not None, pairs)
  differences = [x - y for (x, y) in pairs_without_Nones]  
  return differences

def get_mean_difference(list, list_with_Nones):
  return np.mean(differences)

for topic_id, _, relevances, _, truths in topic_texts_relevances_variances_truths:
  diff = get_differences(relevances, truths)
  print '%s|%0.2f' % (topic_id, np.mean(diff))
