# Clean the file resulting from running jobs with run_on_euler.
# Only leave lines that have three columns separated by tabs
# ARGUMENT 1: input file, from the stderr of Euler jobs
# ARGUMENT 2: output file, to which clean data gets appended

grep -P '^.*\t.*\t.*$' $1 >> $2

