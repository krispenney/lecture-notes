# Lecture 3 - May 9, 2018: Linear Regression

## Regression

Given a pair ![latex-73f862e6-6ac1-4513-b844-23aff01bab5a](data/lecture3/latex-73f862e6-6ac1-4513-b844-23aff01bab5a.png), find a function f such that: ![latex-52812dcb-c7e9-4a82-8874-4f0c774ed172](data/lecture3/latex-52812dcb-c7e9-4a82-8874-4f0c774ed172.png)
- X: d-dim real vector, feature vector
- Y: Continuous response, 1-dim real value

Problems:
1. (X, Y) is uncertain: training samples are from some unknown distribution
  - pulled from some unknown function
  - typically noisy in some aspect
2. Measure the error using a loss function
  - Which one should we use?

### Risk Minimization
- Minimize the expected loss: ![latex-05e644a8-d66c-46c8-b2c9-c24785c402ec](data/lecture3/latex-05e644a8-d66c-46c8-b2c9-c24785c402ec.png)_
- Note that f(x) and Y are in the Y range.
- ![latex-213c1e92-cf6b-4f49-9d8f-677091bc6476](data/lecture3/latex-213c1e92-cf6b-4f49-9d8f-677091bc6476.png)
- Least Squares: ![latex-1fbc7384-cdf4-49b6-8ede-8590db05eb82](data/lecture3/latex-1fbc7384-cdf4-49b6-8ede-8590db05eb82.png)
  - minimize the squared difference between our prediction and the true output

### Regression Function
- We can compose the expectation over 2 steps
  - ![latex-7db39268-9398-4fad-b259-4e55fd72342e](data/lecture3/latex-7db39268-9398-4fad-b259-4e55fd72342e.png)_
  - Note that if we minimize the inner objective (![latex-4d143dc4-1c23-4716-aec7-46561d8a0920](data/lecture3/latex-4d143dc4-1c23-4716-aec7-46561d8a0920.png)), then it's the same as minimzing the entire
  - ![latex-5acbdba1-c17d-4615-b75e-ec100f254ba0](data/lecture3/latex-5acbdba1-c17d-4615-b75e-ec100f254ba0.png)_
  - ![latex-655c6029-f648-450a-9ea4-9cb3c75be6ab](data/lecture3/latex-655c6029-f648-450a-9ea4-9cb3c75be6ab.png)

### linear hypothesis


![graph-65f02134-30c1-47aa-9001-644cc895f4d0](data/lecture3/graph-65f02134-30c1-47aa-9001-644cc895f4d0.svg)

### Example Housing Prices

| Size (square feet) - ![latex-6e5a7dfa-2cef-4fec-b764-26fbab8a3958](data/lecture3/latex-6e5a7dfa-2cef-4fec-b764-26fbab8a3958.png) | # bedrooms ![latex-45ce1c22-b328-4053-a9ae-b071651d9f5a](data/lecture3/latex-45ce1c22-b328-4053-a9ae-b071651d9f5a.png) | Number of floor s![latex-e43bd680-7a0e-4277-add9-5454058e0d49](data/lecture3/latex-e43bd680-7a0e-4277-add9-5454058e0d49.png) | Age of Home ![latex-86bb691a-3f8b-4ef6-b31f-4cfe29e9798f](data/lecture3/latex-86bb691a-3f8b-4ef6-b31f-4cfe29e9798f.png) | Price ($1000s) ![latex-b2f14138-5461-4d64-8ff9-82664a17cf3a](data/lecture3/latex-b2f14138-5461-4d64-8ff9-82664a17cf3a.png) |
|-|-|-|-|-|
| 2104 | 5 | 1 | 45 | 460 |
| 1416 | 3 | 2 | 40 | 232 |
| 1534 | 3 | 2 | 30 | 315 |
| 852 | 2 | 1 | 36 | 178 |

- First 4 columns are the input features
- Last column is the output
- ![latex-a2b737a3-9191-4ff7-95a5-84f993334585](data/lecture3/latex-a2b737a3-9191-4ff7-95a5-84f993334585.png)

#### Formally

Assumptions
- Linear in w
  - this is more important, we can replace x with something non-linear
- Linear in x

![latex-39b13e3b-991e-4e2e-922a-5bff96aa83a4](data/lecture3/latex-39b13e3b-991e-4e2e-922a-5bff96aa83a4.png)
- w and x are both column vectors, this is an inner product.
- Note: ![latex-0b7ae29f-5245-4f44-8b9d-151805bf77fb](data/lecture3/latex-0b7ae29f-5245-4f44-8b9d-151805bf77fb.png)
- Loss function: Mean Squared Error
  - ![latex-062fe93d-ab69-412e-bd8b-99ba3a8e04fb](data/lecture3/latex-062fe93d-ab69-412e-bd8b-99ba3a8e04fb.png)
- Empirical Risk (mean)
  - Ideally we would want to use the true distribution, but we don't know what this is.

### Simplification Again (Slide 11)
- ![latex-e78995e1-fe83-406d-9c41-e72c594776fe](data/lecture3/latex-e78995e1-fe83-406d-9c41-e72c594776fe.png): Just add 1 to the top of x
- add the bias to the top of w, is a d+1 vector
- Last one is L2 Norm

### Connection to ML (slide 13)
1. Likelihood function
  - Recall that this is just the pdf of the underlying distribution
  - For this example it's just the PDF of the normal distribution
Recall that the constant coeifficents can be ignored as they don't effect the optimization of the objective function.
- Maximizing the negative is the same as minimizing the positive

### Normal Equation
- Recall that the squared L2-Norm can be written as ![latex-88a5b7f8-3713-4905-9104-87bfa8190e17](data/lecture3/latex-88a5b7f8-3713-4905-9104-87bfa8190e17.png)
- To simplify remember
  - ![latex-a01bc052-750d-427c-94dd-4806de39b42d](data/lecture3/latex-a01bc052-750d-427c-94dd-4806de39b42d.png)
  - ![latex-b8fb84c7-71af-41eb-b076-9813efc587ee](data/lecture3/latex-b8fb84c7-71af-41eb-b076-9813efc587ee.png)
- Using the facts we get: ![latex-3ca9f11a-51c1-475c-a7db-7824233c4325](data/lecture3/latex-3ca9f11a-51c1-475c-a7db-7824233c4325.png)
  - solve and divide by 2 to get the Normal equation
- Normal Equation: ![latex-def42be3-cf38-4b62-a519-1a76b3307573](data/lecture3/latex-def42be3-cf38-4b62-a519-1a76b3307573.png)
  - Solve this using the system of linear equations
    - Easier / more efficient to implement: ![latex-fe6f97f9-69e8-4940-b1f9-f02759149c6b](data/lecture3/latex-fe6f97f9-69e8-4940-b1f9-f02759149c6b.png), instead of ![latex-77db7bd2-7de6-4aba-93ca-59910a9821e4](data/lecture3/latex-77db7bd2-7de6-4aba-93ca-59910a9821e4.png)
  - Analytical solution is ![latex-3e3532a7-98cb-41ee-96ae-bdf1372c6da9](data/lecture3/latex-3e3532a7-98cb-41ee-96ae-bdf1372c6da9.png)

#### When it is non-invertable
- Redundent features (linearly dependent)
  - Can get around this by deleting the redundent features
- Can also occur if there are too many features ![latex-bfd75579-9c68-415b-9b08-31a24c3aab20](data/lecture3/latex-bfd75579-9c68-415b-9b08-31a24c3aab20.png)
  - Delete features or use regularization

### Gradient Descent
- ![latex-9aa92c15-5501-4609-9d7b-c0cf8768e367](data/lecture3/latex-9aa92c15-5501-4609-9d7b-c0cf8768e367.png)
  - iterate until convergence
  - If the learning rate is too low, the algorithm will take a very long time
  - If the learning rate is too high, it will fail to converge
  - See chapter 9 in Convex Optimization to choose learning rate.
- ![latex-2330f67d-12d8-47a6-a1ca-81f374d1bd84](data/lecture3/latex-2330f67d-12d8-47a6-a1ca-81f374d1bd84.png)
- Need to make sure that the features are on the same scale
  - We can do standardization: ![latex-0b2ba9e1-605a-4078-b5ab-d1402cf8609a](data/lecture3/latex-0b2ba9e1-605a-4078-b5ab-d1402cf8609a.png)
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
  - Recall that ![latex-579f7a37-e9fc-45f2-924d-48df3aacb7e0](data/lecture3/latex-579f7a37-e9fc-45f2-924d-48df3aacb7e0.png)

### Non-Linear Regression
- We can do it by constructing a different features space and doing linear regression in that space

#### Example
- Suppose we have a quadratic model: ![latex-d297351e-2127-49a5-b2d6-c761f81d54a6](data/lecture3/latex-d297351e-2127-49a5-b2d6-c761f81d54a6.png)
- Construct a vector ![latex-c1df1a55-448f-4e4d-a1f0-dc12b096b19f](data/lecture3/latex-c1df1a55-448f-4e4d-a1f0-dc12b096b19f.png), then ![latex-cafebba3-8309-4ea6-bf84-166e983c1c4b](data/lecture3/latex-cafebba3-8309-4ea6-bf84-166e983c1c4b.png)

#### Quadratic Fitting
- underlying function is quadratic
- ![latex-9a8ec2c8-0e53-43a6-b56c-6a88d88fcc6e](data/lecture3/latex-9a8ec2c8-0e53-43a6-b56c-6a88d88fcc6e.png)
- Polynomial Regression: ![latex-18b34e42-e05a-443f-a570-29901cc0b413](data/lecture3/latex-18b34e42-e05a-443f-a570-29901cc0b413.png)
  - Use the linear regression framework as usual.
