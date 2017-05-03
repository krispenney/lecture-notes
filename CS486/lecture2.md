# Lecture 2 - Solving Problems by Searching - May 2, 2017

## Uninformed Search
- The algorithm knows nothing about the problem domain

## Informed Search
- The algorithm knows information about the problem domain, can exploit this information.

## Search Trees
- No loops
- Can be very large, depending on the search space
- Typically partially constructed on the fly

### Search Nodes
- A basic data structure of a search tree, these represent a single state (configuration)
- Executing an action takes you to a different node

## Generic Search Algorithm
1. Initialize search algorithm with initial state of the problem
2. Repeat
  1. if no nodes can be expanded, fail
  2. choose a node to expand (search strategy)
  3. If the chosen node contains the goal state, success!
  4. otherwise expand the node, apply legal operations

This algorithm is typcially implemented using a (prioritized) queue

## Breadth First Search
- Expand all nodes on a given level
- FIFO queue
1. Dequeue the first node
2. expand all of the neighbours and add them to the queue.
3. Repeat until empty

## Evaluating Search Algorithms

### Completness
- Is the algorithm guaranteed to find a solution if a solution exists?
- Not very useful if it misses solutions

### Optimality
- Does the algorithm find the optimal solution?
- The lowest path cost of all solutions

### Time Complexity
- Minimize the amount of time for algorithm to run.

### Space Complexity
- Minimize the amount of space to store nodes in the queue (i.e. memory).

### Variables
- **Branching Factor**: the number of states generated from expanding (ex. for a tree it is 2)
- **Depth of shallowest goal node**:
- **Maximum length of any path in the search space**
