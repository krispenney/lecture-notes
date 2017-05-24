# Lecture 8 - May 24, 2017

### Slide 19
Don't have P(c) Directly, need to apply the rule again to get P(c)

## Bayesian Networks
- DAG
- Given a set of conditional probabilities corresponding to nodes and their parents

### Slide 24 Probabilities
**A**:
P(A) - don't need not, because inferred
**C**:
|A|C|P(A|C)|
|-|-|-----|
|a|c|0.9|
|a|~c|0.3|
|~a|c|0.1|
|~a|~c|0.7|
Again, only need the first two, because can inferr

**D**
|A|B|D|P(D|A,B)|
|-|-|-|--------|
|a|b|d||
|a|b|~d||
|a|~b|d||
|a|~b|~d||
|~a|b|d||
|~a|b|~d||
|~a|~b|d||
|~a|~b|~d||

### Simple Rule to estimate table size
2^{num of parents}

### Semantics of a Bayes Net
The structure of the BN means: every X_i is conditionally independent of all of it's non-descendants given its parents:

Therefore, P(x_1, x_2, ..., x_n) = P(x_n|x_n-1,...,x_1)...P(x_1) = P(x_n|Parents(x_n))P(x_n-1|Parents(x_n-1))...P(x_1)

Most variables will only be dependant on a few local variables.

### Constructing a Bayes Net
Given any distribution over variables X_1, ..., X_n we can construct a BN that faithfully represents that distribution
Go though all of the variables and determine their dependants (parents)

### Compactness of BNs
- The table size is exponential in the number of parents

### Assignment 2
- Given some information in text
- Need to build the conditional probability table
- The numbers will correspond to some variables given their parents

### Testing Independence
**D-separation**: A set of variables E d-separates X and Y if it blocks every undirected path in the BN between X and Y
  1. One arc on P goes into Z and one goes out of Z, and Z in E. Only one undirected path
  2. From Z, one arc out to A, one arc out to B. No information flows between X and Y
  3. If none of Z and it's decendants are not in evidence
    - Like the reverse of the other rules
    - Blocked while we don't know Z

- A simple graphical property

**Slide 34 Examples**
- Subway and Thermometer: Rule 1
  - If we don't observe anything then information can flow in both directions
  - Learning new information would change our belief in both directions
  - Independant given flu
- Aches and Fever
  - Apply rule 2
  - The path is blocked when we observe flu
  - This is the only path
- Aches and Thermometer
  - Rule 2
  - If we observe flu, the path will be blocked and the variables are independant
- Flu and Malaria
  - Corresponds to rule number 3
  - If we do not observe fever and thermometer, then flu and malaria are independent
  - If we observe a symptom then it would influence our belief of the causes.
  - When observed, they become dependent
    - Note: even if we observe thermometer
    - Observing this would give information about potential symptomes
- Subway and ExoticTrip
  - Rule 3 on Fever

## Bayes Nets 2

### Inference in BNs

**Backwards Inference**
- Can use Baye's rule to transform backwards inference into a forward inference problem

### Variable Elimination
