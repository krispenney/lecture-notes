# Lecture 3 - May 9, 2018: Linear Regression

## Regression

Given a pair ![latex-ee862413-fe8d-4004-9ce7-0ccd48cdb9fb](data/lecture3/latex-ee862413-fe8d-4004-9ce7-0ccd48cdb9fb.png), find a function f such that: ![latex-ce1fb138-ea1f-4e9c-92e7-961b84388f35](data/lecture3/latex-ce1fb138-ea1f-4e9c-92e7-961b84388f35.png)
- X: d-dim real vector, feature vector
- Y: Continuous response, 1-dim real value

Problems:
1. (X, Y) is uncertain: training samples are from some unknown distribution
  - pulled from some unknown function
  - typically noisy in some aspect
2. Measure the error using a loss function
  - Which one should we use?

### Risk Minimization
- Minimize the expected loss: ![latex-66e94cee-e7f6-411c-847c-82e254b8136e](data/lecture3/latex-66e94cee-e7f6-411c-847c-82e254b8136e.png)_
- Note that f(x) and Y are in the Y range.
- ![latex-5927c129-4df9-4611-8855-c1d55ced8a58](data/lecture3/latex-5927c129-4df9-4611-8855-c1d55ced8a58.png)
- Least Squares: ![latex-2e80456e-6614-426e-a705-226580d5904c](data/lecture3/latex-2e80456e-6614-426e-a705-226580d5904c.png)
  - minimize the squared difference between our prediction and the true output

### Regression Function
- We can compose the expectation over 2 steps
  - ![latex-8374a896-1cf6-4204-9aef-129d8a6ba64d](data/lecture3/latex-8374a896-1cf6-4204-9aef-129d8a6ba64d.png)_
  - Note that if we minimize the inner objective (![latex-ddce66a7-c8f9-4fae-9be9-f09143a70be0](data/lecture3/latex-ddce66a7-c8f9-4fae-9be9-f09143a70be0.png)), then it's the same as minimzing the entire
  - ![latex-6a2bf1f4-4043-4e73-aa5c-dadb66b0cec1](data/lecture3/latex-6a2bf1f4-4043-4e73-aa5c-dadb66b0cec1.png)_
  - ![latex-651a74b1-c1ad-490c-aaf9-14f415f7aceb](data/lecture3/latex-651a74b1-c1ad-490c-aaf9-14f415f7aceb.png)

### linear hypothesis


![graph-043d242e-fccc-4d12-87ca-3a80f1e21754](data/lecture3/graph-043d242e-fccc-4d12-87ca-3a80f1e21754.svg)

### Example Housing Prices

| Size (square feet) - ![latex-daef3b56-ad5f-4ac9-99c0-fc482146a014](data/lecture3/latex-daef3b56-ad5f-4ac9-99c0-fc482146a014.png) | # bedrooms ![latex-bbf44f1d-513d-475c-906e-b1b152fcf9e2](data/lecture3/latex-bbf44f1d-513d-475c-906e-b1b152fcf9e2.png) | Number of floor s![latex-4eca0322-2aaf-43e3-bd2a-4dc1e71c9c66](data/lecture3/latex-4eca0322-2aaf-43e3-bd2a-4dc1e71c9c66.png) | Age of Home ![latex-8da25691-ef47-43a5-b92b-35570dc0f047](data/lecture3/latex-8da25691-ef47-43a5-b92b-35570dc0f047.png) | Price ($1000s) ![latex-ed1c8da3-e7d0-43b1-bdd5-1d9de377380c](data/lecture3/latex-ed1c8da3-e7d0-43b1-bdd5-1d9de377380c.png) |
|-|-|-|-|-|
| 2104 | 5 | 1 | 45 | 460 |
| 1416 | 3 | 2 | 40 | 232 |
| 1534 | 3 | 2 | 30 | 315 |
| 852 | 2 | 1 | 36 | 178 |

- First 4 columns are the input features
- Last column is the output
- ![latex-7a3444da-7e6d-4778-8f7b-354860d0c811](data/lecture3/latex-7a3444da-7e6d-4778-8f7b-354860d0c811.png)

#### Formally

Assumptions
- Linear in w
  - this is more important, we can replace x with something non-linear
- Linear in x

![latex-1d731801-42ec-42fc-abac-b45a08492750](data/lecture3/latex-1d731801-42ec-42fc-abac-b45a08492750.png)
- w and x are both column vectors, this is an inner product.
- Note: ![latex-d3200e5e-6c04-49f5-b514-d22d3175625a](data/lecture3/latex-d3200e5e-6c04-49f5-b514-d22d3175625a.png)
- Loss function: Mean Squared Error
  - ![latex-49f176f3-c0fc-4da7-9ae9-9047f68c2407](data/lecture3/latex-49f176f3-c0fc-4da7-9ae9-9047f68c2407.png)
- Empirical Risk (mean)
  - Ideally we would want to use the true distribution, but we don't know what this is.

### Simplification Again (Slide 11)
- ![latex-936da5a7-b51c-4f40-b936-e2f975687a69](data/lecture3/latex-936da5a7-b51c-4f40-b936-e2f975687a69.png): Just add 1 to the top of x
- add the bias to the top of w, is a d+1 vector
- Last one is L2 Norm

### Connection to ML (slide 13)
1. Likelihood function
  - Recall that this is just the pdf of the underlying distribution
  - For this example it's just the PDF of the normal distribution
Recall that the constant coeifficents can be ignored as they don't effect the optimization of the objective function.
- Maximizing the negative is the same as minimizing the positive

### Normal Equation
- Recall that the squared L2-Norm can be written as ![latex-7bf44073-40bf-472c-b02f-af5632b6fc9c](data/lecture3/latex-7bf44073-40bf-472c-b02f-af5632b6fc9c.png)
- To simplify remember
  - ![latex-4b70ec56-39bf-4b22-818d-391b2260e218](data/lecture3/latex-4b70ec56-39bf-4b22-818d-391b2260e218.png)
  - ![latex-336044f7-f6a6-4258-8647-899f038006c8](data/lecture3/latex-336044f7-f6a6-4258-8647-899f038006c8.png)
- Using the facts we get: ![latex-cfdc2dde-885a-4131-8ccf-26cf767399db](data/lecture3/latex-cfdc2dde-885a-4131-8ccf-26cf767399db.png)
  - solve and divide by 2 to get the Normal equation
- Normal Equation: ![latex-5b29b19b-ffa3-46b0-97b8-c27f3805e1e1](data/lecture3/latex-5b29b19b-ffa3-46b0-97b8-c27f3805e1e1.png)
  - Solve this using the system of linear equations
    - Easier / more efficient to implement: ![latex-c92907d5-f5e1-4c51-b6df-045e2b3f540b](data/lecture3/latex-c92907d5-f5e1-4c51-b6df-045e2b3f540b.png), instead of ![latex-05876266-639d-40d4-9202-f68ea63aaef4](data/lecture3/latex-05876266-639d-40d4-9202-f68ea63aaef4.png)
  - Analytical solution is ![latex-7446b5b2-257e-4c04-877e-32e80719c421](data/lecture3/latex-7446b5b2-257e-4c04-877e-32e80719c421.png)

#### When it is non-invertable
- Redundent features (linearly dependent)
  - Can get around this by deleting the redundent features
- Can also occur if there are too many features ![latex-6840832f-9ab8-4435-a2eb-3716df310629](data/lecture3/latex-6840832f-9ab8-4435-a2eb-3716df310629.png)
  - Delete features or use regularization

### Gradient Descent
- ![latex-bb9ce7ae-1874-4767-8184-384d9c12363f](data/lecture3/latex-bb9ce7ae-1874-4767-8184-384d9c12363f.png)
  - iterate until convergence
  - If the learning rate is too low, the algorithm will take a very long time
  - If the learning rate is too high, it will fail to converge
  - See chapter 9 in Convex Optimization to choose learning rate.
- ![latex-a9c26e63-664f-41cf-aafe-47dfc6f528f0](data/lecture3/latex-a9c26e63-664f-41cf-aafe-47dfc6f528f0.png)
- Need to make sure that the features are on the same scale
  - We can do standardization: ![latex-36a4a10f-7a2b-4ba6-9af2-0135c113246d](data/lecture3/latex-36a4a10f-7a2b-4ba6-9af2-0135c113246d.png)
  - Example: In the housing example the features are not on the same scale

### Gradient vs. Normal Equation Trade-offs

Gradient
- need to choose learning rate
- many iterations
- works well for many features

Normal Equation
- No learning rate
- No iterations
- Slow if the number of features is large
  - Recall that ![latex-5c420d26-fdc5-43f7-bd55-9122c0a10c41](data/lecture3/latex-5c420d26-fdc5-43f7-bd55-9122c0a10c41.png)

### Non-Linear Regression
- We can do it by constructing a different features space and doing linear regression in that space

#### Example
- Suppose we have a quadratic model: ![latex-abfe7599-2462-4576-9411-b3d95ad4fdb5](data/lecture3/latex-abfe7599-2462-4576-9411-b3d95ad4fdb5.png)
- Construct a vector ![latex-eb6bb54a-ea52-4e4a-902a-6c90595b748b](data/lecture3/latex-eb6bb54a-ea52-4e4a-902a-6c90595b748b.png), then ![latex-b652f03e-e1d5-48f2-91dd-d9a4c57ac601](data/lecture3/latex-b652f03e-e1d5-48f2-91dd-d9a4c57ac601.png)

#### Quadratic Fitting
- underlying function is quadratic
- ![latex-55e3e60a-c676-4c33-8410-63aabf259aa5](data/lecture3/latex-55e3e60a-c676-4c33-8410-63aabf259aa5.png)
- Polynomial Regression: ![latex-391227d4-a24a-4d2e-b03d-751be740b301](data/lecture3/latex-391227d4-a24a-4d2e-b03d-751be740b301.png)
  - Use the linear regression framework as usual.
