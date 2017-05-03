# Lecture 2 - May 3, 2017

## Verifying Polynomial Identities - Univariate
- Input: A list of numbers: a_1, a_2, ..., a_n, b_0, ..., b_n-1
- Output: bit indicating whether or not the polynomials are the same
(X - a_1)(X - a_2)...(X - a_n) = b_0 + b_1x + b_2x^2 + ... + x^n

### Example
(x-1)(x-2) = x^2 + 3x + 2 -> 1

In a deterministic solution, would need O(n^2) arithmetic operations. There are also solutions that use FFT to improve.
Note: Can evaluate the polynomials in linear time.

### Proposed Randomized Algorithm
- Pick a random x (in some range)
- evaluate the LHS and RHS, if equal output 1, else output 0
Note it is possible that the two functions may intersect, give a false positive.

### The fundamental theorem of algebra
Over any field, any polynomial of degree n has at most n roots (i.e. equal to 0), where n != 0.

We can use this theorem, the algorithm can fail for a most n choices.
To fix, set the range of values to samples from {0, 1, 2, ..., 100n-1}. This gives a failure probability of n/100n -> 1/100, success: 99/100

Suppose we want a success probability of 1-ep
Failure probability would be n/(1/epn) = ep
Sample from the range {0, 1, 2, ..., (1/ep)n-1}

Say ep = 1/2, then one-sided error probability = 1/2
Repeat the process k times, using independant randomness each time.
Then the failure probability is 1/2^k
Note that this k would be factored into the run time cost. So select a k = 40, this is 1/trillion

Note:
To represent {0, 1, .., n-1} need lg(n) bits
To represent {0, 1, ..., 2^40 n-1} 40 + lg(n) bits

## Verifying Polynomial Identities - Multivariate
Input: 2 specifications of polynomials of degree *d* in variables X_1, ..., X_2
Output: a bit indicating if they are the same polynomial or not

### Example
determinant of M, nxn matrix of the form: Vandermonte matrix
[[1, x_1, x_1^2, ..., x_1^n-1],
...
[1, x_n, x_n^2, ..., x_n^n-1]]

PI {i > j} = (X_2 - X_1)(X_3 - X_2)(X_3-X_1) ... (X_n - X_n-1) ... (X_n - X_1)

The degree of this is n(n-1)/2

Arithmetic Formula vs. Arithmetic Circuits

### Probabalistic Algorithm
**Schwartz - Zippel Lemma**: Let f(x_1, ..., x_n) be a multivariate polynomial of degree d >= 0 over a field F (e.v. rational, reals, prime integers).
Let S be a subset of F, and suppose y_1, ..., y_n are sampled uniformly from S (independantly)
Then Pr[f(y_1, ..., y_n) = 0] <= d/|S|
If |S| = 2d, then we get Pr[f(y_1, ..., y_n) = ] <= d/2d = 1/2. Can use the previous method to amplify.

Note: d is the degree of the largest monomial when expanded out.


