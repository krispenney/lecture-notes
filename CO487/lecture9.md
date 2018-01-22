# Lecture 9 - January 22, 2018

## Encryption at Google

### Web pages + servers:
SSL / TLS

### Machines in Datacenters
ATLS: Application TLS

### Data Stored in datacenters
Uses a separate service

#### Key Management Service
- AES256-GCM (Galois Counter Mode)
- Manages Key Encryption Keys
- Physical backup of the Root KMS Master is made incase of system reboot.
  - All other are stored in RAM

## Hash Functions
- Very large maximum input size of ![latex-e104d2ca-69c8-49b1-8720-86fa5918d8bf](data/lecture9/latex-e104d2ca-69c8-49b1-8720-86fa5918d8bf.png) (typically just `*`, because it's so large)
- ![latex-9f51ece3-5277-4433-a06f-ee8df28c7cd8](data/lecture9/latex-9f51ece3-5277-4433-a06f-ee8df28c7cd8.png) can be efficiently computed
- **Note:** The description of a hash function is public, there are no secret keys.
- hash value, hash, message digest

**Goal**: One way, can't reverse
  - collisions should be very hard to find
  - fingerprint (usually a fixed length)
  - ![latex-fbae259c-f847-46d9-aa68-ca496e7f6a52](data/lecture9/latex-fbae259c-f847-46d9-aa68-ca496e7f6a52.png), should have no relation between them

### SHA-256
![latex-c4548346-e3ad-4cfa-9563-3cfda26575b5](data/lecture9/latex-c4548346-e3ad-4cfa-9563-3cfda26575b5.png)

### Davies Meyer Hash function (from block ciphers)

- ![latex-fce674c4-182f-4c2b-ab98-a1270f75b2ce](data/lecture9/latex-fce674c4-182f-4c2b-ab98-a1270f75b2ce.png) be an m-bit block chiper with n-bit key k
- IV be a fixed m-bit initializing value
- Break up ![latex-baaf02d9-6bba-49f1-94f0-7d4a91f39466](data/lecture9/latex-baaf02d9-6bba-49f1-94f0-7d4a91f39466.png) into m-sized blocks. (append 1 to the end and then pad with 0's)
- ![latex-cde72a04-6f17-430b-aeea-4b1c63c8d481](data/lecture9/latex-cde72a04-6f17-430b-aeea-4b1c63c8d481.png)
- Use each message block as the "key", feed though all blocks

## Properties
- ![latex-af9d6f48-a253-41e9-b0c8-397b7fa0de4c](data/lecture9/latex-af9d6f48-a253-41e9-b0c8-397b7fa0de4c.png), `1001` is a **preimage** of `01`
- **second preimage**: ![latex-8e1d4929-77b9-4934-8f66-659f3a6b3df7](data/lecture9/latex-8e1d4929-77b9-4934-8f66-659f3a6b3df7.png), `10` is a **second preimage** of 01

### Preimage Resistance
Given a hash y, It should be computationally infeasible to find an x such that ![latex-04fa8618-e7e0-4a22-baf8-2e8e422cdeb4](data/lecture9/latex-04fa8618-e7e0-4a22-baf8-2e8e422cdeb4.png).
- Should have non-negligible probability of success.
- With a large bit-length, this should be very small (i.e. unlikely to randomly guess)

### Second Preimage Resistance
Given a message x, it is computationally infeasible to find a second input x` (`x != x'`) such that the hashes are the same.

#### Modigication Detection Codes (MDCs)
To ensure that a message is not modified in a malicious way, compute the hash of the message and protects H(m) from un-authorized modification
- Virus protection
- Validating software / files
- Requires second preimage resistance

### Collision Resistance
Computationally infeasible to find 2 distinct inputs, such that their hashes match.
- Trade off between hash computation time and probability of finding a collision.

#### Message Digests for digital signature schemes
- Instead of signing the actual message, sign the digest (more efficient)
- Message space huge (![latex-9d05f0df-2060-49ca-aacf-a54c60107ebb](data/lecture9/latex-9d05f0df-2060-49ca-aacf-a54c60107ebb.png)), but smaller hash space (![latex-78a14ffc-71bd-4827-8fe9-b33e5957e581](data/lecture9/latex-78a14ffc-71bd-4827-8fe9-b33e5957e581.png))
- requires all forms of resistance

### Relationships
**Note:** When proving these relationships, prove the contrapositive

1. Collision resistance implies 2nd preimage resistance
2. 2nd preimage resistance does not guarantee collision resistance
  - ![latex-d77f4dc0-01fd-4b34-941a-390375369a9e](data/lecture9/latex-d77f4dc0-01fd-4b34-941a-390375369a9e.png): Not Collision resistanct because of (0, 1)
  - ![latex-a7afcf6c-3709-4114-81d5-3c554095efb5](data/lecture9/latex-a7afcf6c-3709-4114-81d5-3c554095efb5.png): Is 2nd preimage resistant,
  - Collision resistance is harder to guarantee.
3. Collision resistance does not guarantee preimage resistance.
  - ![latex-b4521153-0e01-4d29-a67c-84abb0dfe44f](data/lecture9/latex-b4521153-0e01-4d29-a67c-84abb0dfe44f.png): Is collision resistant: All n-bit x's have unique hash values, all other x's are in the second case, which depends on `H`.
  - Not preimage-resistant because preimages can be easily found for (at least) half of all possible.
    - If the hash starts with a 1, simply guess the n-bits after the 1.
4. Collision Resistance implies preimage resistance **(in practice)**
  - Real hash functions are designed to be reasonably uniform
  - Low probability of guessing
  - If it's not preimage resistance, there are many pre-images that can be found thus `(x, x')` is a collision (not collision resistant)


