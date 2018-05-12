# Lecture 2, May 7, 2018

## Point Estimation
- Used to estimate the model parameters

### Probability Basics
- Chain Rule: ![latex-107f95e8-babe-4513-96c6-3c0609306d19](data/lecture2/latex-107f95e8-babe-4513-96c6-3c0609306d19.png)
- Bayes Rule: ![latex-f693ef03-1c0c-4f45-aaa4-9096fe8f606e](data/lecture2/latex-f693ef03-1c0c-4f45-aaa4-9096fe8f606e.png)
- Example: What is the prob that a randomly selected individual with a positive test is a drug user?
  - ![latex-84dfe8fb-0273-4ce4-bf95-336a17cfa77e](data/lecture2/latex-84dfe8fb-0273-4ce4-bf95-336a17cfa77e.png)
  - ![latex-08c0c748-b43a-4fcf-bf59-872b62d94b1f](data/lecture2/latex-08c0c748-b43a-4fcf-bf59-872b62d94b1f.png)
  - ![latex-0874eb12-c4ac-4068-ac18-9c750c241b48](data/lecture2/latex-0874eb12-c4ac-4068-ac18-9c750c241b48.png)
  - Why is the drug 99% specific? Large population, with large number of non-users will bring this down.

### Bias and Variance
- Point Esimator: A single estimation of parameter
  - An estimation of ![latex-13bc62b4-7be6-4496-93c9-5f7bebb1e48e](data/lecture2/latex-13bc62b4-7be6-4496-93c9-5f7bebb1e48e.png) is ![latex-eef35c36-34aa-41a5-a31b-9f531e7668e5](data/lecture2/latex-eef35c36-34aa-41a5-a31b-9f531e7668e5.png)
- Bias: ![latex-e5329ef1-dab2-440c-b645-6c16cd7250d3](data/lecture2/latex-e5329ef1-dab2-440c-b645-6c16cd7250d3.png)
  - Expectation - the true param
  - ![latex-fa0a455d-f422-4288-ac96-3cd49d7f2160](data/lecture2/latex-fa0a455d-f422-4288-ac96-3cd49d7f2160.png) is fix and unknown, ie. not random
  - If the bias is 0, unbiased
- Variance: ![latex-fe3deff7-e78f-47e8-ac26-f7205445efac](data/lecture2/latex-fe3deff7-e78f-47e8-ac26-f7205445efac.png)
  - Your dataset is random, may be noisy

- We would prefer a small bias and small variance
  - We would prefer unbiased

### Likelihood Function
- Descrete: ![latex-e3039a17-8b70-4244-9101-f11610f7096e](data/lecture2/latex-e3039a17-8b70-4244-9101-f11610f7096e.png)
  - Use the probability mass function
  - Notice L is a function of ![latex-0c671db4-3c78-42c4-b161-9784e24c3f03](data/lecture2/latex-0c671db4-3c78-42c4-b161-9784e24c3f03.png), but pms is a function of x given ![latex-c3ab47a5-4a3d-41c9-94f8-0318aa1a7178](data/lecture2/latex-c3ab47a5-4a3d-41c9-94f8-0318aa1a7178.png)
- Continuous: ![latex-2de64296-1836-4f20-9666-543d56346929](data/lecture2/latex-2de64296-1836-4f20-9666-543d56346929.png)
  - Density function
- We would typically use the log-likelihood function
  - ![latex-6fe0e4b6-7394-4828-802d-319f76d3194c](data/lecture2/latex-6fe0e4b6-7394-4828-802d-319f76d3194c.png)
  - Note that log is strictly an increasing function, therefore optimization of log-likelihood is the same as the likelihood

### Maximum Likelihood (ML)
- Observations from some distribution: ![latex-74ddc54c-61e4-47e3-9ddd-1ac305d3104a](data/lecture2/latex-74ddc54c-61e4-47e3-9ddd-1ac305d3104a.png)
- Family of probability distributions: ![latex-c4a62bb1-5b05-4515-86f3-3d4da8343979](data/lecture2/latex-c4a62bb1-5b05-4515-86f3-3d4da8343979.png)
- Maximize the log-likelihood function to get ![latex-ad36f78a-176b-4349-8cba-1aa1a1f2a883](data/lecture2/latex-ad36f78a-176b-4349-8cba-1aa1a1f2a883.png)
  - Or typically, minimize the negative log-likelihood function

#### Example: Bernoulli Distribution
- Suppose ![latex-eb82a001-d547-4b69-b0b7-8c1ce2c6c576](data/lecture2/latex-eb82a001-d547-4b69-b0b7-8c1ce2c6c576.png)
1. Write down the likelihood function
  - ![latex-53b5fb6c-8d4f-4d8e-af12-cdd65b1ac0be](data/lecture2/latex-53b5fb6c-8d4f-4d8e-af12-cdd65b1ac0be.png)
2. Log Likelihood function
  - ![latex-4668cbd9-6c8e-4d1b-8f1b-838f40c2f050](data/lecture2/latex-4668cbd9-6c8e-4d1b-8f1b-838f40c2f050.png)
3. Argmax:
  - ![latex-1c2550a8-c84d-4cd7-babd-a4f260d3a917](data/lecture2/latex-1c2550a8-c84d-4cd7-babd-a4f260d3a917.png)
4. solve Derivative for 0:
  - ![latex-38c386ca-c87b-491a-83d3-1b7112350d62](data/lecture2/latex-38c386ca-c87b-491a-83d3-1b7112350d62.png)

Suppose that we have a **convex** function ![latex-7ab89c57-0dc4-4ed9-ba0e-d33db7161255](data/lecture2/latex-7ab89c57-0dc4-4ed9-ba0e-d33db7161255.png), and is **differentiable**. A necessary and sufficient condition is to solve ![latex-e7393cf6-613b-4ea1-a1ad-cddb5713259f](data/lecture2/latex-e7393cf6-613b-4ea1-a1ad-cddb5713259f.png)
- **Convex**: A function f is convex, if ![latex-e162bb84-4ac8-417c-95bc-e56f8ff86f71](data/lecture2/latex-e162bb84-4ac8-417c-95bc-e56f8ff86f71.png)

#### How many samples are needed?
- Using Hoeffding's Inequality
- Note that ![latex-d520c7aa-7919-4349-adf6-2fdefa411038](data/lecture2/latex-d520c7aa-7919-4349-adf6-2fdefa411038.png) is the true parameter

#### Example: Gaussian Distribution
- Estimate u and ![latex-4f84e02a-269b-430b-b0d7-5a6ec69f856e](data/lecture2/latex-4f84e02a-269b-430b-b0d7-5a6ec69f856e.png) using ML
1. Likelihood Function
  - ![latex-2ad85153-48db-4a96-8337-3bc988aab390](data/lecture2/latex-2ad85153-48db-4a96-8337-3bc988aab390.png)
2. Log-likelihood
  - See the slides
- Solve for u and ![latex-0ef8506f-6bad-43f2-a364-239177faf15d](data/lecture2/latex-0ef8506f-6bad-43f2-a364-239177faf15d.png) by taking partial derivatives
  - Note that u must be done first
- Note that ![latex-d80ff167-c9de-4d50-a198-d70f6be768f7](data/lecture2/latex-d80ff167-c9de-4d50-a198-d70f6be768f7.png)

#### Limiting property of ML
- If the data was generated by the assumed model, then the ML estimation will converge to the true probability (with enough data points)
- But, in practice data is never generated by an assumed model. There is always some noise, or our assumption can be wrong.

### Maximum A Posteriori (MAP)
- Bayesian Perspective: treat parameter ![latex-f2c7987a-3c5b-490b-a499-3cba811a4039](data/lecture2/latex-f2c7987a-3c5b-490b-a499-3cba811a4039.png) as random with prior distribution ![latex-158bc182-c1de-4fcb-937c-bb8cd94a2bf0](data/lecture2/latex-158bc182-c1de-4fcb-937c-bb8cd94a2bf0.png) (ex. uniform, gaussian)
  - Therefore, it's not fixed
- Given data x, maximize posterior distribution to get ![latex-058e7cd2-0fed-4f9b-85f2-9686bcbeb305](data/lecture2/latex-058e7cd2-0fed-4f9b-85f2-9686bcbeb305.png)
  - ![latex-8b3527d0-26c4-42f0-872c-faffb8e018df](data/lecture2/latex-8b3527d0-26c4-42f0-872c-faffb8e018df.png)
  - The dinominator is independent of ![latex-a1062797-e692-4755-902f-872c9d183671](data/lecture2/latex-a1062797-e692-4755-902f-872c9d183671.png), only relies on x.
- Difference to ML: multiply by the prior

### Fully Bayesian Approach
- Include all possible values of ![latex-ee09fe2b-179f-4082-af9d-86f812ff04a9](data/lecture2/latex-ee09fe2b-179f-4082-af9d-86f812ff04a9.png)
- Typically generalize better with limited training data, high computational cost, usually intractable.
- ![latex-60b3912a-d5a3-4d50-bcd1-8cc1ecd86b45](data/lecture2/latex-60b3912a-d5a3-4d50-bcd1-8cc1ecd86b45.png)
- ![latex-03957ea0-8db2-449a-9f42-5be89b70f37c](data/lecture2/latex-03957ea0-8db2-449a-9f42-5be89b70f37c.png)

## Bias-Variance Tradeoff
- Recall that we would like a small bias and small variance, but there are some tradeoffs...
- High bias: Bad assumptions (underfitting)
- High variance: sensitive to small changes in the training set (overfitting)

### Mean Squared Error
- Assume ![latex-8ba09f38-386d-42e3-9a3e-550a1b248038](data/lecture2/latex-8ba09f38-386d-42e3-9a3e-550a1b248038.png)
- ![latex-caa8f5b2-8c9d-4c04-8ac5-a9d252dcdf45](data/lecture2/latex-caa8f5b2-8c9d-4c04-8ac5-a9d252dcdf45.png)
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
  - ![latex-3f091565-c41d-4906-aca1-60152efb7c08](data/lecture2/latex-3f091565-c41d-4906-aca1-60152efb7c08.png)
  - ![latex-2aacdb7b-2e7d-4f0f-8906-3517ad4d4744](data/lecture2/latex-2aacdb7b-2e7d-4f0f-8906-3517ad4d4744.png) (The mean)

When to do standardization
- Some features are significantly smaller or larger than the others.
- Orders of magnitude.

### Normalization
- Choose the mean and maximum of each feature
- Make it between 0 and 1
