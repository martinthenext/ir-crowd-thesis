from data import texts_vote_lists_truths_by_topic_id
import numpy as np
from itertools import izip, ifilter
from copy import deepcopy
import random
from plots import plot_to_file

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


def get_accuracy_sequence(n_votes_to_sample, vote_lists, truths, n_strict=True):
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
      # We ran out of votes for this document, stop sequencing
      if n_strict:
        return None
      else:
        continue
    vote = unknown_votes[updated_doc_idx].pop()
    known_votes[updated_doc_idx].append(vote)
    # Recalculate the estimate on the affected document
    estimates[updated_doc_idx] = get_majority_vote(known_votes[updated_doc_idx])
    # Calucate the accuracy_sequence
    accuracy_sequence[index] = get_accuracy(estimates, truths)

  return accuracy_sequence

TOPIC_ID = '20690'

texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[TOPIC_ID]
n_documents = len(texts)

# Firthermore we only work with votes and truths, sampling votes, updating 
# majority vote estimates and measuring therir accuracy w.r.t. truths

estimates = [get_majority_vote(vote_list) for vote_list in vote_lists]
print get_accuracy(estimates, truths)

#TODO: take care of cases when the beginning of sequence is Nones

n_runs = 10000
min_votes_per_doc = 1
max_votes_per_doc = 10

start_idx, stop_idx = min_votes_per_doc * n_documents, max_votes_per_doc * n_documents
votes_per_document = np.arange(float(start_idx), float(stop_idx)) / n_documents
sequences = []

for _ in xrange(n_runs):
  sequence = get_accuracy_sequence(stop_idx, vote_lists, truths)
  if sequence:
    sequences.append(np.array(sequence[start_idx:]))

results = np.vstack(sequences)

x = votes_per_document
y = np.mean(results, axis=0)

plot_to_file('Learning curve, 10000 runs', x, y, 'Votes per document', 'Accuracy')
