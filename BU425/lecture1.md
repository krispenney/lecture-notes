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
- ![latex-56fad552-017d-4f55-8298-c4ba80d38d0b](data/lecture1/latex-56fad552-017d-4f55-8298-c4ba80d38d0b.png) - n independent variables
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
![latex-6dc83aab-a4f2-4bec-b00b-aac097012a39](data/lecture1/latex-6dc83aab-a4f2-4bec-b00b-aac097012a39.png)

The betas are unknown and need to be estimated from the data.

### Estimation of Params
Let ![latex-ce2f804f-983e-4a7f-95c8-9924e2c0b044](data/lecture1/latex-ce2f804f-983e-4a7f-95c8-9924e2c0b044.png) be our estimate for the true function.
To find the best estimation for the samples, optimize the squared error: ![latex-ca59ebe5-5a5c-4ea8-804c-13e1a3d09dc8](data/lecture1/latex-ca59ebe5-5a5c-4ea8-804c-13e1a3d09dc8.png)

### Example

> Does doing homework influence exam grade?

- Exam grade is dependent
- Independent are number of homeworks completed
- **Note:** There could be missing information/variables that represent the true relationship (ex. hours studied, attendence)

This could produce ![latex-9be97ff0-c291-446c-9e76-029223c14dc2](data/lecture1/latex-9be97ff0-c291-446c-9e76-029223c14dc2.png)

## Multiple Linear Regression
Regression model with ![latex-e998a42e-9a38-449d-a1c1-5a47575c2077](data/lecture1/latex-e998a42e-9a38-449d-a1c1-5a47575c2077.png) independent variables. Each indepedent variable influences the relationship in some proportion

## Assessing a Regression Model
Least squares will produce a regression line *regardless* if there is actually a linear relationship in the data.

### Model Error
- Residuals: Error between the models and the sample data.

### Coefficent of Determination
- Measures goodness of fit
- Adding independent variables **always** increases $$R^2![latex-e19eb431-b118-4356-a869-8da49fc01623](data/lecture1/latex-e19eb431-b118-4356-a869-8da49fc01623.png)

### Hypothesis Testing (p-value)
- Null hypothesis: ![latex-05f27a7a-8ead-4594-a3e1-d16111733b47](data/lecture1/latex-05f27a7a-8ead-4594-a3e1-d16111733b47.png)
- lower p-values are better

## Assumptions
- Y is linearly related to X
- Relevant X's are used
