# Lecture 5 - January 12

## Representation of Neural Networks
- Input, output vectors
- Weights on the edges and a bias vector
- Can represent everything as matrix-vector operations.
- A layer can be represented as ![latex-c1fcd20c-14e9-41ed-bbbc-081d9ff01f89](data/lecture5/latex-c1fcd20c-14e9-41ed-bbbc-081d9ff01f89.png) and ![latex-3935e96f-0385-44ae-9e92-3ba58d1eb101](data/lecture5/latex-3935e96f-0385-44ae-9e92-3ba58d1eb101.png)


![graph-e81df7b7-4daa-4ce4-ac40-e4ac92cabce4](data/lecture5/graph-e81df7b7-4daa-4ce4-ac40-e4ac92cabce4.svg)

Alternatevly:


![graph-e089757f-aecf-418e-8538-397a2053f5fc](data/lecture5/graph-e089757f-aecf-418e-8538-397a2053f5fc.svg)

## Neural Learning
- To get the network to do what you want, you must find the connection weights that yeild the desired behaviour.
- Adjust connection weights + biases

### Supervised Learning
- Labelled data
- Can compute the real error and adjust.

### Unsupervised Learning
- Unlabelled data
- Not clear what the output should be
- Goal is to find an efficient representation of the structure of the data.

### Reinforement Learning
- Given infrequent feedback to guide
- Example: feedback when win/loose a game, no mention of inbetween steps / how to improve.

## Cost Functions
Need to quantify how close the true output and prediction were for input $x$, our target is ![latex-5e2ca615-0394-4e69-8af4-46575d9b00f4](data/lecture5/latex-5e2ca615-0394-4e69-8af4-46575d9b00f4.png) and the output of the network is ![latex-7c59c2ad-a3fe-4a75-8ca4-70fe861d702c](data/lecture5/latex-7c59c2ad-a3fe-4a75-8ca4-70fe861d702c.png).

### Mean Squared Error
- Associated with linear or ReLu activation functions
- Regression problems

![latex-b282e11d-45a4-4902-91cf-719cb24a6748](data/lecture5/latex-b282e11d-45a4-4902-91cf-719cb24a6748.png)

### Cross Entropy
- **Assumption**: Output is between `[0,1]` / binary.
- Sigmoid activation functions

![latex-6b346d8f-a91e-43d4-a04c-11cb2c3ba2e7](data/lecture5/latex-6b346d8f-a91e-43d4-a04c-11cb2c3ba2e7.png)

#### Sidenote: Softmax Activation Function
- Ensures the elements add up to 1 (think a probability distribution)
- Take each element as the power of e (i.e. ![latex-07f31e71-1a73-4864-94f4-461a36976ef2](data/lecture5/latex-07f31e71-1a73-4864-94f4-461a36976ef2.png)), divided by the sum of the new vector.
- ![latex-ac8d1971-07b3-44d6-bcf5-53504b1e10f5](data/lecture5/latex-ac8d1971-07b3-44d6-bcf5-53504b1e10f5.png)
- ![latex-1934d56d-c7b7-4aeb-b873-46d99af53e0d](data/lecture5/latex-1934d56d-c7b7-4aeb-b873-46d99af53e0d.png)

#### One-Hot Encoding
- Set the max element of a vector to 1, the remainder to 0

## Optimization
- One the cost function is formulated, we can define the neural network as an optimization problem.

Let the network be represented by ![latex-53f72cd9-0b12-491e-bf43-f45d1858e786](data/lecture5/latex-53f72cd9-0b12-491e-bf43-f45d1858e786.png)
Goal: ![latex-7e733311-b547-4d23-9b59-824ce9427c6b](data/lecture5/latex-7e733311-b547-4d23-9b59-824ce9427c6b.png)
