# Lecture 11 - June 6, 2018

## Review of K-Means
1. start with k random centers
2. label data points with the closest center
3. recompute centers, goto 2 until convergence.

Hard clustering: Each sample can only belong to a single cluster

## Review of Mixture Models

For when we want soft clusters: assign a probability of the sample belonging to each particular class.

Define a latent variable z (one-hot vector)
- then, ![latex-8c91270e-953c-459f-b42d-2238b51ede44](data/lecture11/latex-8c91270e-953c-459f-b42d-2238b51ede44.png)
- ![latex-6adf6bea-f7a1-46f8-8645-5f08ab560013](data/lecture11/latex-6adf6bea-f7a1-46f8-8645-5f08ab560013.png)
  - If gaussian

Responsibility is what we call the posterior probability
- slide 10
- using bayes rule
- if we observe some data, what is the proability that it comes from the k-th component

ML Estimate
- We can't compute the inner derivative, use iterative approaches instead
- Use gradient descent
- EM - Expectation Maximization:

### Expectation Maximization

Similar steps to k-means
- Take derivative of log-likelihood wrt the mean
  - The denominator is the responsibility
  - assuming we have the responsibility, we can get a closed for solution for the mean
  - multiply by the inverse covariance, can do this since it's contant over the summation, therefore can eliminate it.
  - The mean is just a "soft" average of all the effective points in the cluster.
- Take the derivative of the log-likelihood wrt the covariance
- do the same thing for ![latex-6bf89d15-c7b2-49de-99d6-c00b3ad5f056](data/lecture11/latex-6bf89d15-c7b2-49de-99d6-c00b3ad5f056.png)
  - constraint: ![latex-909badcf-50c3-4f21-8655-8a301b10e24a](data/lecture11/latex-909badcf-50c3-4f21-8655-8a301b10e24a.png)
  - N is the total number of samples, ![latex-b0368d88-f8a9-4ca5-9dd0-e775007a4873](data/lecture11/latex-b0368d88-f8a9-4ca5-9dd0-e775007a4873.png) is the effective number of samples.

We typically would start with some initial values for these parameters
- Use K-means for the initial assignment

Expectation step
- Take expectation over the latent variable (cluster assignments) that we don't know
Maximization step
- Maximize the parameters

## Hard Margin SVMs
Support Vector Machines

Problems with kernel methods: predictions requires evaluating the kernel function for all training samples, expensive.
- Goal: Find a sparse solution that allows us to consider a subset of the samples.

### Recall: Perceptron
- we assume that the data is linearly seperable
- ![latex-1cd5c4ec-3be7-42d5-a91f-8168ad28ddbf](data/lecture11/latex-1cd5c4ec-3be7-42d5-a91f-8168ad28ddbf.png) assign positive / negative based on this threshold
- the final solution is influenced by the initial weights and biases, as well as the order in which the training samples as presented.

### Hard Margin SVM
- Binary classification
- assume the data is linearlly seperable
- find the weights and biases such that the margin between the two classes is maximized

#### Recall: MArgin
- minimize the separator for all values of x
- take the maximum for all w, b

#### SVM Optimization
- ![latex-61b4c7e6-1c9c-49e7-8cde-d74d6774cb8c](data/lecture11/latex-61b4c7e6-1c9c-49e7-8cde-d74d6774cb8c.png) function can be incorporated, but it doesn't effect the optimization
- note that ![latex-0536db53-4418-4298-b719-2a7c16701e30](data/lecture11/latex-0536db53-4418-4298-b719-2a7c16701e30.png)
- If our prediction was correct, then the target and the prediction will have the same sign, making the product positive.

Note that if we multiply the weights and biases by a constant factor, k. The actual distance doesn't change.
- ASsume ![latex-4b9c4de9-948a-4bec-ac45-1b4d456ae87f](data/lecture11/latex-4b9c4de9-948a-4bec-ac45-1b4d456ae87f.png) for the closest point (just divide by the value of the closest point.
- Then the margin is ![latex-d5714cad-5161-4fe5-851d-4fbe11fe5d96](data/lecture11/latex-d5714cad-5161-4fe5-851d-4fbe11fe5d96.png), prediction is 1.
- this gives the maximization problem on slide 8
- Therefore, we can minimize the inverse. ![latex-0a14e99c-c8cd-4e2d-a7b7-504efddf4878](data/lecture11/latex-0a14e99c-c8cd-4e2d-a7b7-504efddf4878.png)
- finally, ![latex-78e0d6ab-13b1-47fe-aea6-de7487228dca](data/lecture11/latex-78e0d6ab-13b1-47fe-aea6-de7487228dca.png)
