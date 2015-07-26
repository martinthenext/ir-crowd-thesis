# 1to3votesPerDoc


```r
filename <- "seq-1to3.first-run.tsv"
col.names <- c("AC", "NVotes", "RunId", "Method", "Topic", "Accuracy")
col.types <- c("character", "numeric", "factor", "character", "factor", "numeric")

accuracy <- read.delim(filename, header=FALSE, col.names = col.names, colClasses = col.types)
accuracy$AC <- NULL

head(accuracy)
```

```
##   NVotes               RunId Method Topic Accuracy
## 1     90 1505634721106260714     MV 20972   0.6000
## 2     91 1505634721106260714     MV 20972   0.7333
## 3     92 1505634721106260714     MV 20972   0.6667
## 4     93 1505634721106260714     MV 20972   0.6000
## 5     94 1505634721106260714     MV 20972   0.7333
## 6     95 1505634721106260714     MV 20972   0.6667
```
