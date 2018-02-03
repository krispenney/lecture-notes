# Lecture 14 - February 2, 2018

## Deep Neural Networks
- Universal Approximation Theorem

## Enhancing Optimization
- Minimize the expected loss over all training samples
- Inputs and targets are individual vectors, can assemble these into matricies.
  - Use each in a column, then weights can multiply out
  - Perform outer product with `[1, 1, ...., 1]` on bias to apply to all

### Backprop

#### Output Layer
- ![latex-dcaf50e6-59eb-4231-af7a-78c38e21815c](data/lecture14/latex-dcaf50e6-59eb-4231-af7a-78c38e21815c.png)
- ![latex-e4285638-a19f-4550-abc2-1d4ecf068a6b](data/lecture14/latex-e4285638-a19f-4550-abc2-1d4ecf068a6b.png)
  - Y rows, P columns

#### Working Back
- Basically do the same thing as before, but each sample is a column
- ![latex-7bbfad13-a258-4df2-ac7d-4f7ff893a7ab](data/lecture14/latex-7bbfad13-a258-4df2-ac7d-4f7ff893a7ab.png)
  - 1 column for each sample

#### Problems
- This approach is slow if the dataset is very large
- Very few updates

### Stochastic Gradient Descent
- Take mini-batches of training samples
- Randomly select from the dataset
- Use batches to determine weight updates
- More stable than processing individuals at a time.
- this can use the matrix ideas as above, just number of columns == batch size

### Momentum
- During gradient descent, there is oscillation (stepping past, going back)
- From physics: ![latex-47367ff6-b6ca-4ef3-a175-d4c080178b50](data/lecture14/latex-47367ff6-b6ca-4ef3-a175-d4c080178b50.png) and ![latex-556d6346-cd27-4fd2-a41e-39b334fb7c6e](data/lecture14/latex-556d6346-cd27-4fd2-a41e-39b334fb7c6e.png)
- Solving numerically using Euler's method
- Think about friction, take your foot off of the accelerator, slow down over time

