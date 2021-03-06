# Lecture 5 - February 2, 2018

## Data Wrangling
- Real data is messy
- Can clean things up to make it easier to work with

### Wide vs Long Data
- Basically rows vs. column vectors
- Use `reshape2`
- `dcast`: long -> wide
- `melt`: wide -> long

#### Wide

| Stock | Date | Price |
|-|-|-|
| APPL | 2017-01-01 | 101 |
| APPL | 2017-02-01 | 105 |
| APPL | 2017-03-01 | 125 |

```r
dcast(stocks, tic~date, value.var='PRC', fun.aggregate='sum'_
```

#### Long

| Stock | Jan1 | Feb1 | March1 |
|-|-|-|-|
| APPL | 101 | 105 | 125 |

## Midterm
- In 2 weeks
- 1 hour

## Similarity and Recommendation - Clustering
- Possible means of classification: look at the k-closest neighbours

### K Nearest Neighbours
- Given an unlabelled data element, x, classify it
- Look at the classes of the k closest neighbours
- Assign the most common class to x

- Can use euclidian distance (in the n-dimensional space of features)
- Could potentially weight the neighbours depending on their distance from the origin point.

#### Implications
- As we increase k, some regions may collapse. There may not be enough samples within the class, meaning the closest are a different class.
  - Misclassification, potentially higher error
  - Eventually, as k becomes very large, we will only classify the largest class.
- Increasing k creates a simpler model.

#### Similarity Metrics
- How do we define "distance" / which points are closest?

##### euclidean distance
- sqrt of the sum of differences of squares of each feature
- i.e. L2 Norm

##### Manhattan distance
- sum of the absolute differences

##### Cosine distance
- Cosine of the angle between pair of individuals
- magnitude of the angle
- ![latex-8682e92b-319d-4c77-ad2e-7cf1eb584ec8](data/lecture5/latex-8682e92b-319d-4c77-ad2e-7cf1eb584ec8.png)
- Can give better indication of similarity than euclidean distance.
  - Consider volume of 2 products
  - As people buy fewer of products, it may be closer (euclidean) to other products causing misclassifications than it is to people who bought more of the same product.
  - Using cosine angle, same products have the same angle

#### Use cases
- May want to weight the neighbours based off their distance
- Perform some sort of aggregation, depending on your use case.

##### Classification
- Choose the most popular category of neighbours

##### Probability estimation
- Return proportion of the neighbours for each category

##### Regression
- Take a mean / median for Y values of the neighbours

### Recommendation
- Prediction task based off of past usage, usage of other users / customers etc.

#### Characteristics of data
- when training models, there are unique characteristics of data
- problems when compared to other types of inference.
- We want to make useful predictions for users

##### Data set is very wide
- There could be hundreds/thousands/millions of products to select from
- Multiple data points from each item
- Need to choose a subset from a large data set,
- ex. rows could look like: `(cid, item1, item2, item3, ...., itemn)`

##### Sparse Data
- Most users have only purchased a small number of items
- Lots of missing data
- How can we make good inferences?

##### Noisy
- For example: review data
- Some users have a positive / negative / neutral bias
- This can skew our recommendations

#### How to recommend

##### Bad
- could try to predict purchases for each unpurchased item
- rank based off of probability
- Too many predictions

##### Collaborative Filtering
- Designed for sparse, wide data
- Can use nearest neighbours
- latent variable
  - engineer new features
  - could be some common underlying features that actually cause the behaviour.
