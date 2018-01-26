# Lecture 11 - January 26, 2018

## Analysis Time Stage 1
- Using birthday paradox: approx ![latex-698525dd-31d9-4c6d-b968-1fe19cdb70f8](data/lecture11/latex-698525dd-31d9-4c6d-b968-1fe19cdb70f8.png)
- expected number of steps for a collision to occur + number of steps to detect the collision

## Analysis Time Stage 2
- ![latex-8cf7d210-e626-4978-afe0-6698eac6d86a](data/lecture11/latex-8cf7d210-e626-4978-afe0-6698eac6d86a.png)
- Minor detail: Navigating 2 paths between 2 pairs of distringuished points.

## Total Expected Time
- ![latex-6c47d2f6-5f07-4a64-bee0-61599d426529](data/lecture11/latex-6c47d2f6-5f07-4a64-bee0-61599d426529.png)

## Expected Space
- ![latex-378eb5f9-2e1f-4d5f-96f6-ec2c63a1e787](data/lecture11/latex-378eb5f9-2e1f-4d5f-96f6-ec2c63a1e787.png) bits.
- Size of a table entry: ![latex-9d28e573-e171-4a5e-a2ff-4c2a1e431be0](data/lecture11/latex-9d28e573-e171-4a5e-a2ff-4c2a1e431be0.png) `(x_i, i, LP)`

### Example
- n = 128
- h: {0, 1}(128) -> {0, 1}128

#### Naive Method
- Time ~ ![latex-24aacf10-1aa5-4bb1-a9cf-d660531cfb1d](data/lecture11/latex-24aacf10-1aa5-4bb1-a9cf-d660531cfb1d.png)
- Space ~ ![latex-df933939-cd37-4ba3-b8eb-7e1010b3cbd9](data/lecture11/latex-df933939-cd37-4ba3-b8eb-7e1010b3cbd9.png) tbytes

#### VW Method
- ![latex-b4231f05-3751-4c5a-9006-ebad5bb1ec57](data/lecture11/latex-b4231f05-3751-4c5a-9006-ebad5bb1ec57.png)
- Time ~ ![latex-96199f35-3f58-48be-a9f9-b156379ceff6](data/lecture11/latex-96199f35-3f58-48be-a9f9-b156379ceff6.png)
  - Note that since were only storing 1 in ~billion results, lookup time is negligible.
- Space ~ 256 Gbytes
  - Feasible for consumer to obtain this much storage

## Parallelizing VW (with m processors)
- Ideal case: Hope for a speed up factor of m
- Idea: Have each processor pick a different starting point.
  - For each machine, pick a different (random) starting point
  - Each machine reports the distingished points to a central server.
  - Sequences could collide with itself, or with another processor.

### Expected Time
- ![latex-aa3d0df7-3469-4f0c-8b3f-f95a362bb4c9](data/lecture11/latex-aa3d0df7-3469-4f0c-8b3f-f95a362bb4c9.png)

### Expected Space
- same as before
- ![latex-0b512b46-bd94-4850-85cc-81c2d90ada30](data/lecture11/latex-0b512b46-bd94-4850-85cc-81c2d90ada30.png)
- Note, would need some additional space to store the index of the processor (say an extra n bits), which is negligible.

### Notes
1. Speedup is by a factor of `m`
2. Communication does not need to happen between processors, only to the central server.
3. **Objection**: Realistically, the collision produced are really 2 random messages. Therefore, useless in a specific application.
  - Note: Small modifications to the attack can be made to produce meaningful collisions.

## Finding Meaningful Collisions With VW

- let ![latex-95d8b241-466e-4d6b-ba9c-dc7a225a21bb](data/lecture11/latex-95d8b241-466e-4d6b-ba9c-dc7a225a21bb.png) "Alice owes Bob $1 million...."
- let ![latex-8f2f68de-ddcd-4cd5-927a-2bbd9d7a0bc8](data/lecture11/latex-8f2f68de-ddcd-4cd5-927a-2bbd9d7a0bc8.png) "Alice owes Bob $1...."
- Alice would like to find variant ![latex-be3b9ac6-fe2c-40e2-99f7-f57d79a9a63b](data/lecture11/latex-be3b9ac6-fe2c-40e2-99f7-f57d79a9a63b.png) of ![latex-541aef3d-e7fe-4802-8fa6-ecf3561ae62e](data/lecture11/latex-541aef3d-e7fe-4802-8fa6-ecf3561ae62e.png)
  - Change the message from a bit-string point of view, but keep the same meaning
  - Such that ![latex-2ded9e6b-61a0-4ce9-9c72-c95a9352498f](data/lecture11/latex-2ded9e6b-61a0-4ce9-9c72-c95a9352498f.png)

- Define ![latex-e0998b87-3f7c-44b7-8bcf-55fe12051adb](data/lecture11/latex-e0998b87-3f7c-44b7-8bcf-55fe12051adb.png) as follows
- Fix n positions in ![latex-6258b63e-0ce1-4285-b7b3-fb69eefb7096](data/lecture11/latex-6258b63e-0ce1-4285-b7b3-fb69eefb7096.png), say ![latex-ab1da190-122d-4d01-b275-ad30a55d846c](data/lecture11/latex-ab1da190-122d-4d01-b275-ad30a55d846c.png)
- Then for n-bit string ![latex-4b1a8412-f355-4398-a0c4-de01355da6b6](data/lecture11/latex-4b1a8412-f355-4398-a0c4-de01355da6b6.png), define ![latex-7d275d6b-4f95-4cdb-80c9-d3508a56d7ac](data/lecture11/latex-7d275d6b-4f95-4cdb-80c9-d3508a56d7ac.png) by adding, for each ![latex-46da1212-3a86-41ba-b7aa-431941815955](data/lecture11/latex-46da1212-3a86-41ba-b7aa-431941815955.png), a space at position ![latex-54231794-d92a-46fe-8e35-ce2e99a613ac](data/lecture11/latex-54231794-d92a-46fe-8e35-ce2e99a613ac.png) iff the ith bit of r is 1.
- **Note** ![latex-84c5547c-d8e0-4493-b412-ff8f427281d5](data/lecture11/latex-84c5547c-d8e0-4493-b412-ff8f427281d5.png) has the same meaning as ![latex-eb3e24b6-265a-4d98-9b58-65b200bdf392](data/lecture11/latex-eb3e24b6-265a-4d98-9b58-65b200bdf392.png).
- Do the same for ![latex-c2660d14-5b66-4c23-b015-758b70fffd9d](data/lecture11/latex-c2660d14-5b66-4c23-b015-758b70fffd9d.png), define ![latex-ec8f14c3-c82d-4848-82da-e44a6a9fad79](data/lecture11/latex-ec8f14c3-c82d-4848-82da-e44a6a9fad79.png)
- Define some function f: n-bit -> n-bit
  - Divide n-bit strings into 2 sets ![latex-7e0599fd-8dea-482b-8f0e-f0ad78498424](data/lecture11/latex-7e0599fd-8dea-482b-8f0e-f0ad78498424.png) of equal size. (say bitstrings starting with 0 or 1)
  - Then for bit-string r, define ![latex-1cb82a81-0491-4c8e-87cd-0eab8ebc647b](data/lecture11/latex-1cb82a81-0491-4c8e-87cd-0eab8ebc647b.png)
    - Check if ![latex-d4684dd0-0d1e-43eb-b5a8-84f620fc59ae](data/lecture11/latex-d4684dd0-0d1e-43eb-b5a8-84f620fc59ae.png), compute ![latex-6df7c7c0-0f86-4dd3-94ce-ff4d63250671](data/lecture11/latex-6df7c7c0-0f86-4dd3-94ce-ff4d63250671.png)
    - Otherwise, ![latex-ccc52dc2-b733-4c48-929a-ed378bfa922d](data/lecture11/latex-ccc52dc2-b733-4c48-929a-ed378bfa922d.png), compute ![latex-abef5a44-ab56-4607-907c-24a7d3744536](data/lecture11/latex-abef5a44-ab56-4607-907c-24a7d3744536.png)
- If H is a random function, the so is f
  - Since f applies H, a random Hash value, it must also be random
- run parallel VW to find a collision for f.
  - (a, b): collision
  - ![latex-6afea2d7-fdca-44a6-871a-3f63da71a7cb](data/lecture11/latex-6afea2d7-fdca-44a6-871a-3f63da71a7cb.png)
  - We hope (with prob 50%) that they are in different sets. Say ![latex-fa2b58c6-ca9e-4f34-b274-7c7f9b5d665b](data/lecture11/latex-fa2b58c6-ca9e-4f34-b274-7c7f9b5d665b.png) and ![latex-a330dacd-a2b4-4689-84e7-0f85ac9e556d](data/lecture11/latex-a330dacd-a2b4-4689-84e7-0f85ac9e556d.png)
  - ![latex-d69ca4ac-691b-431d-9d10-92998c674b2a](data/lecture11/latex-d69ca4ac-691b-431d-9d10-92998c674b2a.png)
- Let ![latex-8d9b28da-6ec5-455f-a61e-dd1161fa436f](data/lecture11/latex-8d9b28da-6ec5-455f-a61e-dd1161fa436f.png) and ![latex-58e83c01-f251-4913-8d09-d90504b11f3a](data/lecture11/latex-58e83c01-f251-4913-8d09-d90504b11f3a.png)
- Finally, ![latex-a1e82a8c-de60-4877-8d6f-6aa982de8a54](data/lecture11/latex-a1e82a8c-de60-4877-8d6f-6aa982de8a54.png)
- So we have found a meaningful collision for H.

### How to resist the attack?
- Don't use a bit-length of 128

