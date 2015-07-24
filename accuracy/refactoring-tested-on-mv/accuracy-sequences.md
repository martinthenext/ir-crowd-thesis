# accuracy-sequences.Rmd


```r
boxplot.accuracies <- function(filename) {

  before <- read.delim(filename, header=FALSE)
  
  before$V1 <- NULL
  # before$V2 <- as.factor(before$V2)
  before$V3 <- as.factor(before$V3)
  before$V5 <- as.factor(before$V5)
  colnames(before) <- c("VotesPerDoc", "RunId", "Method", "Topic", "Accuracy")
  
  head(before)
  
  mean.accuracy.df <- aggregate(Accuracy ~ VotesPerDoc, before, mean)
  plot(Accuracy ~ VotesPerDoc, data=mean.accuracy.df)
  
  boxplot(Accuracy ~ VotesPerDoc, data=before)
  
  print (mean.accuracy.df$Accuracy)
    
}

boxplot.accuracies("BEFORE-accuracy-1.0to1.2.tsv")
```

![](accuracy-sequences_files/figure-html/unnamed-chunk-1-1.png) ![](accuracy-sequences_files/figure-html/unnamed-chunk-1-2.png) 

```
##  [1] 0.6487462 0.6495856 0.6629162 0.6570831 0.6562487 0.6520819 0.6462488
##  [8] 0.6479169 0.6537513 0.6516700 0.6591669 0.6533331 0.6633306 0.6583325
## [15] 0.6625013 0.6704150 0.6720869 0.6716681 0.6745862 0.6675031 0.6729150
## [22] 0.6766656 0.6812525 0.6629150
```

```r
boxplot.accuracies("AFTER-BUGFIX1-accuracy-1.0to1.2.tsv")
```

![](accuracy-sequences_files/figure-html/unnamed-chunk-1-3.png) ![](accuracy-sequences_files/figure-html/unnamed-chunk-1-4.png) 

```
##  [1] 0.6423541 0.6465335 0.6526816 0.6507194 0.6554237 0.6529400 0.6577794
##  [8] 0.6605200 0.6560780 0.6573863 0.6628743 0.6589543 0.6573845 0.6618316
## [15] 0.6616980 0.6592161 0.6691508 0.6620892 0.6613075 0.6639225 0.6636604
## [22] 0.6624837 0.6675824 0.6661433
```
