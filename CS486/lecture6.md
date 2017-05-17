# Lecture 6 - May 17, 2017

## Hill Climbing Issues
- It can get stuck
- Local Optimum (max / min): Cannot guarantee global optimum
  - Get around this by using random restarts
- Plateaus: Could get stuck moving sideways forever

- **Randomized Hill Climbing**
  - Like regular hill climbing
  - Pick a random point from the move set, move to it if it's better than the current state.

- **WALKSAT**
  - **Incomplete**: If there is no solution that will satisfy it will never terminate

### Simulated Annealing
Based on properties of nature. As water cools down, the moecules will settle into a configuration that uses less energy.

1. Let S be the initial configuration and V = Eval(S)
2. Let i be a random move from the moveset and let S_i be the next configuration, V_i = Eval(S_i)
3. If V < V_i, then S = S_i and V = V_i
4. Else with probability p, S = S_i and V = V_i
  - p = 0.1 (or some fixed value)
  - Probability decreases with time?
  - Probability decreases over time and as V - V_i increases?
  - Exp(-(V - V_i)/T)
    - T is a constant, called the Temprature
    - Boltzmann Distribution
5. Goto 2 until you are bored

### Genetic Algorithms
- Encoded candidate solution is an **individual**
  - Typically a bit string
- Each individual has a fitness, measures the quality of the solution
- A **population** is a set of individuals

- Start with a random population of size N
- Compute the fitness of each member of the population
- Loop
  - For i in 1 to N
    - Choose 2 parents each with probability proportional to fitness scores (higher fitness more likely)
    - Crossover the 2 parents to produce a new child bitstring
    - With some small probability, mutate the child
    - Add child to the population
- Repeat until a child it fit enough, or bored
- Return the best child in the population according to fitness function

- **Crossover**
  - Pick a random point in the strings
  - Pick the right side of one, left of the other and combine

- **Mutation**
  - Allow features not present in the original population to be generated
  - Typically means: flip a bit with probability p

## Uncertainty
Logic breaks down because we can't enumerate all of the possibilities, we don't have all the information.

### Discrete Random Variables
- Random variable A describes an outcome that can't be determined in advance (ex. rolling a dice)
- Discrete: The outcomes come from a countable and finite domain (sample space)
- Boolean random variable: {True, False}

### Events
- A complete specification of the state of the world in which the agen is uncertain, a subset of the sample space
- Events must be:
  - Mutually Exclusive
  - Exhaustive (at least one event must be true)

### Probabilities
- P(A) == the "degree of belief" we have that the statement A is true
  - P(A) **DOES NOT** correspond to a degree of truth
  - Observation can change degree of belief
  - Draw a card from a shuffled deck,
    - Before looking at it P(Ace of spades) = 1/52
    - After, P(Ace of spaces) = 1 or 0

### Axioms of probability
- 0 <= P(A) <= 1
- P(True) = 1
- P(False) = 0
- P(A or B) = P(A) + P(B) + P(A and B)
