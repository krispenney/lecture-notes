# Lecture 25 (Midterm Q&A) - March 7, 2018

## Encryption at Google on MT?
- Very little
- Mostly just used as a vague case study.

## Relationships between hash function properties
- Pre image: Given some random hash function value, find a message x that sums to that hash, in a feasible amount of time.
- 2nd PreImage: Given an input, find a second distinct message whose hash is the same, again feasible amount of time.
- Collision resistance: Find two distinct inputs that sum to the same hash

The following examples only focus on uniform hash functions (i.e. no contrived examples ![latex-9aee1732-7203-4606-b476-60006f0435ee](data/lecture25/latex-9aee1732-7203-4606-b476-60006f0435ee.png))
- Always prove these with the contra-positive
- **NEVER SAY "EXISTS"**: they always do, the attack just needs to be feasible


![graph-5c77fc85-6c52-4615-943c-c6b7bc97c1a7](data/lecture25/graph-5c77fc85-6c52-4615-943c-c6b7bc97c1a7.svg)

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
- ![latex-a4612431-70a3-48cd-b443-b95764ab8942](data/lecture25/latex-a4612431-70a3-48cd-b443-b95764ab8942.png)
- ![latex-36cd711a-aa9c-4148-89a1-5a0feed2102f](data/lecture25/latex-36cd711a-aa9c-4148-89a1-5a0feed2102f.png)

## Sample MT 1

### 3
- Goal of question, show how the modification to DES doesn't help

#### Part a
- ![latex-e15d4dac-5267-4642-9989-a665613fce7a](data/lecture25/latex-e15d4dac-5267-4642-9989-a665613fce7a.png)

#### Part b
- By exhaustive key search: Can solve in ![latex-4a5e7ae4-6742-40ed-9c75-1f5580aae2ae](data/lecture25/latex-4a5e7ae4-6742-40ed-9c75-1f5580aae2ae.png) steps (infeasible)
- can compute ![latex-cb97df14-a323-4b62-825e-175012c7919d](data/lecture25/latex-cb97df14-a323-4b62-825e-175012c7919d.png)
  - Make a guess for ![latex-a40de7cd-5cfc-4a30-9f90-5c4fd62923b4](data/lecture25/latex-a40de7cd-5cfc-4a30-9f90-5c4fd62923b4.png), check that you get the result (check you can get k2).
  - If yes, check on the other pairs
- We want the number of false keys to be close to 0.
  - The number of foreign keys ![latex-9f18097a-b2ba-4e2a-b31d-f62b39bd980e](data/lecture25/latex-9f18097a-b2ba-4e2a-b31d-f62b39bd980e.png)

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
- Iterate from: ![latex-73194631-3cca-4cc9-ad57-5a7b83b1b155](data/lecture25/latex-73194631-3cca-4cc9-ad57-5a7b83b1b155.png),
  - Bit length of n is ![latex-6f30e80f-9ea3-4adb-b6f5-c0f003609234](data/lecture25/latex-6f30e80f-9ea3-4adb-b6f5-c0f003609234.png)
  - Algorithm takes ![latex-81697fff-015b-418b-863c-741c5a12e7cc](data/lecture25/latex-81697fff-015b-418b-863c-741c5a12e7cc.png) steps
- Therefore, not polynomial time.

### 3c
- Show CBC mode is not semantically secure against chosen-ciphertext attack
  - Note that it is against chosen plaintext attacks
- Have a decryption oracle, can decrypt anything except for the chosen ciphertext
- Given a target ciphertext, modify it (flip 1 bit of IV), gives a new ciphertext
  - can check that it's the same as the original plaintext, with the first bit flipped (then flip it back to get the original plaintext)
