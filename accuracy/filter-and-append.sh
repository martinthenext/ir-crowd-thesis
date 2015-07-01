# Clean the file resulting from running jobs with run_on_euler 
# and append the clean data to results file
# Only leave lines that have three columns separated by tabs
# ARGUMENT 1: input file, from the stderr of Euler jobs
# ARGUMENT 2: output file, to which clean data gets appended

# Example 
# ./filter-and-append.sh exp-gp-accuracy-1-vote-per-doc.tsv exp-gp-accuracy-1-vote-per-doc.tsv.new 

grep -P '^.*\t.*\t.*$' $1 >> $2

