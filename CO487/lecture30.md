# Lecture 30 - March 19, 2018

## ECDH
- Scheme for key agreement

Public Params:
- A prime ![latex-18abdb68-db39-41cb-b0db-39371be24082](data/lecture30/latex-18abdb68-db39-41cb-b0db-39371be24082.png)
- ![latex-92fe10ab-7158-4e52-af08-10fca3f257ed](data/lecture30/latex-92fe10ab-7158-4e52-af08-10fca3f257ed.png)
- n (number of points)
- ![latex-fac83364-385b-4d67-9d69-f7528514043e](data/lecture30/latex-fac83364-385b-4d67-9d69-f7528514043e.png)

### Unauthenticated
- Alice: ![latex-6a9bd35a-5d13-4648-9218-a990d0f5b26a](data/lecture30/latex-6a9bd35a-5d13-4648-9218-a990d0f5b26a.png)
  - Public: ![latex-71652aae-b982-4a4f-9111-7d38dfe8ef89](data/lecture30/latex-71652aae-b982-4a4f-9111-7d38dfe8ef89.png)
  - Send this to Bob
  - ![latex-fb9b9668-ee53-433a-802a-bd38465513f0](data/lecture30/latex-fb9b9668-ee53-433a-802a-bd38465513f0.png)
- Bob: ![latex-262365af-6252-4a5b-b9e2-ada5c0500fa3](data/lecture30/latex-262365af-6252-4a5b-b9e2-ada5c0500fa3.png)
  - Public: ![latex-d5c877ad-f323-4291-a82f-c1ec4b86cb2b](data/lecture30/latex-d5c877ad-f323-4291-a82f-c1ec4b86cb2b.png)
  - Send this to Bob
  - ![latex-6659c207-e06b-42b2-b879-64771cbb9fb8](data/lecture30/latex-6659c207-e06b-42b2-b879-64771cbb9fb8.png)
- **Problem**: This is open to an intruder in the middle attack

### Authenticated
- Each party signs the points they exchange (ex. with their RSA private key)
- The reciever verifies the point user the senders public key
- ![latex-c27de473-5bf7-4452-81d7-e2df79c60a47](data/lecture30/latex-c27de473-5bf7-4452-81d7-e2df79c60a47.png) is signed by Alice
  - In practice this is typically only one way, you can't expect users to manage certificates.
  - So Alice would verify the point recieved by Bob.
- ![latex-b608c5ac-d1e6-43a8-a6ed-abaadf430183](data/lecture30/latex-b608c5ac-d1e6-43a8-a6ed-abaadf430183.png) is signed by Bob

## RSA Key Transport
- Alice select session key k, Alice encrypts k with Bob's RSA public key.
- Why use ECDH over this?
  - Google example
  - ECDH provides **forward secrecy**:
    - If an attacker obtains a ciphertext, then later gains access to Bob's private key, they can decrypt the ciphertexts
    - Uncover the session key k, get the plaintexts that were encrypted with k
    - Giving up a private key (which is in use for a fairly long period of time, +1 year), allows for the decryption of a long term of data. Getting this out would be bad.
    - Using unique RSA keys is expensive, it is easy to pick a random point on the curve.
  - Once the keys are exchanged, at the end of the session both parties should delete their points (y and x) and the shared secret K.
    - This provides forward secrecy
    - If the NSA comes to Google, demanding the private key, they don't have it, meaning any captured ciphertexts can't be decrypted.

## ECDSA: Elliptic Curve Digital Signature Algorithm
- Same EC public params as before

### Key generation:

Each user does the following
1. Select ![latex-b8f66d41-5ce8-4e91-90e8-b807c327efd8](data/lecture30/latex-b8f66d41-5ce8-4e91-90e8-b807c327efd8.png)
2. Compute ![latex-c06a428d-40ed-49d8-b69f-dc5e897b1b28](data/lecture30/latex-c06a428d-40ed-49d8-b69f-dc5e897b1b28.png)
3. a is Alice's private key, A is Alice's public key
  - Recall the security of this relies on the ECDLP

### Signature Generation

To sign a message of any length
1. Compute ![latex-9ac8405d-1d80-4452-9df2-b539ed00616c](data/lecture30/latex-9ac8405d-1d80-4452-9df2-b539ed00616c.png)
2. Selects a random secret k (**per-message secret**), ![latex-07bad653-feb8-48c3-908c-492e3ce332ae](data/lecture30/latex-07bad653-feb8-48c3-908c-492e3ce332ae.png)
  - **THIS IS VERY IMPORTANT**
3. Compute the corresponding point ![latex-311498d3-e1d4-49ed-84f0-2ffb41b480e7](data/lecture30/latex-311498d3-e1d4-49ed-84f0-2ffb41b480e7.png)
  - You want to extract a number from this point
  - ![latex-5aa7db5e-e5c5-41d2-adce-11607ffdeefb](data/lecture30/latex-5aa7db5e-e5c5-41d2-adce-11607ffdeefb.png). Take the x coordinate mod n of R.
  - If ![latex-3ef775fe-609a-43be-9c5e-128c03523856](data/lecture30/latex-3ef775fe-609a-43be-9c5e-128c03523856.png) then go back to step 2
4. Compute the ECDSA signing equation: ![latex-90c6a60f-a098-42bf-afe0-b7578cba7763](data/lecture30/latex-90c6a60f-a098-42bf-afe0-b7578cba7763.png)
  - Goal is to compute a number that can only be generated using the message key and the private key
  - Recall that n is prime, ![latex-6508beb9-c6fa-4ba3-92df-0983e8cf794b](data/lecture30/latex-6508beb9-c6fa-4ba3-92df-0983e8cf794b.png) must exist because it is non-zero.
  - If ![latex-4fe437ed-37b7-45c3-8ade-97d4c6b88463](data/lecture30/latex-4fe437ed-37b7-45c3-8ade-97d4c6b88463.png), go back to 2.
5. Alice's signature on M is ![latex-b2dadddb-fa55-4f57-801b-000f3accae27](data/lecture30/latex-b2dadddb-fa55-4f57-801b-000f3accae27.png)

We want ![latex-bf2370e1-0738-4c2e-b075-22b87bf0f59d](data/lecture30/latex-bf2370e1-0738-4c2e-b075-22b87bf0f59d.png)

### Signature Verification

To verify ![latex-4b8e7228-80d9-4f00-ba20-187ef96ae08f](data/lecture30/latex-4b8e7228-80d9-4f00-ba20-187ef96ae08f.png), Bob does the following:
1. Obtain an authenticate copy of Alice's public key
  - Through a CA, etc
2. Check that ![latex-f018cccd-dc8b-46b7-82f1-f99076268e34](data/lecture30/latex-f018cccd-dc8b-46b7-82f1-f99076268e34.png)
  - If r was 0 then, the signature would not depend on the private key.
  - If not then **reject**
3. Compute ![latex-b2b60cd9-799c-4951-866e-691611d4b739](data/lecture30/latex-b2b60cd9-799c-4951-866e-691611d4b739.png)
- ![latex-0d99946e-46d3-46f0-8ea9-b200765405d8](data/lecture30/latex-0d99946e-46d3-46f0-8ea9-b200765405d8.png)
  - Bob can't check this directly, he doesn't know k or a.
  - ![latex-9a07342d-5786-4f61-9924-21b7e85dd801](data/lecture30/latex-9a07342d-5786-4f61-9924-21b7e85dd801.png)
    - This is why ![latex-bc23a815-74fa-4aa3-9bc6-104e374dc98b](data/lecture30/latex-bc23a815-74fa-4aa3-9bc6-104e374dc98b.png), otherwise ![latex-e0b3b271-8a0f-4302-99bf-a8fb0af3d1ad](data/lecture30/latex-e0b3b271-8a0f-4302-99bf-a8fb0af3d1ad.png) would not exist
  - ![latex-6e3f00cf-2126-4ca8-86f9-e31d71aff598](data/lecture30/latex-6e3f00cf-2126-4ca8-86f9-e31d71aff598.png), this is because ![latex-5d75a6fa-942d-49b5-9d45-ee239e9f22aa](data/lecture30/latex-5d75a6fa-942d-49b5-9d45-ee239e9f22aa.png)
  - ![latex-fd003b7e-7029-4ccc-a26b-1594d8df6697](data/lecture30/latex-fd003b7e-7029-4ccc-a26b-1594d8df6697.png)
  - ![latex-7c13c94c-d86a-41c6-9efd-a1bba76981cb](data/lecture30/latex-7c13c94c-d86a-41c6-9efd-a1bba76981cb.png)
    - Bob can compute the right hand side of the equation using the information he knows.
    - Recall ![latex-f7472188-d1a9-4804-ac69-2ea510f4260b](data/lecture30/latex-f7472188-d1a9-4804-ac69-2ea510f4260b.png)
  - ![latex-af243a33-25eb-4dd2-b796-57b9ed7f0ef9](data/lecture30/latex-af243a33-25eb-4dd2-b796-57b9ed7f0ef9.png)
  - ![latex-def4dccb-b562-4a60-b818-587bc9104f24](data/lecture30/latex-def4dccb-b562-4a60-b818-587bc9104f24.png)
4. Compute ![latex-3aa727ed-d168-4680-8f93-41410e564562](data/lecture30/latex-3aa727ed-d168-4680-8f93-41410e564562.png) and ![latex-e606c348-322a-407f-8d2d-90bef7f26a27](data/lecture30/latex-e606c348-322a-407f-8d2d-90bef7f26a27.png)
5. Compute ![latex-f6443574-4e23-451c-99f1-44983de897a4](data/lecture30/latex-f6443574-4e23-451c-99f1-44983de897a4.png) and ![latex-eb6beb60-1ab7-4662-a470-b9b7e8cdefd0](data/lecture30/latex-eb6beb60-1ab7-4662-a470-b9b7e8cdefd0.png)
6. Check that ![latex-5a9fc7fd-0cd8-49ae-a103-8141dae9ee72](data/lecture30/latex-5a9fc7fd-0cd8-49ae-a103-8141dae9ee72.png)
  - If so, accept
  - If not, reject

#### Notes
1. ECDSA is believed to be secure (existentially unforgable against chosen message attacks)
  - As long as the ECDLP in ![latex-7d921596-b67f-48b6-8a05-68cc08ce05a3](data/lecture30/latex-7d921596-b67f-48b6-8a05-68cc08ce05a3.png) is hard
  - And SHA-256 is a secure hash function.
2. If p is 256-bits (as is the case with P-256), then a signature is 512-bits long
  - Recall that n is roughly p
  - In comparision, an RSA signature with a 3072-bit modulous.
3. Recall RSA signature generation is slower than ECDAS signature generation
  - Since ![latex-20075cd9-f611-4f4a-8354-73b0ecadde2b](data/lecture30/latex-20075cd9-f611-4f4a-8354-73b0ecadde2b.png) is with a 3072-bit d and n.
  - In contrast, in computing ![latex-1076df70-de5f-4415-a65e-5096ad3f5590](data/lecture30/latex-1076df70-de5f-4415-a65e-5096ad3f5590.png), k is a 256-bit number, as are the coordinates of ![latex-ca7e386c-5fc0-4203-9fa4-515c187e0229](data/lecture30/latex-ca7e386c-5fc0-4203-9fa4-515c187e0229.png). So the arithmetic is with 256 bit numbers.
