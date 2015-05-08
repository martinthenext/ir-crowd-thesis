"""
This takes all the accuracies from pickles and exports it to a huge text table:

topic_id | method | accuracy

"""


import numpy as np
from data import texts_vote_lists_truths_by_topic_id


def print_R_accuracy_export(topics, methods, phase):
  baseline_method = 'MajorityVote'

  for topic_id in topics:
    baseline_accuracies = np.load("pickles/%s-%s-%s-accuracies---.pkl" % (topic_id, baseline_method, phase))

    for accuracy in baseline_accuracies:
      print "%s\t%s\t%0.5f" % (topic_id, baseline_method, accuracy)

    for method in methods:
      accuracies = np.load("pickles/%s-%s-%s-accuracies---.pkl" % (topic_id, method, phase))
      for accuracy in accuracies:
        print "%s\t%s\t%0.5f" % (topic_id, method, accuracy)


loser_topics = ['20644','20922']
topics = [t for t in texts_vote_lists_truths_by_topic_id.keys() if t not in loser_topics]

#print_accuracy_table(topics_for_table, ['MergeEnoughVotes(1)', 'MergeEnoughVotes(1),Active(1)'], 'begin')
print_R_accuracy_export(topics, ['MergeEnoughVotes(1)', 'MergeEnoughVotes(1),Active(1)'], 'begin')

