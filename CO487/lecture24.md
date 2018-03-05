# Lecture 24, March 5, 2018

## Bleichenbacher's Attack - Break PKCS 1 V1.5 RSA signatures by hand
- ![latex-582b91e7-d656-41af-a105-ff1ae8d8b4fc](data/lecture24/latex-582b91e7-d656-41af-a105-ff1ae8d8b4fc.png): message, signature pair
- ![latex-e0d7a883-570c-44fb-a225-54ba4f358a94](data/lecture24/latex-e0d7a883-570c-44fb-a225-54ba4f358a94.png) = Padded Hash value, k bytes long (k is the byte length of the RSA modulous)
- ![latex-7227f06d-c542-4572-aca3-dfb6cc726bfe](data/lecture24/latex-7227f06d-c542-4572-aca3-dfb6cc726bfe.png):
  - Hash name: 15 bytes long
  - The way the standard was written meant it didn't specify that there are anything at the end of the padding, the basis of this attack.

### Assumptions

1. n: 3072 bits long, WLOG
2. Suppose H = SHA-1 (again WLOG)
3. ![latex-d13e82c3-e23a-4c5b-8dab-e7b0b6ddb913](data/lecture24/latex-d13e82c3-e23a-4c5b-8dab-e7b0b6ddb913.png) (widely used in practice, efficiency reasons)
4. Verifier doesn't check that there are no extra bytes at the end of the padding (after h)

### Attack

1. Select an arbitrary message, m
  - Note that this is a total break, can use any message you choose
2. Compute the has of the message, ![latex-e1bd5bb4-2c4c-4007-9a07-b97e4fe06f25](data/lecture24/latex-e1bd5bb4-2c4c-4007-9a07-b97e4fe06f25.png)
3. Let 288 bit string ![latex-3f302bfa-e105-412a-a5e1-9f1d6e2d8200](data/lecture24/latex-3f302bfa-e105-412a-a5e1-9f1d6e2d8200.png)
4. Let ![latex-15f94b10-4b14-4357-b972-562bd0de5664](data/lecture24/latex-15f94b10-4b14-4357-b972-562bd0de5664.png), note that ![latex-19c6e014-496f-4fa8-823c-3139b9eb8833](data/lecture24/latex-19c6e014-496f-4fa8-823c-3139b9eb8833.png)
5. Suppose that ![latex-7dde0ec1-c4fc-45c9-9dea-fc7f451a5bd6](data/lecture24/latex-7dde0ec1-c4fc-45c9-9dea-fc7f451a5bd6.png) (Happens with prob ![latex-ed73f9d1-62bf-4399-ab97-9c6a08635203](data/lecture24/latex-ed73f9d1-62bf-4399-ab97-9c6a08635203.png)
  - IF not, modify m slightly and goto 2
6. Let ![latex-139a2301-fe9f-4f64-bea0-10a5cd9d6a64](data/lecture24/latex-139a2301-fe9f-4f64-bea0-10a5cd9d6a64.png)

#### Prove The claim: The verifier will accept (m, s)

The verifier computes ![latex-40737229-599c-4f48-9263-1637078724fe](data/lecture24/latex-40737229-599c-4f48-9263-1637078724fe.png)
- Note that ![latex-1e97bfb5-d3f8-48be-b4f9-d8348b6db956](data/lecture24/latex-1e97bfb5-d3f8-48be-b4f9-d8348b6db956.png)
![latex-0e244437-84ea-413e-814c-9222a9f7fe05](data/lecture24/latex-0e244437-84ea-413e-814c-9222a9f7fe05.png) (call the last 2 terms garbage)
- ![latex-88cd33c9-a8da-4c1a-9f6f-243818d7e84b](data/lecture24/latex-88cd33c9-a8da-4c1a-9f6f-243818d7e84b.png) dominates the ![latex-11174c8f-5332-4128-b7c6-54bfa2c95e09](data/lecture24/latex-11174c8f-5332-4128-b7c6-54bfa2c95e09.png), thus the garbage is positive
![latex-0b4fbf1f-caac-48c4-9219-c2bc7b718ac9](data/lecture24/latex-0b4fbf1f-caac-48c4-9219-c2bc7b718ac9.png)
- Again the ![latex-cd746caa-e2c7-42b6-a654-9ae1342e411e](data/lecture24/latex-cd746caa-e2c7-42b6-a654-9ae1342e411e.png) term dominates, the the result is positive and ![latex-cdc6d5b0-b7ac-4044-9353-e814b219d59a](data/lecture24/latex-cdc6d5b0-b7ac-4044-9353-e814b219d59a.png)
- Because of this, we can ignore the ![latex-55cbfa1d-11da-42f7-a4ab-beff813b8857](data/lecture24/latex-55cbfa1d-11da-42f7-a4ab-beff813b8857.png), thus the problem looses it's hardness (cube roots are easy to find, cube roots mod n are hard)

![latex-3dd79a77-73d0-49bc-ad17-09c6ae0f08c3](data/lecture24/latex-3dd79a77-73d0-49bc-ad17-09c6ae0f08c3.png)
![latex-2bd45eda-2e55-42ef-9cf7-795edd90d3b7](data/lecture24/latex-2bd45eda-2e55-42ef-9cf7-795edd90d3b7.png)
![latex-3bb9b9b6-ac54-444c-9699-4a68be1ce1f3](data/lecture24/latex-3bb9b9b6-ac54-444c-9699-4a68be1ce1f3.png)

Writing this as a bit string, we can see that left bit shifts are applied
- D is shifted to the right 2072 bits to the left
- Note that 2^{697} - 1 is just a string of 697 1's

3072 bits:

![latex-07022079-2d6f-4a79-b2ea-827947b25554](data/lecture24/latex-07022079-2d6f-4a79-b2ea-827947b25554.png)

![](lecture24.jpg)

## Key Management
- Whatever it takes to support the establishment and maintenace of keys for many users

In practice, you have to manage a huge number of keys to secure all data.
- Recall Google's key management

1. Suppose A wishes to use public key crypto to encrypt a mesage for B: A needs an authentic copy of B's public key
  - Send a confidential email
2. Suppose A recieved a message purportedly signed by B. To verify the signature on the message, A needs an authentic copy of B's public key
  - A person wishes to verify a software update

### Public Key Management
- Where do you get the key, verify it?
- How to do keys with properties?
  - I.e. bank wants to limit the total transaction size of Bob's public key
- What happens if private keys are lost/compromised?
- How can a public key be revoked?

In the real world, public key management is hard.

#### Techniques for distributing

1. point to point delivery
  - trusted courier
  - Hard to implement at scale
2. Direct access to a trusted public file
  - Digitally signed file
3. Use of online trusted servers
4. Offline Certification Authority (CA)

### Certification Authorities
- CA issues certificate that bind an entity's identity and it's public key
- Certification constist of
  - Data part: A's identifiy, public key, and other info (validity info)
  - Signature part: CA's signature of the data part
- B obtains an authentic copy of A's public key
  1. obtain an authentic copy of the CA's public key (shipped in browser or OS)
  2. Obtain CertA over an unsecured channel
  3. verify the CA's signature S on Data
- The trust is now concentrated to trusting the CA's public key
  - The CA doesn't need to know the user's private key
  - The CA must be trusted to not create false certificates

### Public Key Infrastructure (PKI)
- The supporting services (tech, legal, business) that are needed if public key crypto is to be deployed at scale

#### Contains
- Certificate format: Needs to be right at the beginning, very hard to change
- the certification process
- Certificate revocation
  - Warn users not to trust certs anymore
- Trust models
  - Hope the CA did it's job well
- Certificate distribution
- Certificate policy: Details of intended use
- **Certification practice statement (CPS)**: Practices and policies followed by the CA
  - Describes how the CA is liable to you, it they do something wrong

#### Problems
- Interoperability
  - Have standards
- Revoke Certs
- Trust models
- Liability: Whose liable to you, and for how much
  - Business model: Charge users to provide certificates and handle liability


