# Lecture 1 - May 1, 2017

## Overview

### Algorithms in a variety of contexts:
* Computational Complexity
  * **Resource**: Time or space
* Query Complexity
  * **Resource**: accessors to data. (ex. a database contains some data for a problem, how much of the db do you need to access?)
* Communication Complexity
  * **Resource**: communication between distributed systems.
  * ex. multiple processors, how much do they need to communicate.
* Online Paradigm
  * **Resource**: commitment
  * The data is streamed
  * You have to commit to something before you know all of the data.

There are typically tradeoffs between using different contexts. ex. If space is important, may need increased communication

### Types of algorithms
* Deterministic
* Randomized (ex. Monte Carlo)
* Quantum

### Various tasks performed
* Compute some function of the input
* Compute an approximation of a function

### Efficiency
1. Polynomial
2. Exponential
3. Fixed-Parameter Polynomial

Typically can be categorized in a different class depending on the context of **n**.

## Randomized (Probabalistic) Algorithms

### Basic Framework of Probability Theory
Set Omega, p: Omega -> Positive Real Number, such that P(o in  Omega) >= 0. Sum of all possibile values = 1

**Events**: A, B in Omega
Pr[A] = sum p(w) (w in A)

**Example**
- A: It is a sunny day. Pr[A] = 0.9
- B: I ride a bicycle to work. Pr[B] = 0.5
- Suppose Pr[A and B] = 0.4
- Pr[A or B] = Pr[A] + Pr[B] - Pr[A and B]
- => 0.9 + 0.5 - 0.4 = 1

**Conditional Probability**: Pr[B|A] = Pr[A and B] / Pr[A]
* Well defined if PR[A] != 0
* Pr[A and B] = Pr[A] * Pr[B|A]

**Random Variables**: X: Omega -> Real Numbers
* Function that assigns a real number to every value in the probability space.

**Expectation of a Random Variable**: Exp[X] = sum{w in Omega} p(w)X(w)

### Simple Search Scenario
**Input**: X_1, X_2, ..., X_n in {0, 1} ; An array accessed via queries
* Algorithm specifies an index 1 <= j <= n to query oracle
* oracle returns X_j

**Problem**: Find j in {1, ..., n} such that X_j = 1
Suppose we assume there exists such a X_j

**Deterministic Algorithm**
* Can solve the problem with N-1 queries
  * This is optimal for worst-case inputs
  * [0, 0, 0, 0, ..., 1]
  * To prove this, can use an adversary argument to prove. It could know that the first n-2 queries will result in 0's.

**Aside: Average Case Analysis**
* Could be on a deterministic algorithm where you make some assumptions about the probability distribution of the input.

**Probabalistic Algorithms**
* Can choose queries according to a random strategy.
1. Make a unique random guess between 1..n
  * Repeat until you find 1.
  * Expected Number of queries?
Proof: Let Z = Omega -> R, be the expected number of queries
* Pr[Z = 1] = 1/N
* Pr[Z = 2] = (1 - 1/N)(1/(N-1)) = 1/N
* Pr[Z = k] = 1/N
* Pr[Z = N] = 1/N
* Exp[Z] = sum k = 1..N (1/n * k) = 1/N((N(N+1))/2) = (N+1)/2

**New Assumption**: At least half of the bits in X are 1.
* **Deterministic**: floor(N/2), at this point have either found one or know that the next one is a one.
* **Randomized**: <= 2, just randomly guess from the list. Each spot has a 50% chance of being a 1.

* Abundance of witnesses
* Foiling an adversary
