# Lecture 2, May 7, 2018

## Point Estimation
- Used to estimate the model parameters

### Probability Basics
- Chain Rule: ![latex-2cee3be9-e1d9-456a-bc9c-201abe8aa6fe](data/lecture2/latex-2cee3be9-e1d9-456a-bc9c-201abe8aa6fe.png)
- Bayes Rule: ![latex-98bc13c7-6114-487d-a670-dc31c22ba7a0](data/lecture2/latex-98bc13c7-6114-487d-a670-dc31c22ba7a0.png)
- Example: What is the prob that a randomly selected individual with a positive test is a drug user?
  - ![latex-7baae309-da59-4375-9a6c-aab37b4ad6a0](data/lecture2/latex-7baae309-da59-4375-9a6c-aab37b4ad6a0.png)
  - ![latex-a13ae6be-a1ed-46cf-ae83-4457730fc28a](data/lecture2/latex-a13ae6be-a1ed-46cf-ae83-4457730fc28a.png)
  - ![latex-b2856ffc-221c-4a11-9315-726398bbbeba](data/lecture2/latex-b2856ffc-221c-4a11-9315-726398bbbeba.png)
  - Why is the drug 99% specific? Large population, with large number of non-users will bring this down.

### Bias and Variance
- Point Esimator: A single estimation of parameter
  - An estimation of ![latex-f5cd7b38-f41a-465b-8827-3f75cf99d508](data/lecture2/latex-f5cd7b38-f41a-465b-8827-3f75cf99d508.png) is ![latex-1fffdefc-6598-4b4a-9faf-27015633e1d3](data/lecture2/latex-1fffdefc-6598-4b4a-9faf-27015633e1d3.png)
- Bias: ![latex-a45101e2-d9b9-4158-84be-7709d7f06d61](data/lecture2/latex-a45101e2-d9b9-4158-84be-7709d7f06d61.png)
  - Expectation - the true param
  - ![latex-4003b089-2d74-4457-bb17-3de76dabf7d6](data/lecture2/latex-4003b089-2d74-4457-bb17-3de76dabf7d6.png) is fix and unknown, ie. not random
  - If the bias is 0, unbiased
- Variance: ![latex-d4edd260-9192-4f38-ab77-5e578a510f14](data/lecture2/latex-d4edd260-9192-4f38-ab77-5e578a510f14.png)
  - Your dataset is random, may be noisy

- We would prefer a small bias and small variance
  - We would prefer unbiased

### Likelihood Function
- Descrete: ![latex-32ed1ad8-a9bc-4f64-a4d4-d2c4abd18f48](data/lecture2/latex-32ed1ad8-a9bc-4f64-a4d4-d2c4abd18f48.png)_
  - Use the probability mass function
  - Notice L is a function of ![latex-62f1f8de-d563-4593-9923-259e6e1ec257](data/lecture2/latex-62f1f8de-d563-4593-9923-259e6e1ec257.png), but pms is a function of x given ![latex-ce1b687b-0c6a-421c-94dd-db775a468f9f](data/lecture2/latex-ce1b687b-0c6a-421c-94dd-db775a468f9f.png)
- Continuous: ![latex-035ab4f5-f62e-442e-a41b-d25a582c62a5](data/lecture2/latex-035ab4f5-f62e-442e-a41b-d25a582c62a5.png)_
  - Density function
- We would typically use the log-likelihood function
  - ![latex-917740c2-3aa0-41c2-93e0-67ba032474b2](data/lecture2/latex-917740c2-3aa0-41c2-93e0-67ba032474b2.png)
  - Note that log is strictly an increasing function, therefore optimization of log-likelihood is the same as the likelihood

### Maximum Likelihood (ML)
- Observations from some distribution: ![latex-85db7657-2fc0-4362-a5ac-88599fb69b8a](data/lecture2/latex-85db7657-2fc0-4362-a5ac-88599fb69b8a.png)
- Family of probability distributions: ![latex-29f014fc-a2b4-4824-8ef0-a58d7e62efc5](data/lecture2/latex-29f014fc-a2b4-4824-8ef0-a58d7e62efc5.png)
- Maximize the log-likelihood function to get ![latex-648de8fd-cc52-423c-b132-fd8294327b7c](data/lecture2/latex-648de8fd-cc52-423c-b132-fd8294327b7c.png)
  - Or typically, minimize the negative log-likelihood function

#### Example: Bernoulli Distribution
- Suppose ![latex-eef710bf-3056-4481-af0a-918f60f41a25](data/lecture2/latex-eef710bf-3056-4481-af0a-918f60f41a25.png)
1. Write down the likelihood function
  - ![latex-4eacc2e9-ba42-49cf-bf31-a3c11ce2e3d6](data/lecture2/latex-4eacc2e9-ba42-49cf-bf31-a3c11ce2e3d6.png)
2. Log Likelihood function
  - ![latex-ab5d1221-1569-44af-8452-2de9f57b207f](data/lecture2/latex-ab5d1221-1569-44af-8452-2de9f57b207f.png)
3. Argmax:
  - ![latex-b495aca8-465e-492b-85fa-56413d4a4c0a](data/lecture2/latex-b495aca8-465e-492b-85fa-56413d4a4c0a.png)
4. solve Derivative for 0:
  - ![latex-46b8df93-995c-4f49-8c1d-03d00f3d05e1](data/lecture2/latex-46b8df93-995c-4f49-8c1d-03d00f3d05e1.png)

Suppose that we have a **convex** function ![latex-e04368d9-018a-42ff-afb8-74cca8408288](data/lecture2/latex-e04368d9-018a-42ff-afb8-74cca8408288.png), and is **differentiable**. A necessary and sufficient condition is to solve ![latex-d539b2f1-4eeb-4d0b-8883-4d85bf3a7a74](data/lecture2/latex-d539b2f1-4eeb-4d0b-8883-4d85bf3a7a74.png)
- **Convex**: A function f is convex, if ![latex-f997cb35-91dd-4e00-b767-ebe6950b96a5](data/lecture2/latex-f997cb35-91dd-4e00-b767-ebe6950b96a5.png)

#### How many samples are needed?
- Using Hoeffding's Inequality
- Note that ![latex-cdca76f0-7e6f-470a-9371-1f4329741294](data/lecture2/latex-cdca76f0-7e6f-470a-9371-1f4329741294.png) is the true parameter

#### Example: Gaussian Distribution
- Estimate u and ![latex-d60c8dfa-b39c-47cd-b4e2-917dd6a72aaa](data/lecture2/latex-d60c8dfa-b39c-47cd-b4e2-917dd6a72aaa.png) using ML
1. Likelihood Function
  - ![latex-847c099f-90eb-4fd5-9268-7f8a9e0d37f8](data/lecture2/latex-847c099f-90eb-4fd5-9268-7f8a9e0d37f8.png)
2. Log-likelihood
  - See the slides
- Solve for u and ![latex-403d8c43-48e0-40d3-974c-f1ab9d893568](data/lecture2/latex-403d8c43-48e0-40d3-974c-f1ab9d893568.png) by taking partial derivatives
  - Note that u must be done first
- Note that ![latex-19ba9553-7d0f-4ec6-a479-9da9b6721f50](data/lecture2/latex-19ba9553-7d0f-4ec6-a479-9da9b6721f50.png)

#### Limiting property of ML
- If the data was generated by the assumed model, then the ML estimation will converge to the true probability (with enough data points)
- But, in practice data is never generated by an assumed model. There is always some noise, or our assumption can be wrong.

### Maximum A Posteriori (MAP)
- Bayesian Perspective: treat parameter ![latex-6bd999d2-83a9-4cee-8e1d-75d4fadb4243](data/lecture2/latex-6bd999d2-83a9-4cee-8e1d-75d4fadb4243.png) as random with prior distribution ![latex-70acf854-5cdf-48dc-ad0b-29c3ee151875](data/lecture2/latex-70acf854-5cdf-48dc-ad0b-29c3ee151875.png) (ex. uniform, gaussian)
  - Therefore, it's not fixed
- Given data x, maximize posterior distribution to get ![latex-eac452ae-f5a9-45ef-8489-3121e55531be](data/lecture2/latex-eac452ae-f5a9-45ef-8489-3121e55531be.png)
  - ![latex-47ed77eb-19c3-45ad-bed7-c96bdb41b678](data/lecture2/latex-47ed77eb-19c3-45ad-bed7-c96bdb41b678.png)
  - The dinominator is independent of ![latex-727f43a9-0c09-47ba-b68d-6b0bbe9f6489](data/lecture2/latex-727f43a9-0c09-47ba-b68d-6b0bbe9f6489.png), only relies on x.
- Difference to ML: multiply by the prior

### Fully Bayesian Approach
- Include all possible values of ![latex-368ebec9-6a27-4818-a2af-1a53f8555614](data/lecture2/latex-368ebec9-6a27-4818-a2af-1a53f8555614.png)
- Typically generalize better with limited training data, high computational cost, usually intractable.
- ![latex-d94b2330-b212-4afd-8672-2819abf328af](data/lecture2/latex-d94b2330-b212-4afd-8672-2819abf328af.png)_
- ![latex-3176009b-5144-4685-a226-6ea9f1bd74e2](data/lecture2/latex-3176009b-5144-4685-a226-6ea9f1bd74e2.png)_

## Bias-Variance Tradeoff
- Recall that we would like a small bias and small variance, but there are some tradeoffs...
- High bias: Bad assumptions (underfitting)
- High variance: sensitive to small changes in the training set (overfitting)

### Mean Squared Error
- Assume ![latex-7aaf1f23-f54e-4402-ac68-baa62398b42c](data/lecture2/latex-7aaf1f23-f54e-4402-ac68-baa62398b42c.png)
- ![latex-905d2af1-3aea-4bf5-84fd-aa16f774c642](data/lecture2/latex-905d2af1-3aea-4bf5-84fd-aa16f774c642.png)
  - You can't do anything to remove the noise
  - Noise has mean = 0, variance

### Training and Testing Error
- Divide the dataset into a training and testing part
  - They should both come from independent and identically distributed
  - Important: The test data cannot be used for training the model
- **Objective**: Low test error
  - The more complex the model, the lower the training error will be. But this will likely make the testing error worse as the model fails to generalize.
  - training error is a bad measure because you have the answers, it is only used to construct the model.

## Feature Scaling

- We want to scale our feature set as a part of preprocessing
- Each feature should contribute equally to the model, i.e. features with large values should not be the main predictors.

### Standardization
- Centering: Make sure no features are arbitrarily large
  - Mean 0, variance 1
- Scaling: Make sure all features have roughly the same scale
  - ![latex-2c8196ab-eeaa-4d34-b67e-928fd8fa3ba0](data/lecture2/latex-2c8196ab-eeaa-4d34-b67e-928fd8fa3ba0.png)
  - ![latex-bc738297-d5b1-47f7-881e-5149e39692f9](data/lecture2/latex-bc738297-d5b1-47f7-881e-5149e39692f9.png)_ (The mean)

When to do standardization
- Some features are significantly smaller or larger than the others.
- Orders of magnitude.

### Normalization
- Choose the mean and maximum of each feature
- Make it between 0 and 1
