# Lecture 2 - January 12, 2018

## Logistic Regression

![latex-8abfaa56-85f3-4e94-9297-f69ccc70b45e](data/lecture2/latex-8abfaa56-85f3-4e94-9297-f69ccc70b45e.png)
![latex-28bfc1a3-72ef-4951-b843-30b47bf93805](data/lecture2/latex-28bfc1a3-72ef-4951-b843-30b47bf93805.png)

The goal is to find optimal params ![latex-67dc2aa7-4b9d-42fc-a8d1-4f4fd09e5057](data/lecture2/latex-67dc2aa7-4b9d-42fc-a8d1-4f4fd09e5057.png) to optimize log likelihood

### Explanetory context
Example: What is causing someone to where a jacket
- Interperet results as a probability.
- ![latex-ef7e9607-0e8e-45f2-960a-da8bd05cc760](data/lecture2/latex-ef7e9607-0e8e-45f2-960a-da8bd05cc760.png)
- **Parametric assumption**: Follow sigmoid shape, low-high or high-low

### Odds Ratio

![latex-5edbf8c0-a592-4d84-b4db-4476f06bc982](data/lecture2/latex-5edbf8c0-a592-4d84-b4db-4476f06bc982.png)

Example: The horse has ![latex-adcd7529-6d5b-4edc-bec6-ce1272417898](data/lecture2/latex-adcd7529-6d5b-4edc-bec6-ce1272417898.png) odds of winning the race, probability of winning is 5/7.

### Linear Log odds ratio

![latex-7cddc24c-c287-4835-9acb-8efe53037f44](data/lecture2/latex-7cddc24c-c287-4835-9acb-8efe53037f44.png)

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

![graph-7b9b9979-360a-4a7b-ab48-a1399864b04c](data/lecture2/graph-7b9b9979-360a-4a7b-ab48-a1399864b04c.svg)

or maybe?


![graph-fbabbd4a-58e2-4797-9cb2-d79122f2e953](data/lecture2/graph-fbabbd4a-58e2-4797-9cb2-d79122f2e953.svg)

There could be some other variable(s) that effect both online and profits, for example:


![graph-c777a946-cfe0-47c1-8341-08e2c509e7bb](data/lecture2/graph-c777a946-cfe0-47c1-8341-08e2c509e7bb.svg)

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
- ![latex-21126e18-1cdd-42ac-a09a-91ecf89fab60](data/lecture2/latex-21126e18-1cdd-42ac-a09a-91ecf89fab60.png) is important: it is the error/accuracy measure

## Classification
- Prediction for categorical variables

