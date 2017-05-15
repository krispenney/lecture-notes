# Lecture 5 - May 15, 2017

## Properties of CSPs

### Types of Variables
- Discrete and finite
  - Can enumerate all possibilities
  - map colouring
  - 8-queens
- Discrete variables with infinite domains
  - scheduling jobs in a calendar
  - require a **constraint language**
- Continuous domains
  - Cannot enumerate all possibilities
  - Use Linear Programming
  - Not for this course

### Types of Constraints
- Unary
  - relates a single variable to a value
  - Queensland = Blue
- Binary
  - Relates two variables
  - SA != NSW
- Higher order constraints involve 3+ variables

### CSP and Search
- Start with an empty assignment
- Continue to assign and check for validity

### CSP and Commutativity
- The order in which we assign values to the variables doesn't matter
- **Note:** The order may effect the size of the search space

## Most Constrained Variable
- Variable with the smallest domain

## Most Constraining Variable
- Select the variable with the most constraints
- Assignment to this variable will cause the neighbours domains to be affected
- Helps to detect failures quickly

## Least Constraining Value
- The variable that rules out the fewest values in the remaining variables
- Idea: Pick a good value initially

## Forward Checking
- Keep track of remaining legal values for unassigned variables
- Terminate the search if a variables domain set is empty

## Local Search
All of the current search algorithms that we have looked at keep one or more path in memory.
In many cases, we don't care about the path to the goal, we just care about the solution.

### Hill Climbing
- Possible to fall into a local max/min
- Flat areas (plateaus) provide no information
