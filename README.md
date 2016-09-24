Searching for a nice way to crowdsource IR relevance judgements
===============

The use of crowdsourcing for document relevance assessment has been found to be a viable alternative to corpus annotation by highly trained experts. The question of quality control is a recurring challenge that is often addressed by aggregating multiple individual assessments of the same topic-document pair from independent workers. In the past, such aggregation schemes have been weighted or filtered by estimates of worker reliability based on a multitude of behavioral features. In this paper, we propose an alternative approach by relying on document information. Inspired by the clustering hypothesis of information retrieval, we assume textually similar documents to show similar degrees of relevance towards a given topic. Following up on this intuition, we propagate crowd-generated relevance judgments to similar documents, effectively smoothing the distribution of relevance labels across the similarity space.

Our experiments are based on TREC Crowdsourcing Track data and show that even simple aggregation methods utilizing document similarity information significantly improve over majority voting in terms of accuracy as well as cost efficiency.

Please see [the project log](log.md). Experiment results are in `results`. Resulting paper is [here](http://dl.acm.org/citation.cfm?id=2806460).
