# Lecture 7 - May 23, 2017

## Interpreting the axoims
- 0 <= P(A) <= 1
- P(True) = 1
- P(False) = 0
- P(A OR B) = P(A) + P(B) - P(A and B)
- P(~A) = 1 - P(A)

### Betting Game
- Agent 1 looses money because P(A OR B) > P(A) + P(B)
- Agent 2 can take advantage of Agent 1 such that it will always make money

### Multivalued Random Variables
- Assume domain of A = {v_1, v_2, ..., v_k}
- A can take on exactly one value out of this set
- P(v_i AND v_j) = 0 ; i != j
- P(v_1 OR v_2 ... OR v_k) = 1

### Probability Distribution
- A specification of a probability for each event in out sample space
- Sum sum to 1

### Joint Probability Distribution
- Specification of probabilities for all events
- Describe an entire world of events
- P(A = a AND B = b) Forall a, b

- Marginalization (sumout rule)
  - P(A = a) = Sum for all b P(A = a AND B = b)

### Conditional Probability
- P(A|B) = P(H AND F) / P(F)
- Fraction of worlds in which B is true that also have A true

### Chain Rule
- P(A and B) = P(A|B)P(B)
- Define a joint distribution in terms of a conditional

### Inference
- Reasoning is incorrct, the probability we should be concerned with is P(Flue | Headache)
  - P(F AND H) = P(F)P(H|F) = 1/80
  - = P(F|H) = P(F AND H) / P(H) = (1/80)/(1/10) = 1/8

### Bayes Rule
- P(B|A) = P(A|B)P(B) / P(A)
Since:
- P(A|B)P(B) = P(A AND B) = P(B AND A) = P(B|A)P(A)

**Bayes Rule for Inference**
- Often we want to form a hypothesis about the world based on what we have observed
- Likelihood = prob the the evidence is realized given that the hypothesis is true

### Slide 32 Example
- P(Fever | Asian Flu) = 0.95
- P(Asian Flu) = 10^-7
- P(Fever) = 1/100
- You go to the doctor with a fever, what is the probability that Asian flu is the cause of the fever?
  - P(Asian Flu | Fever) = P(Fever | Asian Flu)P(Asian Flu) / P(Fever) = 0.95 * 10^-7 / 0.01 = 0.95 * 10^-5

## Probabilistic Inference
Given a prior distribution P(X) over variables X of interest, representing degrees of belief, given new evidence E = e for some variable E. Revise you degrees of belief: posterior P(X | E = e)

- How do your degrees of belief change as a result of learning E?

### Semantics of Conditioning

**Problems**
- For set of random variables {X_1, X_2, ..., X_n}, the number of worlds is exponential
- Then, to answer query P(X_1, X_2, ..., X_n), must sum over exponential number of worlds
- In practice, use conditional independence to get around.

### Independence
- X and Y are independant if: P(X=x) = P(X=x | Y=y)

### Conditional Independence
- 2 variables X and Y are conditionally independent given variable Z
P(X=x|Z=z) = P(X=x|Y=y,Z=z)
- Allows a full joint distribution to be specified using n variables (linear)
- Full conditional independence is pretty rare.


