from data import texts_vote_lists_truths_by_topic_id

TOPIC_ID = '20690'

texts, vote_lists, truths = texts_vote_lists_truths_by_topic_id[TOPIC_ID]
print 'document #11'
print 'text:' + repr(texts[11])[:100]
print 'votes:' + repr(vote_lists[11])
print 'truth:' + repr(truths[11])
