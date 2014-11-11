from data import texts_vote_lists_truths_by_topic_id
import numpy as np
from itertools import izip, ifilter

TOPIC_ID = '20690'

def get_accuracy(estimate_list, list_with_Nones):
  """ 
  This gets boolean lists of estimates and truths with corresponding
  positions and returns a fraction of matching items
  """
  pairs = izip(estimate_list, list_with_Nones)
  pairs_without_Nones = ifilter(lambda x: x[1] is not None, pairs)
  matching = [x == y for (x, y) in pairs_without_Nones]
  return np.mean(matching)

def get_majority_vote(vote_list):
  """
  Get a boolean relevance estimate for a document given
  a list of votes with majority voting

  """
  return np.mean(vote_list) > 0.5

texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[TOPIC_ID]
print 'document #11'
print 'text:' + repr(texts[11])[:100]
print 'votes:' + repr(vote_lists[11])
print 'truth:' + repr(truths[11])

# Firthermore we only work with votes and truths, sampling votes, updating 
# majority vote estimates and measuring therir accuracy w.r.t. truths

estimates = [get_majority_vote(vote_list) for vote_list in vote_lists]
print get_accuracy(estimates, truths)



"""
for iteration in max_iterations:
  sample vote
  update estimates
  compare estimates with truths

"""