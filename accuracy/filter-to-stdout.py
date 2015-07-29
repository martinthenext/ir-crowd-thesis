#!/usr/bin/env python
"""

This script filters iterations from the stardard accuracy file
finding the appropriate records produced by accuracy_seq

ARGUMENT 1: input file in accuracy_seq tsv format
STDOUT: filtered lines of the input file

"""
import sys
import re

column_regexps = [
  'AC',
  '\d+',
  '\d+',
  '[^\t]+',
  '\d+',
  '[0-9\.]+',
]

regex = '\t'.join( ['(%s)' % s for s in column_regexps] )

with open(sys.argv[1], 'r') as f:
  for line in f:
    match = re.search(regex, line)

    if match:
      # The line has thr right info, write it to STDOUT
      columns = [match.group(i) for i in range(1, 7)]
      print '\t'.join(columns)
    else:
      continue
