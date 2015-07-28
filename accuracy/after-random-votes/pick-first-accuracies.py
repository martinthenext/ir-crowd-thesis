"""

This script takes first iterations from the stardard accuracy file

"""
import sys

with open(sys.argv[1], 'r') as f:
  current_method = ""
  for line in f:
    try:
      ac, iter, run_id, method, topic, accuracy = line.split('\t')
      
      if method != current_method:
        sys.stdout.write("\t".join([ac, iter, run_id, method, topic, accuracy]) )
        current_method = method

    except ValueError:
      continue
