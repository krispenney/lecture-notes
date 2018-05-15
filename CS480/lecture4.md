# Lecture 4 - May 14, 2018

## Linear Regression
- Must be linear wrt w, we can make a transform using a non-linear basis function for x.

### What if the normal equation matrix is not invertible?
- Too many features
  - delete redundant
- Add regularization terms

### Gradient Descent
- Need to do feature scaling in order to increase likelihood of convergence

## Generalized Linear Regression
- Why do we do this? We know linear regression well, this allows use to extend our knowledge to non-linear problems.

## Overfitting
- Model can't generalize to new data.
- Very low training error, high testing error

### How to address?
- Reduce the number of features
- regularization: penalize high magnitude features

### Polynomial Curve Fitting Example
- ![latex-63dec5c1-a2ae-4eeb-8a06-c4dba8eb583a](data/lecture4/latex-63dec5c1-a2ae-4eeb-8a06-c4dba8eb583a.png)
- ![latex-f955003d-91ae-4d58-9e15-95c3327f34df](data/lecture4/latex-f955003d-91ae-4d58-9e15-95c3327f34df.png)
- If we set ![latex-13a266d7-a156-424d-af8c-74c2d235bbb5](data/lecture4/latex-13a266d7-a156-424d-af8c-74c2d235bbb5.png) to be very large, then when we minimize the objective functions, these terms will be zero close to 0.

### Ridge Regression
- Add a penalty term
- Some hyperparameter ![latex-088bda13-d81d-4d01-b7d4-25182e04805f](data/lecture4/latex-088bda13-d81d-4d01-b7d4-25182e04805f.png), that controls the penalty
  - Larger lambda puts those terms to 0
- L1, L2 norms.

Goals of the terms
- First: Minimize the training error
- Second: Regulatization terms. Goal is to get a simplify the model.
  - This term is only related to w, not to the bias.
  - The reason for this is that bias just control the intercept, not really the complexity of the model.

- ![latex-c40327f9-2be7-4b3b-8048-58922502265b](data/lecture4/latex-c40327f9-2be7-4b3b-8048-58922502265b.png) (small): basically back to Least Squares
- ![latex-430bf5fb-7c58-4bc2-987d-5d25e50260f8](data/lecture4/latex-430bf5fb-7c58-4bc2-987d-5d25e50260f8.png): w close to 0.

What happens if we remove ![latex-58d2f527-3684-4665-9e78-32d90460e8b1](data/lecture4/latex-58d2f527-3684-4665-9e78-32d90460e8b1.png)?
- changes the optimal ![latex-135c4e50-321a-4297-af38-88c39d657332](data/lecture4/latex-135c4e50-321a-4297-af38-88c39d657332.png)

### Pre-processing
- To simplify the model, we can remove the intercept param via centering and standardization

#### Center Output
- ![latex-bc26f797-3bee-4b7c-a7f8-0154562f3b12](data/lecture4/latex-bc26f797-3bee-4b7c-a7f8-0154562f3b12.png)_
  - subtract by the mean
- See feature scaling

#### Standardize input
- subtract by the mean, divide by standardization.

#### Solution (slide 31)
- Optimal value of ![latex-ffa21dd1-38dc-4fb1-abb3-79db62994515](data/lecture4/latex-ffa21dd1-38dc-4fb1-abb3-79db62994515.png)
- Take the derivative of the equation, solve for b.
- Basically redefine X and Y in terms of the centered and standardized output
- Quadratic optimization problem

#### Ridge Regression with Gradient Descent
- ![latex-23baac94-cca5-4370-91e2-f94762bcaa7c](data/lecture4/latex-23baac94-cca5-4370-91e2-f94762bcaa7c.png)

#### Predictions
- We have some new input value
- Need to standardize it (using the empirical values on the training set)
- transform the output by adding the empirical mean ![latex-8324b034-28f1-48e5-85be-4ab7efa54170](data/lecture4/latex-8324b034-28f1-48e5-85be-4ab7efa54170.png) back (again from the model)

### Connection to MAP
- ![latex-f66e2a4c-e110-43df-b52a-fd527e15d210](data/lecture4/latex-f66e2a4c-e110-43df-b52a-fd527e15d210.png) ~ N(u, sig)
  - pdf is regular normal
- ![latex-1b8b7e78-46e9-4840-a480-664023e6cbe4](data/lecture4/latex-1b8b7e78-46e9-4840-a480-664023e6cbe4.png)

### Sparse
- When terms are close to 0
- Use L1 regularization
- downside: no closed form solution

## Cross Validation

### Conventional Validation
- Partition datasets into train, validation, and test sets (typical ratio: 60/20/20)
  - Train: Helps us fit the model
  - validation set: helps us to choose the best hyperparams
  - test set: assess the model (generalization error)
