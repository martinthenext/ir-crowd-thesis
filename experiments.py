from data import texts_vote_lists_truths_by_topic_id
import numpy as np
from itertools import izip, ifilter
from copy import deepcopy
import random

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

def copy_and_shuffle_sublists(list_of_lists):
  """ Get a copy with all lists shuffled
  Use this to draw 'random' votes with .pop()
  """
  result = []
  for l in list_of_lists:
    new_list = deepcopy(l)
    random.shuffle(new_list)
    result.append(new_list)

  return result

texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[TOPIC_ID]

# Firthermore we only work with votes and truths, sampling votes, updating 
# majority vote estimates and measuring therir accuracy w.r.t. truths

estimates = [get_majority_vote(vote_list) for vote_list in vote_lists]
print get_accuracy(estimates, truths)

def get_accuracy_sequence(n_votes_to_sample, vote_lists, truths):
  """ Randomly sample votes 
  """
  unknown_votes = deepcopy(vote_lists)
  known_votes = []

  accuracy_sequence = np.zeros(n_votes_to_sample)
  for index in xrange(n_votes_to_sample):
    # draw one vote for a random document
    pass

"""
for iteration in max_iterations:
  sample vote
  update estimates
  compare estimates with truths

"""