#!/bin/bash
#
# Run accuracy_seq.py for all topics
#
# This file contains a command that has been run after the 
# corresponding code has been commited to the repo

OUTPUT_NAME='exp-acc-seq-1to3-majority-vote'

# Every time you run stuff on Euler, there is gonna be a new file
# You need to clean it and append to results with filter-and-append.sh
batch_id=$RANDOM

# Excluding the loser topics: 20644 and 20922
# topic_ids=(20932 20488 20910 20958 20714 20636 20956 20424 20916 20542 20778 20690 20696 20694 20832 20962 20812 20814 20704 20780 20766 20764 20642 20686 20976 20972 20584 20996)
topic_ids=(20910 20584)

for topic_id in "${topic_ids[@]}"
do

  runid=$RANDOM
  bsub -o "lsf.stdout.common.${batch_id}" -e "accuracy/${OUTPUT_NAME}.stderr-${batch_id}.tsv" -R "rusage[mem=2000]" "python -W ignore accuracy_seq.py $topic_id" 

done

