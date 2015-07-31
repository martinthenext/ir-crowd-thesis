"""

This script takes first iterations from the stardard accuracy file

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
  current_method = ""
  for line in f:
    match = re.search(regex, line)

    if match:
      method = match.group(4)
      if method != current_method:
        columns = [match.group(i) for i in range(1, 7)]
        current_method = method
        print '\t'.join(columns)
    else:
      continue
