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


## Deliverables

- Report (Grad)
- Video



# Project Checklist

## Preprocessing
- [ ] Highlights from exploratory data analysis, if appropriate
- [ ] Appropriate choices for variables with missing values
- [ ] Appropriate choices for categorical and ordinal variables.
- [ ] Appropriate choices for any unusual circumstances


## Feature Engineering
- [ ] (The opportunity to create new variables varies widely by dataset, may not be appropriate for all data sets)
- [ ] Were any new variables derived?
- [ ] Are the new features creative/innovative/sensible?

## Modeling
- [ ] Use of at least 2 different techniques (gradient boosting and xgboost are both boosting and are NOT considered two different techniques)
- [ ] If an algorithm was used that was not discussed in class, there is sufficient explanation to make the reader believe the authors understand the algorithm
- [ ] Appropriate tuning
- [ ] It is clear how the model is used (what key choices have been made)
- [ ] (negative) Algorithm is presented in terms of which software button/software option) to push
- [ ] (negative) Reader gets the impression that the algorithms are not really understood


## Stacking
- [ ] (stacking may not be appropriate/useful for all data sets)
- [ ] Did the authors attempt stacking?
- [ ] Is it clear how exactly stacking was used?


## Clarity
- [ ] (key) Writing is easy to understand. Ideas are easy to follow.
- [ ] Figures: axis labels/any text are readable
- [ ] Tables are readable
- [ ] Are human-understandable names used? (x5 being an important variable means nothing to me. Income being an important variable does. If brevity demands, you can use x5 in a graph or formula as long as there is an explanation nearby).
- [ ] (report only) Figures and tables are referred to in the text.
- [ ] (report only) Figures and tables have a caption.
- [ ] (report only) Report starts with a well written abstract

## Insight
- [ ] Did the reader gain any special insight about the data or techniques used? Examples:
    - A particular feature engineered variable was key (ideally quantify in some way)
    - None of the feature engineering variables mattered. If appropriate, a brief reflection about why this is surprising.
    - Stacking was key (ideally, quantify in some way)
    - Something was surprising because …
    - Original variable <readable name> was key. (ideally, quantify in some way)
    - A pre-processing step was key
- [ ] Insight can be the icing on the cake, but do not overdo it.
- [ ] (strong negative) A laundry list of things that are not really insightful. It means the authors have difficulties understanding the essential aspects of their results.


## Participation
- [ ] (Presentation) All team members present. The presentation time should not be highly uneven (a bit uneven is ok, it is the nature of things)
- [ ] All team members contribute to analysis, coding and presentation/report.

