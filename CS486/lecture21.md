# Lecture 21: July 12, 2017

## Gradient Q Learning
Can't just update the individual states

### Convergence Properties of Gradient Q Learning
**Recall**: For Tabular Q-Learning, convergence is based off of properties of the learning rate
- For **Linear** Gradients: The same conditions also hold
- For **NonLinear**: Might diverge
  - We only want to adjust the weights at a particular (s, a), but errors might be introduced at nearby (s', a') pairs
  - The output of Q will effect the next step

### Mitigate Divergance
These reduce the changes of divergence significantly (doesn't guarantee convergence)

1. Experience Replay
2. Use 2 networks
  - Q-Network
  - Target Network

### Experience Replay
- Store the previous experiences (s, a, s', r)
- Sample a mini-batch of previous experiences at each learning step
- Allows updates throughout the network
- Because we're updating more frequently and more dispersed, this helps to stabalize the impact of updating the weights.
- Correct errors potentially created elsewhere
- Small buffer/batch size could cause the network to overfit, samples the same experiences many times.

### Target network
- Use a separate network that is only updated periodically
- Essentially performs value iteration
- Tradeoff between
  - Speed of learning
    - Lower frequency decreases the likelihood of divergence (increased stability), but will take longer
  - Update frequency

## Deep Reinforcement Learning; AlphaGo

