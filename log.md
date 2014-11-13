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
