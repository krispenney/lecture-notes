# Lecture 3ish? - May 15, 2017

## How do we ask questions
- **Note**: A query could be valid, but the information is determined by what's in the table
- If the data is bad, the results will be bad
- The database itself has no idea what the context actually is.

## The Relational Model
- Signature == Schema
  - A list of all of the relations
- Instance
  - Contains the domain / universe
  - All possible values that you can talk about
  - The system doesn't understand the values
    - If you uniformly change information everywhere (ex. ids), the system won't notice.

## Queries
Complex queries can be built from many simple ones using logical connectives and quantifiers

### ShortHand:
{ (x, y) | x^2 + y^2 = 1 }

### Formally
{ (x, y) | Ex z, w st. TIMES(x, x, z) AND TIMES(y, y, w) AND PLUS(z, w, 1) }
{ ANSWER | QUERY }

### Answer Tuples
- An answer tuple for Q assign values to Q's free variables
- An answer to a query, Q, is the set of all answer tuples that satify the query.

### A1
- Assignment 1 will probably include translations / query generations

### Modify Data in a table
- Just exchanging the instances

### Integrity Constraints
- Set of constraints that define if a database instance is valid

### Views
- Answers to queries can be used to define derived relations (views)
- Exted a DB schema
- **Example**
  - Boss(z) = ${z | Exists x, y st. EMP(x, y, z) }$
  - For all z, Boss(z) <-> (Exists x, y st. EMP(x, y, z)))

### Safe Queries
- Databases cannot be infinite
- Cannot allow infinite queries
- **Range Restricted Queries**
  - Restrict the query language
  - at least one of the variables must be a variable of the query
  - At junctions (OR, AND NOT), answer vaiables must be the same (union compatability)
  - A negation is applied to a positive query (which is finite) and just reduces the space.
