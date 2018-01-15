# Lecture 6 - January 15, 2018

## Supervised Learning
Types of problems:

### Regression
Goal: Estimate some continuous value
- Mean squared error is a more relevant cost function

### Classification
Goal: Estimate the class of the input
- Example: Given an image, determine what digit it is.
- Think the cross-entropy cost function

## Cross-Entropy Cost Function Derivation - Assignment 2


![graph-186d1346-292b-4a2e-b6ad-bd0836ae8755](data/lecture6/graph-186d1346-292b-4a2e-b6ad-bd0836ae8755.svg)

Suppose we are given a training set:

![latex-09db3139-9df5-435e-8243-c11644f12004](data/lecture6/latex-09db3139-9df5-435e-8243-c11644f12004.png)

Where the true class is expressed in the target: ![latex-c400d7d2-52b4-4e63-81c2-557cdc540c7e](data/lecture6/latex-c400d7d2-52b4-4e63-81c2-557cdc540c7e.png)

```
t^i = 1 if x^i in C
t^i = 0 otherwise
```

![latex-cd500fe2-17b0-4dd5-bcd6-0a914ab91997](data/lecture6/latex-cd500fe2-17b0-4dd5-bcd6-0a914ab91997.png)

The liklihood of observing the data set is the product:

![latex-3cb22618-b89c-41b7-adf0-62b6e9ec632a](data/lecture6/latex-3cb22618-b89c-41b7-adf0-62b6e9ec632a.png)
![latex-33c9a2c6-79b5-49a1-99a6-0cd698557221](data/lecture6/latex-33c9a2c6-79b5-49a1-99a6-0cd698557221.png)

More convenient to look at log liklihood (note ![latex-48a77229-0d82-4586-ae15-077fd0baf552](data/lecture6/latex-48a77229-0d82-4586-ae15-077fd0baf552.png))

![latex-e426abfb-66dd-4f4a-b329-041098feaaea](data/lecture6/latex-e426abfb-66dd-4f4a-b329-041098feaaea.png)

## Perception
Most basic neural network.


![graph-25a52853-b38e-4079-a226-ea9fa9eb59ea](data/lecture6/graph-25a52853-b38e-4079-a226-ea9fa9eb59ea.svg)
