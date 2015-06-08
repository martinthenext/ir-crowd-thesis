#!/bin/bash
module load matlab/8.2
cd ~/ir-crowd-thesis/matlab
matlab -nodisplay -nojvm -singleCompThread -r rungp
module unload matlab
