# Lecture 11 - June 5, 2017

## Decision Networks (Influence Diagrams)
Provide a way of representing sequential decision problems
- Represent the variables in the problem as you would in a BN
- Decision variables:  variables you "control"
- utility variables: how good different states are (maximum expected utility)
  - Doctor might ask for your preference on different possible treatments

### Chance Nodes
- RAndom variables
- Ovals in a diagram

### Decision Nodes
- Denoted by squares
- variables set by decision make
- Parents reflect the informatino avaliable at time decision is to be made:

### Value Node (Utility Node)
- Denoted by diamonds
- specifies utility of a state
- accepts some real numbers, which indicate different preferences for a particular state
  - Higher the value, the more utility, thus more preferable
- In general, there is only one value node in a decision network
- The parents refer to the variables that are taken into account for the utility
  - Optional: may or may not influence the utility (i.e. blood test and not afraid of needles, wouldn't take into account)

### Assumptions
- Decision Networks are totally ordered
  - Decisions are made in sequence (ex. need to decide on a bloodtest before prescribing a drug)

- **No forgetting Property**
  - Any information avaliable when D_i is made, is avaliable when D_j is made (i < j)
  - Assuming the same agent is making the decisions (i.e. Doctor remembers / writes down information as they learn)
  - Denoted by dashed-arcs
  - Can cause cluttered networks (thus dashed lines may not be there), but the property still holds.

### Policies
- Mapping of information that we have to a decision
- Mapping of parent of a decision node, to a value in the domain of the decision node.
- Dom(Par(D_i)) -> Dom(D_i)

### Value of Policies
The value of a policy is the expected utility given that decisions are executed according to a policy.

### Optimal Policies
- An optimal policy is a policy such that it is the highest utility for all policies

- When computing the policies for decisions, start with the last decision and work backwards
For the last decision to be made, it will have lots of parents (previous decisions)
  - Choose the decision that maximizes the expected utility based on the parent's instantiation

### Decision Net Example


## Value of Information
- In the example, cost of inspection is $50, which makes it worth it to get an inspection
- But if the cost of inspection was $60, would it still be worth it?
  - It wouldn't in this case

