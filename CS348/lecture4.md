# Lecture 4 - May 17, 2017

### Assignment 1
- SQL schema diagram: Top section represents primary key for that table

## Sample Queries

- List all composite numbers
  - COMPOSITE(x) = { x | Exist y, z st. TIMES(y, z, x) AND x != y AND x != z }
- List all Prime Numbers
  - { x | (Exist y, z st. TIMES(x, y, z)) AND NOT COMPOSITE(x) }
- List all publications without authors:
  - Select all publications, then subtract the ones without authors
  - { x | (Exist y st. publication(x, y)) AND NOT (Exist y,z st. wrote(y, x) AND author(y, z)) }
  - { x | (Exist y st. publication(x, y)) AND NOT (Exist y st. wrote(y, x)) }
    - We know that the first param of wrote must be an author
- List titles of publications written by a single author:
  - { y | Exist x st. publication(x, y) AND (Exist z st. wrote(z, x)) AND (Forall z_1, z_2 st. (wrote(z_1, x) AND wrote(z_2, x)) -> z_1 = z_2) }
  - Need to rewrite last part to be logically sound
    - NOT (Exist z_1, z_2 wrote(z_1, x) AND wrote(z_2, x) AND z_1 != z_2)

- Forall x_1, x_2, y, z PLUS(x_1, y, z_1) AND PLUS(x_2, y, z_2) AND x_1 >= x_2 -> z_1 >= z_2
  - Note <= AND >= are undefined
  - x_1 >= x_2: (Exist z st. PLUS(x_2, z, x_1))

### Computational Properties
- The limitations of the language allow queries to be easily parallelized

### What queries cannot be experessed in RC?
Because RC is not turning complete, there must be computable queries that can't be written in RC

- Bulti-in OPerations
  - Ordering, arithmetic, strings
- Counting / Aggregation
  - Carinality of sets (pairity)
- Reachabliity / Connectivity
  - Paths in a graph (binary relation)

Incompleteness / Inconsistency in Data Models
- Tuples with unknown (but existing) values
- incomplete relations and open world assumption
- conflicting information (e.g. from different data sources)

## SQL
Structured Query Lanaguage

- Based on Relational Calculus
  - Conjunctive (SELECT) queries
  - Set operations and aggregation (Extensions)
  - Update language (Extension)

Q ::= R(x_1, ..., x_k) \| Q AND Q \| Q AND x = y \| Exist x st. Q \| Q_1 Or Q_2 \| Q_1 AND NOT Q_2

- BAG (multiset) semantics
  - Now have to manage additional queries
- NULL values
  - Avoid if possible

### Part of the language
1. DML (Data manipulation language)
  - Query lanaguage
  - Update language
2. DDL (Data Definition Language)
  - Defines schema for relations
  - Creates (modifies / destroys) database objects
3. DCL (Data Control Language)
  - Access Control

1 and 2 are used by Programmers
2 and 3 are used by Sysadmins

FROM author a == author(a.auid, a.name)

{x, e-s+1 | Exist z st. article(x, z, s, e) }
e-s+1 shorthand for MINUS(e, s, p) AND PLUS(p, 1, p')
