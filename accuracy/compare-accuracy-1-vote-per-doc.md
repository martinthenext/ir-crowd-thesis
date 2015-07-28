# Accuracy comparison at 1 vote per document

## Dataset

Reading accuracy levels for different methods from a `tsv` file.


```r
filename <- "after-random-votes/seq-around1-first.tsv"

col.names <- c("AC", "NVotes", "RunId", "Method", "Topic", "Accuracy")
col.types <- c("character", "numeric", "factor", "factor", "factor", "numeric")

accuracy <- read.delim(filename, header=FALSE, col.names = col.names, colClasses = col.types)
accuracy$AC <- NULL

head(accuracy)
```

```
##   NVotes               RunId    Method Topic Accuracy
## 1     90 6988017342641747161        MV 20972   0.5333
## 2     90 6988017342641747161    MEV(1) 20972   0.5333
## 3     90 6988017342641747161 MVNN(0.5) 20972   0.6000
## 4     90 6988017342641747161        GP 20972   0.7333
## 5     90 8955059189446076658        MV 20972   0.4667
## 6     90 8955059189446076658    MEV(1) 20972   0.7333
```

```r
nrow(accuracy)
```

```
## [1] 3360
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
|20424 |               120|
|20488 |               120|
|20542 |               120|
|20584 |               120|
|20636 |               120|
|20642 |               120|
|20686 |               120|
|20690 |               120|
|20694 |               120|
|20696 |               120|
|20704 |               120|
|20714 |               120|
|20764 |               120|
|20766 |               120|
|20778 |               120|
|20780 |               120|
|20812 |               120|
|20814 |               120|
|20832 |               120|
|20910 |               120|
|20916 |               120|
|20932 |               120|
|20956 |               120|
|20958 |               120|
|20962 |               120|
|20972 |               120|
|20976 |               120|
|20996 |               120|

Amount of data available for different methods:


```r
method.rows.sorted <- as.data.frame(sort(table(accuracy$Method)))
colnames(method.rows.sorted) <- "Points in dataset"
kable(method.rows.sorted, format="markdown")
```



|          | Points in dataset|
|:---------|-----------------:|
|GP        |               840|
|MEV(1)    |               840|
|MV        |               840|
|MVNN(0.5) |               840|

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



|Method    |Topic |  Accuracy|Best |
|:---------|:-----|---------:|:----|
|GP        |20424 | 0.7400000|*    |
|MEV(1)    |20424 | 0.6433333|     |
|MV        |20424 | 0.6033333|     |
|MVNN(0.5) |20424 | 0.6533333|     |
|GP        |20488 | 0.8033333|*    |
|MEV(1)    |20488 | 0.7566667|     |
|MV        |20488 | 0.7000000|     |
|MVNN(0.5) |20488 | 0.7900000|     |
|GP        |20542 | 0.7355567|     |
|MEV(1)    |20542 | 0.7444433|*    |
|MV        |20542 | 0.7044433|     |
|MVNN(0.5) |20542 | 0.6822267|     |
|GP        |20584 | 0.8571333|*    |
|MEV(1)    |20584 | 0.7971433|     |
|MV        |20584 | 0.6885767|     |
|MVNN(0.5) |20584 | 0.7647633|     |
|GP        |20636 | 0.7200000|     |
|MEV(1)    |20636 | 0.7733333|*    |
|MV        |20636 | 0.7400000|     |
|MVNN(0.5) |20636 | 0.7633333|     |
|GP        |20642 | 0.8422233|*    |
|MEV(1)    |20642 | 0.7489000|     |
|MV        |20642 | 0.7022233|     |
|MVNN(0.5) |20642 | 0.7288867|     |
|GP        |20686 | 0.7444433|     |
|MEV(1)    |20686 | 0.7088900|     |
|MV        |20686 | 0.7466700|*    |
|MVNN(0.5) |20686 | 0.6800000|     |
|GP        |20690 | 0.8240000|*    |
|MEV(1)    |20690 | 0.7800000|     |
|MV        |20690 | 0.6960000|     |
|MVNN(0.5) |20690 | 0.7413333|     |
|GP        |20694 | 0.8116667|*    |
|MEV(1)    |20694 | 0.7933333|     |
|MV        |20694 | 0.7316667|     |
|MVNN(0.5) |20694 | 0.7833333|     |
|GP        |20696 | 0.7200000|*    |
|MEV(1)    |20696 | 0.6000000|     |
|MV        |20696 | 0.5266667|     |
|MVNN(0.5) |20696 | 0.5866667|     |
|GP        |20704 | 0.9633333|*    |
|MEV(1)    |20704 | 0.8300000|     |
|MV        |20704 | 0.6900000|     |
|MVNN(0.5) |20704 | 0.7866667|     |
|GP        |20714 | 0.9000000|*    |
|MEV(1)    |20714 | 0.8433333|     |
|MV        |20714 | 0.7733333|     |
|MVNN(0.5) |20714 | 0.8200000|     |
|GP        |20764 | 0.3600000|     |
|MEV(1)    |20764 | 0.7033333|*    |
|MV        |20764 | 0.6633333|     |
|MVNN(0.5) |20764 | 0.6166667|     |
|GP        |20766 | 0.8200000|     |
|MEV(1)    |20766 | 0.8700000|*    |
|MV        |20766 | 0.7766667|     |
|MVNN(0.5) |20766 | 0.7866667|     |
|GP        |20778 | 0.7066667|*    |
|MEV(1)    |20778 | 0.6833333|     |
|MV        |20778 | 0.6400000|     |
|MVNN(0.5) |20778 | 0.6766667|     |
|GP        |20780 | 0.8133367|*    |
|MEV(1)    |20780 | 0.7377733|     |
|MV        |20780 | 0.6355467|     |
|MVNN(0.5) |20780 | 0.7088933|     |
|GP        |20812 | 0.7022267|     |
|MEV(1)    |20812 | 0.7133333|*    |
|MV        |20812 | 0.6444467|     |
|MVNN(0.5) |20812 | 0.7022300|     |
|GP        |20814 | 0.8800000|*    |
|MEV(1)    |20814 | 0.8600000|     |
|MV        |20814 | 0.7600000|     |
|MVNN(0.5) |20814 | 0.7533333|     |
|GP        |20832 | 0.6366667|     |
|MEV(1)    |20832 | 0.7166667|*    |
|MV        |20832 | 0.6800000|     |
|MVNN(0.5) |20832 | 0.6900000|     |
|GP        |20910 | 0.6866667|     |
|MEV(1)    |20910 | 0.7355600|*    |
|MV        |20910 | 0.7133267|     |
|MVNN(0.5) |20910 | 0.6866667|     |
|GP        |20916 | 0.6366667|*    |
|MEV(1)    |20916 | 0.6000000|     |
|MV        |20916 | 0.6000000|     |
|MVNN(0.5) |20916 | 0.6100000|     |
|GP        |20932 | 0.6577833|*    |
|MEV(1)    |20932 | 0.5911067|     |
|MV        |20932 | 0.5600000|     |
|MVNN(0.5) |20932 | 0.5844400|     |
|GP        |20956 | 0.8400000|*    |
|MEV(1)    |20956 | 0.7000000|     |
|MV        |20956 | 0.6800000|     |
|MVNN(0.5) |20956 | 0.6800000|     |
|GP        |20958 | 0.6933333|*    |
|MEV(1)    |20958 | 0.6400000|     |
|MV        |20958 | 0.6233333|     |
|MVNN(0.5) |20958 | 0.5933333|     |
|GP        |20962 | 0.6666667|*    |
|MEV(1)    |20962 | 0.6033333|     |
|MV        |20962 | 0.5900000|     |
|MVNN(0.5) |20962 | 0.6000000|     |
|GP        |20972 | 0.4777800|     |
|MEV(1)    |20972 | 0.6800000|*    |
|MV        |20972 | 0.6622233|     |
|MVNN(0.5) |20972 | 0.6377767|     |
|GP        |20976 | 0.6033333|     |
|MEV(1)    |20976 | 0.7000000|*    |
|MV        |20976 | 0.6366667|     |
|MVNN(0.5) |20976 | 0.6700000|     |
|GP        |20996 | 0.3633333|     |
|MEV(1)    |20996 | 0.5366667|     |
|MV        |20996 | 0.5633333|*    |
|MVNN(0.5) |20996 | 0.5266667|     |

## Results

### Best methods for topics


```r
best.methods <- means[means$Best == '*', c("Topic", "Method")]

row.names(best.methods) <- NULL
kable(best.methods, format="markdown")
```



|Topic |Method |
|:-----|:------|
|20424 |GP     |
|20488 |GP     |
|20542 |MEV(1) |
|20584 |GP     |
|20636 |MEV(1) |
|20642 |GP     |
|20686 |MV     |
|20690 |GP     |
|20694 |GP     |
|20696 |GP     |
|20704 |GP     |
|20714 |GP     |
|20764 |MEV(1) |
|20766 |MEV(1) |
|20778 |GP     |
|20780 |GP     |
|20812 |MEV(1) |
|20814 |GP     |
|20832 |MEV(1) |
|20910 |MEV(1) |
|20916 |GP     |
|20932 |GP     |
|20956 |GP     |
|20958 |GP     |
|20962 |GP     |
|20972 |MEV(1) |
|20976 |MEV(1) |
|20996 |MV     |

### Method totals


```r
counts <- table(best.methods$Method)
counts <- counts[counts!=0]
counts <- counts[order(counts, decreasing=TRUE)]
counts
```

```
## 
##     GP MEV(1)     MV 
##     17      9      2
```
