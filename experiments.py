from data import texts_vote_lists_truths_by_topic_id
import numpy as np
from itertools import izip, ifilter, chain, imap
import random
from plots import plot_learning_curve, plot_lines
from scipy.stats import nanmean
from sklearn.externals.joblib import Parallel, delayed
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import datetime
from scipy.stats import ttest_ind
import sys
from scipy.special import logit, expit
from sklearn import gaussian_process
import gc
from scipy import sparse, io
import subprocess
import datetime
import shutil


N_CORES = 1
MATLAB_TEMP_DIR = '/scratch/' # Local scratch folder that gets deleted automatically when the job is done


def get_accuracy(estimates, truths):
  """ 
  This gets boolean lists of estimates and truths with corresponding
  positions and returns a fraction of matching items

  If any of the pair (estimate, truth) is None, it is disregarded

  Symmetric w.r.t. argument order
  """
  pairs = izip(estimates, truths)
  pairs_without_Nones = ifilter(lambda x: None not in x, pairs)
  matching = [x == y for (x, y) in pairs_without_Nones]
  if not matching:
    return None
  else:
    return np.mean(matching)


unit_to_bool_random = lambda x: random.choice([True, False]) if (x == 0.5 or x is None) else (x > 0.5)

get_mean_vote = lambda vote_list: np.mean(vote_list) if vote_list else None


def p_majority_vote(texts, vote_lists):
  """ This is how all confidence functions should look like
      Return value in [0, 1] means certainty in document's relevance
  """
  return imap(get_mean_vote, vote_lists)


def est_majority_vote(texts, vote_lists, X, text_similarity):
  """ This is how all estimator functions should look like
  """
  return ( unit_to_bool_random(conf) for conf in p_majority_vote(texts, vote_lists) )


def copy_and_shuffle_sublists(list_of_lists):
  """ Get a copy with all lists shuffled
  Use this to draw 'random' votes with .pop()
  """
  return [sorted(l, key=lambda x: random.random()) for l in list_of_lists]


def get_accuracy_sequence(estimator, n_votes_to_sample, texts, 
  vote_lists, truths, X, text_similarity, idx=None, return_final=False, *args):
  """ Randomly sample votes and re-calculate estimates.
  """
  random.seed() # This is using system time

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
    
    # Recalculate all the estimates for the sake of consistency
    estimates = estimator(texts, known_votes, X, text_similarity, *args)

    # Calucate the accuracy_sequence
    accuracy_sequence[index] = get_accuracy(estimates, truths)

  return accuracy_sequence


def get_indexes_of_sublists_smaller_than(length, list_of_lists):
  """
  >>> get_indexes_of_sublists_smaller_than(4, [[1,1], [2,2,2,2], [3,3,3]])
  [0, 2]
  """
  return [index for index, element in enumerate(list_of_lists) if len(element) < length]


def boolean_slice(l, take_bool):
  """
  >>> boolean_slice(range(5), [False, False, False, False, True])
  [4]
  >>> boolean_slice(['a','b','c','d','e'], [False, True, False, False, True])
  ['b', 'e']
  """
  return [el for el, take in zip(l, take_bool) if take]


def get_indexes_with_neighborhood_votes_less_than(votes_required, vote_lists, 
  text_similarity, sufficient_similarity):
  """ For every document, if all documents which are closer than sufficient_similarity
      have cumulatively less than votes_required votes, it's index is added to resulting list
  """
  result_idx = []
  for idx in xrange(len(vote_lists)):
    if len(vote_lists[idx]) < votes_required:
      # Join votes of all documents closer than sufficient_similarity and see if it's enough
      similarities = text_similarity[:, idx]
      similarities[idx] = 0.0
      # Boolean indexes of neighbors are: similarities > sufficient_similarity
      lengths = [len(vote_list) for vote_list in boolean_slice(vote_lists, similarities > sufficient_similarity)]
      if sum(lengths) < votes_required:
        result_idx.append(idx)
  return result_idx


def get_accuracy_sequence_active(estimator, n_votes_to_sample, texts, 
  vote_lists, truths, text_similarity, active_pars, idx=None, return_final=False, *args):
  """ Active version of the function above
  """

  unknown_votes = copy_and_shuffle_sublists(vote_lists)
  known_votes = [ [] for _ in unknown_votes ]

  estimates = [None for _ in vote_lists]

  accuracy_sequence = [None] * n_votes_to_sample

  (votes_required, sufficient_similarity) = active_pars 

  for index in xrange(n_votes_to_sample):
    if sufficient_similarity:
      # Count all sufficiently similar documents' votes together
      interesting_idx = get_indexes_with_neighborhood_votes_less_than(votes_required, 
        vote_lists, text_similarity, sufficient_similarity)
    else:
      # Just get votes_required votes per document
      interesting_idx = get_indexes_of_sublists_smaller_than(votes_required, known_votes)

    if interesting_idx:
      # There are still documents to fill, pick a random
      updated_doc_idx = random.choice(interesting_idx)
    else:
      # All documents have required number of votes, pick random from all
      updated_doc_idx = random.randrange(len(vote_lists))

    if not unknown_votes[updated_doc_idx]:
      # We ran out of votes for this document, diregard this sequence
      return None

    vote = unknown_votes[updated_doc_idx].pop()
    known_votes[updated_doc_idx].append(vote)
    
    # Recalculate all the estimates for the sake of consistency
    estimates = estimator(texts, known_votes, X, text_similarity, *args)

    # Calucate the accuracy_sequence
    accuracy_sequence[index] = get_accuracy(estimates, truths)

  return accuracy_sequence

def index_sublist_items(list_of_lists):
  """
  >>> a = [[1, 2], [65, 66], [12, 13, 14]]
  >>> list(index_sublist_items(a))
  [(0, 1), (0, 2), (1, 65), (1, 66), (2, 12), (2, 13), (2, 14)]
  """
  indexed_items = [ [ (idx, list_el) for list_el in l ]
    for idx, l in enumerate(list_of_lists) ]
  return list(chain(*indexed_items))


def plot_learning_curves_for_topic(topic_id, n_runs, votes_per_doc, estimators_dict, comment=None):
  texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[topic_id]
  n_documents = len(texts)

  vectorizer = TfidfVectorizer()
  X = vectorizer.fit_transform(texts)
  text_similarity = cosine_similarity(X)

  min_votes_per_doc, max_votes_per_doc = votes_per_doc
  start_idx, stop_idx = int(min_votes_per_doc * n_documents), int(max_votes_per_doc * n_documents)
  x = np.arange(float(start_idx), float(stop_idx)) / n_documents

  estimator_y = {}

  for estimator_name, estimator_and_args in estimators_dict.iteritems():
    print 'Calculating for %s' % estimator_name
    estimator, args, active_pars = estimator_and_args
    if active_pars is None:
      sequences = Parallel(n_jobs=N_CORES)( delayed(get_accuracy_sequence)(estimator, stop_idx, texts, 
        vote_lists, truths, X, text_similarity, idx, False, *args) for idx in xrange(n_runs) )
    else:
      sequences = Parallel(n_jobs=N_CORES)( delayed(get_accuracy_sequence_active)(estimator, stop_idx, texts, 
        vote_lists, truths, text_similarity, active_pars, idx, False, *args) for idx in xrange(n_runs) )      

    good_slices = [ s[start_idx:] for s in sequences if s is not None ]
    if good_slices:
      results = np.vstack(good_slices)

      # Pickling is not necessary yet
      '''
      begin_accuracies = results[:, 0]
      middle_accuracies = results[:, int(results.shape[1] / 2)]
      end_accuracies = results[:, -1]

      begin_accuracies.dump("pickles/%s-%s-begin-accuracies---.pkl" % (topic_id, estimator_name) )
      '''

      estimator_y[estimator_name] = np.mean(results, axis=0)
    else:
      print 'Query %s is not represented with estimator %s' % (topic_id, estimator_name)

  if comment:
    title = 'Query %s, %s runs, %s' % (topic_id, n_runs, comment)
  else:
    title = 'Query %s, %s runs' % (topic_id, n_runs)
  plot_learning_curve(title, x, estimator_y, 'Votes per document', 'Accuracy')


def plot_learning_curves_across_topics(n_runs, start_idx, stop_idx, estimators_dict, comment=None):
  """
  TODO Most probably buggy
  """
  for topic_id, data in texts_vote_lists_truths_by_topic_id.iteritems():
    print 'Loading topic %s' % topic_id
    texts, vote_lists, truths = data
    n_documents = len(texts)

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(texts)
    text_similarity = cosine_similarity(tfidf)

    x = np.arange(start_idx, stop_idx)

    y_by_estimator = dict( (estimator, []) for estimator in estimators_dict.keys() )

    for estimator_name, estimator_and_args in estimators_dict.iteritems():
      print 'Calculating for %s' % estimator_name
      estimator, args, active_pars = estimator_and_args
      if active_pars is None:
        sequences = Parallel(n_jobs=4)( delayed(get_accuracy_sequence)(estimator, stop_idx, texts, 
          vote_lists, truths, text_similarity, idx, False, *args) for idx in xrange(n_runs) )
      else:
        sequences = Parallel(n_jobs=4)( delayed(get_accuracy_sequence_active)(estimator, stop_idx, texts, 
          vote_lists, truths, text_similarity, active_pars, idx, False, *args) for idx in xrange(n_runs) )      

      good_slices = [ s[start_idx:] for s in sequences if s is not None ]
      if good_slices:
        results = np.vstack(good_slices)

        begin_accuracies = results[:, 0]
        end_accuracies = results[:, -1]
        
        begin_accuracies.dump("pickles/%s-%s-begin-accuracies--.pkl" % (topic_id, estimator_name) )
        end_accuracies.dump("pickles/%s-%s-end-accuracies--.pkl" % (topic_id, estimator_name))

        # We will then need to vstack and avg though all the topic accuracies for each estimator
        y_by_estimator[estimator_name].append( np.mean(results, axis=0) )
      else:
        print 'Topic %s is not represented with estimator %s' % (topic_id, estimator_name)

    result_by_estimator = {}

    for estimator_name, mean_accuracy_sequences in y_by_estimator.iteritems():
      if mean_accuracy_sequences:
        to_avg = np.vstack(mean_accuracy_sequences)
        result_by_estimator[estimator_name] = np.mean(to_avg, axis=0)
      else:
        print "Nope"
  if comment:
    title = 'Across topics, %s runs, %s' % (n_runs, comment)
  else:
    title = 'Across topics, %s runs' % topic_id
  plot_learning_curve(title, x, result_by_estimator, 'Votes sampled', 'Accuracy')


def t_test_accuracy(topic_id, n_runs, estimator_params_votes_per_doc_tuples):
  """ Test if accuracy for estimators with given parameters is
      significantly better than that of the first estimator in the tuple
  """
  texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[topic_id]
  vectorizer = TfidfVectorizer()
  text_similarity = cosine_similarity(vectorizer.fit_transform(texts))

  accuracy_arrays = []
  for estimator, args, votes_per_doc in estimator_params_votes_per_doc_tuples:
    stop_idx = votes_per_doc * len(texts)
    # Now get n_runs accuracies and put then into numpy arrays
    accuracies = Parallel(n_jobs=4)( delayed(get_accuracy_sequence)(estimator, stop_idx, texts, 
        vote_lists, truths, text_similarity, idx, True, *args) for idx in xrange(n_runs) )
    accuracy_arrays.append( np.array( filter(lambda x: x is not None, accuracies) ) )

  # Baseline
  result_row = []
  result_row.append( "%0.2f" % np.mean(accuracy_arrays[0]) )
  # T-tests
  for accuracy_array in accuracy_arrays[1:]:
    _, pval = ttest_ind(accuracy_array, accuracy_arrays[0], equal_var=False)
    significance_indicator = lambda p: "*" if p < 0.01 else " "
    is_better = "$" if np.mean(accuracy_array) > np.mean(accuracy_arrays[0]) else " "
    result_row.append( "%0.2f %s %s" % (np.mean(accuracy_array), significance_indicator(pval), is_better))

  return "|".join(result_row)


def get_p_and_var(vote_list):
  if not vote_list:
    return None, None

  p = get_mean_vote(vote_list)
  if p is None:
    return None, None
  n = len(vote_list)

  # Variance is None if there is only one vote
  var = p * (1 - p) / n if n > 1 else None
  return p, var


def is_doc_variance_better(doc_var, neighbor_var):
  """ Returns True if the document variance is less than leighbor variance
  """
  if neighbor_var is None:
    return True
  else:
    if doc_var is None:
      return False
    else:
      return (doc_var < neighbor_var)


def get_sufficient_similarity(n):
  return 1 - 1 / float(n - 1) if n > 1 else 0


def p_majority_vote_or_nn(texts, vote_lists, text_similarity, sufficient_similarity):
  """ If the nearest neighbor's similarity to you is bigger than sufficient_similarity
      and variance smaller than yours, take neighbor's conf instead of yours

      if sufficient_similarity is None it's selected by number of votes 
  """
  result_p = []
  for doc_index, vote_list in enumerate(vote_lists):
    doc_p, doc_var = get_p_and_var(vote_list)
    similarities = text_similarity[:, doc_index]
    similarities[doc_index] = 0
    nn_similarity = similarities.max()

    if sufficient_similarity is None:
      # Select similarity threshold depending on amount of votes
      sufficient_similarity = get_sufficient_similarity(len(vote_list))

    if nn_similarity > sufficient_similarity:
      nn_index = similarities.argmax()
      nn_p, nn_var = get_p_and_var(vote_lists[nn_index])
      p = doc_p if is_doc_variance_better(doc_var, nn_var) else nn_p
    else:
      p = doc_p
    result_p.append(p)

  return result_p


def est_majority_vote_or_nn(texts, vote_lists, X, text_similarity, sufficient_similarity):
  return ( unit_to_bool_random(p) for p
   in p_majority_vote_or_nn(texts, vote_lists, text_similarity, sufficient_similarity) )


def p_majority_vote_with_nn(texts, vote_lists, text_similarity, sufficient_similarity):
  result_p = []
  for doc_index, doc_vote_list in enumerate(vote_lists):
    similarities = text_similarity[:, doc_index]
    similarities[doc_index] = 0
    nn_similarity = similarities.max()

    if nn_similarity > sufficient_similarity:
      # Join their votes
      nn_vote_list = vote_lists[ similarities.argmax() ]
      joint_vote_list = doc_vote_list + nn_vote_list
      p, var = get_p_and_var(joint_vote_list)
    else:
      p, var = get_p_and_var(doc_vote_list)

    result_p.append(p)

  return result_p


def est_majority_vote_with_nn(texts, vote_lists, X, text_similarity, sufficient_similarity):
  return ( unit_to_bool_random(p) for p
   in p_majority_vote_with_nn(texts, vote_lists, text_similarity, sufficient_similarity) )


def p_merge_enough_votes(texts, vote_lists, text_similarity, votes_required):
  """ Merge votes from nearest neighbors until a sufficient amount of votes 
      is reached
  """
  result_p = []
  for doc_index, doc_vote_list in enumerate(vote_lists):
    if len(doc_vote_list) >= votes_required:
      p, var = get_p_and_var(doc_vote_list)
    else:
      # Gather votes around from neighbors
      similarities = text_similarity[:, doc_index]
      similarities[doc_index] = 0

      decreasing_order_idx = np.argsort(similarities)[::-1]
      # Fill the vote list until it's big enough
      vote_list = doc_vote_list[:]
      for neighbor_idx in decreasing_order_idx:
        vote_list += vote_lists[neighbor_idx]
        if len(vote_list) >= votes_required:
          break
      # Derive estimate from that vote list
      p, var = get_p_and_var(vote_list)

    result_p.append(p)

  return result_p


def est_merge_enough_votes(texts, vote_lists, X, text_similarity, votes_required):
  return ( unit_to_bool_random(p) for p
   in p_merge_enough_votes(texts, vote_lists, text_similarity, votes_required) )


def p_gp(texts, vote_lists, X, text_similarity):
  """ Smooth estimates with Gaussian Processes using linear correlation function
      Extrapolate to get estimates for unknown values as well
  """
  # for every vote in a vote list we have to get a vector of features 
  labels = []
  feature_vectors = []

  bool_to_plus_minus_one = lambda b: 1.0 if b else -1.0

  for doc_idx, vote_list in enumerate(vote_lists):
    for vote in vote_list:
      labels.append( bool_to_plus_minus_one(vote) )
      feature_vectors.append( X[doc_idx, :] )

  X_new = sparse.vstack(feature_vectors)
  y = np.array(labels, dtype=np.float64)[np.newaxis].T

  # Preparing a temp folder for running MATLAB
  random.seed()
  folder_id = random.randint(0, sys.maxint)
  
  matlab_folder_name = MATLAB_TEMP_DIR + 'matlab_' + str(folder_id)
  shutil.copytree('matlab', matlab_folder_name)

  io.savemat(matlab_folder_name + '/train.mat', mdict = {'x' : X_new, 'y' : y})
  io.savemat(matlab_folder_name + '/test.mat', mdict = {'t' : X })

  print 'Running MATLAB, started %s' % str(datetime.datetime.now())
  code = subprocess.call(['matlab/run_in_dir.sh', matlab_folder_name])
  if code != 0:
    raise OSError('MATLAB code couldn\'t run') 
  print 'Finished %s' % str(datetime.datetime.now())

  print 'Getting the matrix'

  # Loads a `prob` vector
  prob_location = matlab_folder_name + '/prob.mat'
  print 'Loading prob vector from %s' % prob_location
  mat_objects = io.loadmat(prob_location)
  prob = mat_objects['prob']

  result = prob[:, 0]
  
  """
  print 'prob.shape'
  print prob.shape

  print 'y[30:]'
  print y[30:]

  print 'prob[30:]'
  print prob[30:]

  print 'X.shape'
  print X.shape

  print 'X_new.shape'
  print X_new.shape

  print 'result'
  print result
  """

  # Remove the temp folder
  # Not necessary for local scratch
  # shutil.rmtree(matlab_folder_name)

  return result

def est_gp(texts, vote_lists, X, text_similarity):
  return ( unit_to_bool_random(p) for p 
    in p_gp(texts, vote_lists, X, text_similarity) )


if __name__ == "__main__":
  loser_topics = ['20644','20922']

  print "started job at %s" % datetime.datetime.now()
  for topic_id in ['20910']:
    print 'topic %s' % topic_id
    plot_learning_curves_for_topic(topic_id, 1000, (1.0, 3.0), {
      'MajorityVote' : (est_majority_vote, [], None),
  #    'MajorityVote,Active(3)' : (est_majority_vote, [], [ 3, None ]),
  #    'MergeEnoughVotes(1),Active(1)' : (est_merge_enough_votes, [ 1 ], [ 1, None ]),
  #    'MergeEnoughVotes(1)' : (est_merge_enough_votes, [ 1 ], None),
  #    'GP(1)' : (est_gp, [ 1 ], None),
      'GP' : (est_gp, [ None ], None),
    }, comment="")
  print "finished job at %s" % datetime.datetime.now()

