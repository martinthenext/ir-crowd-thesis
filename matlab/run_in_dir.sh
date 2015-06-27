#!/bin/bash
# pass matlab temp folder name as a first argument
module load matlab/8.2
cd ~/ir-crowd-thesis/$1
matlab -nodisplay -nojvm -singleCompThread -r rungp
module unload matlab

