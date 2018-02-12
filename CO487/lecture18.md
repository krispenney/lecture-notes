# Lecture 18 - February 12, 2018

## Public Key Crypto
- Generate a key pair ![latex-3f21dbc0-0864-4a26-be9f-a4ed9a1a2b04](data/lecture18/latex-3f21dbc0-0864-4a26-be9f-a4ed9a1a2b04.png)
- ![latex-225360b2-fb8b-4719-afdc-a6ab91d78e95](data/lecture18/latex-225360b2-fb8b-4719-afdc-a6ab91d78e95.png): Public Key for Alice
- ![latex-6ac2ac23-421d-4417-a501-5ee0bc5ac2d3](data/lecture18/latex-6ac2ac23-421d-4417-a501-5ee0bc5ac2d3.png): Secret key for Alice

### Encryption
- Alice encrypt's her message with ![latex-ffd7acc6-92bb-4748-aa52-e03dbdec5c7d](data/lecture18/latex-ffd7acc6-92bb-4748-aa52-e03dbdec5c7d.png), Bob's public key ![latex-680bbca5-d8a6-4ca0-b98a-2a92f13ed720](data/lecture18/latex-680bbca5-d8a6-4ca0-b98a-2a92f13ed720.png)
- Bob can decrypt the message: ![latex-8ea02e1c-384d-4e94-a637-062d301be271](data/lecture18/latex-8ea02e1c-384d-4e94-a637-062d301be271.png)

### Digital Signatures
- Alice computes a signing function using her secret key
- Bob can verify the message using Alice's public key
- Signatures depend on the messages being sent
  - Not the same as a physical signature, i.e. the signature is not the same
  - Can't just cut off the signature and append to a different message
- Large application: Software updates
  - Can't use a MAC scheme, Microsoft can't share the same key with Alice and Bob
  - Instead, Microsoft broadcasts the signed software to everyone
  - Each user can verify the update using Microsoft's public key.

### Advantages over Symmetric-Ley
- No need for secret channel
- Only 1 key pair
- A signed message can be verified by anyone

### Disadvantages for symmetric-key
- Public keys are larger than symmetric key
- Public-key schemes are slower than symmetric key schemes
- **In practice**: combine both

## Hybrid Scheme
- Functionalty of public-key and speed of symmetric key

### Encryption
Alice does the following:
- Compute a signed message using her secret key
  - In practice, sign the message
  - If the hash function is collision resistent, then can't generate collisions, valid signature
- ![latex-784157ac-e4be-4c1f-a91d-1d8e70397f59](data/lecture18/latex-784157ac-e4be-4c1f-a91d-1d8e70397f59.png) and ![latex-1da78db2-3082-4745-b6f5-e6bec975bab7](data/lecture18/latex-1da78db2-3082-4745-b6f5-e6bec975bab7.png)

### Decryption
- Bob first decrypt's ![latex-2e82fe7d-5438-4f9c-8281-67c0adfab081](data/lecture18/latex-2e82fe7d-5438-4f9c-8281-67c0adfab081.png) using his secret key
- Uses the symmetric secret key to decrypt ![latex-041f7efc-4ed7-4e75-ad71-1c3de210a96f](data/lecture18/latex-041f7efc-4ed7-4e75-ad71-1c3de210a96f.png)
- Bob can then verify using Alice's public key

## Algorithmic Number theory

### Fundamental Theorem of Arithmetic
- Every integer ![latex-1b1c93a0-fafd-454b-b845-8635f0e5c0a7](data/lecture18/latex-1b1c93a0-fafd-454b-b845-8635f0e5c0a7.png) has a unique prime factorization
- Question: What is the factorization -> how to find it?
  - Can it be found **efficiently**?
  - No great algorithm to do this
- How do we efficiently veify an alleged prime factorization
  - Need to check if the given factor's are prime
  - this can be done quickly
- Given an integer, how do we efficiently decide whether n is prime or composite?
  - this can be done quickly

### Complexity Theory
- Measure efficiency in terms of the input size
- Number of bits: ![latex-ae4143e9-f757-43b4-881a-8fb0f77614de](data/lecture18/latex-ae4143e9-f757-43b4-881a-8fb0f77614de.png)
- An algorithm is polynomial time: ![latex-1c97e0e5-b8e8-4683-8ecc-a590714d4559](data/lecture18/latex-1c97e0e5-b8e8-4683-8ecc-a590714d4559.png)

#### GCD

##### Naive Method
- Write ![latex-267834ae-6e39-4b7f-9498-098e5ed26f08](data/lecture18/latex-267834ae-6e39-4b7f-9498-098e5ed26f08.png) (prime factorization)
- ![latex-ba4dadab-4eee-4420-9d97-93b17e840959](data/lecture18/latex-ba4dadab-4eee-4420-9d97-93b17e840959.png)
- Note that since we don't have an efficient algorithm for prime factorization, so this is not polynomial time

##### Euclid's Method
- Find the answer without factoring everything
- Find ![latex-0d84bffc-493b-49fe-b05e-a98414188cec](data/lecture18/latex-0d84bffc-493b-49fe-b05e-a98414188cec.png)
- ![latex-7ac13d47-6396-4269-b925-8b1d4e631c97](data/lecture18/latex-7ac13d47-6396-4269-b925-8b1d4e631c97.png)
- ![latex-904d8da1-bbfd-479e-9dfe-625468001d65](data/lecture18/latex-904d8da1-bbfd-479e-9dfe-625468001d65.png)
- ![latex-63c85098-7987-451b-beec-656f638d2104](data/lecture18/latex-63c85098-7987-451b-beec-656f638d2104.png)
- ![latex-7c550755-a007-4bf8-a3b0-a0baa7a76a1d](data/lecture18/latex-7c550755-a007-4bf8-a3b0-a0baa7a76a1d.png)
- ![latex-c8734681-a25d-45b5-b188-c0c07a44d178](data/lecture18/latex-c8734681-a25d-45b5-b188-c0c07a44d178.png)
- ![latex-5d9ee8ee-47ef-4edb-a002-1d8e40804fb3](data/lecture18/latex-5d9ee8ee-47ef-4edb-a002-1d8e40804fb3.png)
- ![latex-27a71ad5-482b-4ab0-b1b9-d7a3a6476a0e](data/lecture18/latex-27a71ad5-482b-4ab0-b1b9-d7a3a6476a0e.png)
- k-bit numbers
- At most ![latex-04240cf1-a15c-414d-b370-80d9a30f6ca7](data/lecture18/latex-04240cf1-a15c-414d-b370-80d9a30f6ca7.png) divisions, ![latex-6ac65b27-7ca2-44bf-8f8f-33d613e032c4](data/lecture18/latex-6ac65b27-7ca2-44bf-8f8f-33d613e032c4.png)
  - Worst case is sequential fibbonacci numbers
  - See A4 for another gcd algorithm to analyze.

### Modulous Arithmetic
- k-bit integer ![latex-2bbd71ee-8100-46c2-b9c8-41477eb09e03](data/lecture18/latex-2bbd71ee-8100-46c2-b9c8-41477eb09e03.png), integers ![latex-c7280f8c-eee4-48ac-bd23-bcda4ab50f3d](data/lecture18/latex-c7280f8c-eee4-48ac-bd23-bcda4ab50f3d.png)
- ![latex-6922c1b8-214f-486f-bd6e-d64252853409](data/lecture18/latex-6922c1b8-214f-486f-bd6e-d64252853409.png): the remainder upon deviding a by n.

#### Inverse
- ![latex-96946eb3-fb90-47af-9597-a3bee30c8d32](data/lecture18/latex-96946eb3-fb90-47af-9597-a3bee30c8d32.png), note that ![latex-6f5f6419-7cbf-4173-888e-20e546e99717](data/lecture18/latex-6f5f6419-7cbf-4173-888e-20e546e99717.png)
- Can be efficiently computed using the extended euclidean algorithm

#### Exponentiation
- to compute ![latex-031aecd0-9b96-4c9f-90ff-c4c1831d3c60](data/lecture18/latex-031aecd0-9b96-4c9f-90ff-c4c1831d3c60.png) first compute ![latex-40a65012-389a-4c76-a561-d2031db461c5](data/lecture18/latex-40a65012-389a-4c76-a561-d2031db461c5.png), then ![latex-892f0d42-f89c-4d8e-847f-a004fed3eefc](data/lecture18/latex-892f0d42-f89c-4d8e-847f-a004fed3eefc.png)
  - This is not polynomial time, ![latex-0a923785-f2d4-4a65-8350-8908cfb6ae13](data/lecture18/latex-0a923785-f2d4-4a65-8350-8908cfb6ae13.png)
- Want: ![latex-aa21e080-b590-4ef7-bb30-0122967961af](data/lecture18/latex-aa21e080-b590-4ef7-bb30-0122967961af.png)
  - Write ![latex-994da26a-2cc2-4c9e-a226-9213ae01f3f5](data/lecture18/latex-994da26a-2cc2-4c9e-a226-9213ae01f3f5.png)
  - ![latex-545f9b7c-fa54-464d-be34-042507dae095](data/lecture18/latex-545f9b7c-fa54-464d-be34-042507dae095.png)
  - Then repeatly compute ![latex-1a322ecd-20a2-45c2-b590-ac39dd88a8d6](data/lecture18/latex-1a322ecd-20a2-45c2-b590-ac39dd88a8d6.png)
  - Note: Never increases to more than ![latex-1c514be1-3251-470e-8dfd-1650f7b90dbf](data/lecture18/latex-1c514be1-3251-470e-8dfd-1650f7b90dbf.png) bits
