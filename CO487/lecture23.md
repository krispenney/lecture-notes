# Lecture 23, March 2, 2018

## Equivalent Security Level
- Dependent on the capabilities of integer factorization
- NVS

## RSA Signature Scheme

Each entity A does the following:

1. Randomly select 2 large distinct primes p and q
2. compute ![latex-649d4a64-b83e-4718-8c96-4d1c35885bc0](data/lecture23/latex-649d4a64-b83e-4718-8c96-4d1c35885bc0.png)
3. Select arbitrary ![latex-a5bace03-c41e-4a2b-a74c-16cdc7118ec8](data/lecture23/latex-a5bace03-c41e-4a2b-a74c-16cdc7118ec8.png)
4. Compute d, private key
5. public key is ![latex-71cd22bf-41df-4f6a-9b7c-cbe8264af25e](data/lecture23/latex-71cd22bf-41df-4f6a-9b7c-cbe8264af25e.png)

### Example
- Alice wants to sign message **m**
- private key d must be used to sign, public key to verify

#### Signing
- ![latex-a7435a55-1df0-4573-bc33-5bc062be7e98](data/lecture23/latex-a7435a55-1df0-4573-bc33-5bc062be7e98.png): Is an RSA signature
- Alice would send the message and the signature to Bob

#### Verification
- Bob would use Alice's public key to verify
- ![latex-6c8e0559-33ea-4c80-a196-7e6634674464](data/lecture23/latex-6c8e0559-33ea-4c80-a196-7e6634674464.png)

### Security
- Requires that finding e-th roots mod n is an intractable problem
- RSA problem has to be hard (same as encryption)

#### Security properties of the hash function

##### Preimage resistance
- If not, an attacker can incover a message that would equal the hash

##### Second Preimage Resistant
- If not: given ![latex-1c4d6e61-0fe8-4381-b141-3a7bef6e2009](data/lecture23/latex-1c4d6e61-0fe8-4381-b141-3a7bef6e2009.png) can find a ![latex-dec2ea62-6ff0-40a4-a375-d5698008a5d9](data/lecture23/latex-dec2ea62-6ff0-40a4-a375-d5698008a5d9.png)
- ![latex-555ded24-0560-4af7-80e1-5dd445c09d0d](data/lecture23/latex-555ded24-0560-4af7-80e1-5dd445c09d0d.png) is valid

##### Collision resistance
- Can select two messages with the same hash value
- Ask alice to sign one of the messages
- The signature is valid for the other

#### Goals of the adversary

1. **Total Break**: E can recover the private key, or can compute the signature for any message of their choice
2. **Existential Forgery**: E forges A's signature for a single message, E may not have any control over the structure or content of the message

##### Attack model
1. **key only attack**: Attacker only has public key
2. **known message attack**: E knows some message, signature pairs
3. **Chosen message attack**: E can pick messages of their choice, get alice to sign them. E can then compute the signature for any future message (not already signed by Alice)

##### SEcurity Definition
- Signature scheme is said to be secure if it is existentially unforegable by a computationally bounded adversary who launches a chosen mesage attack.
  - **Note the similarity to the security notion of a MAC scheme**
- Adversary has access to a signing oracle, goal is to compute a single valid message signature pair

###### Is sha 256 secure if used
- No, if the hash values are much smaller than the bit length of the modulous
- Make the hash values at least as big as the modulous
- Use "full-domain" hash RSA

### Full Domain Hash RSA
Map the hash values to the full domain of the RSA function

- Theorem: if RSAP is intractable and H is a random function, then RSA-FDH is a secure signature scheme.
  - As before H will be random-like in practice.
  - Therefore, the theorem doesn't always apply in practice.

#### How to extend hash values to full domain
- **naive way**: is just repeated hashing with a counter

##### PKCS

###### Signing
- compute ![latex-29a38c3a-ca0e-410c-802b-542cf6ed7583](data/lecture23/latex-29a38c3a-ca0e-410c-802b-542cf6ed7583.png), where H is a hash function (ex. SHA-1, SHA-256, ...)
  - Point is the hash function is not fixed
- Format h:
  - Let k by the byte length of n
  - To the right of the hash, append 15 byte hash name
    - This is an ISO standard table
  - ![latex-fba15de1-28ea-4ce8-8549-02803d635281](data/lecture23/latex-fba15de1-28ea-4ce8-8549-02803d635281.png)
- Finally sign the formatted hash value: ![latex-1c53ee62-1e81-4a67-bc64-4296b04c9fdf](data/lecture23/latex-1c53ee62-1e81-4a67-bc64-4296b04c9fdf.png)
- Alice sends the message and the signature

###### Verification
1. Obtain an authentic copy of Alice's public key ![latex-0ed13a89-cfc8-46f5-a81e-2ffb44da03b1](data/lecture23/latex-0ed13a89-cfc8-46f5-a81e-2ffb44da03b1.png)
2. Compute ![latex-f5cefe19-937f-410b-b54b-f7649640df5b](data/lecture23/latex-f5cefe19-937f-410b-b54b-f7649640df5b.png), to obtain the formatted hash value
3. Check the formatting (from left to right)
  1. Ensure that the padding matches (00, 01, FFFFFFF...., etc)
  2. Extract the hash name
  3. Use that hash function to hash the message
  4. check that the hashes match up
  5. Need to check that there are no more bytes left over
    - Buffer underflow attack
4. Either accept or reject the message

###### Bug: "Buffer Underflow Attack"
- RSA signatures can be forged by hand
- PIck any message, hash it, then you can write the signature by hand
- **Need to check that there are no bytes left over**

Highlights the importance of being specific in standards.
- Similar: "Uniform and Independtly random primes" when selecting RSA primes, some people just pick the next prime (both are random, but not independent)
