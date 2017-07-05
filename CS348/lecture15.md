# Lecture {{No Idea?}}

## Midterm Solutions

### Question 2 Bonus
Have an employee, look up work assignments
- Brute force all of the possible start and end points and see what's in between

**See the course website for the SQL**

### Equivalent Queries

**Part 1**
All of them are different, based on the number of duplicates


| Table R | |
|-|-|
| 1 | 2 |
| 1 | 3 |
| 2 | 3 |

| Table S | |
|---|---|
| 2 | 3 |
| 2 | 4 |
| 3 | 4 |

a: 1, 1, 1, 2
b: 1, 1, 2
c: 1, 2

**Part 2**
R.a is a primary key, therefore all R.a's are unique
- In this case query b won't return duplicates

| Table R | |
|-|-|
| 1 | 2 |
| 2 | 3 |

a: 1, 1, 2
b: 1, 2
c: 1, 2

Therefore b and c are the same

**Part c**
- S.a is a primary key.
- a and b cannot be different since every tuple in R can match only once, they become the same query.

Table S becomes:

| Table S | |
|---|---|
| 2 | 3 |
| 3 | 4 |

a: 1, 1, 2
b: 1, 1, 2
c: 1, 2

### Question 5

**PArt 1**
> For every entity in E, the value of an attribute A is unique

Not Exist e, a1, a2. E-A(e, a1) AND NOT E-A(e, a2) AND a1 != a2

or

FOR ALL e, a1, a2. E-A(e, a1) AND E-A(e, a2) -> a1 = a2
