# Lecture 10 - June 4, 2018

## Gaussian Processes
Facts
1. If x is Gaussian, then ![latex-17b0ea57-fac9-4df7-af63-382c389a03c3](data/lecture10/latex-17b0ea57-fac9-4df7-af63-382c389a03c3.png) is Gaussian
2. If ![latex-1978cc56-b323-4d86-87e4-4f64d0767473](data/lecture10/latex-1978cc56-b323-4d86-87e4-4f64d0767473.png) are gaussian, then ![latex-b4f404af-40f2-4885-b6cb-f96c168c671f](data/lecture10/latex-b4f404af-40f2-4885-b6cb-f96c168c671f.png) is gaussian
- Gaussian process is a set of joint functions

### Verifying a Kernel
- Gram matrix K, where ![latex-0523961a-0c70-4eac-9871-b9e20f518f77](data/lecture10/latex-0523961a-0c70-4eac-9871-b9e20f518f77.png)
  - symmetric: ![latex-e161d312-ea97-46ea-8153-f60dac4fd428](data/lecture10/latex-e161d312-ea97-46ea-8153-f60dac4fd428.png)
  - positive semi-definate

### Relating to covariance function
- can verify that it's symmetric and PSD
- given any mean function and kernel function, there exists a gaussian process

### Gaussian Process for Regression

- we have a linear model: ![latex-3b4be601-f05f-48ce-95e3-7f7a75d5a46c](data/lecture10/latex-3b4be601-f05f-48ce-95e3-7f7a75d5a46c.png), ![latex-de738c53-a2fe-487d-9236-c9831616fd38](data/lecture10/latex-de738c53-a2fe-487d-9236-c9831616fd38.png)
- Using a feature space mapping for x, ![latex-a149a9bf-7e0c-44fc-9fcf-b63238484a19](data/lecture10/latex-a149a9bf-7e0c-44fc-9fcf-b63238484a19.png)
- Construct a ![latex-8f0a12d8-4cbd-4f9c-8c17-8bf0783bf55c](data/lecture10/latex-8f0a12d8-4cbd-4f9c-8c17-8bf0783bf55c.png) matrix, where ![latex-b8512e7c-8d48-4af3-8956-c87c11e703f7](data/lecture10/latex-b8512e7c-8d48-4af3-8956-c87c11e703f7.png)
  - this ![latex-073a347b-fe74-49cc-9fc7-c211904f7474](data/lecture10/latex-073a347b-fe74-49cc-9fc7-c211904f7474.png) matrix is nxm
  - basically take our feature mapping, and stack all of our samples
- Then, ![latex-ed6858b6-2b96-4d5a-a43c-97cf276d96fa](data/lecture10/latex-ed6858b6-2b96-4d5a-a43c-97cf276d96fa.png)
  - y is also a vector
- We can recall the fact that ![latex-eaafc717-56f5-470c-ab9c-769308c3c9e6](data/lecture10/latex-eaafc717-56f5-470c-ab9c-769308c3c9e6.png) is Gaussian, then y is also gaussian.
  - mean is 0, since mean w is 0
  - covarience is: ![latex-0a1b0614-47f9-42fe-b35f-19b7886553e1](data/lecture10/latex-0a1b0614-47f9-42fe-b35f-19b7886553e1.png)
    - This is just the kernel function, Gram matrix
    - Therefore, we only need the kernel function, not ![latex-7ef540b4-d5ac-46fe-9d07-b77de46a2a79](data/lecture10/latex-7ef540b4-d5ac-46fe-9d07-b77de46a2a79.png)

#### With Noise

![latex-1f804356-bd24-40a6-9d4d-c19979f16b34](data/lecture10/latex-1f804356-bd24-40a6-9d4d-c19979f16b34.png)
- w is same as before
- ![latex-b37d6973-1708-4389-bbde-8d3a6dae03eb](data/lecture10/latex-b37d6973-1708-4389-bbde-8d3a6dae03eb.png)

Prediction:

![latex-92d6c4a2-c15e-4349-8e78-e319c5e13271](data/lecture10/latex-92d6c4a2-c15e-4349-8e78-e319c5e13271.png)_
- we know ![latex-3c6b0d05-229e-4ada-9578-24b918711bc3](data/lecture10/latex-3c6b0d05-229e-4ada-9578-24b918711bc3.png) and ![latex-231a37b1-26b9-4724-8b77-243950d85708](data/lecture10/latex-231a37b1-26b9-4724-8b77-243950d85708.png) are both gaussian, use fact 2. We can obtain ![latex-e8c081f5-386c-45c1-9768-1a74eab8f3bb](data/lecture10/latex-e8c081f5-386c-45c1-9768-1a74eab8f3bb.png)
- ![latex-a3a32c97-b1da-4111-93f9-28e730b02c1f](data/lecture10/latex-a3a32c97-b1da-4111-93f9-28e730b02c1f.png) is a gaussian process, Gaussian,
  - covariance matrix: ![latex-69774475-8250-4a0b-97a3-397f6c6613a6](data/lecture10/latex-69774475-8250-4a0b-97a3-397f6c6613a6.png)
  - delta is 0-1 error

#### Baysian Linear Regression
- as before we knwo ![latex-36409217-097f-4f62-81f1-2d1230ae03d6](data/lecture10/latex-36409217-097f-4f62-81f1-2d1230ae03d6.png)
- Therefore by 2: ![latex-ea0f275c-232d-4e7d-8f27-9cd125941c16](data/lecture10/latex-ea0f275c-232d-4e7d-8f27-9cd125941c16.png)

### Gaussian Process for Classification

output is no longer continuous, comes from some finite set

#### Binary Classification
- outputs in {0, 1}
- N data samples
- Given an N+1 input, want to predict ![latex-42d985d5-f55d-4a36-b3e1-9f157ed4924e](data/lecture10/latex-42d985d5-f55d-4a36-b3e1-9f157ed4924e.png)_
- ![latex-f4c34dad-0e91-43b2-a614-46030cabf30a](data/lecture10/latex-f4c34dad-0e91-43b2-a614-46030cabf30a.png) is a GP, which has continuous output. Transform this with the sigmoid function ![latex-d25d4dda-668b-468c-bb21-9ade8e169c1b](data/lecture10/latex-d25d4dda-668b-468c-bb21-9ade8e169c1b.png)
- recall logistic regression:
- ![latex-c8996505-128d-4a18-9ca8-290592c729cd](data/lecture10/latex-c8996505-128d-4a18-9ca8-290592c729cd.png)
- Can construct the likelihood function
  - ![latex-af1e64ff-4f14-423b-a433-14a009c86ad7](data/lecture10/latex-af1e64ff-4f14-423b-a433-14a009c86ad7.png)

## Mixture Models and EM

### K-Means Clustering
- don't assume any distributional information
- N data samples, want to group into k clusters (given)
- ![latex-c429c01c-1e6e-4407-99c0-437e02b0d2fa](data/lecture10/latex-c429c01c-1e6e-4407-99c0-437e02b0d2fa.png)_ then the n-th point belongs to the k-th cluster
- Objective function: want to minimize the distance between each data point to the center of the cluster.
  - ![latex-78934cbb-5b2c-40ea-a59e-8dcd3ea5b7ef](data/lecture10/latex-78934cbb-5b2c-40ea-a59e-8dcd3ea5b7ef.png)
  - Note that each point can only be in a single cluster, therefore only 1 term in the inner sum.

Algorithm
1. Minimize J with respect to the mappings, keeping the centers fixed
  - New mappings
  - Each point belongs to the cluster with the closest center
2. Minimize J with respect to the centers, keeping the mappings fixed
  - compute new centers
  - Centers are just average of all of the points in the cluster
3. repeat (some convergence criteria)
  - iterations
  - stability
  - check loss delta, set some threshold

**Hard Clustering**
- Each point can only belong to a single cluster
- K-MEAN

**Soft Clustering**
- Each point has a probability distribution over the clusters.
- Gaussian

### Mixture Models
- Notice that each gaussian distribution has a single peak (at the mean)
- Mixtures allow for multiple peaks
- Mixed Gaussian: ![latex-9886128c-65e1-46a1-b6bd-d0361eae0fbe](data/lecture10/latex-9886128c-65e1-46a1-b6bd-d0361eae0fbe.png)
  - sum of the ![latex-8f7b057f-0eb3-4f05-8bb5-f00b2bf763b0](data/lecture10/latex-8f7b057f-0eb3-4f05-8bb5-f00b2bf763b0.png)s must equal 1.
- **Latent Random Variables**: Not observed directly, inferred from other observed variables
  - Introduce z to model this mixed distribution
