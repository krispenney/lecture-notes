# Lecture 15 - February 5, 2018

- capgrass illusion: differential between visual response and emotional response

## Stochastic Gradient Descent: Review
- Updating weights after every sample is infeasible
- instead process in batches, then update errors
- Help smooth learning

### Momentum
- Analogy can be made between Acceleration, Velocity, Distance and Error gradient, weights update, weights
- ![latex-17d6abef-db99-45d4-a0d4-ffdab0d4039e](data/lecture15/latex-17d6abef-db99-45d4-a0d4-ffdab0d4039e.png): Accumulation of momentum
- ![latex-df1cb66d-1eca-460c-8ba7-8af5d9a5b787](data/lecture15/latex-df1cb66d-1eca-460c-8ba7-8af5d9a5b787.png): Actually update the weights

## Unsupervised Learning
- 2 networks
  - Encoder
  - Decoder
- Output of encoder is sent to the input as the decoder
- things could be setup such the decoder is a true inverse of the encoder, or so that they are explicity distinct.
  - When performing backprop, tie the weights (i.e. perform the same increment)
  - ![latex-e85fc7f7-2aca-44fe-8d26-0b11032b8a3e](data/lecture15/latex-e85fc7f7-2aca-44fe-8d26-0b11032b8a3e.png)


![graph-64811b1d-a714-46df-95a3-c74d0fcd21ac](data/lecture15/graph-64811b1d-a714-46df-95a3-c74d0fcd21ac.svg)

