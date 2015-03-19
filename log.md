# Incremental log of the project

## Looking at data

Q: In trec_judgements in team 6 there are judgements with ranked jusgements (0.5). Is this already aggregated from something?

### Testing the clustering hypothesis

TF-IDF cosine similarities between relevant documents (inner similarities) are compared to distances between relevant documents and irrelevant (outer similarities). Two-sample Welch t-test was used on the similarities.

topic|inner mean similarity|outer mean similarity|inner sd|outer sd|total texts in topic|p-value|judgement variance|comment
-----|----|----|----|----|---|-----|-----|----
20932|0.43|0.37|0.23|0.21|115|1e-42|0.195|
20488|0.50|0.35|0.21|0.22|110|2e-157|0.158|
20910|0.32|0.19|0.23|0.17|115|1e-187|0.160|
20958|0.39|0.29|0.21|0.15|100|6e-58|0.164|
20714|0.37|0.31|0.25|0.23|110|2e-28|0.167|
20636|0.43|0.37|0.18|0.23|100|2e-14|0.173|
20956|0.62|0.32|0.18|0.25|110|0e+00|0.174|
20424|0.40|0.29|0.17|0.17|100|2e-127|0.107|
20916|0.21|0.13|0.18|0.14|110|6e-63|0.174|
20542|0.53|0.19|0.22|0.20|115|6e-304|0.154|
20778|0.28|0.19|0.17|0.13|110|2e-163|0.160|
20690|0.46|0.19|0.19|0.17|125|0e+00|0.160|
20696|0.40|0.23|0.19|0.16|110|0e+00|0.106|
20694|0.57|0.39|0.20|0.23|100|8e-209|0.139|
20832|0.27|0.30|0.23|0.26|100|1e-04|0.148|weird
20962|0.29|0.25|0.18|0.17|110|1e-24|0.197|
20812|0.42|0.29|0.22|0.21|115|7e-136|0.189|
20814|0.28|0.15|0.22|0.15|100|3e-121|0.174|
20704|0.54|0.26|0.21|0.19|90|5e-248|0.138|
20922|0.40|0.32|0.22|0.17|100|3e-48|0.150|
20780|0.47|0.17|0.25|0.14|115|5e-99|0.159|
20766|0.55|0.44|0.24|0.24|110|2e-91|0.149|
20644|0.57|0.36|0.21|0.20|105|8e-197|0.075|
20764|0.35|0.21|0.23|0.15|100|5e-96|0.157|
20642|0.40|0.30|0.18|0.17|115|4e-116|0.169|
20686|0.31|0.26|0.20|0.19|115|6e-37|0.173|
20976|0.68|0.61|0.17|0.25|90|3e-20|0.161|
20972|0.57|0.36|0.24|0.22|90|8e-74|0.190|
20584|0.44|0.26|0.24|0.20|105|5e-241|0.165|
20996|0.22|0.08|0.24|0.09|110|1e-25|0.164|

Judgements per doc: 14.4746875

Weird topic (inner similarity smaller than outer):

    <row>
      <field name="number">20832</field>
      <field name="query">orlando sentinel</field>
      <field name="description">I am looking for the Orlando Sentinel home page</field>
      <field name="narrative">The Orlando Sentinel home page is highly relevant.  An active link to the Orlando Sentinel home page is relevant.  Material found on the Orlando Sentinel web site (but not the home page) is relevant.</field>
      <field name="category">Navigational (looking for a web site)</field>
    </row>

Computed the [pooled variance](http://en.wikipedia.org/wiki/Pooled_variance) for judgemens on every topic: for every document variance of relevance judgements was computed, then these variances were pooled (weighed with sample sizes) for every topic.

### Ground truth

We have 395 "ground truth" relevance assessments. For documents which had "ground truth" available differences between average worker assessment and "ground truth" have been studied. See means of the differences and t-test results in the table below.

topic|truth known / #documents|mean difference between avg. vote and truth|p-value
-----|------|------|-----
20932|15/115|-0.15|2e-01
20488|10/110|0.19|3e-02
20910|15/115|0.36|1e-05 *
20958|10/100|0.13|2e-01
20714|10/110|0.09|2e-01
20636|10/100|0.14|2e-01
20956|10/110|0.05|6e-01
20424|10/100|0.28|6e-02
20916|10/110|-0.03|8e-01
20542|15/115|0.07|4e-01
20778|10/110|0.22|2e-02
20690|25/125|0.12|7e-02
20696|10/110|0.18|3e-01
20694|20/100|0.14|1e-02
20832|10/100|0.21|8e-03 *
20962|10/110|0.14|4e-01
20812|15/115|0.34|2e-05 *
20814|10/100|0.13|8e-02
20704|10/90|0.25|1e-02
20922|10/100|0.55|1e-03 *
20780|15/115|0.00|1e+00
20766|10/110|0.12|7e-02
20644|15/105|0.33|1e-01
20764|10/100|0.14|3e-02
20642|15/115|0.02|8e-01
20686|15/115|0.19|4e-02
20976|10/90|0.36|5e-03 *
20972|15/90|-0.00|1e+00
20584|35/105|0.13|2e-02
20996|10/110|-0.16|2e-01

Stars designate p-values less than `0.01`: mean difference between average worker vote and "ground truth" on topic documents is signifantly different from 0.

### Minimum amount of judgements per document

topic|min judgements per document
-----|------
20932|15.0
20488|11.0
20910|16.0
20958|7.0
20714|1.0
20636|15.0
20956|15.0
20424|3.0
20916|3.0
20542|14.0
20778|14.0
20690|17.0
20696|2.0
20694|14.0
20832|5.0
20962|8.0
20812|16.0
20814|5.0
20704|4.0
20922|1.0
20780|14.0
20766|6.0
20644|1.0
20764|10.0
20642|16.0
20686|15.0
20976|6.0
20972|14.0
20584|16.0
20996|14.0
global|1.0

There are documents in the dataset which only have 1 judgement attached to them. If we implement the active learning setting assuming we can query additional judgements for any document, those should be removed or topic only restricted to the ones with high values in this table.

## Majority voting

### Learning curves

To get a baseline result of using majority voting for estimating relevances document relevances for a particular topic (`20690`) this [has been done](https://github.com/martinthenext/ir-crowd-thesis/blob/3a184ffff8ac92426c4b964cb51132a1ff29e16e/experiments.py) 10000 times:

1. Relevance judgements (votes) were randomly drawn one by one
2. For every new judgement estimates of relevances were updates using majority voting
3. Accuracy of the estimate was measured using the ground truth

Resulting 10000 accuracy sequences were averaged and shown on the below graph. The vertical axis shows **amount of votes per document**. 

![sequence-avg10000-axis](https://cloud.githubusercontent.com/assets/810383/5001323/018bfac4-69f5-11e4-846f-e7219387e28e.png)

The accuracy of the majority vote using all the available data is `0.92`.

*Sidenote* If during the run a vote was requested for a document that ran out of votes the accuracy sequence was discarded. Below you can see the graph in which the sequence was still considered. At the end of the curve you can see visible disruptions caused by the fact that for the end of sequences (around 10 votes per document) the probability of running out of votes for a document was higher.

![sequence-avg10000](https://cloud.githubusercontent.com/assets/810383/5001638/33869a22-69f8-11e4-8270-48fd49dd3fdf.png)

There is a substantial amount of `None`s in the beginning of the sequences as well (due to lack of votes for any ground truth), they are just not visible given the amount of simulations.

**UPDATE** New graph with the best estimate (made using all information) marked with a grey line.

![learning-curve-for-majority-voting-topic-20690-10000-runs- 1](https://cloud.githubusercontent.com/assets/810383/5049220/3a1a0274-6c24-11e4-9a39-19bb98940131.png)

**UPDATE** For a topic `20932` learning curve looks strange.

![learning-curve-for-majority-voting-topic-20932-10000-runs- 93](https://cloud.githubusercontent.com/assets/810383/5049769/81a93d4a-6c28-11e4-8d7e-98a44f389223.png)

As we exclude the sequences in which votes for a document run out, increasing the maximum number of votes per document in an experiment decreases the number of sequences and makes a plot "random". In topic `20932` minimal amount of votes per document is 15, so making an experiment from 1 to 14 results in this:

![learning-curve-for-majority-voting-topic-20932-10000-runs- 90](https://cloud.githubusercontent.com/assets/810383/5051937/3f6c1e34-6c3c-11e4-8f67-3a6505fedf27.png)

For 12 votes per document the plot is smoother:

![learning-curve-for-majority-voting-topic-20932-10000-runs- 39](https://cloud.githubusercontent.com/assets/810383/5051944/4d4f47ba-6c3c-11e4-9c7e-20fc91fc0aa5.png)

For topic `20910` the convergence is also strange:

![learning-curve-for-majority-voting-topic-20910-10000-runs- 5](https://cloud.githubusercontent.com/assets/810383/5052713/4ab1da84-6c43-11e4-8c5a-adaec8e76b68.png)

This is suspicious, code review is required.

Some other topics are ok though:

![learning-curve-for-majority-voting-topic-20812-10000-runs- 69](https://cloud.githubusercontent.com/assets/810383/5054741/de0f1386-6c58-11e4-8595-48b40839db94.png)

This lurning curve has been plotted with accuracy being measured not against the ground truth, but against the estimates obtained with all the information available. This way the maximum accuracy is 1.

![learning-curve-for-topic-20932-100-runs-seed-731- 14](https://cloud.githubusercontent.com/assets/810383/5169317/77cef2ca-7406-11e4-85cb-ba1516a28683.png)

### Discrete accuracy measuments

For every iteration, we sample one more vote for every document and measure accruacy with regards to the ground truth.

![topic-20932 -accuracies-at-k-votes-per-doc-10000-runs- 69](https://cloud.githubusercontent.com/assets/810383/5184708/04479c58-74ba-11e4-9122-fa8ff802cb01.png)

The grey line representing accuracy of the majority vote estimate on all the available data is retrieved at every run by sampling all the residual votes (to make sure the vote sampling process works properly).

For the 'nice' topic:

![topic-20812 -accuracies-at-k-votes-per-doc-10000-runs- 79](https://cloud.githubusercontent.com/assets/810383/5184747/21a1256c-74ba-11e4-98d3-79941efc6f2b.png)

### Random majorty vote

In case of even vote distribution for 'relevant' and 'irrelevant' let us take a random vote instead.

```python
def get_majority_vote(vote_list):
  """ 
  Get a boolean relevance estimate for a document given 
  a list of votes with majority voting
  """
  if vote_list:
    relevance = np.mean(vote_list)
    if relevance == 0.5:
      return random.choice([True, False])
    else:
      return (relevance > 0.5)
  else:
    return None
```

This yields this version of the discrete accuracy measument plot:

![topic-20932 -accuracies-at-k-votes-per-doc-10000-runs- 88](https://cloud.githubusercontent.com/assets/810383/5185334/f9a37bb4-74be-11e4-84ef-0a705e9e016d.png)

And this version of the above shown learning curve.

![learning-curve-for-topic-20932-10000-runs-seed-731- 52](https://cloud.githubusercontent.com/assets/810383/5200174/4bfd54d0-7563-11e4-8744-f09c834ef403.png)

If we exclude the cases of undecisive votes from consideration when calculating accuracy:

```python
def get_majority_vote(vote_list):
  """ 
  Get a boolean relevance estimate for a document given 
  a list of votes with majority voting
  """
  if vote_list:
    relevance = np.mean(vote_list)
    if relevance == 0.5:
      return None
    else:
      return (relevance > 0.5)
  else:
    return None
```

This is how it changes the picture of discrete accuracy plot:

![topic-20932 -accuracies-at-k-votes-per-doc-10000-runs- 29](https://cloud.githubusercontent.com/assets/810383/5187427/5f5b1b20-74cd-11e4-9c27-1072416d27b9.png)

Zigzag behaviour might be explained by that now that we disregard the equilibrium estimates when calculating accuracy, we also do it on the even iterations only. So the even iterations have accuracy estimated only on documents where situation is far from equilibrium, hence the accuracy must be higher. Learning curve:

![learning-curve-for-topic-20932-10000-runs-seed-731- 50](https://cloud.githubusercontent.com/assets/810383/5200204/82f0c60c-7563-11e4-9924-350c0142146b.png)

# Combining two estimators

Combining boolean (relevant/irrelevant) results of two estimator functions doesn't make sense. If you prioritize between them you will always pick answers of the estimator with the highest priority because there is no way to 'combine' boolean judgements. Hence, we need to combine the estimated confidence levels in [0, 1]. For example, mean judgement of a document (`mean(1,0,0,1,1,1)`) can be perceived as a confidence that the document is relevant.

# Majority vote vs Nearest Neighbor

The simple strategy to use distance information to improve over the majority vote estimate is to look at the nearest neighbor. For the first experiment votes have been sampled for randomly chosen documents one by one and on every iteration:

1. Probability of relevance `p` has been estimated for all the documents as mean of votes
2. Variance of this estimate was calculated as `p * (1 - p) / n`, there `n` is a number of votes for a particular document (Binomial distribution). As variance was intended to be used as a measure of uncertainty, the fact that a variance of a one-point estimate is always 0 was problematic. So instead the variance of one point was assumed to be infinity.
3. If the nearest neighbor was closer than `0.5` (out of 1) and had a smaller variance, the point estimate for `p` was taken from the neighbor.

This is the resulting graph:

![learning-curve-for-topic-20932-100-runs- 73](https://cloud.githubusercontent.com/assets/810383/5269032/4177175c-7a5f-11e4-8c51-eb0754ab6dfb.png)

As expected, the nearest neighbor approach works better on a small amount of votes per document. The fact that it gets dominated by the majority voting could be possibly fixed with a nicer use of `n` in uncertainty estimation.

*UPDATE* This is not true, variance of 1 is actually is the maximum variance you can get. So just variance is a good enough relative measure of uncertainty.

Another topic and more simulations:

![learning-curve-for-topic-20690-1000-runs- 23](https://cloud.githubusercontent.com/assets/810383/5270294/13849576-7a6a-11e4-80dd-33676ff6428f.png)

Simulation has been running for 9 hours, using 4 cores. Functional-style code recalculates distance matrix every time, need to reconsider.

*UPDATE* Similarity is now only calculated once. 

In the algorithm described below the nearest neighbor's estimate is considered if it's similar enough. This is the comparison of different sufficient similarity measures:

![topic-20690-1000-runs-for-different-sufficient-similarity-levels- 54](https://cloud.githubusercontent.com/assets/810383/5279200/5a60c9ba-7ae2-11e4-9de6-3700f89e77a7.png)

As expected, lower values yield slightly better results. For another topic Majorty votes gets betten than NN almost instantly:

![topic-20910-1000-runs-for-different-sufficient-similarity-levels- 45](https://cloud.githubusercontent.com/assets/810383/5280673/7c0fe6d8-7af4-11e4-99fe-d0067ed652ca.png)

Another topic and more levels:

![topic-20812-1000-runs-for-different-sufficient-similarity-levels- 43](https://cloud.githubusercontent.com/assets/810383/5290688/6fe2c54c-7b49-11e4-90ae-22d4067f85dd.png)

Sufficient similarity of 1 means that neighbor's estimate never gets used, which is the same as just majority voting:

![topic-20584-10000-runs-for-different-sufficient-similarity-levels- 40](https://cloud.githubusercontent.com/assets/810383/5297468/6305d60a-7baf-11e4-96c2-2f9f32962996.png)

Sometimes it works great from the beginning:

![topic-20780-10000-runs-for-different-sufficient-similarity-levels- 86](https://cloud.githubusercontent.com/assets/810383/5308499/a4349432-7c17-11e4-9325-1260bde09fd2.png)

## Adaptive sufficient similarity

We can adjust sufficient similarity to increase from 0.5 to 1 as the amount of votes for a particular document increases. That means that if the document has only 1 vote it will take the estimate from any other document closer to it than 0.5 with smaller variance. But if it has more than 10 votes the document would need to be almost identical to influence the estimate:

```

def get_sufficient_similarity(n):
  return 1 - 1 / float(n - 1) if n > 1 else 0

```

To compare with the plot above for topic `20584` we just add the new adaptive estimate:

![topic-20584-10000-runs-for-different-sufficient-similarity-levels- 78](https://cloud.githubusercontent.com/assets/810383/5317109/f089329e-7c93-11e4-8e06-d3a112b90a8f.png)

## Accuracy T-test

To quantify the way distance-aware estimator can be better than majority voting, estimator accuracy has been measured against the baseline of majority voting with the average of 3 votes per document. A 1000 runs of simulations were performed identical to the ones yielding the above graphs. For topic `20780`:

Votes per doc for NN estimator|Majority vote, 10 votes per doc|NN,ss=0.1|NN,ss=0.3|NN,ss=0.5|NN,ss=0.7|NN,ss=0.9
------------------------------|-------------|---------|---------|---------|---------|---------
3 |0.86|0.88 *|0.88 *|0.87  |0.84 *|0.83 *
4 |0.86|0.90 *|0.90 *|0.89 *|0.86  |0.84 *
5 |0.87|0.92 *|0.91 *|0.91 *|0.87  |0.85 *
6 |0.86|0.92 *|0.93 *|0.91 *|0.88 *|0.86  
7 |0.86|0.93 *|0.93 *|0.93 *|0.88 *|0.86  
8 |0.86|0.93 *|0.94 *|0.93 *|0.89 *|0.87  
9 |0.86|0.94 *|0.94 *|0.93 *|0.90 *|0.87  

A star shows significance at `0.01` level.

For topic `20812`, all accuracies are signifantly lower than that of majority voting:

Votes per doc for NN estimator|Majority vote, 10 votes per doc|NN,ss=0.1|NN,ss=0.3|NN,ss=0.5|NN,ss=0.7|NN,ss=0.9
------------------------------|-------------|---------|---------|---------|---------|---------
3 |0.91|0.77 *|0.76 *|0.82 *|0.82 *|0.81 *
4 |0.90|0.78 *|0.77 *|0.84 *|0.83 *|0.83 *
5 |0.91|0.79 *|0.78 *|0.85 *|0.84 *|0.84 *
6 |0.91|0.79 *|0.79 *|0.85 *|0.85 *|0.86 *
7 |0.90|0.80 *|0.79 *|0.86 *|0.86 *|0.86 *
8 |0.90|0.80 *|0.80 *|0.86 *|0.86 *|0.86 *
9 |0.90|0.80 *|0.80 *|0.86 *|0.86 *|0.87 *

## Joining votes with nearest neighbor

Instead of using the nearest neighbor's vote like before it makes sense to join votes with them. Below is the learning curve of such an estimator (named 'Majority vote with NN').

![topic-20690-10000-runs-for-different-sufficient-similarity-levels- 71](https://cloud.githubusercontent.com/assets/810383/5777764/d32e0cb0-9d95-11e4-951b-8d9709ec0608.png)

Behavior of this estimator with different sufficient similarity levels should be investigated.

## Joining votes until a required number is received

Another strategy would be to require a certain number of votes, and in case a document doesn't have this number consecutevely join votes with the nearest neighbor until the required number is reached. This strategy proves to be even more effective:

![topic-20690-10000-runs-for-different-sufficient-similarity-levels- 2](https://cloud.githubusercontent.com/assets/810383/5789186/ae4dcfae-9e60-11e4-9c00-4608051cf7da.png)

Results for some other topic, where previous results were pretty bad:

![topic-20910-10000-runs-for-different-sufficient-similarity-levels- 58](https://cloud.githubusercontent.com/assets/810383/5801071/318f8696-9fe7-11e4-8647-abb97a12483c.png)

Sometimes mejority vote with NN outperforms 'merge enough votes' strategy. Also, optimal parameter for the latter is not always 3 as it seems.

![topic-20780-10000-runs-for-different-sufficient-similarity-levels- 44](https://cloud.githubusercontent.com/assets/810383/5819072/4ac17276-a0bb-11e4-9033-021e16d75c5e.png)

## Using GP package from Scikit-Learn

For the task of "predicting" relevance probabilities from the given TF-IDF document vectors we try using Gaussian Processes regression `tf-idf vector` -> `relevance probability`. With a simple code like that:

```python
MY_FAVOURITE_NUMBER = 2900
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts).toarray()
y = np.array(list(p_majority_vote(texts, vote_lists)))
gp = gaussian_process.GaussianProcess(nugget=MY_FAVOURITE_NUMBER)
print gp.fit(X, y)
```

We get an exception:

> Exception: Multiple input features cannot have the same target value.

As we supply the `nugget` that should be possible, but it's not. Author [suggests](https://github.com/scikit-learn/scikit-learn/issues/642#issuecomment-67366214) this is an implementation problem.

The exception could be quickly "fixed" by [monkey patching](http://en.wikipedia.org/wiki/Monkey_patch) the `sklearn` locally and allowing GP to run. The predicted values yielded by GP are slightly different (mean difference is 5e-18 but noticable), which is a desirable behaviour because we want an algorithm to converge to majority voting results when given plenty of data.

This is `sklearn/gaussian_process/gaussian_process.py`:

```python

         # Calculate matrix of distances D between samples
         D, ij = l1_cross_distances(X)
#        if (np.min(np.sum(D, axis=1)) == 0.
#                and self.corr != correlation.pure_nugget):
#            raise Exception("Multiple input features cannot have the same"
#                            " target value.")


```


## First GP results

Here is an example comparison of mean vote estimates for relevance probability vs Gaussian Processes:

```
Mean vote:
[0.0, 0.0, None, None, None, None, None, None, 1.0, None, None, 1.0, 0.0, None, None, 0.5, 0.0, 1.0, 0.0, None, 0.0, None, None, 0.0, 0.5, 0.0, None, None, 1.0, 0.0, None, 0.33333333333333331, 0.0, None, None, None, 1.0, 0.0, None, 0.0, None, None, None, 1.0, 1.0, None, None, None, None, None, None, 0.5, None, None, 0.0, 0.0, 0.0, None, 0.0, None, None, 0.0, None, None, None, 1.0, 0.0, None, 0.0, 0.33333333333333331, None, 0.0, 1.0, None, 1.0, None, None, 0.0, 0.0, None, 0.0, None, None, 0.0, 1.0, None, None, None, None, 1.0, None, None, 0.0, None, None, None, 1.0, None, None, None, 0.0, None, None, 1.0, 1.0, 1.0, None, None, None, None, None, None, 0.0, None, None]
GP:
[0.34528071444815872, 0.34485360723787234, None, None, None, None, None, None, 0.43618980658985174, None, None, 0.43618980658985174, 0.34528071444815872, None, None, 0.39073526051900526, 0.34528071444815872, 0.43618980658985174, 0.34528071444815872, None, 0.34528071444815872, None, None, 0.34528071444815872, 0.39073526051900526, 0.34528071444815872, None, None, 0.43618980658985174, 0.34528071444815872, None, 0.37558374588689636, 0.34528071444815872, None, None, None, 0.43618980658985174, 0.34528071444815872, None, 0.34528071444815872, None, None, None, 0.43618980658985174, 0.43618980658985174, None, None, None, None, None, None, 0.39076545834754334, None, None, 0.34528071444815872, 0.31631480117959171, 0.34528071444815872, None, 0.34528071444815872, None, None, 0.34528071444815872, None, None, None, 0.43618980658985174, 0.34528071444815872, None, 0.34528071444815872, 0.37558374588689636, None, 0.34528075940607789, 0.43618980658985174, None, 0.43619565728262016, None, None, 0.34528071444815872, 0.34528071444815872, None, 0.34528071444815872, None, None, 0.31631494391527976, 0.43618980658985174, None, None, None, None, 0.43618980658985174, None, None, 0.34528071444815872, None, None, None, 0.43618980658985174, None, None, None, 0.34528071444815872, None, None, 0.43618977905735268, 0.43618980658985174, 0.43618980658985174, None, None, None, None, None, None, 0.34528071444815872, None, None]

```

## Memory problems

Ran into memory problems bacause gigantic dense tf-idf matrices don't get garbage-collected properly. Trying different strategies and going to do profiling. 

Experiments show that memory is not enough to process one [sic] accuracy sequence.

**UPDATE** This got implemented and is now running. Going to have a list of accuracy sequences in an `csv` file and then plot them in Excel.

Now GPs seem to be running, we need to get them to an appropriate quality.
Results that we're aiming at: way higher accuracy than majority voting at low amount of votes per document. Plan:

1. Reimplement the accuracy measurement to include **all documents into the measurement**. Possibly toss a coin with the empirical probability of success measured from the dataset.

2. Try getting parameters for the GP right. Parameters cannot be found by looking at the final accuracy, there should be some other way.

## First GP results

Now every accuracy sequence is generated separately and is written to a text file. GP with nugget parameter of `1` was compared to the previous successful baseline result of "Merge Enough Votes" with 3 votes required and Majority Voting. For every sequence 100 experiments were run and results from 1 to 5 votes per document are shown.

![default](https://cloud.githubusercontent.com/assets/810383/6204550/e60d9dec-b54f-11e4-85b1-033118ab0391.png)

GP are worse than everything, but this is because we don't know the right parameters yet. 

**UPDATE** Nugget `0.1` does obviously better. If nugget parameter means variance, it should be in a range of `0.01`. Results are going to be around soon.

![default](https://cloud.githubusercontent.com/assets/810383/6219777/45aeb1da-b62e-11e4-85fb-4f7e7eebe65c.png)

**UPDATE** Very surprisingly enough, Nugget `0.01` doesn't differ much from `0.1`:

![default](https://cloud.githubusercontent.com/assets/810383/6258090/0807f05a-b7c6-11e4-80ff-6180627c8ab2.png)

**UPDATE** New graph for nugget `0.3`, which appears not do that much difference

![default](https://cloud.githubusercontent.com/assets/810383/6383980/bb264e44-bd56-11e4-9558-737b63cddfd9.png)

## Proposed explanation for strange convergence

Question: Why on some graphs the accuracy of estimates made with lower amount of votes per document is higher than the accuracy of the estimate made with all the available votes? 

Answer: The procedure of drawing votes when generating a particular accuracy sequence is the following:

1. Out of all documents a random one is chosen
2. For this document a new vote is queried. In case there is no votes left for the document the entire sequence is disregarded

As this procedure is more likely to diregard documents with smaller amount of votes, the documents with high amount of votes are more accounted for when calculated average accuracy at every particular iteration. Document with higher vote count are more likely to have good majority vote estimates. Hence, average accuracies measured for accuracy sequences can be higher than the one simply accounting all the data as low vote count documents are also accounted for.

**UPDATE** Went back to the strage plot of topic `20932` and tried getting the [equal number of votes for every document](https://github.com/martinthenext/ir-crowd-thesis/blob/strangeplots/experiments.py#L45), still we have the same effect:

![learning-curve-for-majority-voting-topic-20932-1000-runs- 81](https://cloud.githubusercontent.com/assets/810383/6284377/a0229ad2-b8ef-11e4-97d6-605b4d92fdce.png)

If we restrict number of votes per document even below mininum - to 10, this happens:

![learning-curve-for-majority-voting-topic-20932-10000-runs- 24](https://cloud.githubusercontent.com/assets/810383/6284764/406aa4ea-b8f4-11e4-9ee9-1c8f5e10162b.png)

Still goes above the all-information estimate.

## Active learning

First attempt at active learning: requiring a certain amount of votes per document and "filling" documents to the required number of votes instead of chosing randomly. This strategy is being used in conjunction with a simple Majority Vote estimator. Below are results for two different topics:

![topic-20690-1000-runs-comparing-with-active-learner- 61](https://cloud.githubusercontent.com/assets/810383/6396145/1cb2b0f4-bddd-11e4-96c8-c7afc2155ed3.png)

![topic-20910-10000-runs-comparing-with-active-learner- 22](https://cloud.githubusercontent.com/assets/810383/6396028/761e3f92-bddc-11e4-8e1c-d695ffb18cdc.png)

It would be interesting to see how that strategy goes with the sufficient similarity method.

**UPDATE** Results of using the simplest type of Active Learning with multiple baseline types (code [here](https://github.com/martinthenext/ir-crowd-thesis/blob/active-graphs/experiments.py) ):

![topic-20910-10000-runs-comparing-with-active-learner- 12](https://cloud.githubusercontent.com/assets/810383/6414640/226a4694-be99-11e4-8cec-85c33879a578.png)

We can see that for *Majority voting*, *Majority voting with NN, suff.sim. 0.5* and *Merge enough votes, required 1* active learning performs better than passive learning. The best results belongs to *Merge enough votes* with 1 vote required, performed actively. What it does if a document doesn't have any votes at all, it assigns it's label to the label of a nearest neighbor which has a vote. Active learning works trying to get at least one vote for every document first.

Gonna look at a different topic now.

**UPDATE** For another topic we still have the same winner.

![topic-20812-10000-runs-comparing-with-active-learner- 20](https://cloud.githubusercontent.com/assets/810383/6426344/05f9f30c-bf56-11e4-9997-6500f40a747d.png)

**UPDATE** Gaussian Process classifier is now trained on available data only (documents which have votes) and used on *all* documents.

![default](https://cloud.githubusercontent.com/assets/810383/6460444/9c23a920-c197-11e4-9d43-55efa92fc2a3.png)

The proper way of doing it is using a link function, going to implement it next.

## New ground truth

In [TREC 2011 Crowdsourcing track](https://sites.google.com/site/treccrowd/2011) some ground-truth NIST labels are given to teams to evaluate their techniques. This development (training) data is available [here](https://sites.google.com/site/treccrowd/2011/stage2-dev.tar?attredirects=0). It only has 25 topics, and, what a surpise, all of different from ones we used up until now.

## Random MV

Returning to the question of tie in Majority Voting. TREC evaluation procedure requires a label assigned to every document, meaning that you cannot return `None`. Returning to the strategy of tossing a fair coin in tie situations, [we can compare](https://github.com/martinthenext/ir-crowd-thesis/blob/active-graphs/experiments.py) MV and random MV on the state-of-the-art baseline plot:

![topic-20910-10000-runs-comparing-with-active-learner- 59](https://cloud.githubusercontent.com/assets/810383/6514148/7ce26a52-c380-11e4-8a9c-8cc269d62320.png)

Now we need to completely switch all estimators to do a toin coss in case of a tie (as in, when relevance estimate is exactly `0.5`).

**UPDATE** The [updated code](https://github.com/martinthenext/ir-crowd-thesis/commit/cb8e097bcf8fabbcf950aa64a0e824efbd6b0d9b) uses coin tosses for all situations where p=0.5. See the corresponding version of the above plot:

![topic-20910-10000-runs-comparing-with-active-learner- 12](https://cloud.githubusercontent.com/assets/810383/6517205/0bebdd60-c399-11e4-8fb5-8d6fda09f6be.png)

Now the lines change their behaviour at the explainable positions.

**UPDATE** [Updated code](https://github.com/martinthenext/ir-crowd-thesis/commit/c4bdf253655dd8335cb29986ac08766b84664ebb) gets accuracy sequences for all possible topics and then averages them.

![across-topics-1000-runs-comparing-with-active-learner- 20](https://cloud.githubusercontent.com/assets/810383/6525237/703c8052-c403-11e4-9ae7-307215c5bc7c.png)

**UPDATE** For larger amount of simulations:

![across-topics-10000-runs-comparing-with-active-learner- 71](https://cloud.githubusercontent.com/assets/810383/6541916/794d4920-c4e8-11e4-8e94-0bd0d39bf6ba.png)

## With rounding bug fixed

[Fixed](https://github.com/martinthenext/ir-crowd-thesis/commit/604f900c7aa364ff0bdc33a870d5ee20821d43ed) a bug in a procedure that takes a relevance estimate in [0, 1] and outputs the label. Now if the input is `None` it also outputs a fair coin toss. The updated plot:

![across-topics-10000-runs-comparing-with-active-learner- 17](https://cloud.githubusercontent.com/assets/810383/6593601/3f841e04-c7da-11e4-9fa0-581f4a69c5a5.png)

## Comparison: Passive vs. Active learning with Majority Vote

![across-topics-10000-runs-comparing-with-active-learner- 90](https://cloud.githubusercontent.com/assets/810383/6622793/2d63cf20-c8df-11e4-852b-dca428046389.png)

## Ground truth new stats

Topic|#ground truth/#documents|mean ground truth relevance
-----|------------------------|---------------------------
20932|15/115|0.80
20488|10/110|0.60
20910|15/115|0.67
20958|10/100|0.70
20714|10/110|0.50
20636|10/100|0.70
20956|10/110|0.80
20424|10/100|0.60
20916|10/110|0.80
20542|15/115|0.67
20778|10/110|0.50
20690|25/125|0.72
20696|10/110|0.80
20694|20/100|0.60
20832|10/100|0.80
20962|10/110|0.70
20812|15/115|0.67
20814|10/100|0.70
20704|10/90|0.50
20922|10/100|0.60
20780|15/115|0.53
20766|10/110|0.50
20644|15/105|0.53
20764|10/100|0.70
20642|15/115|0.87
20686|15/115|0.73
20976|10/90|0.60
20972|15/90|0.60
20584|35/105|0.74
20996|10/110|0.90

Overall mean relevance - `0.68`. There is only one topic where more than 80% of ground truth judgments show relevance.

## Inner vs outer similarity histograms

![inner- 45](https://cloud.githubusercontent.com/assets/810383/6701367/16cf8e3e-cd1c-11e4-9d4f-f7791c8d1745.png)

![outer- 47](https://cloud.githubusercontent.com/assets/810383/6701370/1fd05270-cd1c-11e4-9549-f8c04bf6c550.png)

Somehow the inner similarity has a spike close to 1, although we delete all the distances with self. Out of all the topics there are only two which have a lot of inner distances bigger than `0.95`: `20694` and `20584`.

**UPDATE** I've checked documents with high similarity and they appear just to have different ads. Example difference between two relevant documents having similarity of `0.97`:

```
Watch the latest videos on YouTube.com

Dental Assisting Programs
Dental Journals
Dental Blogs
Dental Health Literature
Pre-Dental Programs NEW

Alabama Dental Hygiene Schools
Alaska Dental Hygiene Schools
Arizona Dental Hygiene Schools
Arkansas Dental Hygiene Schools
California Dental Hygiene Schools
Colorado Dental Hygiene Schools
Connecticut Dental Hygiene Schools
Delaware Dental Hygiene Schools
District of Columbia DH Programs
Florida Dental Hygiene Schools
Georgia Dental Hygiene Schools
Hawaii Dental Hygiene Schools
Find more programs below

[...]

Email a friend about this page:   

Assessor Links USA    All Things Political    Engineers Guide USA    State 
Health Links    healthlinksusa.com    Juggling Cats    Doomsday Guide

Health Resource Guide     County Recorders    County Treasurers   Health 
Resource USA    Buy Yellow Roses    Innovators Guide

To report a broken link or to suggest a new site for our online resource 
guide, please Contact Us.
Proquantum Corporation.
Copyright @ 2002-2007
Use of this website is expressly subject to the various terms and 
conditions set forth in our
User Agreement/Disclaimer  and Privacy Policy

Visit online mba review.

visits since 8/31/03

```

```

Health Guide USA  
America's Online Health Resource Guide

Enter your search terms Submit search form
Web    www.healthguideusa.org

To Home Page
 


North Dakota Dental Hygiene Programs - Dental Hygienist Schools

Other resources: Dental Hygienist Job Outlook
State Dental Hygienist Licensing Information
State Dental Health Programs

North Dakota State Dental Hygiene Program

 

Find more dental related resources below:




State Dental Boards
[...]

Email a friend about this page:   

Assessor Links USA    All Things Political    Engineers Guide USA    State 
Health Links    healthlinksusa.com    Juggling Cats    Doomsday Guide

Health Resource Guide     County Recorders    County Treasurers   Health 
Resource USA    Buy Yellow Roses    Innovators Guide

To report a broken link or to suggest a new site for our online resource 
guide, please Contact Us.
Proquantum Corporation.
Copyright @ 2002-2007
Use of this website is expressly subject to the various terms and 
conditions set forth in our
User Agreement/Disclaimer  and Privacy Policy

Visit online mba review.

visits since 8/31/03

```

## More string exclusion criterion for inner similarities

Now excluding all similarities which are closer than 10^-5 to 1. This deleted more similarities, which means that there is a bunch of de-facto similar documents within the ground truth. New inner similarity plot:

### Inner similarities

![similarities-between-relevant-documents- 13](https://cloud.githubusercontent.com/assets/810383/6743175/fcb03be4-ce96-11e4-82be-c21eec4ba928.png)
