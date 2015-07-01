# Accuracy comparison at 1 vote per document

## Dataset

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
## [1] 30795
```

```r
head(accuracy)
```

```
##                    Method Topic Accuracy
## 1 MajorityVoteWithNN(0.5) 20714      1.0
## 2 MajorityVoteWithNN(0.5) 20714      0.9
## 3     MergeEnoughVotes(1) 20714      0.8
## 4            MajorityVote 20696      0.7
## 5     MergeEnoughVotes(1) 20696      0.6
## 6            MajorityVote 20696      0.3
```

Look at amount of data available for different topics:


```r
library(knitr)

topic.rows.sorted <- as.data.frame(sort(table(accuracy$Topic)))
colnames(topic.rows.sorted) <- "Points in dataset"
kable(topic.rows.sorted, format="markdown")
```



|      | Points in dataset|
|:-----|-----------------:|
|20714 |               150|
|20696 |               327|
|20424 |               706|
|20916 |              1059|
|20704 |              1078|
|20584 |              1157|
|20780 |              1160|
|20814 |              1183|
|20488 |              1197|
|20642 |              1197|
|20694 |              1197|
|20832 |              1197|
|20958 |              1197|
|20766 |              1198|
|20976 |              1198|
|20686 |              1199|
|20690 |              1199|
|20910 |              1199|
|20932 |              1199|
|20972 |              1199|
|20996 |              1199|
|20542 |              1200|
|20636 |              1200|
|20764 |              1200|
|20778 |              1200|
|20812 |              1200|
|20956 |              1200|
|20962 |              1200|

Amount of data available for different methods:


```r
method.rows.sorted <- as.data.frame(sort(table(accuracy$Method)))
colnames(method.rows.sorted) <- "Points in dataset"
kable(method.rows.sorted, format="markdown")
```



|                        | Points in dataset|
|:-----------------------|-----------------:|
|Matlab GP               |              7678|
|MajorityVoteWithNN(0.5) |              7684|
|MajorityVote            |              7710|
|MergeEnoughVotes(1)     |              7723|

Method classes are balanced, safe for testing.

## Computing accuracy

Calculate mean accuracies:


```r
means <- aggregate(Accuracy ~ Method + Topic, accuracy, mean)
```

Let us print a star in front of a best method for a topic


```r
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
|MajorityVote            |20424 | 0.6127778|     |
|MajorityVoteWithNN(0.5) |20424 | 0.6267857|     |
|Matlab GP               |20424 | 0.7210227|*    |
|MergeEnoughVotes(1)     |20424 | 0.6258242|     |
|MajorityVote            |20488 | 0.6763333|     |
|MajorityVoteWithNN(0.5) |20488 | 0.7563333|     |
|Matlab GP               |20488 | 0.8225589|*    |
|MergeEnoughVotes(1)     |20488 | 0.7620000|     |
|MajorityVote            |20542 | 0.6880000|     |
|MajorityVoteWithNN(0.5) |20542 | 0.6853320|     |
|Matlab GP               |20542 | 0.7151107|     |
|MergeEnoughVotes(1)     |20542 | 0.7308923|*    |
|MajorityVote            |20584 | 0.6876828|     |
|MajorityVoteWithNN(0.5) |20584 | 0.7578303|     |
|Matlab GP               |20584 | 0.8586314|*    |
|MergeEnoughVotes(1)     |20584 | 0.7887714|     |
|MajorityVote            |20636 | 0.6826667|     |
|MajorityVoteWithNN(0.5) |20636 | 0.7396667|     |
|Matlab GP               |20636 | 0.7093333|     |
|MergeEnoughVotes(1)     |20636 | 0.7653333|*    |
|MajorityVote            |20642 | 0.7035543|     |
|MajorityVoteWithNN(0.5) |20642 | 0.7271133|     |
|Matlab GP               |20642 | 0.8673391|*    |
|MergeEnoughVotes(1)     |20642 | 0.7675553|     |
|MajorityVote            |20686 | 0.7075557|*    |
|MajorityVoteWithNN(0.5) |20686 | 0.6291127|     |
|Matlab GP               |20686 | 0.7054622|     |
|MergeEnoughVotes(1)     |20686 | 0.6879993|     |
|MajorityVote            |20690 | 0.6909333|     |
|MajorityVoteWithNN(0.5) |20690 | 0.7302667|     |
|Matlab GP               |20690 | 0.8287625|*    |
|MergeEnoughVotes(1)     |20690 | 0.7720000|     |
|MajorityVote            |20694 | 0.7260000|     |
|MajorityVoteWithNN(0.5) |20694 | 0.7700000|     |
|Matlab GP               |20694 | 0.8232323|*    |
|MergeEnoughVotes(1)     |20694 | 0.8041667|     |
|MajorityVote            |20696 | 0.5390805|     |
|MajorityVoteWithNN(0.5) |20696 | 0.6197531|     |
|Matlab GP               |20696 | 0.7213333|*    |
|MergeEnoughVotes(1)     |20696 | 0.6571429|     |
|MajorityVote            |20704 | 0.6959108|     |
|MajorityVoteWithNN(0.5) |20704 | 0.8157895|     |
|Matlab GP               |20704 | 0.9422222|*    |
|MergeEnoughVotes(1)     |20704 | 0.8131868|     |
|MajorityVote            |20714 | 0.8258065|     |
|MajorityVoteWithNN(0.5) |20714 | 0.8500000|     |
|Matlab GP               |20714 | 0.9106383|*    |
|MergeEnoughVotes(1)     |20714 | 0.8526316|     |
|MajorityVote            |20764 | 0.6593333|     |
|MajorityVoteWithNN(0.5) |20764 | 0.6350000|     |
|Matlab GP               |20764 | 0.4600000|     |
|MergeEnoughVotes(1)     |20764 | 0.6810000|*    |
|MajorityVote            |20766 | 0.7678930|     |
|MajorityVoteWithNN(0.5) |20766 | 0.7913043|     |
|Matlab GP               |20766 | 0.8246667|     |
|MergeEnoughVotes(1)     |20766 | 0.8563333|*    |
|MajorityVote            |20778 | 0.6343333|     |
|MajorityVoteWithNN(0.5) |20778 | 0.6856667|     |
|Matlab GP               |20778 | 0.6963333|*    |
|MergeEnoughVotes(1)     |20778 | 0.6940000|     |
|MajorityVote            |20780 | 0.6793093|     |
|MajorityVoteWithNN(0.5) |20780 | 0.7328721|     |
|Matlab GP               |20780 | 0.7917193|*    |
|MergeEnoughVotes(1)     |20780 | 0.7586214|     |
|MajorityVote            |20812 | 0.6866670|     |
|MajorityVoteWithNN(0.5) |20812 | 0.7146683|     |
|Matlab GP               |20812 | 0.7135560|     |
|MergeEnoughVotes(1)     |20812 | 0.7295550|*    |
|MajorityVote            |20814 | 0.7807432|     |
|MajorityVoteWithNN(0.5) |20814 | 0.7552189|     |
|Matlab GP               |20814 | 0.9149153|*    |
|MergeEnoughVotes(1)     |20814 | 0.8776271|     |
|MajorityVote            |20832 | 0.6581940|     |
|MajorityVoteWithNN(0.5) |20832 | 0.6696667|     |
|Matlab GP               |20832 | 0.6768456|*    |
|MergeEnoughVotes(1)     |20832 | 0.6760000|     |
|MajorityVote            |20910 | 0.6486680|     |
|MajorityVoteWithNN(0.5) |20910 | 0.6435563|     |
|Matlab GP               |20910 | 0.6802732|     |
|MergeEnoughVotes(1)     |20910 | 0.6973343|*    |
|MajorityVote            |20916 | 0.6327138|     |
|MajorityVoteWithNN(0.5) |20916 | 0.6208494|     |
|Matlab GP               |20916 | 0.7007692|*    |
|MergeEnoughVotes(1)     |20916 | 0.6343173|     |
|MajorityVote            |20932 | 0.5768897|     |
|MajorityVoteWithNN(0.5) |20932 | 0.5742210|     |
|Matlab GP               |20932 | 0.6804903|*    |
|MergeEnoughVotes(1)     |20932 | 0.5891117|     |
|MajorityVote            |20956 | 0.6280000|     |
|MajorityVoteWithNN(0.5) |20956 | 0.6370000|     |
|Matlab GP               |20956 | 0.8216667|*    |
|MergeEnoughVotes(1)     |20956 | 0.6603333|     |
|MajorityVote            |20958 | 0.6016667|     |
|MajorityVoteWithNN(0.5) |20958 | 0.6020000|     |
|Matlab GP               |20958 | 0.6639731|*    |
|MergeEnoughVotes(1)     |20958 | 0.6400000|     |
|MajorityVote            |20962 | 0.5760000|     |
|MajorityVoteWithNN(0.5) |20962 | 0.6013333|     |
|Matlab GP               |20962 | 0.6620000|*    |
|MergeEnoughVotes(1)     |20962 | 0.6046667|     |
|MajorityVote            |20972 | 0.6826657|     |
|MajorityVoteWithNN(0.5) |20972 | 0.6426703|     |
|Matlab GP               |20972 | 0.4744729|     |
|MergeEnoughVotes(1)     |20972 | 0.7035560|*    |
|MajorityVote            |20976 | 0.6596667|     |
|MajorityVoteWithNN(0.5) |20976 | 0.6563333|     |
|Matlab GP               |20976 | 0.6067114|     |
|MergeEnoughVotes(1)     |20976 | 0.7046667|*    |
|MajorityVote            |20996 | 0.5693333|*    |
|MajorityVoteWithNN(0.5) |20996 | 0.5336667|     |
|Matlab GP               |20996 | 0.3668896|     |
|MergeEnoughVotes(1)     |20996 | 0.5530000|     |

## Results

### Best methods for topics


```r
best.methods <- means[means$Best == '*', c("Topic", "Method")]

row.names(best.methods) <- NULL
kable(best.methods, format="markdown")
```



|Topic |Method              |
|:-----|:-------------------|
|20424 |Matlab GP           |
|20488 |Matlab GP           |
|20542 |MergeEnoughVotes(1) |
|20584 |Matlab GP           |
|20636 |MergeEnoughVotes(1) |
|20642 |Matlab GP           |
|20686 |MajorityVote        |
|20690 |Matlab GP           |
|20694 |Matlab GP           |
|20696 |Matlab GP           |
|20704 |Matlab GP           |
|20714 |Matlab GP           |
|20764 |MergeEnoughVotes(1) |
|20766 |MergeEnoughVotes(1) |
|20778 |Matlab GP           |
|20780 |Matlab GP           |
|20812 |MergeEnoughVotes(1) |
|20814 |Matlab GP           |
|20832 |Matlab GP           |
|20910 |MergeEnoughVotes(1) |
|20916 |Matlab GP           |
|20932 |Matlab GP           |
|20956 |Matlab GP           |
|20958 |Matlab GP           |
|20962 |Matlab GP           |
|20972 |MergeEnoughVotes(1) |
|20976 |MergeEnoughVotes(1) |
|20996 |MajorityVote        |

### Method totals


```r
counts <- table(best.methods$Method)
counts <- counts[counts!=0]
counts <- counts[order(counts, decreasing=TRUE)]
counts
```

```
## 
##           Matlab GP MergeEnoughVotes(1)        MajorityVote 
##                  18                   8                   2
```
