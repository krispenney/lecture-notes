# Lecture 3 - May 8, 2017

## Uninformed Search
- Have no information about the problem
- By taking into account information about specific problems, we are able to do much better (time, space)

### BFS
- Complete: Yes
- Optimal: Yes
- Time: Exponential

### Uniform Cost Search
- Variation of BFS
- Expands the node with the lowest path cost
- Use a priority queue

### Depth First Search
- Expand the deepest node
- Using a stack
- **Completness**: No, imagine an infinitly long path (cycle)
- **Optimal**: No
  1. May not find a solution (see completness)
  2. If it finds a solution, it may find a deeper (and more costly) path first
- **Time**
  - In the worst case will explore everything
- **Space**
  - For each node, need to store the neighbours of the nodes that we've expanded
  - In the worst case, this is the branching factor * the longest path length

### Depth-Limited Search
- DFS, but set an upper bound on the depth that we will explore
- **Completeness**: Still no
  - If you limit the depth, the limit may stop you from actually finding a solution (which could be deeper)
  - Set depth limit to 3, but only solution is at depth 4
- **Optimal**: Still no
  - IF we can't find a solution in the first place, can't guarantee an optimal one

### Iterative Deepening
- Set a depth limit, if we don't find a solution increase the limit
- This looks similar to BFS
- **Key Benefit**: Still have a linear space complexity (like DFS), instead of exponential
  - This benefit outweighs the cost of repeating some of the work.
- Repeating work
  - Most of the work will be done on the next layer
- Popular algorithm in practice

## Informed Search
- Uninformed search algorithms don't take into account any information about the problem
- Informed search ranks nodes based on merit
  - If we want to minimize the cost of the solution, merit might be the cost of getting to the goal
  - Could be based on computation time

### Heuristic functions
- h(n_1) < h(n_2), then we guess that it is cheaper to reach the goal from n_1, than n_2
- h(n) = 0, if n is a goal node
- h(n) >= 0 for all other nodes

### Greedy Best-First Search
- Expand the node with the lowest heuristic value
- Flaw, heuristic doesn't take into account the actual path cost -> **Not Optimal**
- **Not Complete**: Can get stuck in loops

### A\* Search
- f(n) = g(n) + h(n)
  - g(n) = the cost of the path to node n
  - h(n) = the heuristic estimate of the cost of reaching the goa from node n
- Expand the node with the lowest *f* vaule

### A\* Example
| Selected | Queue |
|----------|-------|
| S | A(5) |
| S, A | B(5), C(7) |
| S, A, B, | C(5), C(7) |
| S, A, B, C | G(6), C(7) |
| S, A, B, C, G | C(7) |

| Selected | Queue |
|----------|-------|
| S | B(4), A(8) |
| S, B | C(4), A(8) |
| S, B, C | A(8), G(10) |

- Which one should we pick?
  - If we want an optimal solution, probably better to continue and expand A
  - But, if we just want *a* path, expand G and be done with it
  - **In General**, only terminate if a goal state is in the queue and it has the lowest f value.

| Selected | Queue |
|----------|-------|
| S | G(3), A(7) |
| G | |

- Is A\* optimal?
  - No, in this example the heuistic cost is too high
  - If the heuristic is inaccurate, then it will mislead A\*

### Admissible Heuristics
- Let h^\*(n) be the true minimal cost to the goal from node n
- A heuristic, h, is **admissible** if:
  - h(n) <= h\*(n) for all n
  - Admissible heuristics never overestimate the cost to the goal.
  - If we can show this, then A\* is optimal
