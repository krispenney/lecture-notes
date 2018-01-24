# Lecture 10 - January 24, 2018

## Hash functions

### Recall: 3 Cryptographic requirements
- preimage resistance
  - Given a hash, find any input with that hash.
  - **One Way Hash Function (OWHF)**
- second preimage resistance
  - Given an input, find another that has the same hash.
  - **Note**: Control over only 1 of the inputs.
- collision resistance
  - Find 2 inputs that sum to the same hash.
  - Note that collisions **will** exist, but it needs to be very hard/slow/inefficient to find!

#### Excercise: Prove that Pre image resistance doesn't imply collision resistance
- **Note**: Always prove the contrapositive.

#### Excercise: Prove that second Pre image resistance proves preimage resistance
- Assume H is uniform.
- The argument can be made that second pre image resistance is a harder problem to satisfy, if you can't find two inputs, you can't find one.

### Applications of Hash Functions

1. Message Authentication Codes (HMAC)
2. Pseudorandom bit generation
  - Get a bunch of "random" information
  - Hash it
3. Key Derivation Function (KDF)
4. Bitcoin / Blockchain
  - Proof of work
5. Quantum-safe signature schemes

### Generic Attacks
- The attack will work on any hash function
- doesn't exploit any property of a specific hash function
- For analysis, assume the hash function is random
  - Note that truely random functions aren't practical

#### Find Preimages
- Generate a random n-bit string
- Hash it
- Check if `H(x) = y`
- Expected number of steps ![latex-e7fc3480-02a7-481d-8210-3104908308be](data/lecture10/latex-e7fc3480-02a7-481d-8210-3104908308be.png)
- Therefore, make ![latex-dee1a82c-d7bf-4b2b-be6b-b02cd3ff30d6](data/lecture10/latex-dee1a82c-d7bf-4b2b-be6b-b02cd3ff30d6.png) to make it infeasible.

#### Find Collisions
- Pick an arbitrary n-bit string
- Hash it, store `(H(x), x)` in a sorted table
- Keep doing this until you find `x'` that's different
- Running time: ![latex-0203f377-f02d-497f-bf75-ad46b08760ac](data/lecture10/latex-0203f377-f02d-497f-bf75-ad46b08760ac.png)
- Attack is infeasible if ![latex-d8fc11fd-94e4-4759-8d34-600e33951e1d](data/lecture10/latex-d8fc11fd-94e4-4759-8d34-600e33951e1d.png)
- Expected running time ![latex-95c995e3-ba8e-47de-ad31-eb2f26750c91](data/lecture10/latex-95c995e3-ba8e-47de-ad31-eb2f26750c91.png)
- **Problem**: requires a huge amount of storage space.
  - Would require the storage capabilities of multiple Google's

##### VW Parallel Collision Search
- See notes on learn
- Easy to do in parallel
- Has negligible space requirements

- **Problem:** Find a collisino for an n-bit hash function
- **TLDR;**
  - Define a sequence of hash values ![latex-116d8e05-d9f9-4ac5-aa28-a5eba6f4cce8](data/lecture10/latex-116d8e05-d9f9-4ac5-aa28-a5eba6f4cce8.png)
  - ![latex-9a9d669d-d3c5-45ee-bed7-826cc416b5fd](data/lecture10/latex-9a9d669d-d3c5-45ee-bed7-826cc416b5fd.png), ![latex-b5bea627-d2be-491f-bf4d-1d00e89a07cb](data/lecture10/latex-b5bea627-d2be-491f-bf4d-1d00e89a07cb.png)
  - Eventually this sequence will result in a collision, because there are only a finite number of hash values.
  - When the sequence repeats, it will repeat forever. Because of the generation of new ![latex-d93828cf-d61e-4f2e-8898-c1f619930efd](data/lecture10/latex-d93828cf-d61e-4f2e-8898-c1f619930efd.png)'s are based off of the previous.
  - ![latex-140b565b-e60b-4215-a6a4-0e991dc40158](data/lecture10/latex-140b565b-e60b-4215-a6a4-0e991dc40158.png): by birthday paradox
  - The collision should occur somewhere in the middle of the sequence.
  - The collision is ![latex-743a9b8d-6899-4bda-9d45-b4614fd7b92d](data/lecture10/latex-743a9b8d-6899-4bda-9d45-b4614fd7b92d.png), because ![latex-e20c70f6-a355-4e26-b6ae-07f94463da2d](data/lecture10/latex-e20c70f6-a355-4e26-b6ae-07f94463da2d.png) are the same (note how the sequence is generated)

![graph-08cf16b8-c895-4cfd-9902-e46944704ca6](data/lecture10/graph-08cf16b8-c895-4cfd-9902-e46944704ca6.svg)

###### How do we find the collision without too much storage?
- Note the inefficiency: Can't store all of the intermediate points
- **Answer**: Store only _distinguished points_
  - Define some easily testable property of points, eg. the most significant 32 bits are all 0.
  - Let ![latex-d9f2066d-5cde-4619-89c4-ad2d78438181](data/lecture10/latex-d9f2066d-5cde-4619-89c4-ad2d78438181.png) be the proportion of all points that are distinguished
    - ![latex-cf724d06-26f4-4420-ae9a-958565bf6a21](data/lecture10/latex-cf724d06-26f4-4420-ae9a-958565bf6a21.png)
  - You know you've found a collision, when you've found the same distinguished point again.
  - Note: Try to make the sequence long enogh that the probability of not finding a distinguished point in the sequence is very small.
  - When you store a distinguished point, store it's index and predecessor
  - Then, you can go to the previous distinguighed points, keep hashing forwards in the sequence until the values meet

```python
# Stage 1: Detecting a collision
select x_0 + store (x_0, 0, -) in a sorted table
last_point_stored = x_0

for d = 1, 2, 3...,:
  compute x_d = H(x_d-1)
  if x_d is distinguished:
    if x_d is in the table and x_d == x_b and b < d:
      store (x_d, d, last_point_stored)
      last_point_stored = x_d
      goto stage 2

# Stage 2: Finding the collision
l1 = b-a
l2 = d-c
assert(l1 >= l2)
k = l1 - l2

compute x[a+1], x[a+2], ..., x[a+k]
compute x[a+k+m], x[c+m] for m in (1, 2, 3, ...):
  until they are equal

The collision is x[a+k+m-1], x[c+m-1]
```
