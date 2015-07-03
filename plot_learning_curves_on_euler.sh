#!/bin/bash
bsub -o plot_learning_curves.euler.log -N 8 -R "rusage[mem=2000]" "python -W ignore experiments.py" 
