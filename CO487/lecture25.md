# Lecture 25 (Midterm Q&A) - March 7, 2018

## Encryption at Google on MT?
- Very little
- Mostly just used as a vague case study.

## Relationships between hash function properties
- Pre image: Given some random hash function value, find a message x that sums to that hash, in a feasible amount of time.
- 2nd PreImage: Given an input, find a second distinct message whose hash is the same, again feasible amount of time.
- Collision resistance: Find two distinct inputs that sum to the same hash

The following examples only focus on uniform hash functions (i.e. no contrived examples ![latex-04768cb0-5648-4bf3-af07-bd70aef907af](data/lecture25/latex-04768cb0-5648-4bf3-af07-bd70aef907af.png))
- Always prove these with the contra-positive
- **NEVER SAY "EXISTS"**: they always do, the attack just needs to be feasible


![graph-ea0c36e2-73f7-4cce-b266-cef742ff4663](data/lecture25/graph-ea0c36e2-73f7-4cce-b266-cef742ff4663.svg)

- Note that PR does not imply 2PR
- 2PR does not imply CR

## Real world example of encryption / decryption oracles

| . | Public Key | Symmetric Key |
|-|-|-|
| Encryption | You can easily get the public key and DIY | Alice and Bob are devices owned by the same party (home and work computer) |
| Decryption | QQ Browser, you can get partial information back, formatted plaintext or no response (restricted chosen ciphertext attack) | Similar thing |

## Key Derivation Functions (KDF)
- Sample as many sources as random bits as possible
- KDF mixes up all of the sources of randomness
- ![latex-24f03667-66ed-4fdf-a3cb-18cdbdc0f4b1](data/lecture25/latex-24f03667-66ed-4fdf-a3cb-18cdbdc0f4b1.png)
- ![latex-b6eca342-5535-4e75-ac5e-30e194b4b94b](data/lecture25/latex-b6eca342-5535-4e75-ac5e-30e194b4b94b.png)

## Sample MT 1

### 3
- Goal of question, show how the modification to DES doesn't help

#### Part a
- ![latex-74f87528-5801-4336-98d4-fd1ffba36936](data/lecture25/latex-74f87528-5801-4336-98d4-fd1ffba36936.png)

#### Part b
- By exhaustive key search: Can solve in ![latex-7b89ea9a-2ea6-4a52-a28a-607d3517a6bd](data/lecture25/latex-7b89ea9a-2ea6-4a52-a28a-607d3517a6bd.png) steps (infeasible)
- can compute ![latex-905fa07e-6c70-4f3d-a7f3-b955d8e50a93](data/lecture25/latex-905fa07e-6c70-4f3d-a7f3-b955d8e50a93.png)
  - Make a guess for ![latex-486490ef-8d8f-43e3-8ea1-622ddd30b280](data/lecture25/latex-486490ef-8d8f-43e3-8ea1-622ddd30b280.png), check that you get the result (check you can get k2).
  - If yes, check on the other pairs
- We want the number of false keys to be close to 0.
  - The number of foreign keys ![latex-53379875-7838-45d6-8d9f-79cca94a676c](data/lecture25/latex-53379875-7838-45d6-8d9f-79cca94a676c.png)

### 4b
- ECB Mode is not semantically secure
  1. If someone encrypts the same plaintext blocks, the ciphertexts are the same
  2. Chosen plaintext attacks: Can learn information about the plaintexts by guessing
- CBC works by chaining blocks together, can't perform the same chosen plaintext attacks
- Useless Block Chaining (as defined in the question), show that's is not better
  - Why useless? You know the previous blocks, can simply XOR. Then it's the same case as ECB mode.

## Sample MT 2

### 1g
- Polytime: in terms of the input size
- Iterate from: ![latex-064c086c-a745-4f91-81f1-b16dd4accf29](data/lecture25/latex-064c086c-a745-4f91-81f1-b16dd4accf29.png),
  - Bit length of n is ![latex-d9479385-65e7-4cfb-8a8e-f0254da32b61](data/lecture25/latex-d9479385-65e7-4cfb-8a8e-f0254da32b61.png)
  - Algorithm takes ![latex-3288c33b-c675-445e-9553-3f8fe5c8ca81](data/lecture25/latex-3288c33b-c675-445e-9553-3f8fe5c8ca81.png) steps
- Therefore, not polynomial time.

### 3c
- Show CBC mode is not semantically secure against chosen-ciphertext attack
  - Note that it is against chosen plaintext attacks
- Have a decryption oracle, can decrypt anything except for the chosen ciphertext
- Given a target ciphertext, modify it (flip 1 bit of IV), gives a new ciphertext
  - can check that it's the same as the original plaintext, with the first bit flipped (then flip it back to get the original plaintext)
