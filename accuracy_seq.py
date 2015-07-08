"""

This calculated accuracy sequences and puts writes them to STDERR
separated by tabs

"""

from experiments import get_accuracy_sequence, est_gp, est_majority_vote, est_merge_enough_votes, est_majority_vote_with_nn
from data import texts_vote_lists_truths_by_topic_id
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys


def print_accuracy_sequences_to_stderr(estimator_dict, votes_per_doc, topic_id, n_sequesnces_per_estimator):
  texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[topic_id]
  n_documents = len(texts)

  vectorizer = TfidfVectorizer()
  X = vectorizer.fit_transform(texts)
  text_similarity = cosine_similarity(X)

  min_votes_per_doc, max_votes_per_doc = votes_per_doc
  start_idx, stop_idx = int(min_votes_per_doc * n_documents), int(max_votes_per_doc * n_documents)
  
  sequence_length = int(max_votes_per_doc * n_documents)

  for estimator_name, estimator_args in estimator_dict.iteritems():
    estimator, args = estimator_args
    for _ in xrange(n_sequesnces_per_estimator):
      seq = get_accuracy_sequence(estimator, sequence_length, texts, vote_lists, truths, X, text_similarity,
          None, False, *args)
      if seq is not None:
        accuracy_sequence = seq[start_idx: ]
        string_repr = "\t".join( [ ("%.4f" % acc) for acc in accuracy_sequence ] )
        sys.stderr.write("%s\t%s\t%s\n" % (estimator_name, topic_id, string_repr) )


if __name__ == "__main__":
  try:
    topic_id = sys.argv[1]
  except IndexError:
    raise Error("Please supply the topic id")

  print_accuracy_sequences_to_stderr({
#       'Matlab GP' : (est_gp, []),
       'MajorityVote' : (est_majority_vote, []),
#       'MergeEnoughVotes(1)' : (est_merge_enough_votes, [ 1 ]),
#       'MajorityVoteWithNN(0.5)' : (est_majority_vote_with_nn, [ 0.5 ]),
  }, (1, 3), topic_id, 2)

