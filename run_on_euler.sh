#!/bin/bash
#
# This file contains a command that has been run after the 
# corresponding code has been commited to the repo

bsub -W 4:00 "python oneaccuracy.py" -R "rusage[mem=16000]" -e results/accuracies2

