# Lecture 9 - May 29, 2017

### Simple Backward Inference
Use Bayes Rule to rewrite the problem:
- P(ET | j) = aP(j | ET) P(ET)

## Variable Elimination
- Apply the sumout rule repeatedly

### Factors
- A function f(X_1, X_2, ..., X_k)
- A tabular representation for each instantiation for each variable
- ex. each Conditional Probability Table in a BN is a factor

### CPT as a Numpy array
|A/B|0|1|
|0|0.6|0.4|
|1|0.1 |0.9|

```python
# f(A, B)
f = np.array([[0.6, 0.4],
              [0.1, 0.9]])

# g(B, C)
g = np.array([[0.2, 0.8],
              [0.3, 0.7]])

'''
   Take advantage of python's broadcasting rules,
   Can directly multiply if the dimensions are the same or one of the dimensions is 1
'''

# f is currently (2, 2)
# Define an empty dimension for C
f.reshape(2, 2, 1)

# g is currently (2, 2)
# Define an empty dimension for A
g.reshape(1, 2, 2)

# Produce h of dimension (2, 2, 2)
h = f * g
print(h.shape)
```

### Summing a variable out of a factor
- Use marginalization
- **Note**: It is okay for factors to sum to greater than 1, as they may not always be probabilities.

### Restricting a Factor
- Restrict only to values where X=x
- Used for evidence in inference, conditioning based on evidence
- In python, use slicing to achieve this

```python
# Slice f(A, B) with A=True
f[1, :]

# Use the slice object
slc = [slice(None)] * 2
f[slc]
```

### Polytree
- A BN that consists of multiple trees
- Tree does not have branches that merge back (i.e. every node only has a single path)
- Polytree's make it easy to find the optimal ordering. Work from the outside in.
- *Singly-Connected Nodes*: Only have one parent
  - The leaves of a tree are always singly connected

### Effects of different ordering
- Heuristic: Eliminate the variables with the fewest connections first, then the ones with the most at the end

### Relevance
- important for Last question on the Assignment
- Certain variables have no impact on the query
- Can we figure out with part of the network is relevant to answer a given query? Can approximate with relevance

- When is it relavent?
  - If a variable V is relevant
  - It's parents are relevant
  - It's decendants are relevant


