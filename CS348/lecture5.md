# Lecture 5 - May 23, 2017

## Assignment 2
- First time: Only have enrollments, no grades
- Can assume that we have a substring function in relational calculus (i.e. checking the course code)
- Slide 46

## SQL
- Junctions must obey **union-compatibility**

### Slide 28
{x | (Exist y. publication(x, y)) AND NOT (Exist y, z, w. article(x, y, z, w))}

### Slide 34 in RC
{y | (Exist x. publication(x, y) AND ((Exist. y, x. book(x, y, z)) OR (Exist y, z, w. Journal(x, y, z, w))}

{y | publication(x, y) AND book(x', y', z') AND journal(x'', y'', z'', w'') AND (x = x' OR x = x'')}

- If we want to should that two queries are **not** the same, we need to provide a counterexample
- Difference between the queries, First selects book or journal, second book and journal.

### Slide 41 Example
- This is what we would have to write if we didn't have the `NOT IN` syntax avaliable to us.

{ (x, y) | wrote(x, y) AND NOT ((Exist z, w. book(y, z, w)) AND (Exist z, w, t. journal(y, z, w, t)))}
- Note that this doesn't have union compatibility
- Note: A AND NOT B === A AND NOT(A AND B)
{ (x, y) | wrote(x, y) AND NOT (wrote(x, y) AND (Exist z, w. book(y, z, w)) AND (Exist z, w, t. journal(y, z, w, t)))}

``` SQL
(SELECT * from wrote)
EXCEPT
(SELECT w.author, w.publication FROM wrote w, ((select pubid from book) union (select pubid from journal)) bj
WHERE w.pubid = bj.pubid)
```
