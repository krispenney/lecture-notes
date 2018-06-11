# Lecture 12 - June 11, 2018

## Hard Margin SVM
- Same setup as the perceptron algorithm
- binary classification, linearly separable, take the `sign`
- Decision boundary sets the weights and bias such that the margin (of the training set) is maximized.

### Generalization
- SVM's rarely overfit

### SVM Optimization
- We get the objective function by simplifying the margin equation.
- include the output (![latex-75b838f2-3908-4bc9-9d21-f42fe0da7b5e](data/lecture12/latex-75b838f2-3908-4bc9-9d21-f42fe0da7b5e.png)) to get rid of the absolute value
  - this value is always positive (the output is just + or - 1).
- If you multiply the weights and bias by some constant, k. Then the distance to the hyperplane doesn't change. Notice the k cancels out in the margin equation.
- Next, we assume that ![latex-2564c4a6-076b-42de-92fb-5d7990bd0849](data/lecture12/latex-2564c4a6-076b-42de-92fb-5d7990bd0849.png) is 1 for the minimum point. If it's not, then we can just multiply by some k such that this condition is true.
- Then replace with 1, add a condition ![latex-c3f7c342-f31d-47a4-9ee8-4c4bb411c189](data/lecture12/latex-c3f7c342-f31d-47a4-9ee8-4c4bb411c189.png)
- Next transform the optimization problem to a minimization problem (![latex-48b0ad7a-5c68-4eef-9113-a9ee86a2c54a](data/lecture12/latex-48b0ad7a-5c68-4eef-9113-a9ee86a2c54a.png) - if f is positive for all inputs)
- Next, do the squared L2 norm, this gets rid of the square root. Note that ![latex-e50e0e7a-64a4-47b0-8677-28814030e494](data/lecture12/latex-e50e0e7a-64a4-47b0-8677-28814030e494.png)
- Some times we divide by ![latex-cec52fda-f289-4c26-9721-2594b1f6c025](data/lecture12/latex-cec52fda-f289-4c26-9721-2594b1f6c025.png), this assists when we take a derivative, the 2 cancels out. (as we arrive at slide 9)

#### How to solve this optimization problem (Lagrange multipliers)?
- For an unconstrained optimization problem, we can just take the derivative by the minimization variable.
- In the case of SVM, we have use the Lagrange multiplier

We assume we have a convex optimization problem
- quadratic

We have ![latex-8baeca3e-f99a-4347-9417-0a920b904736](data/lecture12/latex-8baeca3e-f99a-4347-9417-0a920b904736.png) st. ![latex-10bc1e08-bb5c-40c8-82db-4f69423d0384](data/lecture12/latex-10bc1e08-bb5c-40c8-82db-4f69423d0384.png)
- Where f is a convex function

![latex-8bc2438a-ea24-4f65-8358-a1c4a6eef54b](data/lecture12/latex-8bc2438a-ea24-4f65-8358-a1c4a6eef54b.png)
- a is an m-dimensional vector
- ![latex-b042d3dc-5721-44ad-801d-629e769308fb](data/lecture12/latex-b042d3dc-5721-44ad-801d-629e769308fb.png)
- Transform a constained optimization problem to an unconstrained problem include the constaints in the objective.

Primal Problem: ![latex-57dbb8af-0a68-45df-900e-b83da0227da3](data/lecture12/latex-57dbb8af-0a68-45df-900e-b83da0227da3.png)_

Dual Problem: ![latex-8f9d6371-1b40-432d-aa10-c2c2c55ab827](data/lecture12/latex-8f9d6371-1b40-432d-aa10-c2c2c55ab827.png)
- Turn it into a maximization problem: ![latex-81131ec3-e81e-41c8-a59a-91313817132d](data/lecture12/latex-81131ec3-e81e-41c8-a59a-91313817132d.png) st ![latex-b7183a89-9bd7-40f4-ab7e-5ca0daab1094](data/lecture12/latex-b7183a89-9bd7-40f4-ab7e-5ca0daab1094.png)
- point can be a max-min: ![latex-31a85443-ce77-4951-b5ce-f971b7a834da](data/lecture12/latex-31a85443-ce77-4951-b5ce-f971b7a834da.png)
- p-star = d-star

#### Karush-Kuhn-Tucker (KKT) conditions
- sufficient conditions for optimality for points with a zero duality gap

#### Slide13
- note that for prediction, the kernel function is not sparse
- to get around this we use: the values of a that are ![latex-793c46b8-82a2-4dce-9f60-4e2e1ae7638f](data/lecture12/latex-793c46b8-82a2-4dce-9f60-4e2e1ae7638f.png)
- Use these to support the prediction
- ![latex-aa3dddd1-9904-4bed-b840-a09a20b984fe](data/lecture12/latex-aa3dddd1-9904-4bed-b840-a09a20b984fe.png)
  - either ![latex-16e24f42-5399-4784-88cc-f97ea0236e79](data/lecture12/latex-16e24f42-5399-4784-88cc-f97ea0236e79.png) or the second term is 0.
  - using condition 3 of KKT
- Then prediction is utilizing the set of support vectors slide 14 (which is a sparse solution)

#### Slide 15
- decision boundary
- margin boundary: Minimum points lie on the boundry, basis for support vectors (use only these for prediction)

#### How to derive params
Next: Need to derive ![latex-3d697fb3-12ff-40ba-9ce4-08702b0f8eda](data/lecture12/latex-3d697fb3-12ff-40ba-9ce4-08702b0f8eda.png)
- ![latex-48ea4618-3722-4c6b-9cd2-5568bbca56d8](data/lecture12/latex-48ea4618-3722-4c6b-9cd2-5568bbca56d8.png) need to solve the dual problem

Derive ![latex-53fe5017-7682-4e99-8df2-45908b494272](data/lecture12/latex-53fe5017-7682-4e99-8df2-45908b494272.png)
- Solve the duel, get a
- Solve for b using any support vector
- A more stable approach is to take the average value of b across all support vectors

Note that multiplying the equation by ![latex-63e4258e-11ee-4b24-9224-7ea39fc10c64](data/lecture12/latex-63e4258e-11ee-4b24-9224-7ea39fc10c64.png) is just multiplying by (1 or -1), solve for b. Then take the average across all support vectors

### Convex sets and Convex hull
- **convex set**: a set of points C is convex is a line segment connecting any two points in C is contained in C.
- **Convex Hull**: Smallest convex set containing C

#### Slide 23

We want to make the optimization problem in terms of a only
- set ![latex-e23380e3-071c-4682-b1f0-29c60a2f8d95](data/lecture12/latex-e23380e3-071c-4682-b1f0-29c60a2f8d95.png)

## Soft Margin SVM

In the Hard margin SVM we assume the dataset is linearlly separable in the feature space ![latex-444514e7-a6fe-4436-939c-bf1b0f692837](data/lecture12/latex-444514e7-a6fe-4436-939c-bf1b0f692837.png)
- Remove the hard constrain, allow some points to be on the wrong side of the boundary

Fix a few edge-cases
- non-linearly separable data
- The data is linearly separable, but we want to avoid noisy data points.

Add a penalty term that increases linearly with the distance from the margin boundary
- 0 for points on the correct side of the margin
