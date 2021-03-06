# Lecture 1 - May 2, 2018

## Midterm and Final
- Open notes, no electronics
- All theoretical questions, concepts. No programming / pseudocode needed.

## What is Machine Learning
- computers learn without being explicitly programmed
- Automatically detect patterns in data
  - use these underlying patterns to predict future results
  - perform descision making under uncertainty
- Today, increased capabilities of hardware, cheaper storage, **big datasets**
  - Enables more learning oppourtunities

### Learning Categories

#### Supervised Learning
- Learn from an existing dataset (features and some target)
- Use the model to predict targets for new samples
- Regression: Predict some continuous labels
  - A model will map a function that fits to the training data points. A good hypothesis will generalize well to new, unseen data samples (not overfit to the training set).
  - example: Future Stock price
- Classification: Predict some descrete class based on features
  - Example: The type of animal in a picture

##### Formally
- Given a training set of input features and output labels, return some function which is capable of producing a new label given a feature set.
- ![latex-f3f0241b-7251-4eb1-a88f-45457ef4de57](data/lecture1/latex-f3f0241b-7251-4eb1-a88f-45457ef4de57.png)
  - h: hypothesis

Define some loss (error) function to train the model. This function determines the error from the predicted labels (![latex-a9ad79f3-b5c2-4d32-923d-67a72e22f7b2](data/lecture1/latex-a9ad79f3-b5c2-4d32-923d-67a72e22f7b2.png)), from the true training labels (![latex-e383ba9b-0575-434f-9a31-4e3cb43bd5e1](data/lecture1/latex-e383ba9b-0575-434f-9a31-4e3cb43bd5e1.png))
- Goal is to minimize the loss function, without overfitting to the training data.
- Mean Squared Error: ![latex-aefcc533-1ed9-43da-a48d-dfed7cdbc6cd](data/lecture1/latex-aefcc533-1ed9-43da-a48d-dfed7cdbc6cd.png)_

#### Unsupervised Learning

No labels for the dataset, goal is to learn some arbitrary patterns.
- Find the underlying structure in the data.
- Given a training set (features), no labels to compare to.
- Clustering
  - Separate the data into an arbitrary number of distinct clusters

##### K-Means
```
- Select K random centroids
- Compute the distance to the centroids for each point in the training set
  - Mark the cluster as the centroid that is closest to the sample
- Set the centroids as the mean of the members
- Repeat for i iterations / until convergence
```

##### Autoencoders
- Neural Networks
- Encode: the input data into some lower dimensional space
- Decode: project back into the original higher dimensional space
- Can be used to generate novel samples
- Perform **Dimensionality Reduction**
  - Example: MNIST ![latex-5619c7cb-665e-4e8e-bb46-514b7993c259](data/lecture1/latex-5619c7cb-665e-4e8e-bb46-514b7993c259.png), can project into a 25-dimensional space

#### Reinforcement Learning
- "Semi-supervised"
- Give the model positive/negative feedback on some recurring basis
  - reward for good performance
  - punish for bad performance
- Let it run as it learns from these experiences.
