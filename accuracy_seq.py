"""

This calculated accuracy sequences and puts writes them to STDERR
separated by tabs

"""

from experiments import get_accuracy, est_gp, est_majority_vote, est_merge_enough_votes, est_majority_vote_with_nn, copy_and_shuffle_sublists
from data import texts_vote_lists_truths_by_topic_id
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
import random


def get_accuracy_sequences(estimator_dict, sequence_length, texts, vote_lists, truths, X, text_similarity):

  random.seed() # This is using system time

  document_idx_vote_seq = []

  # Conduct an experiment where you randomly sample votes for documents
  for _ in xrange(sequence_length):
    # Randomly pick a document
    updated_doc_idx = random.randrange(len(vote_lists))
    
    # Randomly pick a vote for this document
    vote_idx = random.randrange(len(vote_lists[updated_doc_idx]))

    vote = vote_lists[updated_doc_idx][vote_idx]
    document_idx_vote_seq.append( (updated_doc_idx, vote ) )

  # Here we know the sequence of draws was successful
  # Let us measure estimator accuracies now
  accuracy_sequences = {}

  for estimator_name, estimator_args in estimator_dict.iteritems():
    estimator, args = estimator_args
    accuracy_sequences[estimator_name] = []

    # Go through the generated sequence of draws and measure accuracy
    known_votes = [ [] for _ in vote_lists ]

    for document_idx, vote in document_idx_vote_seq:
      known_votes[document_idx].append(vote)
      
      # Recalculate all the estimates for the sake of consistency
      estimates = estimator(texts, known_votes, X, text_similarity, *args)

      # Calucate the accuracy_sequence
      try:
        accuracy =  get_accuracy(estimates, truths)
      except OSError:
        print '#OS ERROR'
        # Leave the function
        return None

      accuracy_sequences[estimator_name].append(accuracy)
  
  return accuracy_sequences

def print_accuracy_sequences_to_stderr(estimator_dict, votes_per_doc, topic_id, n_sequesnces_per_estimator):
  texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[topic_id]
  n_documents = len(texts)

  vectorizer = TfidfVectorizer()
  X = vectorizer.fit_transform(texts)
  text_similarity = cosine_similarity(X)

  min_votes_per_doc, max_votes_per_doc = votes_per_doc

  start_vote_count = int(min_votes_per_doc * n_documents)
  # In an accuracy sequence, element 0 corresponds to the vote count of 1.
  start_idx = start_vote_count - 1

  sequence_length = int(max_votes_per_doc * n_documents)

  for _ in xrange(n_sequesnces_per_estimator):
    # Getting accuracy for all esimators
    # If failed, attempt at getting a sequence until it's not None
    sequences = None
    counter = 0
    while sequences is None:
      counter += 1
      print '#ATTEMPT\t%s' % counter
      sequences = get_accuracy_sequences(estimator_dict, sequence_length, texts, vote_lists, truths, X, text_similarity)

    # Got a sequence
    # Write all sequences from this dict to stderr
    run_id = random.randint(0, sys.maxint)

    for estimator_name, accuracy_sequence in sequences.iteritems():
      accuracy_sequence_trimmed = accuracy_sequence[start_idx: ]
      
      for index, accuracy in enumerate(accuracy_sequence_trimmed):
        sys.stderr.write("AC\t%s\t%s\t%s\t%s\t%s\n" % (start_vote_count + index, run_id, estimator_name, topic_id, "%.4f" % accuracy) )


if __name__ == "__main__":
  try:
    topic_id = sys.argv[1]
  except IndexError:
    raise Exception("Please supply the topic id")

  N_SEQS_PER_EST = 1

  print_accuracy_sequences_to_stderr({
       'GP' : (est_gp, []),
       'MV' : (est_majority_vote, []),
       'MEV(1)' : (est_merge_enough_votes, [ 1 ]),
       'MVNN(0.5)' : (est_majority_vote_with_nn, [ 0.5 ]),
  }, (1.0, 3.0), topic_id, N_SEQS_PER_EST)


