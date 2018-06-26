# Lecture 14 - June 25, 2018

## Backpropagation

Method to compute the gradient at various points in the network
- Results can be used in an optimization algorithm
  - SGD, Adam, RMSProp
- forward pass: compute the hidden values, output, error
- backward pass: Work backwards through the network, computing gradients
  - use the chain rule
  - ![latex-8a88c1d9-6ebc-4ab8-8a6e-d53f9abe59e1](data/lecture14/latex-8a88c1d9-6ebc-4ab8-8a6e-d53f9abe59e1.png)
- Complexity: Linear in the number of edges in the network
- Slow to converge
  - can get stuck in local optima
- Overfitting
  - **Early Stopping**: stop training when test error begins to rise
  - **Dropout:** During training "drop" nodes from the network

## Activation Functions

![latex-7efb33a7-a057-4af7-8a55-38533d1a8a63](data/lecture14/latex-7efb33a7-a057-4af7-8a55-38533d1a8a63.png)
![latex-22c73ae9-1841-49b4-bd0a-40a61e242037](data/lecture14/latex-22c73ae9-1841-49b4-bd0a-40a61e242037.png)
- Range: (0, 1)
- small gradient at saturated regions (extreme ![latex-5c0f086c-31ee-46fb-bdf2-52fe840e533f](data/lecture14/latex-5c0f086c-31ee-46fb-bdf2-52fe840e533f.png), and ![latex-1958a0a5-62b9-4ceb-92d2-6dd01fd9a601](data/lecture14/latex-1958a0a5-62b9-4ceb-92d2-6dd01fd9a601.png))
  - using a gradient base algorithm, means very small updates

tanh
- range: (-1, 1)
- ![latex-ea089340-b2ae-4778-8a68-80dce02c3f9e](data/lecture14/latex-ea089340-b2ae-4778-8a68-80dce02c3f9e.png)
- same problem, small gradients at extremes

### Vanishing gradient problem
- Small gradient values in activiation functions
- For a deep neural network, the gradients of earlier layers results in a large product of values ![latex-3ca13642-1d84-46fa-8235-a33b8737ce60](data/lecture14/latex-3ca13642-1d84-46fa-8235-a33b8737ce60.png), producing a very small delta
- Problem worsens as additional layers are added

#### How to avoid
- initialization of network parameters
- choose activation functions that do not saturate
  - ReLU family
- LSTM or GRU

#### ReLU

[More](https://keras.io/activations/#elu)

- **ReLU**: ![latex-bc974b9b-32d5-45b4-99ba-fd864c36412c](data/lecture14/latex-bc974b9b-32d5-45b4-99ba-fd864c36412c.png)
  - gradient is 1 when positive, 0 otherwise
- **Leaky ReLU**: ![latex-7ab900e9-368c-40b8-80cd-0878d83e63c4](data/lecture14/latex-7ab900e9-368c-40b8-80cd-0878d83e63c4.png)
  - gradient is 1 when positive, -constant value when negative
- **Elu**: x if x positive, ![latex-b92eb9ac-4391-498b-ab92-36c16b66c0e1](data/lecture14/latex-b92eb9ac-4391-498b-ab92-36c16b66c0e1.png) is negative
- **Maxout**: Activation function where the output is the max of it's inputs, [more](https://stats.stackexchange.com/questions/129698/what-is-maxout-in-neural-network)

## Regularization
- Neural networks are likely to overfit
- The number of parameters can exceed the number of data samples
- **Regularization**: modify the learning algorithm in such a way that the **testing performance** is improved
  - Recall L1 and L2 regularization

### Bagging
- Bootstrap Aggregation: train several different models, hope that their average performance converges to the target
  - unlikely for each model to make the same error

#### Method
1. Build a new dataset for each model (say k models)
2. Each dataset has the same size as the original
3. sample **with replacement** from the original dataset
4. Train each model

#### Prediction
- Regression: Average
- Classification: Majority vote

### Dropout
- During training, drop hidden neuron from network with probability p
  - do this for each training sample
- Idea is network can't rely on specific neurons for output, spread capabilities throughout the network.
  - Get results that are similar to training a large ensemble model (with shared params)
- How to set the probability of keeping unit
  - could set it the same for all layers
  - alternaively, set a lower p for overfitting units
    - large number of units
  - usually keep it close to 1

#### Example
- ![latex-a10aa170-b1b1-41e6-a547-74089013640e](data/lecture14/latex-a10aa170-b1b1-41e6-a547-74089013640e.png)
  - suppose h is 4x1
- Randomly (prob p) generate a binary vector, d (same size as h). 1 indicates keeping the neuron
- Hadamard product of h and d
- **Inverted Dropout:** ![latex-711cb15e-505a-4fe8-a25f-de211fb1ef2c](data/lecture14/latex-711cb15e-505a-4fe8-a25f-de211fb1ef2c.png)
  - goal is to keep the mean value of the output unchanged

#### Prediction
- Training: Use inverted dropout on each training example
- Prediction: don't use dropout
  - If inverted dropout was used during training, no need for additional scaling

### Data Augmentation

Neural networks typically perform better with a larger dataset. You can often engineer a larger dataset utilizing your existing data.
- transform the input in some fashion
  - ex. rotating / transforming images
- May not be possible in all domains
  - ex. can't flip handwritten digits

### Early Stopping
- During training, train error will decrease. validation error will decrease, and eventually increase as the model overfits
- Stop training when this happens

### Batch Normalization (BN)
- Divide dataset into mini-batches
- compute mean and variance for each mini-batch, normalize each point in the mini-batch
- ![latex-0288e89a-2708-4af0-becc-5b2df505c96e](data/lecture14/latex-0288e89a-2708-4af0-becc-5b2df505c96e.png) is there to stablize the calculation
