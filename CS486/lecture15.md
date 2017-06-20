# Lecture 15 - June 19, 2017

## Machine Learning
> A program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E
- Experience ==== Data
- Task === The goal. i.e. What you are trying to do with the data (Classification, regression, clustering)
- Performance Measure === How well the algorithm is doing with respect to the task

### Representation
Representation of the learned information will determine how the learning algorithm will work.

### Inductive Learning
aka: Concept Learning
- Given a training set of examples of the form (x, f(x)) (input, output)
- Return a function **h** the approximates **f**. h is the hypothesis.

### Regression
- Fit a real value to a function
- Find function h that fits f at instances x

### Hypothesis Space
The set of all hypothesis that the learner may consider
- Can therefore think of learning as a search problem

Objective
- Find h that agrees with training examples

### Generalization
What about unseen examples?
- Need to be able to use h to answer new questions, make predictions etc.
- A good h will generalize well

- The simplest form of machine learning is just to "memorize" the training set.
- A h found to approximate the target function well over a sufficiently large set of traiing examples will also approximate the target function well over any unobserved examples

Need lots of data in general.

### Inductive Learning
- Construct / adjust h to agree with f on training set
- h is **consistent** if it agrees with f on all examples

**Ockham's Razor**: Prefer the simplest hypothesis that is consistent with the data.
- Have to be careful, data might be noisy (wrong, outliers)
- Depends on the senario

- Finding a consistent hypothesis depends on the hypothesis space
  - I.e. learning f(x) = sin(x) is impossible if H = the space of polynomials of finite degree
  - Proof: approximate sin(x) with a Taylor Series expansion, need an infinite degree polynomial to be consistent.

A learning problem is realizable if the hypothesis space contains the true function, otherwise it is unrealizable
- In real life it's difficult to determine whether a learning problem is realizable since the true function is not known.

There is a tradeoff between expressiveness of a hypothesis class and complexity of finding simple ,consistent hypothesis within the space.
- i.e. fitting linear functions is easy, polynomials harder, Turing machines very very hard!

### Decision Trees
Used for classification

- Nodes: Labeled with attributes
- Edges: labeled with attribute values
- Leaves: Labeled with classes

Classify by starting at the root and work down to the leaves. Make decisions at each step.
- Return the class that was found

**Note**: The tree does not have to make use of all of the features. Some of the given features may be irrelevant to the outcome.

Can represent a given decision tree by a logical formula. Formula will be multiple ORs for each "yes" branch.

### Decision Tree Representations
Decision trees are fully expressive within the class of propositional languages
- i.e. any boolean function can be written as a decision tree
- But, there is no representation that is efficient for all functions.

### Inducing a Decision Tree
Goal: Find a small tree consistent with the training examples
Idea: recursively choose the "most significant" attribute as the root of the (sub)tree

### Choosing an attribute
A good attribute splits the examples into subsets that are all in agreement (i.e. all positive or all negative)

- Measure uncertainty via Entropy
- Intuition: How many bits we would need to communicate on average
- Example: Flipping a coin, possible results are Heads or Tails
  - I(P(Head), P(Tail)) = I(p, 1-p)
  - For example, if the coin is biased (i.e. P(Head) = 1), there is no uncertainty, therefore you don't need to communicate anything.

### Information Gain
remainder(A): How much entropy will remain after we split the data.

IG(A) = I(p, 1-p) - remainder(A)

Compute IG for each child, Choose the attribute with the largest IG.

### Performance of Learning Algorithms
A learning algorithm is good if it produces a hypothesis that does a god job of predicting classifications of unseen examples.
Verify performance with a **test set**
1. Collect a large set of examples
2. Divide into two disjoint sets (training, test)
3. Train using only the training set -> learn h
4. Test h using the test set, measure the correct classifications
5. Repeat 2-4 for different randomly selected training sets of varying sizes.

### Learning curves for tree sizes
- As the tree size increases, accuracy on the training set will improve.
- But as the training set is used on the growing tree, accuracy will decrease

### Overfitting
Can't generalize to new examples
- Decision tree grows until all training eamples are perfectly classified

Can also happen if
- The data is noisy: If you haven't seen enough, you won't have good hypothesis
- training set is too small to give a representative conclusion

**Definition**
- h is higher on the training set, lower on testing set
- h' is lower on the training set, but higher on testing set

**How to avoid?**
1. Prune statistically irrelevant node (Kai^2 test)
2. stop growing the tree early when test set performance starts decreasing
  - Via cross-validation
  - k-fold cross validation, means k experiments, each time putting aside 1/k of the data to test on.
  - Take the average of all experiments
