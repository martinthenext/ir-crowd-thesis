# Accuracy comparison at 1 vote per document

Reading accuracy levels for different methods from a `tsv` file.


```r
read.accuracy.df <- function(filename, na.rm=TRUE) {
  accuracy <- read.delim(filename, header=FALSE)
  names(accuracy) <- c("Method", "Topic", "Accuracy")

  if (na.rm) {
    accuracy <- accuracy[!is.na(accuracy$Accuracy), ]
  }
  
  accuracy$Topic <- as.factor(accuracy$Topic)
  row.names(accuracy) <- NULL
  accuracy
}

accuracy <- read.accuracy.df("exp-accuracy-1-vote-per-doc.tsv")

nrow(accuracy)
```

```
## [1] 4211
```

```r
head(accuracy)
```

```
##                    Method Topic Accuracy
## 1 MajorityVoteWithNN(0.5) 20696     0.50
## 2            MajorityVote 20696     0.50
## 3            MajorityVote 20714     0.70
## 4     MergeEnoughVotes(1) 20694     0.90
## 5 MajorityVoteWithNN(0.5) 20694     0.60
## 6               Matlab GP 20694     0.85
```

Calculate mean accuracies:


```r
means <- aggregate(Accuracy ~ Method + Topic, accuracy, mean)
```

Let us print a star in front of a best method for a topic


```r
library(knitr)

means <- cbind(means, Best="")
means$Best <- as.character(means$Best)
for (i in 1:nrow(means)) {
  current <- means[i, "Accuracy"]
  accuracies.on.this.topic <- means[means$Topic == means[i, "Topic"], "Accuracy"]
  max.accuracy <- max(accuracies.on.this.topic)
  if (current == max.accuracy) {
    means[i, "Best"] <- '*'
  }
}

kable(means, format="markdown")
```



|Method                  |Topic |  Accuracy|Best |
|:-----------------------|:-----|---------:|:----|
|MajorityVote            |20424 | 0.5774194|     |
|MajorityVoteWithNN(0.5) |20424 | 0.5857143|     |
|Matlab GP               |20424 | 0.7192308|*    |
|MergeEnoughVotes(1)     |20424 | 0.6208333|     |
|MajorityVote            |20488 | 0.6809524|     |
|MajorityVoteWithNN(0.5) |20488 | 0.7738095|     |
|Matlab GP               |20488 | 0.7809524|*    |
|MergeEnoughVotes(1)     |20488 | 0.7642857|     |
|MajorityVote            |20542 | 0.6716625|     |
|MajorityVoteWithNN(0.5) |20542 | 0.7033375|     |
|Matlab GP               |20542 | 0.7200050|*    |
|MergeEnoughVotes(1)     |20542 | 0.7033275|     |
|MajorityVote            |20584 | 0.6912854|     |
|MajorityVoteWithNN(0.5) |20584 | 0.7505293|     |
|Matlab GP               |20584 | 0.8459829|*    |
|MergeEnoughVotes(1)     |20584 | 0.7874585|     |
|MajorityVote            |20636 | 0.6800000|     |
|MajorityVoteWithNN(0.5) |20636 | 0.7650000|     |
|Matlab GP               |20636 | 0.7150000|     |
|MergeEnoughVotes(1)     |20636 | 0.7675000|*    |
|MajorityVote            |20642 | 0.7040634|     |
|MajorityVoteWithNN(0.5) |20642 | 0.7463415|     |
|Matlab GP               |20642 | 0.8634073|*    |
|MergeEnoughVotes(1)     |20642 | 0.7772390|     |
|MajorityVote            |20686 | 0.6877951|     |
|MajorityVoteWithNN(0.5) |20686 | 0.6227659|     |
|Matlab GP               |20686 | 0.7073195|*    |
|MergeEnoughVotes(1)     |20686 | 0.6617951|     |
|MajorityVote            |20690 | 0.6809756|     |
|MajorityVoteWithNN(0.5) |20690 | 0.7073171|     |
|Matlab GP               |20690 | 0.8243902|*    |
|MergeEnoughVotes(1)     |20690 | 0.7590244|     |
|MajorityVote            |20694 | 0.7231707|     |
|MajorityVoteWithNN(0.5) |20694 | 0.7585366|     |
|Matlab GP               |20694 | 0.8365854|*    |
|MergeEnoughVotes(1)     |20694 | 0.7951220|     |
|MajorityVote            |20696 | 0.5571429|     |
|MajorityVoteWithNN(0.5) |20696 | 0.6461538|     |
|Matlab GP               |20696 | 0.7222222|*    |
|MergeEnoughVotes(1)     |20696 | 0.6500000|     |
|MajorityVote            |20704 | 0.7166667|     |
|MajorityVoteWithNN(0.5) |20704 | 0.7902439|     |
|Matlab GP               |20704 | 0.9470588|*    |
|MergeEnoughVotes(1)     |20704 | 0.8058824|     |
|MajorityVote            |20714 | 0.7714286|     |
|MajorityVoteWithNN(0.5) |20714 | 0.8400000|     |
|Matlab GP               |20714 | 0.9000000|*    |
|MergeEnoughVotes(1)     |20714 | 0.8200000|     |
|MajorityVote            |20764 | 0.6025000|     |
|MajorityVoteWithNN(0.5) |20764 | 0.6850000|     |
|Matlab GP               |20764 | 0.4125000|     |
|MergeEnoughVotes(1)     |20764 | 0.7125000|*    |
|MajorityVote            |20766 | 0.7675000|     |
|MajorityVoteWithNN(0.5) |20766 | 0.7902439|     |
|Matlab GP               |20766 | 0.8243902|     |
|MergeEnoughVotes(1)     |20766 | 0.8658537|*    |
|MajorityVote            |20778 | 0.6300000|     |
|MajorityVoteWithNN(0.5) |20778 | 0.7650000|*    |
|Matlab GP               |20778 | 0.7050000|     |
|MergeEnoughVotes(1)     |20778 | 0.6900000|     |
|MajorityVote            |20780 | 0.6733375|     |
|MajorityVoteWithNN(0.5) |20780 | 0.7250050|     |
|Matlab GP               |20780 | 0.7833300|*    |
|MergeEnoughVotes(1)     |20780 | 0.7816750|     |
|MajorityVote            |20812 | 0.6933325|     |
|MajorityVoteWithNN(0.5) |20812 | 0.6849975|     |
|Matlab GP               |20812 | 0.7247923|*    |
|MergeEnoughVotes(1)     |20812 | 0.6900000|     |
|MajorityVote            |20814 | 0.7775000|     |
|MajorityVoteWithNN(0.5) |20814 | 0.7475000|     |
|Matlab GP               |20814 | 0.9000000|*    |
|MergeEnoughVotes(1)     |20814 | 0.8589744|     |
|MajorityVote            |20832 | 0.6975610|     |
|MajorityVoteWithNN(0.5) |20832 | 0.6829268|     |
|Matlab GP               |20832 | 0.7658537|*    |
|MergeEnoughVotes(1)     |20832 | 0.7050000|     |
|MajorityVote            |20910 | 0.6699244|     |
|MajorityVoteWithNN(0.5) |20910 | 0.6487878|     |
|Matlab GP               |20910 | 0.6634171|     |
|MergeEnoughVotes(1)     |20910 | 0.6812976|*    |
|MajorityVote            |20916 | 0.5868421|     |
|MajorityVoteWithNN(0.5) |20916 | 0.6567568|     |
|Matlab GP               |20916 | 0.7128205|*    |
|MergeEnoughVotes(1)     |20916 | 0.6026316|     |
|MajorityVote            |20932 | 0.5777786|     |
|MajorityVoteWithNN(0.5) |20932 | 0.5984071|     |
|Matlab GP               |20932 | 0.6796780|*    |
|MergeEnoughVotes(1)     |20932 | 0.6000048|     |
|MajorityVote            |20956 | 0.6285714|     |
|MajorityVoteWithNN(0.5) |20956 | 0.6238095|     |
|Matlab GP               |20956 | 0.8333333|*    |
|MergeEnoughVotes(1)     |20956 | 0.6928571|     |
|MajorityVote            |20958 | 0.5904762|     |
|MajorityVoteWithNN(0.5) |20958 | 0.5809524|     |
|Matlab GP               |20958 | 0.6428571|     |
|MergeEnoughVotes(1)     |20958 | 0.6571429|*    |
|MajorityVote            |20962 | 0.5731707|     |
|MajorityVoteWithNN(0.5) |20962 | 0.6243902|     |
|Matlab GP               |20962 | 0.6700000|*    |
|MergeEnoughVotes(1)     |20962 | 0.6170732|     |
|MajorityVote            |20972 | 0.6733325|     |
|MajorityVoteWithNN(0.5) |20972 | 0.6416675|     |
|Matlab GP               |20972 | 0.5233350|     |
|MergeEnoughVotes(1)     |20972 | 0.7083400|*    |
|MajorityVote            |20976 | 0.6125000|     |
|MajorityVoteWithNN(0.5) |20976 | 0.6325000|     |
|Matlab GP               |20976 | 0.6075000|     |
|MergeEnoughVotes(1)     |20976 | 0.6950000|*    |
|MajorityVote            |20996 | 0.5804878|*    |
|MajorityVoteWithNN(0.5) |20996 | 0.5707317|     |
|Matlab GP               |20996 | 0.3146341|     |
|MergeEnoughVotes(1)     |20996 | 0.5317073|     |

List best methods for topics:


```r
best.methods <- means[means$Best == '*', c("Topic", "Method")]

row.names(best.methods) <- NULL
kable(best.methods, format="markdown")
```



|Topic |Method                  |
|:-----|:-----------------------|
|20424 |Matlab GP               |
|20488 |Matlab GP               |
|20542 |Matlab GP               |
|20584 |Matlab GP               |
|20636 |MergeEnoughVotes(1)     |
|20642 |Matlab GP               |
|20686 |Matlab GP               |
|20690 |Matlab GP               |
|20694 |Matlab GP               |
|20696 |Matlab GP               |
|20704 |Matlab GP               |
|20714 |Matlab GP               |
|20764 |MergeEnoughVotes(1)     |
|20766 |MergeEnoughVotes(1)     |
|20778 |MajorityVoteWithNN(0.5) |
|20780 |Matlab GP               |
|20812 |Matlab GP               |
|20814 |Matlab GP               |
|20832 |Matlab GP               |
|20910 |MergeEnoughVotes(1)     |
|20916 |Matlab GP               |
|20932 |Matlab GP               |
|20956 |Matlab GP               |
|20958 |MergeEnoughVotes(1)     |
|20962 |Matlab GP               |
|20972 |MergeEnoughVotes(1)     |
|20976 |MergeEnoughVotes(1)     |
|20996 |MajorityVote            |

Total results


```r
counts <- table(best.methods$Method)
counts <- counts[counts!=0]
counts <- counts[order(counts, decreasing=TRUE)]
counts
```

```
## 
##               Matlab GP     MergeEnoughVotes(1)            MajorityVote 
##                      19                       7                       1 
## MajorityVoteWithNN(0.5) 
##                       1
```
