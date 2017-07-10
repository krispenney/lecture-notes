# Lecture 20, July 20, 2017

## Type of RL

- Model Based: Learn trainsition and reward model, use it to determine the opimal policy
- Model Free: Derive the optimal policy without learning the transition and rewards models
  - **Q-Learning**: Active and Model-Free

### Passive Learning
- Transition and Reward models known
- Transition and Reward models unknown
  - Policy is based on the expectation of the discounted sum of the rewards

### Temporal Difference
At each time step, observe:
- s: Current state
- a: Action
- s': Next state
- r: Reward

Temporal Difference:
- Just taking one sample into account (s')
- Crude estimate
- Temporal Difference should approach 0 over time

### TD Convergence
- For t iterations of the TD alg
- Learning rate typically alpha = `1/N(s)
- Ensures that the learning rate is decreased over time

- 1st condition: "We will keep on learning forever"
- 2nd condition:
  - Temporal difference won't be 0 everywhere
  - By decreasing the learning rate fast enough, we will converge
  - The sum of the squared learning rates will be finite (0 < alpha <= 1)
  - Similar to a geometric sum

### Active Learning
- We want to improve the policy over time

IF the transition and reward models are known
- The Bellman equation can be used, taking the max action

### Q-Learning (Active Temporal Difference)
- Q matrix of size (S, A)
- Represents the value of all state-action pairs
- Policy is then argmax_a Q(s, a) for all s, is optimal

### Exploration methods
Exploration vs Exploitation
- Exploit what we already know too early, we might not learn new better information
- Explore, Learn new information

- epsilon-greedy
  - With prob epsilon execute a random action
  - Otherwise, execute the highest Q(s, :) value
- Boltzmann Equation

## Deep Reinforcement Learning
- Linear representation corresponds to a single layer NN with no activation function (or the identity activation function)

### Gradient Q Learning
- Q is now parameterized by w (weights)
- Use 1/2 squared error to update the weights (gradient descent)
- Keep the weights for the next state action pair fixed
-
