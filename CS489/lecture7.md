# Lecture 7 - January 17, 2018

## Perceptrons
- Basic threshold activation function
- Single Layer (no hidden layers)

### Graphical Representation
Can represent the network as a linear combination of the inputs, represents a plane.
- Linear separation of the data into classes (linear classifier)
- Limits the capabilities of perceptrons, can only separate linear classes. Need more complex architecture to handle nonlinear.

## Gradient Descent

The operations of the network can be written as ![latex-a79b532c-e0d5-4d46-ad45-cc222757fb27](data/lecture7/latex-a79b532c-e0d5-4d46-ad45-cc222757fb27.png) with some cost (loss) function ![latex-8278f378-f486-4e3c-ba1c-425a9b720a4a](data/lecture7/latex-8278f378-f486-4e3c-ba1c-425a9b720a4a.png), then learning is the optimization problem.

![latex-a053738b-18b6-45b6-9694-1d76e44693d6](data/lecture7/latex-a053738b-18b6-45b6-9694-1d76e44693d6.png)

Need the gradient for E: Take partial derivatives wrt to each ![latex-d2764102-636f-442b-8ec6-cadeba77d52f](data/lecture7/latex-d2764102-636f-442b-8ec6-cadeba77d52f.png) param (weights and biases).

![latex-899df687-0b73-4752-a42c-85be395eed50](data/lecture7/latex-899df687-0b73-4752-a42c-85be395eed50.png)

### Gradient Based Optimization

If you want to find the local maximum of a function, start somewhere, and keep going up the hill. Want to maximize ![latex-33e122d9-db25-40bc-8fda-e99e1759542c](data/lecture7/latex-33e122d9-db25-40bc-8fda-e99e1759542c.png):

![latex-3f3a32b6-c677-45ae-8d6b-d9648e5ffda2](data/lecture7/latex-3f3a32b6-c677-45ae-8d6b-d9648e5ffda2.png)

If your current position is ![latex-045c4294-76f9-4d6c-8867-eadd8eff34a6](data/lecture7/latex-045c4294-76f9-4d6c-8867-eadd8eff34a6.png), then the next position is ![latex-a25b1fb1-8fc8-4bff-b235-8b17440241a8](data/lecture7/latex-a25b1fb1-8fc8-4bff-b235-8b17440241a8.png)

In the case of neural networks, we're typically interested in minimizing the loss/error. **Gradient Descent**.

#### Note
Gradient learning provides no guarantees that the optima found is the global optima, possible to get stuck on some local.

#### Approximation of Gradients

We can estimate the partial derivitives ![latex-213b6a84-7209-4975-8222-7fc23c296373](data/lecture7/latex-213b6a84-7209-4975-8222-7fc23c296373.png) neumerically, using **Finite-Difference Approximation**, Central differencing.

![latex-911c1543-ea99-47e6-a7e7-096fa05aeee3](data/lecture7/latex-911c1543-ea99-47e6-a7e7-096fa05aeee3.png)
