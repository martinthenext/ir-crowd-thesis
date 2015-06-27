#!/bin/bash
#
# This file contains a command that has been run after the 
# corresponding code has been commited to the repo

runid=$RANDOM
bsub -o out_run_$runid -e err_runs -R "rusage[mem=2000]" "python -W ignore oneaccuracy.py" 

