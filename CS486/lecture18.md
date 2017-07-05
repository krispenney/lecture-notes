# Lecture ~18ish - July 5, 2017
## Renforcement Learning
### I've really just lost count at this point

## Finish Deep Learning Slides

### Deep NN
- Lots of hidden layers
- **Implication**: Can be very expressive
- **Problem**: Prone to overfitting
  - Vanishing gradient problem

### Dropout
- Solution to overfitting
- Randomly drop some units from the network when training
- Perform at each iteration of gradient descent (backprop)
- This essentially constructs a sub-network
- The network is forced to develop redundencies throughout, therefore becoming more general and less prone to overfitting

**During Testing**
- For a given node, there's a chance that the output could be nullified (because of dropout)
- multiply by 1 - drop prob, to place outputs on the same scale
  - (1-drop) -> probability that the node isn't dropped

### Ensemble Learning
- Dropout approximates this
- During training time, constructing various sub networks, train each of them
- During testing time, we are essentially producing the weighted output of all of the subnetworks

## Reinforcement Learning
- Need to plan a sequence of decisions, learn the best way to go about it.
- Maximize a numerical reward signal

### Types of Machine Learning

| Supervised Learning | Reinforcement Learning | Unsupervised Learning |
|---------------------|------------------------|-----------------------|
| Answers are provided (i.e. optimal) | Hints provided to the learner (good or bad feedback, not optimal)| Learner discovers the answer on their own |

### Definition
Markov decision process with unknown transition and reward models
- Set of states
- Set of actions
- Set of reinforcement signals (rewards)

**Goal**: Learn the optimal policy while interacting with the environment

### CartPole problem

x : Speed of the cart
x' : Velocity of the cart
Theta: Angle of the pole
Theta': Angular velocity of the pole

- Note that all of these are continuous values, i.e. it is impossible to enumerate all of them

### Characteristics
- **Rewards**: Maybe a delay between when the action is committed and the reward is recieved
  - **Temporal Credit Assignment**: We don't know which action should be credited with the reward.
- Exploration vs. Exploitation:
  - Exploit: Take advantage it's current knowledge, but it might not learn anything new
  - Explore: Could learn something new
  - **Implication**: It may be worthwhile to make a few "bad" moves in order to potentially learn something new (i.e. a better solution)
- Lifelong Learning: Agent doesn't just take in a dataset a be done with it, always learning from new states as it goes
  - Similar to humans

### Types of RL

| Passive | Active |
|--------|-------|
| Execute and evaluate a fixed policy | update the policy as the agent learns |

| Model-Based | Model-free |
|------------|-----------|
| Learn transition and reward model. More complex to code. | derive optimal policy without learning the model. Takes longer typically, needs more data. |


