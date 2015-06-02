Searching for a nice way to crowdsource IR relevance judgements
===============

This is `use-gpy` branch, it is kept as an example of code that produced test results for the final draft of the thesis. It works as follows:

1. You run experiments.py, that intend to draw learning curves.
1. Instead of drawing learning curves, they measure accuracies at one particular iteration across multiple runs and serialize them into pickles (see `dump`)
1. `tests.py` looks at these pickles and analyzes the accuracies
1. A snippet of R code to do tests is provided

Please see [the project log](log.md).

