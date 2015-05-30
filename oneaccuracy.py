from experiments import get_accuracy, est_gp, est_gp_noise, est_majority_vote, copy_and_shuffle_sublists
from data import texts_vote_lists_truths_by_topic_id
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import codecs
import sys
import random
import traceback


def get_last_accuracy_in_sequence(estimator, n_votes_to_sample, texts, 
  vote_lists, truths, X, text_similarity, idx=None, return_final=False, *args):
  """ Randomly sample votes and re-calculate estimates.
  """
  unknown_votes = copy_and_shuffle_sublists(vote_lists)
  known_votes = [ [] for _ in unknown_votes ]

  estimates = [None for _ in vote_lists]

  accuracy_sequence = [None] * n_votes_to_sample

  # This is a crowdsourcing procedure
  for index in xrange(n_votes_to_sample):
    # Counter
    # sys.stderr.write(str(index)+'\n')

    # Draw one vote for a random document
    updated_doc_idx = random.randrange(len(vote_lists))
    if not unknown_votes[updated_doc_idx]:
      # We ran out of votes for this document, diregard this sequence
      return None
    vote = unknown_votes[updated_doc_idx].pop()
    known_votes[updated_doc_idx].append(vote)
    
  # Calculate all the estimates
  try:
    estimates = estimator(texts, known_votes, X, text_similarity, *args)
    #sys.stderr.write('Success\n')
    return get_accuracy(estimates, truths)
  except Exception, e:
    traceback.print_exc()
    #sys.stdout.write('Fail\n')
    return None
    

def print_accuracies_to_stderr(estimator_dict, max_votes_per_doc, topic_id, n_runs):
  texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[topic_id]
  n_documents = len(texts)

  vectorizer = TfidfVectorizer()
  X = vectorizer.fit_transform(texts)
  text_similarity = cosine_similarity(X)

  sequence_length = int(max_votes_per_doc * n_documents)

  for estimator_name, estimator_args in estimator_dict.iteritems():
    estimator, args = estimator_args
    for run in xrange(n_runs):  
      accuracy = get_last_accuracy_in_sequence(estimator, sequence_length, texts, vote_lists, truths, X, text_similarity, None, False, *args)
      if accuracy is not None:
        sys.stderr.write("%s\t%s\t%s\n" % ( estimator_name, topic_id, str(accuracy) ))


def print_final_accuracy_to_stderr(estimator, args, topic_id):
  texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[topic_id]
  n_documents = len(texts)

  vectorizer = TfidfVectorizer()
  X = vectorizer.fit_transform(texts)
  text_similarity = cosine_similarity(X)

  try:
    estimates = estimator(texts, vote_lists, X, text_similarity, *args)
    sys.stderr.write('%s\n' % get_accuracy(estimates, truths))
  except Exception, e:
    traceback.print_exc()

if __name__ == "__main__":
  # print_accuracies_to_stderr({'GPy' : (est_gp, [ None ] ) }, 1, '20910', 1)
  print_final_accuracy_to_stderr(est_gp, [None], '20910')

