from data import texts_vote_lists_truths_by_topic_id
import numpy as np

print "Topic|#ground truth/#documents|mean ground truth relevance"
all_judgments = []
for topic_id, data in texts_vote_lists_truths_by_topic_id.iteritems():
  texts, vote_lists, truths = data
  judgments = [t for t in truths if t is not None]
  all_judgments += judgments
  print "%s|%s/%s|%0.2f" % (topic_id, len(judgments), len(texts), np.mean(judgments))
  
print np.mean(all_judgments) 
