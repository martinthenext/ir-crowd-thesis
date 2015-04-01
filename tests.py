import numpy as np
from data import texts_vote_lists_truths_by_topic_id
from scipy import stats

def print_table_row(table_row):
  print '&'.join([str(x) for x in table_row]) + "\\\\ \\hline"


def print_table_head(column_names):
  print "\\begin{table}"
  print "\\begin{tabular}{" + "|".join(["l" for cn in column_names]) + "}"
  print "\\hline"
  print "&".join(column_names) + "\\\\ \\hline"


def print_table_end():
  print "\\end{tabular}"
  print "\\end{table}"


def print_accuracy_table(topics, methods, phase):
  baseline_method = 'MajorityVote'
  header = ['Topic', baseline_method, 'Runs']
  for method in methods:
    header += [method, 'Runs', 'Better than MV, p-value']

  print_table_head(header)
  rows = []

  for topic_id in topics_for_table:
    table_row = []
    table_row.append(topic_id)
    baseline_accuracies = np.load("pickles/%s-%s-%s-accuracies---.pkl" % (topic_id, baseline_method, phase))
    table_row.append("%0.3f" % np.mean(baseline_accuracies))
    table_row.append(len(baseline_accuracies))

    for method in methods:
      accuracies = np.load("pickles/%s-%s-%s-accuracies---.pkl" % (topic_id, method, phase))
      table_row.append("%0.3f" % np.mean(accuracies))
      table_row.append(len(accuracies))

      

      if np.mean(accuracies) > np.mean(baseline_accuracies):
        _, pval = stats.ttest_ind(accuracies, baseline_accuracies, equal_var=False)
        if pval < 0.05:
          table_row.append("*")
        else:
          table_row.append(" ")
      else:
        table_row.append(" ")

    rows.append(table_row)


  rows.sort(key=lambda row: int(row[0]))
  for row in rows:
    print_table_row(row)

  print_table_end()

initial_loser_topics = ['20424','20644','20696','20704','20714','20916','20922']

loser_topics = ['20644','20922']
topics_for_table = [t for t in texts_vote_lists_truths_by_topic_id.keys() if t not in loser_topics]

print_accuracy_table(topics_for_table, ['MergeEnoughVotes(1)', 'MajorityVoteWithNearestNeighbor(0.5)'], 'begin')