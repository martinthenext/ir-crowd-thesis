#!/bin/bash
# pass a full matlab temp directory path as a first argument
module load matlab/8.2
cd $1
matlab -nodisplay -nojvm -singleCompThread -r rungp
module unload matlab

