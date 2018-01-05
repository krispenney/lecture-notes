# Lecture 1 - January 5, 2018

## Types of Analytics
Categorize by the goal, methods used, etc.

### Exploratory Analytics (Unsupervised Learning)
- unlabelled data
- try to group and cluster the data
- find patterns
- "What segments of customers do I have?"

### Descriptive Analysis
- Prep and analyze historical data
- identifies patterns
- "What is the risk of a particaular asset?"

### Explanatory analytics
- Establish causation
- "What determines the price of a house?"
  - number of bedrooms, bathrooms
  - square footage
  - location
  - try to figure out what causes that price => What happens if a renovate the bathroom?

### Predictive Analytics (Supervised Learning)
- Predict future events / unknown characteristics
- Don't care about modifications
- Machine learning
  - labelled data
- "How much will this house sell for?"

### Prescriptive Analytics
- Optimization problems
- "What is the best investment portfolio?"

## Regression Analysis

Utimately want to answer "how is Y related to X?"
- Y dependant
- ![latex-f17cae64-13ce-4bf2-ba33-7c631aacc90a](data/lecture1/latex-f17cae64-13ce-4bf2-ba33-7c631aacc90a.png) - n independent variables
- Linear relationship

### Descriptive POV
Simply quantifying a relationship, describe it.

### Explanatory POV
Try to support some causal claim
- Increase housing price by 10% -> Increase in square footage

### Predictive POV
Use "quantified relationships" to predict new values of Y, given some X values.
- Forecasting
- Given some information about a house, predict it's price.

## Linear regression
![latex-ab52452c-42c0-4823-8eaa-e5557312f0ec](data/lecture1/latex-ab52452c-42c0-4823-8eaa-e5557312f0ec.png)

The betas are unknown and need to be estimated from the data.

### Estimation of Params
Let ![latex-59bbce9c-26b0-468c-beb0-d52fd09ba4b2](data/lecture1/latex-59bbce9c-26b0-468c-beb0-d52fd09ba4b2.png) be our estimate for the true function.
To find the best estimation for the samples, optimize the squared error: ![latex-29eb0a39-b3e9-46a6-9b79-7ed2441f488d](data/lecture1/latex-29eb0a39-b3e9-46a6-9b79-7ed2441f488d.png)

### Example

> Does doing homework influence exam grade?

- Exam grade is dependent
- Independent are number of homeworks completed
- **Note:** There could be missing information/variables that represent the true relationship (ex. hours studied, attendence)

This could produce ![latex-cf3fdc6c-cbaa-4438-a8c5-e8f4a179b67b](data/lecture1/latex-cf3fdc6c-cbaa-4438-a8c5-e8f4a179b67b.png)

## Multiple Linear Regression
Regression model with ![latex-4f8b9802-9c36-4880-9d67-c77456867237](data/lecture1/latex-4f8b9802-9c36-4880-9d67-c77456867237.png) independent variables. Each indepedent variable influences the relationship in some proportion

## Assessing a Regression Model
Least squares will produce a regression line *regardless* if there is actually a linear relationship in the data.

### Model Error
- Residuals: Error between the models and the sample data.

### Coefficent of Determination
- Measures goodness of fit
- Adding independent variables **always** increases R^2
- Model error vs risidual error
![latex-a2106cfe-a038-4c04-9062-fe2d42553bb8](data/lecture1/latex-a2106cfe-a038-4c04-9062-fe2d42553bb8.png)

### Hypothesis Testing (p-value)
- Null hypothesis: ![latex-538e1406-839a-4ba0-a9c2-6fc0e2c8b4d7](data/lecture1/latex-538e1406-839a-4ba0-a9c2-6fc0e2c8b4d7.png)
- lower p-values are better

## Assumptions
- Y is linearly related to X
- Relevant X's are used
