# GP accuracy

Here accuracy of GP method is analyzed. 


```r
accuracy <- read.delim("accuracy_1_vote_per_doc", header=FALSE)
names(accuracy) <- c("Method", "Topic", "Accuracy")
accuracy$Topic <- as.factor(accuracy$Topic)
```

Number of observations per topic:



```r
one.topic <- levels(accuracy$Topic)[1]
length(accuracy$Topic[accuracy$Topic == one.topic])
```

```
## [1] 61
```

Remove `NA` values


```r
accuracy <- accuracy[!is.na(accuracy$Accuracy), ]
```

Mean accuracies for topics


```r
library(knitr)
kable(aggregate(Accuracy ~ Topic, accuracy, mean))
```



Topic     Accuracy
------  ----------
20424    0.6970588
20488    0.7896552
20542    0.7433333
20584    0.8484254
20636    0.7266667
20642    0.8500050
20686    0.7411083
20690    0.8340000
20694    0.8122951
20696    0.7227273
20704    0.9403846
20714    0.8666667
20764    0.4816667
20766    0.8406780
20778    0.6836066
20780    0.7934426
20812    0.7080483
20814    0.8912281
20832    0.7116667
20910    0.6666738
20916    0.6679245
20932    0.6786902
20956    0.8166667
20958    0.6894737
20962    0.6561404
20972    0.5222233
20976    0.6050000
20996    0.3400000

