# Accuracy comparison at 1 vote per document

Reading accuracy table for GP method from a `tsv` file.


```r
read.accuracy.df <- function(filename, na.rm=TRUE) {
  accuracy <- read.delim(filename, header=FALSE)
  names(accuracy) <- c("Method", "Topic", "Accuracy")
  accuracy$Topic <- as.factor(accuracy$Topic)
  if (na.rm) {
    accuracy <- accuracy[!is.na(accuracy$Accuracy), ]
  }
  accuracy
}

accuracy.gp <- read.accuracy.df("exp-gp-accuracy-1-vote-per-doc.tsv")

nrow(accuracy.gp)
```

```
## [1] 1537
```

```r
head(accuracy.gp)
```

```
##      Method Topic Accuracy
## 3 Matlab GP 20636   0.7000
## 4 Matlab GP 20956   0.8000
## 5 Matlab GP 20832   0.8000
## 6 Matlab GP 20778   0.7000
## 7 Matlab GP 20704   1.0000
## 8 Matlab GP 20780   0.7333
```

Reading same table for older methods:


```r
accuracy.older <- read.accuracy.df("exp-older-methods-1-vote-per-doc.tsv")

nrow(accuracy.older)
```

```
## [1] 2350
```

```r
head(accuracy.older)
```

```
##                    Method Topic Accuracy
## 1     MergeEnoughVotes(1) 20916   0.7000
## 2 MajorityVoteWithNN(0.5) 20916   0.9000
## 3            MajorityVote 20916   0.5000
## 4     MergeEnoughVotes(1) 20424   0.3000
## 6            MajorityVote 20424   0.5000
## 7     MergeEnoughVotes(1) 20972   0.7333
```

Join the data frames and calculate the means


```r
accuracy <- rbind(accuracy.gp, accuracy.older)
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
|Matlab GP               |20424 | 0.6970588|*    |
|MajorityVote            |20424 | 0.6333333|     |
|MajorityVoteWithNN(0.5) |20424 | 0.5869565|     |
|MergeEnoughVotes(1)     |20424 | 0.6058824|     |
|Matlab GP               |20488 | 0.7896552|*    |
|MajorityVote            |20488 | 0.6733333|     |
|MajorityVoteWithNN(0.5) |20488 | 0.7633333|     |
|MergeEnoughVotes(1)     |20488 | 0.7733333|     |
|Matlab GP               |20542 | 0.7433333|*    |
|MajorityVote            |20542 | 0.7241345|     |
|MajorityVoteWithNN(0.5) |20542 | 0.6712621|     |
|MergeEnoughVotes(1)     |20542 | 0.7218414|     |
|Matlab GP               |20584 | 0.8484254|*    |
|MajorityVote            |20584 | 0.6930903|     |
|MajorityVoteWithNN(0.5) |20584 | 0.7474677|     |
|MergeEnoughVotes(1)     |20584 | 0.7824839|     |
|Matlab GP               |20636 | 0.7266667|     |
|MajorityVote            |20636 | 0.6800000|     |
|MajorityVoteWithNN(0.5) |20636 | 0.7533333|     |
|MergeEnoughVotes(1)     |20636 | 0.7666667|*    |
|Matlab GP               |20642 | 0.8500050|*    |
|MajorityVote            |20642 | 0.7247290|     |
|MajorityVoteWithNN(0.5) |20642 | 0.7376419|     |
|MergeEnoughVotes(1)     |20642 | 0.7634387|     |
|Matlab GP               |20686 | 0.7411083|*    |
|MajorityVote            |20686 | 0.6817226|     |
|MajorityVoteWithNN(0.5) |20686 | 0.6430161|     |
|MergeEnoughVotes(1)     |20686 | 0.6709645|     |
|Matlab GP               |20690 | 0.8340000|*    |
|MajorityVote            |20690 | 0.6787097|     |
|MajorityVoteWithNN(0.5) |20690 | 0.7419355|     |
|MergeEnoughVotes(1)     |20690 | 0.7767742|     |
|Matlab GP               |20694 | 0.8122951|*    |
|MajorityVote            |20694 | 0.7206897|     |
|MajorityVoteWithNN(0.5) |20694 | 0.7413793|     |
|MergeEnoughVotes(1)     |20694 | 0.7775862|     |
|Matlab GP               |20696 | 0.7227273|*    |
|MajorityVote            |20696 | 0.6100000|     |
|MajorityVoteWithNN(0.5) |20696 | 0.6375000|     |
|MergeEnoughVotes(1)     |20696 | 0.6400000|     |
|Matlab GP               |20704 | 0.9403846|*    |
|MajorityVote            |20704 | 0.6785714|     |
|MajorityVoteWithNN(0.5) |20704 | 0.8074074|     |
|MergeEnoughVotes(1)     |20704 | 0.8346154|     |
|Matlab GP               |20714 | 0.8666667|     |
|MajorityVote            |20714 | 0.7333333|     |
|MajorityVoteWithNN(0.5) |20714 | 0.8500000|     |
|MergeEnoughVotes(1)     |20714 | 0.9000000|*    |
|Matlab GP               |20764 | 0.4816667|     |
|MajorityVote            |20764 | 0.7000000|*    |
|MajorityVoteWithNN(0.5) |20764 | 0.6774194|     |
|MergeEnoughVotes(1)     |20764 | 0.6806452|     |
|Matlab GP               |20766 | 0.8406780|     |
|MajorityVote            |20766 | 0.8064516|     |
|MajorityVoteWithNN(0.5) |20766 | 0.7483871|     |
|MergeEnoughVotes(1)     |20766 | 0.8677419|*    |
|Matlab GP               |20778 | 0.6836066|     |
|MajorityVote            |20778 | 0.6645161|     |
|MajorityVoteWithNN(0.5) |20778 | 0.7096774|*    |
|MergeEnoughVotes(1)     |20778 | 0.7096774|*    |
|Matlab GP               |20780 | 0.7934426|*    |
|MajorityVote            |20780 | 0.7053806|     |
|MajorityVoteWithNN(0.5) |20780 | 0.6946129|     |
|MergeEnoughVotes(1)     |20780 | 0.7376290|     |
|Matlab GP               |20812 | 0.7080483|     |
|MajorityVote            |20812 | 0.6817290|     |
|MajorityVoteWithNN(0.5) |20812 | 0.7247355|     |
|MergeEnoughVotes(1)     |20812 | 0.7376355|*    |
|Matlab GP               |20814 | 0.8912281|*    |
|MajorityVote            |20814 | 0.7833333|     |
|MajorityVoteWithNN(0.5) |20814 | 0.7966667|     |
|MergeEnoughVotes(1)     |20814 | 0.8900000|     |
|Matlab GP               |20832 | 0.7116667|     |
|MajorityVote            |20832 | 0.6903226|     |
|MajorityVoteWithNN(0.5) |20832 | 0.7096774|     |
|MergeEnoughVotes(1)     |20832 | 0.7225806|*    |
|Matlab GP               |20910 | 0.6666738|*    |
|MajorityVote            |20910 | 0.5955633|     |
|MajorityVoteWithNN(0.5) |20910 | 0.6288867|     |
|MergeEnoughVotes(1)     |20910 | 0.6622200|     |
|Matlab GP               |20916 | 0.6679245|*    |
|MajorityVote            |20916 | 0.6370370|     |
|MajorityVoteWithNN(0.5) |20916 | 0.6000000|     |
|MergeEnoughVotes(1)     |20916 | 0.6217391|     |
|Matlab GP               |20932 | 0.6786902|*    |
|MajorityVote            |20932 | 0.5977800|     |
|MajorityVoteWithNN(0.5) |20932 | 0.5755567|     |
|MergeEnoughVotes(1)     |20932 | 0.5977867|     |
|Matlab GP               |20956 | 0.8166667|*    |
|MajorityVote            |20956 | 0.5620690|     |
|MajorityVoteWithNN(0.5) |20956 | 0.6827586|     |
|MergeEnoughVotes(1)     |20956 | 0.6517241|     |
|Matlab GP               |20958 | 0.6894737|*    |
|MajorityVote            |20958 | 0.6516129|     |
|MajorityVoteWithNN(0.5) |20958 | 0.5322581|     |
|MergeEnoughVotes(1)     |20958 | 0.6419355|     |
|Matlab GP               |20962 | 0.6561404|     |
|MajorityVote            |20962 | 0.5935484|     |
|MajorityVoteWithNN(0.5) |20962 | 0.6290323|     |
|MergeEnoughVotes(1)     |20962 | 0.6612903|*    |
|Matlab GP               |20972 | 0.5222233|     |
|MajorityVote            |20972 | 0.6755633|     |
|MajorityVoteWithNN(0.5) |20972 | 0.6577800|     |
|MergeEnoughVotes(1)     |20972 | 0.6911100|*    |
|Matlab GP               |20976 | 0.6050000|     |
|MajorityVote            |20976 | 0.6379310|     |
|MajorityVoteWithNN(0.5) |20976 | 0.6379310|     |
|MergeEnoughVotes(1)     |20976 | 0.7068966|*    |
|Matlab GP               |20996 | 0.3400000|     |
|MajorityVote            |20996 | 0.5064516|     |
|MajorityVoteWithNN(0.5) |20996 | 0.5032258|     |
|MergeEnoughVotes(1)     |20996 | 0.5580645|*    |

List best methods for topics:


```r
best.methods <- means[means$Best == '*', c("Topic", "Method")]

kable(best.methods, format="markdown")
```



|    |Topic |Method                  |
|:---|:-----|:-----------------------|
|1   |20424 |Matlab GP               |
|5   |20488 |Matlab GP               |
|9   |20542 |Matlab GP               |
|13  |20584 |Matlab GP               |
|20  |20636 |MergeEnoughVotes(1)     |
|21  |20642 |Matlab GP               |
|25  |20686 |Matlab GP               |
|29  |20690 |Matlab GP               |
|33  |20694 |Matlab GP               |
|37  |20696 |Matlab GP               |
|41  |20704 |Matlab GP               |
|48  |20714 |MergeEnoughVotes(1)     |
|50  |20764 |MajorityVote            |
|56  |20766 |MergeEnoughVotes(1)     |
|59  |20778 |MajorityVoteWithNN(0.5) |
|60  |20778 |MergeEnoughVotes(1)     |
|61  |20780 |Matlab GP               |
|68  |20812 |MergeEnoughVotes(1)     |
|69  |20814 |Matlab GP               |
|76  |20832 |MergeEnoughVotes(1)     |
|77  |20910 |Matlab GP               |
|81  |20916 |Matlab GP               |
|85  |20932 |Matlab GP               |
|89  |20956 |Matlab GP               |
|93  |20958 |Matlab GP               |
|100 |20962 |MergeEnoughVotes(1)     |
|104 |20972 |MergeEnoughVotes(1)     |
|108 |20976 |MergeEnoughVotes(1)     |
|112 |20996 |MergeEnoughVotes(1)     |

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
##                      17                      10                       1 
## MajorityVoteWithNN(0.5) 
##                       1
```
