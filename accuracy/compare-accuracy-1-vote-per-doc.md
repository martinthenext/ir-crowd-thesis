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
## [1] 9120
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
|20584 |               120|
|20972 |               120|
|20976 |               120|
|20996 |               120|
|20424 |               360|
|20488 |               360|
|20542 |               360|
|20636 |               360|
|20642 |               360|
|20686 |               360|
|20690 |               360|
|20694 |               360|
|20696 |               360|
|20704 |               360|
|20714 |               360|
|20764 |               360|
|20766 |               360|
|20778 |               360|
|20780 |               360|
|20812 |               360|
|20814 |               360|
|20832 |               360|
|20910 |               360|
|20916 |               360|
|20932 |               360|
|20956 |               360|
|20958 |               360|
|20962 |               360|

Amount of data available for different methods:


```r
method.rows.sorted <- as.data.frame(sort(table(accuracy$Method)))
colnames(method.rows.sorted) <- "Points in dataset"
kable(method.rows.sorted, format="markdown")
```



|          | Points in dataset|
|:---------|-----------------:|
|GP        |              2280|
|MEV(1)    |              2280|
|MV        |              2280|
|MVNN(0.5) |              2280|

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
|GP        |20424 | 0.7277778|*    |
|MEV(1)    |20424 | 0.6544444|     |
|MV        |20424 | 0.6055556|     |
|MVNN(0.5) |20424 | 0.6533333|     |
|GP        |20488 | 0.8222222|*    |
|MEV(1)    |20488 | 0.7666667|     |
|MV        |20488 | 0.6777778|     |
|MVNN(0.5) |20488 | 0.7588889|     |
|GP        |20542 | 0.7259267|     |
|MEV(1)    |20542 | 0.7303667|*    |
|MV        |20542 | 0.6822233|     |
|MVNN(0.5) |20542 | 0.6903689|     |
|GP        |20584 | 0.8571333|*    |
|MEV(1)    |20584 | 0.7971433|     |
|MV        |20584 | 0.6885767|     |
|MVNN(0.5) |20584 | 0.7647633|     |
|GP        |20636 | 0.7166667|     |
|MEV(1)    |20636 | 0.7600000|*    |
|MV        |20636 | 0.7044444|     |
|MVNN(0.5) |20636 | 0.7477778|     |
|GP        |20642 | 0.8666667|*    |
|MEV(1)    |20642 | 0.7725956|     |
|MV        |20642 | 0.7177789|     |
|MVNN(0.5) |20642 | 0.7459289|     |
|GP        |20686 | 0.7177744|*    |
|MEV(1)    |20686 | 0.6681533|     |
|MV        |20686 | 0.7088878|     |
|MVNN(0.5) |20686 | 0.6407433|     |
|GP        |20690 | 0.8213333|*    |
|MEV(1)    |20690 | 0.7662222|     |
|MV        |20690 | 0.6973333|     |
|MVNN(0.5) |20690 | 0.7333333|     |
|GP        |20694 | 0.8105556|*    |
|MEV(1)    |20694 | 0.7938889|     |
|MV        |20694 | 0.7222222|     |
|MVNN(0.5) |20694 | 0.7633333|     |
|GP        |20696 | 0.7144444|*    |
|MEV(1)    |20696 | 0.6155556|     |
|MV        |20696 | 0.5466667|     |
|MVNN(0.5) |20696 | 0.6088889|     |
|GP        |20704 | 0.9466667|*    |
|MEV(1)    |20704 | 0.8155556|     |
|MV        |20704 | 0.6822222|     |
|MVNN(0.5) |20704 | 0.8044444|     |
|GP        |20714 | 0.8811111|*    |
|MEV(1)    |20714 | 0.8522222|     |
|MV        |20714 | 0.7988889|     |
|MVNN(0.5) |20714 | 0.8266667|     |
|GP        |20764 | 0.3977778|     |
|MEV(1)    |20764 | 0.6888889|*    |
|MV        |20764 | 0.6533333|     |
|MVNN(0.5) |20764 | 0.6111111|     |
|GP        |20766 | 0.8277778|     |
|MEV(1)    |20766 | 0.8755556|*    |
|MV        |20766 | 0.7900000|     |
|MVNN(0.5) |20766 | 0.7955556|     |
|GP        |20778 | 0.6977778|     |
|MEV(1)    |20778 | 0.6900000|     |
|MV        |20778 | 0.6622222|     |
|MVNN(0.5) |20778 | 0.6977778|*    |
|GP        |20780 | 0.7844478|*    |
|MEV(1)    |20780 | 0.7599967|     |
|MV        |20780 | 0.6636989|     |
|MVNN(0.5) |20780 | 0.7185211|     |
|GP        |20812 | 0.7185200|     |
|MEV(1)    |20812 | 0.7274067|*    |
|MV        |20812 | 0.6770400|     |
|MVNN(0.5) |20812 | 0.7185200|     |
|GP        |20814 | 0.8944444|*    |
|MEV(1)    |20814 | 0.8633333|     |
|MV        |20814 | 0.7777778|     |
|MVNN(0.5) |20814 | 0.7633333|     |
|GP        |20832 | 0.6822222|     |
|MEV(1)    |20832 | 0.6966667|*    |
|MV        |20832 | 0.6477778|     |
|MVNN(0.5) |20832 | 0.6744444|     |
|GP        |20910 | 0.6844456|     |
|MEV(1)    |20910 | 0.7177789|*    |
|MV        |20910 | 0.6933311|     |
|MVNN(0.5) |20910 | 0.6585167|     |
|GP        |20916 | 0.6888889|*    |
|MEV(1)    |20916 | 0.6288889|     |
|MV        |20916 | 0.6177778|     |
|MVNN(0.5) |20916 | 0.6411111|     |
|GP        |20932 | 0.6696356|*    |
|MEV(1)    |20932 | 0.6022178|     |
|MV        |20932 | 0.5807389|     |
|MVNN(0.5) |20932 | 0.5733311|     |
|GP        |20956 | 0.8311111|*    |
|MEV(1)    |20956 | 0.7055556|     |
|MV        |20956 | 0.6688889|     |
|MVNN(0.5) |20956 | 0.6977778|     |
|GP        |20958 | 0.6733333|*    |
|MEV(1)    |20958 | 0.6288889|     |
|MV        |20958 | 0.6211111|     |
|MVNN(0.5) |20958 | 0.5833333|     |
|GP        |20962 | 0.6555556|*    |
|MEV(1)    |20962 | 0.6077778|     |
|MV        |20962 | 0.5600000|     |
|MVNN(0.5) |20962 | 0.5866667|     |
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



|Topic |Method    |
|:-----|:---------|
|20424 |GP        |
|20488 |GP        |
|20542 |MEV(1)    |
|20584 |GP        |
|20636 |MEV(1)    |
|20642 |GP        |
|20686 |GP        |
|20690 |GP        |
|20694 |GP        |
|20696 |GP        |
|20704 |GP        |
|20714 |GP        |
|20764 |MEV(1)    |
|20766 |MEV(1)    |
|20778 |MVNN(0.5) |
|20780 |GP        |
|20812 |MEV(1)    |
|20814 |GP        |
|20832 |MEV(1)    |
|20910 |MEV(1)    |
|20916 |GP        |
|20932 |GP        |
|20956 |GP        |
|20958 |GP        |
|20962 |GP        |
|20972 |MEV(1)    |
|20976 |MEV(1)    |
|20996 |MV        |

### Method totals


```r
counts <- table(best.methods$Method)
counts <- counts[counts!=0]
counts <- counts[order(counts, decreasing=TRUE)]
counts
```

```
## 
##        GP    MEV(1)        MV MVNN(0.5) 
##        17         9         1         1
```
