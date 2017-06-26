# Lecture 12

- Sno, Ino -> Price
- Sno -> Sname, City
- Ino -> Iname

Can also say:
- Sno, Ino -> City

### Efficient reasoning algorithm
Makes use of the Armstrong attributes
- F are all of the current conditions
- X is the left hand side of the implication (X -> X)

### Superkey example

Sno, Ino, Price is a Superkey (not candidate)

From the alg: X+ = {Sno, Ino, Price, city, Sname}
  - Note that this is also a super key
  - Not candidate

Sno, Ino is a candidate key

- Note: Any relation has a superkey (can just put everything in)
- Any relation must have a candidate key
  - Either the superkey itself is a candidate key
  - or you can remove elements to make it a superkey

- A relation with n attributes, can have many candidate keys
  - Easy to check if a set is a candidate key
  - Hard to enumerate them all
- Example
  - R(A_1, ..., A_n, B_1, ..., B_n)
  - F = { A_i -> B_i, B_i -> A_i | (0 < i <= n)}
  - Any candidate key can have either A_i XOR B_i
  - {A_1A_2....A_n}, {B_1A_2...A_n} ... {B_1B_2...B_n} -> 2^n possible candidate keys


