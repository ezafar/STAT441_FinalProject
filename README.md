# Kaggle Competition - STAT441 W'24

## Description
In this kaggle contest, we will use a dataset to predict answers to the question "How important is religion in your life?". There are five possible responses for this question, which are: "no answer, very important, quite important, not important, not at all important".

Each observation represents a survey response of one person in different European countries. Your goal is to predict the correct response for this question based on the training dataset.

A more detailed description for each column could be found in the given file "codebook.txt".


## Evaluation
The evaluation metric for this competition is Multiclass Logarithmic Loss, which is the negative log likelihood divided by the number of observations. Lower is better.

### Submission Format

```
id,no answer,very important,quite important,not important,not at all important
0,0.2,0.2,0.2,0.2,0.2
1,0.2,0.2,0.2,0.2,0.2
2,0.2,0.2,0.2,0.2,0.2
3,0.2,0.2,0.2,0.2,0.2
```


## Dataset

In this kaggle contest, we will use a dataset of survey results to predict "how is religion important in one's life". There are five possible responses for this question, which are: {'no answer':-1, 'very important':1, 'quite important':2, 'not important':3, 'not at all important':4}.

The data contains 48,000 observations for training data and 11438 observations for test data.

Each observation is a survey response of one person in different European countries.

