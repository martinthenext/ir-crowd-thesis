#!/bin/bash
bsub -W 8:00 -n 8 -R "rusage[mem=2000]" "python -W ignore experiments.py" 
