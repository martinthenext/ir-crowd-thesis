from data import texts_vote_lists_truths_by_topic_id
import numpy as np
from itertools import izip, ifilter
from copy import deepcopy
import random
from plots import plot_learning_curve
from scipy.stats import nanmean

def get_accuracy(estimates, truths):
  """ 
  This gets boolean lists of estimates and truths with corresponding
  positions and returns a fraction of matching items

  If any of the pair (estimate, truth) is None, it is disregarded
  """
  pairs = izip(estimates, truths)
  pairs_without_Nones = ifilter(lambda x: None not in x, pairs)
  matching = [x == y for (x, y) in pairs_without_Nones]
  if not matching:
    return None
  else:
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


def get_accuracy_sequence(n_votes_to_sample, vote_lists, truths):
  """ Randomly sample votes and re-calculate estimates
  """
  unknown_votes = copy_and_shuffle_sublists(vote_lists)
  known_votes = [ [] for _ in unknown_votes ]

  estimates = [None for _ in vote_lists]

  accuracy_sequence = [None] * n_votes_to_sample

  for index in xrange(n_votes_to_sample):
    # Draw one vote for a random document
    updated_doc_idx = random.randrange(len(vote_lists))
    if not unknown_votes[updated_doc_idx]:
      # We ran out of votes for this document, diregard this sequence
      return None
    vote = unknown_votes[updated_doc_idx].pop()
    known_votes[updated_doc_idx].append(vote)
    # Recalculate the estimate on the affected document
    estimates[updated_doc_idx] = get_majority_vote(known_votes[updated_doc_idx])
    # Calucate the accuracy_sequence
    accuracy_sequence[index] = get_accuracy(estimates, truths)

  return accuracy_sequence


def plot_learning_curve_for_topic(topic_id, n_runs, votes_per_doc=(1,10)):
  texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[topic_id]
  n_documents = len(texts)

  estimates = [get_majority_vote(vote_list) for vote_list in vote_lists]
  max_accuracy = get_accuracy(estimates, truths)

  min_votes_per_doc, max_votes_per_doc = votes_per_doc

  start_idx, stop_idx = min_votes_per_doc * n_documents, max_votes_per_doc * n_documents
  votes_per_document = np.arange(float(start_idx), float(stop_idx)) / n_documents
  sequences = []

  for _ in xrange(n_runs):
    sequence = get_accuracy_sequence(stop_idx, vote_lists, truths, n_strict=False)
    if sequence:
      sequences.append(np.array(sequence[start_idx:]))

  results = np.vstack(sequences)

  x = votes_per_document
  y = nanmean(results, axis=0)

  plot_learning_curve('Learning curve for majority voting, topic %s, %s runs' % (topic_id, n_runs), 
    x, y, 'Votes per document', 'Accuracy', baseline=max_accuracy)

# TODO votes per doc can only be int

plot_learning_curve_for_topic('20812', 10000, votes_per_doc=(1, 10))
