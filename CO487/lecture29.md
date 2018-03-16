# Lecture 29 - March 15, 2018

## ECDLP
Given ![latex-1730a1eb-622f-4976-b557-7901b6dbb6a6](data/lecture29/latex-1730a1eb-622f-4976-b557-7901b6dbb6a6.png) (n is prime)
- ![latex-fd201c53-d1dc-4fe1-8b3a-469cd40fe498](data/lecture29/latex-fd201c53-d1dc-4fe1-8b3a-469cd40fe498.png)
- ![latex-4974128b-8e08-440b-808f-311280355cdf](data/lecture29/latex-4974128b-8e08-440b-808f-311280355cdf.png)
- ![latex-75de08db-c397-433f-9fc3-3e9ae3205f66](data/lecture29/latex-75de08db-c397-433f-9fc3-3e9ae3205f66.png)

### Attacks on ECDLP
1. Brute Force
  - Keep adding P to itself until you get Q
  - At most, you will go until you get infinity
  - ![latex-caf0af4e-2243-4c3e-b2cb-d517a1ba584b](data/lecture29/latex-caf0af4e-2243-4c3e-b2cb-d517a1ba584b.png)
2. Shank's Algorithm (Meet in the middle)
  - Similar to Double-DES attack
  - Running time: ![latex-39c79559-1fa6-4ca3-a915-82f66eb3940e](data/lecture29/latex-39c79559-1fa6-4ca3-a915-82f66eb3940e.png)
  - Space: ![latex-41bbd130-efb0-4837-a10c-3855bef56c08](data/lecture29/latex-41bbd130-efb0-4837-a10c-3855bef56c08.png)
  - Can modify to trade-off space and time
3. Pollard's Alg
  - Recall VW (for hash collisions)
  - running time: ![latex-382e7fac-0c59-4510-bd9c-526caab28af3](data/lecture29/latex-382e7fac-0c59-4510-bd9c-526caab28af3.png)
  - Space: Negligible
4. Attacks on special elliptic curves
  - There are some weak curves that you shouldn't use. Can easily be avoided in practice
  - Not covered in this class

**TL;DR**: The fastest known attack on ECDLP has fully exponential running time (![latex-b5c3f98a-5739-491b-b78a-88623ff5030a](data/lecture29/latex-b5c3f98a-5739-491b-b78a-88623ff5030a.png))
- **In contrast on RSA**, The fastest known attack on integer factorization hash running time ![latex-06f6afdf-3a7e-4fd2-a0bc-38fd65b0d9d2](data/lecture29/latex-06f6afdf-3a7e-4fd2-a0bc-38fd65b0d9d2.png) which is subexponential.
- Use these hard problems to choose the appropriate modulous.
- **Implication:** Since the fastest attack on ECDLP is slower than Integer Factorization, you can use a smaller params of Elliptic Curve Crypto than for RSA.
  - And you can do so while achieving the same security bit level.

### Comparison of Security Levels

Recall that 128-bit security level is ideal:
- BlackBerry's claim to fame was using a 256-bit security level, problem is that RSA is infeasible at this level, so they adopted ECC.
  - Basically did so for marketing reasons

| Security Level | Block Cipher | Hash functions (VW Attack) | RSA (Bitlength of n) | ECC (Bitlength of p) |
|-|-|-|-|-|
| 80 | SAKJACK | SHA-1 | 1024 | 160 |
| 112| TRIPLE-DES | SHA-224 | 2048 | 224 |
| 128 | AES-128 | SHA-256 | 3072 | 256 |
| 192 | AES-192 | SHA-384 | 7686 | 384 |
| 256 | AES-256 | SHA-512 | 15360 | 512 |

### Curve used in Practice (P-256)
- Provided by the NSA in 1997-1998
- Used ![latex-58ef94f5-8b45-427d-8d87-a49400383d31](data/lecture29/latex-58ef94f5-8b45-427d-8d87-a49400383d31.png)
- Designed to work nicely with 32-bit machines / operations
- ![latex-4a469a38-88f8-4e5e-a95f-078d2c227328](data/lecture29/latex-4a469a38-88f8-4e5e-a95f-078d2c227328.png)
  - b is big
  - People don't trust the NSA, so there is a proceedure for selecting a b, start with a seed, enter it into SHA-1, check that you get p, check that the number of points are prime$$

### ECDH: Elliptic Curve Diffie Hellman (Key agreement)
- Internet is moving to this scheme to agree on shared secret keys
- Original Diffie-Hellman was based on RSA, not used any more

**Goal**: Alice and Bob want to agree upon a shared secret by communicating over an unsecured channel.
- Public params: P-256
  - Prime, equation of curve, number of points on the curve, a fixed point P (not ![latex-2c2080ee-ff2e-4f9c-91e5-bf51ec2f572d](data/lecture29/latex-2c2080ee-ff2e-4f9c-91e5-bf51ec2f572d.png))
- Alice picks a random number: ![latex-aba447ea-35e3-480b-ae40-0659231c8fd0](data/lecture29/latex-aba447ea-35e3-480b-ae40-0659231c8fd0.png). Alice sends $$X$ to Bob.
- Bob picks a random number: ![latex-ef7e7734-634c-4346-ba44-55e7aaa3e256](data/lecture29/latex-ef7e7734-634c-4346-ba44-55e7aaa3e256.png). Bob sends ![latex-20645c2d-de1e-42de-bbca-1f2e44c4cd3c](data/lecture29/latex-20645c2d-de1e-42de-bbca-1f2e44c4cd3c.png) to Alice.
- At this point, Alice and Bob have their own secrets (the logarithms of their respective points points)
- Multiply points by their secrets
  - They each compute computes ![latex-a1956095-3310-46cd-a0c9-6dfffaf53a08](data/lecture29/latex-a1956095-3310-46cd-a0c9-6dfffaf53a08.png)
- Now they share: ![latex-8b4abfe0-eb4b-4da2-b4d2-a3e5261c4ff9](data/lecture29/latex-8b4abfe0-eb4b-4da2-b4d2-a3e5261c4ff9.png)
  - Note that computing x or y from X or Y requires solving the ECDLP problem, which is infeasible (if p is big enough, it is).

#### But.. this is insecure as is: Intruder in the middle attack
- The channel needs to be authenticate
- For example, check RSA public key.
- If an active attacker can impersonate Alice or Bob then they can intercept the communications.
  - Attacker impersonates Bob to Alice, and impersonates Alice to Bob. Establishes shared secrets with each of them.
  - Intruder selects ![latex-19d99805-9be4-4455-9af2-06130cae6efa](data/lecture29/latex-19d99805-9be4-4455-9af2-06130cae6efa.png)
  - Sends ![latex-6cff2578-b66e-489e-80dd-53870b84a0e7](data/lecture29/latex-6cff2578-b66e-489e-80dd-53870b84a0e7.png) to Alice, ![latex-5ba48c3c-e8af-4f52-811c-aa143848cc6b](data/lecture29/latex-5ba48c3c-e8af-4f52-811c-aa143848cc6b.png) to Bob.
  - Alice computes ![latex-35a5467f-d9cc-44f4-9f51-ffda830f95f6](data/lecture29/latex-35a5467f-d9cc-44f4-9f51-ffda830f95f6.png)
  - Bob computes ![latex-05c95e0e-e89b-4a7e-a443-a35e8d73ad1e](data/lecture29/latex-05c95e0e-e89b-4a7e-a443-a35e8d73ad1e.png)
  - The attacker recieves an intercepted message from Alice, decrypts it using ![latex-e8d27a72-a786-4f57-8060-928a2ccda48c](data/lecture29/latex-e8d27a72-a786-4f57-8060-928a2ccda48c.png), encrypts it using ![latex-fcfd8883-68fb-4abe-bebe-cacbe3a3751a](data/lecture29/latex-fcfd8883-68fb-4abe-bebe-cacbe3a3751a.png) and sends it to Bob.
  - Alice and Bob are happy, but the attacker knows the plaintext.
  - **How to defend**: Alice and Bob should authenticate the channel, by signing X and Y using the RSA signature scheme (or ECDSA).


![graph-621620fe-a4d3-4424-b603-8db4db72f152](data/lecture29/graph-621620fe-a4d3-4424-b603-8db4db72f152.svg)

### ECDSA: Signature Algorithm
- Used in Bitcoin
- Next class
