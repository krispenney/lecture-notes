# Lecture 16 - June 21, 2017

## Statistical Learning
- Motivation: We have uncertain knownledge about the world
- How to decrease the uncertainty

### Baysian Learning
- Prior: P(H)
- Likelihood: P(d | H)
- Evidence: d = <d_1, ..., d_n>
- Use Bayes Theorem: P(H| d) = kP(d | H)P(H)

### Baysain Prediction
Make a prediction abount an unknown quantity (i.e. the flavour of the next candy)

P(X | d) = sum {all hypothesis} P(X | d, h) P(h | d) = sum {all hypothesis} P(X | h) P(h | d)

### Identically and Independantly Distributed (IID)
- Same probability of picking any item from the bag (i.e. 50/50 chance of picking a particular candy from the bag)
- If your bag is large enough then this is a reasonable assignment
- Each item
- P(d | h) = pi{each candy} P(**d** | h)

### Bayesian Learning
Properties
- Optimal: No other prediction is correct more often than the Bayesain (Given proper prior)
- No Overfitting: All hypothesis are weighted and considered

Cons
- With a large hypothesis space, Maybe very difficult to specify all possible combinations
- Prediction is a weighted sum (or integral) over the hypothesis, but could also be intractable

### Maximum a posteriori (MAP)
Approximate Bayesain Learning

- Make predictions based on the Most Probable Hypothesis (h\_{MAP})
- h_map = argmax{h_i) P(h_i | d)
- P(X | d) ~ P(X | h_map)

**Problem**: May jump to a conclusion
- Therefore, it is less accurate than Baysian prediction, only relies on 1 hypothesis
- But, with an infinite amount of data: both methods will converge to the same point

**Controlled Overfitting**
- Discount probabilities of complex hypothesis
- Complex will be more specific, more likely to overfit
- Discounting these probabilities will ensure that the prediction is based on the data.

**Big Problem**: Finding h_map may also be intractable
- If there are infinite hypothesis

### Maximum Likelihood
- Further approximate MAP
- Assume the prior is uniform
- h_ML = argmax_h P(d | h)
- P(X | d) ~ P(X | h_ml)

**Different Camps (in agreement)**
1. Frequentist: objective prediction since it relies only on the data (on prior)
2. Bayesian: Prediction based on data and uniform prior (no prior === uniform prior)

**Properties**
- Less accurate than both Bayesian and MAP predictions, it ignores prior info and relies only on one hypothesis h_ML
- Will converge as data increases
- Can't control overfitting
- Easier to find h_ML than h_MAP

## Summary
When to use Bayesain, MAP, or ML

- Complete Data: Data has multiple attributes and all are known
  - **Easy**
- Incomplete data: When data has multiple attributes and some are unknown
  - **Harder**

### LaPlace Smoothing
- Overfitting can happen when there is no sample for a certain outcome (i.e. no cherries eaten so far)
- If the probability is 0 then it rules out outcomes

**Solution**: Simply add one to all counts
- This will ensure that the probability is always > 0
- i.e: P(cherry) = theta = (c+1) / (c + l + 2) > 0

### Naive Bayes
- Assumption: all attributes are independant given the class
- This causes a problem if attributes are actually dependant on eachother
