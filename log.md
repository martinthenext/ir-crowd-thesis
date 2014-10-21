# Incremental log of the project

## Looking at data

Q: In trec_judgements in team 6 there are judgements with ranked jusgements (0.5). Is this already aggregated from something?

### Testing the clustering hypothesis

TF-IDF cosine similarities between relevant documents (inner similarities) are compared to distances between relevant documents and irrelevant (outer similarities). Two-sample Welch t-test was used on the similarities.

topic|inner mean similarity|outer mean similarity|inner sd|outer sd|total texts in topic|p-value|judgement relevance|comment
-----|----|----|----|----|---|-----|-----|
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
