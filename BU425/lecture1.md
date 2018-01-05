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
- ![latex-60364788-cbb7-4994-bb92-c6ec66b0a00b](data/lecture1/latex-60364788-cbb7-4994-bb92-c6ec66b0a00b.png) - n independent variables
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
![latex-0c43c4e9-0efb-46df-ac82-ac00bbd59d28](data/lecture1/latex-0c43c4e9-0efb-46df-ac82-ac00bbd59d28.png)

The betas are unknown and need to be estimated from the data.

### Estimation of Params
Let ![latex-2bb76c28-148d-4c84-a125-822ff3393cc0](data/lecture1/latex-2bb76c28-148d-4c84-a125-822ff3393cc0.png) be our estimate for the true function.
To find the best estimation for the samples, optimize the squared error: ![latex-03131fa0-f371-45e6-aea9-ed11385a852d](data/lecture1/latex-03131fa0-f371-45e6-aea9-ed11385a852d.png)

### Example

> Does doing homework influence exam grade?

- Exam grade is dependent
- Independent are number of homeworks completed
- **Note:** There could be missing information/variables that represent the true relationship (ex. hours studied, attendence)

This could produce ![latex-a216b516-5fc9-4faa-a8f8-1663cc17b2e2](data/lecture1/latex-a216b516-5fc9-4faa-a8f8-1663cc17b2e2.png)


