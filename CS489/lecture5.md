# Lecture 5 - January 12

## Representation of Neural Networks
- Input, output vectors
- Weights on the edges and a bias vector
- Can represent everything as matrix-vector operations.
- A layer can be represented as ![latex-c838dd88-4611-44f1-8979-6c0356afa2e3](data/lecture5/latex-c838dd88-4611-44f1-8979-6c0356afa2e3.png) and ![latex-a4f1d2d1-07dd-41ab-a885-427464b318be](data/lecture5/latex-a4f1d2d1-07dd-41ab-a885-427464b318be.png)


![graph-3962dab2-7479-43f0-b574-a2157865dff9](data/lecture5/graph-3962dab2-7479-43f0-b574-a2157865dff9.svg)

Alternatevly:


![graph-50b28ddf-6402-48d9-8d3e-f7ccbe03cfd4](data/lecture5/graph-50b28ddf-6402-48d9-8d3e-f7ccbe03cfd4.svg)

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
Need to quantify how close the true output and prediction were for input $x$, our target is ![latex-26028eef-1ad4-40c0-8194-f56979b1a4a4](data/lecture5/latex-26028eef-1ad4-40c0-8194-f56979b1a4a4.png) and the output of the network is ![latex-fc888294-d8bf-42a9-abf1-1895d01d4565](data/lecture5/latex-fc888294-d8bf-42a9-abf1-1895d01d4565.png).

### Mean Squared Error
- Associated with linear or ReLu activation functions
- Regression problems

![latex-31651d0a-a233-409b-887d-403a7e6c79db](data/lecture5/latex-31651d0a-a233-409b-887d-403a7e6c79db.png)

### Cross Entropy
- **Assumption**: Output is between `[0,1]` / binary.
- Sigmoid activation functions

![latex-84f7c5af-4dd2-4543-acb2-96f1fcdd348a](data/lecture5/latex-84f7c5af-4dd2-4543-acb2-96f1fcdd348a.png)

#### Sidenote: Softmax Activation Function
- Ensures the elements add up to 1 (think a probability distribution)
- Take each element as the power of e (i.e. ![latex-dbd98c97-b73b-4e88-b199-49adac6709a0](data/lecture5/latex-dbd98c97-b73b-4e88-b199-49adac6709a0.png)), divided by the sum of the new vector.
- ![latex-b18ac302-3ac8-4257-922e-92d52ae5afc4](data/lecture5/latex-b18ac302-3ac8-4257-922e-92d52ae5afc4.png)
- ![latex-19d70d29-ad5b-414e-a8ba-fb1f3bafb9e7](data/lecture5/latex-19d70d29-ad5b-414e-a8ba-fb1f3bafb9e7.png)

#### One-Hot Encoding
- Set the max element of a vector to 1, the remainder to 0

## Optimization
- One the cost function is formulated, we can define the neural network as an optimization problem.

Let the network be represented by ![latex-fc08f8c3-2c73-46d6-a336-9632a2540c0d](data/lecture5/latex-fc08f8c3-2c73-46d6-a336-9632a2540c0d.png)
Goal: ![latex-0225e4b3-9d3d-49f3-b249-8cbe1b71c749](data/lecture5/latex-0225e4b3-9d3d-49f3-b249-8cbe1b71c749.png)
