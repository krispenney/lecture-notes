# Lecture 4 - May 10, 2017

## Optimality of A\*
- Depends on the heuristic

### Admissible Heuristics
- The guess that the heuristic makes never overestimates the true cost

### Consistent (Monotonic) Heuristics
- The cost is always increasing
- h(n) <= cost(n, n') + h(n')

**Proof**
f(G) = g(G)
- This is because h(G) is zero (since we're already at the goal state)

### A\* and Revisiting States
- Revisit a state that was already expanded
- Notice in this example, h is admissible
  - h(A) = 7 < 1 + 7 = 8
  - h(B) = 3 < 2 + 7 = 9
| Selected | Queue |
|----------|-------|
| S | B(4), A(8) |
| S, B | C(5), A(8( |
| S, B, C | A(8), G(10) |
| A | C(4), G(10) |
| A, C | G(9), G(10) |
- Select the G that gives the best path
- Can also draw it out as a tree

### Memory Bounded heuristic search
- IDA\*
  - Similar to IDS, but bound is on the f-value
- SMA\* - Simplified memory-bounded A\*
  - A\*, but when you run out of memory, drop the worst left node (highest f-value)
  - If all f-values are the same, drop the oldest node

### Heuristic functions
Once approach to develop a heuristic is to relax the problem, h(n) is then the cost of reaching the goal in the easier problem.

### 8-Puzzle Example
- In the original game, can only slide adjacent tiles into the balance space
- By simplifying the game, should underestimate the cost.

- Manhatten dominates misplaced tile for all n
  - Manhatten is closer to the actual cost

- If a heuristic is proportional to the cost function, then all moves will be ranked the same as the real cost
  - This will give the optimal solution

## CSP - Constraint Satisfaction Problems
- Have specific constraints that need to be satisfied

### 8 Queens problem
- Brute force: 64!/56! possible states of the board
- Add Constraints
  - Always work left to right (columns)
  - As we place queens, check that they do not attack another queen

### Intro
- In many cases, the same state can be reached independant of the order of moves (communitive)
- Satisfying constraints can be used to drastically decrease the search space

### CSP Definition
- V = set of variables
- D = a set of domains, one for each variable
  - `|D| == |V|`
- C = the set of constraints on the variables

**State**
- an assignment of values to some / all of the vaiables
- an assignment is **consistent** if it does not violate any constraints
- A **solution** is a **complete**, **consistent** assignment

