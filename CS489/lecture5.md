# Lecture 5 - January 12

## Representation of Neural Networks
- Input, output vectors
- Weights on the edges and a bias vector
- Can represent everything as matrix-vector operations.
- A layer can be represented as ![latex-b72acaf2-47f0-4ac9-9378-64dc8d41597b](data/lecture5/latex-b72acaf2-47f0-4ac9-9378-64dc8d41597b.png) and ![latex-607e9dea-a0ec-4863-b520-7f7817d022cb](data/lecture5/latex-607e9dea-a0ec-4863-b520-7f7817d022cb.png)


![graph-68d741ef-e3c3-4d7c-9173-52389b450520](data/lecture5/graph-68d741ef-e3c3-4d7c-9173-52389b450520.svg)

Alternatevly:


![graph-776c640c-a476-45b0-8190-b91043ffeace](data/lecture5/graph-776c640c-a476-45b0-8190-b91043ffeace.svg)

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
Need to quantify how close the true output and prediction were for input $x$, our target is ![latex-c593090e-f369-4bdf-8663-515f9e63748a](data/lecture5/latex-c593090e-f369-4bdf-8663-515f9e63748a.png) and the output of the network is ![latex-054081b1-de7e-41e6-b85f-a11a025c9a3f](data/lecture5/latex-054081b1-de7e-41e6-b85f-a11a025c9a3f.png).

### Mean Squared Error
- Associated with linear or ReLu activation functions
- Regression problems

![latex-5f731788-1b93-48dc-8504-fabbaa74ee0a](data/lecture5/latex-5f731788-1b93-48dc-8504-fabbaa74ee0a.png)

### Cross Entropy
- **Assumption**: Output is between `[0,1]` / binary.
- Sigmoid activation functions

![latex-0a5ec282-aef6-41d4-a780-435fcdcff8fa](data/lecture5/latex-0a5ec282-aef6-41d4-a780-435fcdcff8fa.png)

#### Sidenote: Softmax Activation Function
- Ensures the elements add up to 1 (think a probability distribution)
- Take each element as the power of e (i.e. ![latex-31dcf7c4-e550-45ed-a21f-e17bb0a9b23e](data/lecture5/latex-31dcf7c4-e550-45ed-a21f-e17bb0a9b23e.png)), divided by the sum of the new vector.
- ![latex-66bf9cbe-e73b-4e66-9516-9078afb49e06](data/lecture5/latex-66bf9cbe-e73b-4e66-9516-9078afb49e06.png)
- ![latex-3908f01a-1ecc-4622-a6de-00648a1d275d](data/lecture5/latex-3908f01a-1ecc-4622-a6de-00648a1d275d.png)

#### One-Hot Encoding
- Set the max element of a vector to 1, the remainder to 0

## Optimization
- One the cost function is formulated, we can define the neural network as an optimization problem.

Let the network be represented by ![latex-9ec02028-c1bb-4a26-99a1-330a56983c4d](data/lecture5/latex-9ec02028-c1bb-4a26-99a1-330a56983c4d.png)
Goal: ![latex-15ab8c88-7f1f-4586-8339-1031dc745859](data/lecture5/latex-15ab8c88-7f1f-4586-8339-1031dc745859.png)
