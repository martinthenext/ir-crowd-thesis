#!/bin/bash
#
# Run oneaccuracy.py for all topics
#
# This file contains a command that has been run after the 
# corresponding code has been commited to the repo

N_RUNS_PER_TOPIC=20

# Excluding the loser topics: 20644 and 20922
topic_ids=(20932 20488 20910 20958 20714 20636 20956 20424 20916 20542 20778 20690 20696 20694 20832 20962 20812 20814 20704 20780 20766 20764 20642 20686 20976 20972 20584 20996)

for run in `seq 1 $N_RUNS_PER_TOPIC`;
do

  for topic_id in "${topic_ids[@]}"
  do
  
    runid=$RANDOM
    bsub -o /dev/null -e accuracy/exp-accuracy-1-vote-per-doc.tsv -R "rusage[mem=2000]" "python -W ignore oneaccuracy.py $topic_id" 

  done
done

