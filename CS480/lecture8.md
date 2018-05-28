# Lecture 8 - May 28, 2018

## Perceptrons
- Basic neural network, Inspired by the brain.
- Artifical network: just input and output (no hidden layers)


![graph-ed832f79-d8e7-47a4-9f2a-f7786c335fa0](data/lecture8/graph-ed832f79-d8e7-47a4-9f2a-f7786c335fa0.svg)

Neuron is activated if: ![latex-c9c9d0ec-c511-4e23-8f13-37c91a81db6d](data/lecture8/latex-c9c9d0ec-c511-4e23-8f13-37c91a81db6d.png)
- activation function could be the `sign(t)` function: 1 if t > 0, -1 otherwise
- ![latex-8eb7b329-6923-4fa0-92d3-dab7f6db69fc](data/lecture8/latex-8eb7b329-6923-4fa0-92d3-dab7f6db69fc.png)
- Note that higher order features will have greater influence on the predictions
  - if you want equal, just feature scaling
- batch learning
  - evaluate performance on test dataset
  - divide dataset into training and testing sets
- online learning
  - streaming data samples
  - predict outputs before knowing the target values
  - Interested in making the lowest error possible
- Online -> batch
  - can simply use
  - online to batch may not work properly

### Online training algorithm

```python
for i in range(1, maxIter):
  for (x, y) in D:
    a = np.dot(w.T, x) + b
    if y*a <= 0: # This tells us that the prediction was wrong (differing signs)
      w[d] = w[d] + y*x[d] # for all d = 1..D
      b += y

return w, b
```

Why error driven updates?
- if we're incorrect, push the parameters to the correct direction.

### Spam Filtering Classification Example
- Feature set: 6 words, x[i] is 1 if the word[i] is present
- output: 1 -> ham, -1 -> spam
- initially set all parameters to 0

| Iteration | Weights, bias | prediction |
|-|-|-|
| 0 | ![latex-7efd183f-a8c4-419b-94fb-2e7966653e53](data/lecture8/latex-7efd183f-a8c4-419b-94fb-2e7966653e53.png) | ![latex-d140a0a5-68a1-46ea-bfe5-fbbad15e6605](data/lecture8/latex-d140a0a5-68a1-46ea-bfe5-fbbad15e6605.png) Update|
| 1 | ![latex-d910d5df-275f-431e-9b20-8b21a1aa04e3](data/lecture8/latex-d910d5df-275f-431e-9b20-8b21a1aa04e3.png), ![latex-88bdb21e-9415-4538-be8d-127bac1df9d0](data/lecture8/latex-88bdb21e-9415-4538-be8d-127bac1df9d0.png) | ![latex-a4908084-ccff-427d-896b-9d2773dca402](data/lecture8/latex-a4908084-ccff-427d-896b-9d2773dca402.png) update |
... See slide 13

continue until convergence or have some maximum number of iterations
- convergence: pass through the entire training set, without any updates to weights / bias
  - the algorithm can correctly predict all training examples

### Perceptron Convergence Theorem
- Linearly separable dataset: data points can be separated by some linear function (hyperplane)
- margin: ![latex-732d94a1-78db-40e7-a1e1-5dbbc3dab469](data/lecture8/latex-732d94a1-78db-40e7-a1e1-5dbbc3dab469.png), L1 norm of X is less than or equal to 1
- algorithm will converge after at most ![latex-96f795f3-8467-403d-a6d2-31afe52aaab1](data/lecture8/latex-96f795f3-8467-403d-a6d2-31afe52aaab1.png) updates
- **Note**: if the dataset isn't linearly separable then the algorithm will never converge

#### Margin
- distance between a point x and a hyperplane: ![latex-bda4fe0c-d360-4ae7-a91b-7961c3542d3a](data/lecture8/latex-bda4fe0c-d360-4ae7-a91b-7961c3542d3a.png)
- ![latex-584d7881-c5fd-43f4-a724-cc11e485c227](data/lecture8/latex-584d7881-c5fd-43f4-a724-cc11e485c227.png) for all x (the minimum distance), if linearly separable. Otherwise margin is ![latex-d2cede7a-cf3b-47cf-99d2-f5cfb84e1d67](data/lecture8/latex-d2cede7a-cf3b-47cf-99d2-f5cfb84e1d67.png)
- ![latex-1ee7cb75-b920-4f78-b9cf-82538f878848](data/lecture8/latex-1ee7cb75-b920-4f78-b9cf-82538f878848.png)
  - sup: maximum margin
  - Think support vectors

#### Training tips
- suppose dataset is 500 positive examples, then 500 negative
- origionally, the perceptron algorithm would place too much emphasis on later examples
- **solution**: shuffle the dataset before each training iteration

#### Abitrary Linear Separator
- the larger the margin, the faster convergence
- but it may not stop at the optimal linear separator
  - there could be other separators that work in your dataset
  - order of training examples and initial values of w,b influence this separator

#### When to stop
- online: never
- batch: have some maximum number of iterations
  - 1 too small (underfitting)
  - too high (overfitting)
  - save weights and biases at each iteration, use the ones that give the best test error.

### Alternative Approach
- ![latex-a0f2d146-9377-403e-b717-e78db9bc852d](data/lecture8/latex-a0f2d146-9377-403e-b717-e78db9bc852d.png) be the set of misclassified examples (i.e. ![latex-042afa4b-99b1-4645-89d6-21a5f381bf61](data/lecture8/latex-042afa4b-99b1-4645-89d6-21a5f381bf61.png))
- Use vector forms, add bias to the weights matrix and each feature (augmented form).
- If correct prediction, the loss is 0. Otherwise, ![latex-ed6a127b-520f-4e57-a821-b7f4d482d78f](data/lecture8/latex-ed6a127b-520f-4e57-a821-b7f4d482d78f.png)

#### Stocastic gradient descent
- Perform an update after looking at each sample (note: still online, update as we get stream)
- ![latex-8a3bf570-8a66-4b16-b05f-85828ee40a5a](data/lecture8/latex-8a3bf570-8a66-4b16-b05f-85828ee40a5a.png)
  - n is the learning rate
  - when learning rate is 1, just the threshold algorithm
  - typically want to decrease overtime, sum of squares less than inf, sum less equal to inf

### Multiclass Perceptron
- Up to now, binary classification
- y is now k classes, predictions ![latex-8b522fcd-2776-4316-a226-4bd999bb1b8f](data/lecture8/latex-8b522fcd-2776-4316-a226-4bd999bb1b8f.png)
  - have a weight matrix for each class
  - predicted class is just the output that has the maximum score
- still do error driven updates
  - if incorrect, we know the correct class, update the relevant weight matrix (![latex-d00daf87-0bad-4be5-8580-ef21b5c49d59](data/lecture8/latex-d00daf87-0bad-4be5-8580-ef21b5c49d59.png)) and the incorrect weight matrix (![latex-ed8eea1d-922a-46e9-b8a1-0d98cbe3f77a](data/lecture8/latex-ed8eea1d-922a-46e9-b8a1-0d98cbe3f77a.png))
  - move the weights of the correct class in the right direction, move the incorrect weights away from that guess.

### What not linearlly separable

If not linearlly separable, won't converge
- typically the weights will enter some infinite cycle.
- Find better features
- kernel methods
- Deeper neural networks

## Kernels

### Feature space mappings

Recall basis functions.
Given inputs on some d dimensional space, map them to M dimensions
- ![latex-81392f66-1465-4442-baef-b1b26981b20d](data/lecture8/latex-81392f66-1465-4442-baef-b1b26981b20d.png)
- M could be infinite
- example
  - ![latex-7890e9d2-2249-4ede-99af-e0af87dc153e](data/lecture8/latex-7890e9d2-2249-4ede-99af-e0af87dc153e.png), ![latex-68988f3f-80b9-497b-9407-8fe396accc89](data/lecture8/latex-68988f3f-80b9-497b-9407-8fe396accc89.png)

### Kernel Functions
- some function k: ![latex-89508b75-f424-4888-90be-fe0f4cfc7a62](data/lecture8/latex-89508b75-f424-4888-90be-fe0f4cfc7a62.png)
  - ![latex-2ae80aec-527e-47f8-aa79-8042b5da1824](data/lecture8/latex-2ae80aec-527e-47f8-aa79-8042b5da1824.png)
  - ![latex-8444273e-eab5-44df-b3d0-391ee17aa43c](data/lecture8/latex-8444273e-eab5-44df-b3d0-391ee17aa43c.png) is some feature space mapping
  - just inner product
  - we don't care about the specific values of the phi functions, just the kernel function value.
    - For example, if M is infinite, we can often compute the kernel function without needing the infinite vectors.

#### Verify Kernel Function example
- can just separate the variables, define the phi function, show the inner product.

#### Gram Matrix
- Defines a condition to be a valid kernel function
- N: the number of training examples
- ![latex-acb14fca-a5f9-4ace-b6b4-2de611f351b4](data/lecture8/latex-acb14fca-a5f9-4ace-b6b4-2de611f351b4.png)
  - symmetric: ![latex-1f0e2d50-f635-4654-978c-f493fd26f703](data/lecture8/latex-1f0e2d50-f635-4654-978c-f493fd26f703.png)
  - positive semi-definite: ![latex-882ecb93-ab27-4c20-a9cc-8debfb57ba96](data/lecture8/latex-882ecb93-ab27-4c20-a9cc-8debfb57ba96.png)
    - check that all eigenvalues of K are positive
    - K can be decomposed as ![latex-711cfbe8-5061-49bd-b214-93f8a2256530](data/lecture8/latex-711cfbe8-5061-49bd-b214-93f8a2256530.png)

#### Constructing Kernels
- start with ![latex-fb58c2bb-2d27-44c5-8f47-a8d6f8f9eebc](data/lecture8/latex-fb58c2bb-2d27-44c5-8f47-a8d6f8f9eebc.png), make ![latex-b6ba1767-f6d6-4d6c-b311-72e0bf290be0](data/lecture8/latex-b6ba1767-f6d6-4d6c-b311-72e0bf290be0.png)
- Construct the kernel function directly (without needing to know the phi function)

next class...
