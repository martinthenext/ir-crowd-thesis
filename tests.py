import numpy as np
from data import texts_vote_lists_truths_by_topic_id


def print_table_row(table_row):
  print '|'.join([str(x) for x in table_row])


def print_table_head(column_names):
  print '|'.join(column_names)
  print '|'.join(["----" for cn in column_names])


def print_accuracy_table(topics, methods, phase):
  baseline_method = 'MajorityVote'
  header = ['Topic', baseline_method, 'Runs']
  for method in methods:
    header += [method, 'Runs', 'Better than MV']

  print_table_head(header)

  for topic_id in topics_for_table:
    table_row = []
    table_row.append(topic_id)
    baseline_accuracies = np.load("pickles/%s-%s-%s-accuracies---.pkl" % (topic_id, baseline_method, phase))
    table_row.append(np.mean(baseline_accuracies))
    table_row.append(len(baseline_accuracies))

    for method in methods:
      accuracies = np.load("pickles/%s-%s-%s-accuracies---.pkl" % (topic_id, methods[0], phase))
      table_row.append(np.mean(accuracies))
      if np.mean(accuracies) > np.mean(baseline_accuracies):
        table_row.append("#")
      else:
        table_row.append(" ")
      table_row.append(len(accuracies))

    print_table_row(table_row)


initial_loser_topics = ['20424','20644','20696','20704','20714','20916','20922']

loser_topics = ['20424','20644','20704','20714','20916','20922']
topics_for_table = [t for t in texts_vote_lists_truths_by_topic_id.keys() if t not in loser_topics]

print_accuracy_table(topics_for_table, ['MergeEnoughVotes(1)', 'MajorityVoteWithNearestNeighbor(0.5)'], 'begin')