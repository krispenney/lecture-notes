# Lecture 2 - January 12, 2018

## Logistic Regression

![latex-32082494-bfc1-425e-89e1-910907c9b6e2](data/lecture2/latex-32082494-bfc1-425e-89e1-910907c9b6e2.png)
![latex-875811cd-5006-4a29-ae66-5e9fe1bbfc17](data/lecture2/latex-875811cd-5006-4a29-ae66-5e9fe1bbfc17.png)

The goal is to find optimal params ![latex-7c46f2dc-f0d4-4979-be72-20bfa2547688](data/lecture2/latex-7c46f2dc-f0d4-4979-be72-20bfa2547688.png) to optimize log likelihood

### Explanetory context
Example: What is causing someone to where a jacket
- Interperet results as a probability.
- ![latex-2bb8a744-1918-4f6c-9910-2eb103f44c3c](data/lecture2/latex-2bb8a744-1918-4f6c-9910-2eb103f44c3c.png)
- **Parametric assumption**: Follow sigmoid shape, low-high or high-low

### Odds Ratio

![latex-c22fcb1c-9c33-4535-bc00-009551cd20f3](data/lecture2/latex-c22fcb1c-9c33-4535-bc00-009551cd20f3.png)

Example: The horse has ![latex-e8a320ff-d0ac-4975-9f00-c679cb5ce3a2](data/lecture2/latex-e8a320ff-d0ac-4975-9f00-c679cb5ce3a2.png) odds of winning the race, probability of winning is 5/7.

### Linear Log odds ratio

![latex-c55ca48b-e4fa-41a4-9369-8a81b9b33947](data/lecture2/latex-c55ca48b-e4fa-41a4-9369-8a81b9b33947.png)

## Pilgrim Bank Case A

### Industry
- Retail banking: 2001
  - Dot-com era, pre crash, pre 911
  - Internet big new thing, new oppourtunities
- B2C, lots of small consumers
- Not always clear what drives profits
  - Depends on amount of fees paid
  - Services used
- Customers are pretty loyal, not trivial to switch banks

- Alan Green
  - analyst
  - online banking group
- Bank isn't sure about which business model to use for their online banking channel
  - should they charge a fee for online banking?
  - analysis should provide evidence to support some claim

- Intuitively:
  - reasons for no
    - may cause customers to leave for another bank
    - cheaper for the bank, don't have to use physical banks, employees
  - reasons for yes
    - more profit for online users
    - Not many people have computers yet

### Questions to guide analysis
- Is being online associated with higher profits?
  - Descriptive question
- Does the online channel cause higher profilts?
  - explanatory question

What is the true relationship?

![graph-43c18879-6b0a-426e-ab8b-c787f9bfd0d0](data/lecture2/graph-43c18879-6b0a-426e-ab8b-c787f9bfd0d0.svg)

or maybe?


![graph-0fa39566-2cf1-46a0-94c7-3a2152126ac8](data/lecture2/graph-0fa39566-2cf1-46a0-94c7-3a2152126ac8.svg)

There could be some other variable(s) that effect both online and profits, for example:


![graph-8292ab78-3efa-4f70-ba4f-fa185f0a4ade](data/lecture2/graph-8292ab78-3efa-4f70-ba4f-fa185f0a4ade.svg)

## How to deal with missing data
1. Delete rows with missing values
2. replace missing with default value
  - 0
  - mean
3. Use default values and add an extra column with a missing data flag
4. Imputation: build a model for the missing values, predict the values to fill missing.

## Prediction
- Supervised learning
- **Goal:** Given a labelled data set, predict new label values for future samples.
- Predict continuous values or categorical
- p-values don't neccessarily matter: as long as it's encapsulated in the model then it's ok.
- ![latex-2e7d9ec0-7441-4ce2-98e7-69e2e070c6fd](data/lecture2/latex-2e7d9ec0-7441-4ce2-98e7-69e2e070c6fd.png) is important: it is the error/accuracy measure

## Classification
- Prediction for categorical variables

