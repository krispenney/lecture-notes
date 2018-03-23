# Lecture 32 - March 23, 2018

## Quantum Computers
- We know algorithms (Shor) to solve the following public schemes
  - RSA
  - DL
  - ECC
- For symmetric keys, the best is only ![latex-85fde6b8-c63f-48bb-9766-ca6b1fc8e3e3](data/lecture32/latex-85fde6b8-c63f-48bb-9766-ca6b1fc8e3e3.png)
  - Pick 256-bits, then your good

No one knows when quantum computers will become viable to be a true threat.
- How soon do you start to deploy solutions?
  - NSA transition to quantum resistant algorithms (no specified timeline).
    - Current Algorithms
      - Suite B: Unclassified data, sensitive but unclassified data, classified data
        - 2005
          - Public key: ECC, ECDH, ECDSA
          - Security Level: P-256: 128, P-384: 192
          - Hash Functions: SHA-256, SHA-384
          - Symmetric Key: AES-128, AES-256
        - 2010
          - RSA was added: Bit length ![latex-58107c76-4324-43bb-87c6-7e31eae6fcb7](data/lecture32/latex-58107c76-4324-43bb-87c6-7e31eae6fcb7.png)
            - Smaller n picked for efficiency
          - But ECC is preferred
        - 2015
          - RSA -> ECC -> Quantum Safe
          - They recommended waiting to switch to Quantum Safe when they became available (if your on RSA)
            - They likely did this to prepare for Quantum computers (whenever they happen)
          - Drop P-256
          - Increased the RSA n bitlength to ![latex-a5723336-a8ed-4b39-877d-d0e933a19c94](data/lecture32/latex-a5723336-a8ed-4b39-877d-d0e933a19c94.png)
      - Suite A: Top Secret Data

### Quantum Safe Candidates

#### Hash Based Signature Schemes: Lamport-Diffie One time Signature Scheme
- 1979

Ingredients:
- ![latex-e58e2b62-fb93-41e2-86c6-9b9a43a09da8](data/lecture32/latex-e58e2b62-fb93-41e2-86c6-9b9a43a09da8.png) CR Hash function
- ![latex-66e8f428-90f4-479b-9381-a1a12fe42cba](data/lecture32/latex-66e8f428-90f4-479b-9381-a1a12fe42cba.png) PR Hash function

Key generation: Alices does
1. Select ![latex-89a7a7a2-8fd5-4050-a0ec-e128db80f1d7](data/lecture32/latex-89a7a7a2-8fd5-4050-a0ec-e128db80f1d7.png), ![latex-27413598-1457-490b-a92b-20e0e185cb84](data/lecture32/latex-27413598-1457-490b-a92b-20e0e185cb84.png)
2. Compute ![latex-c4cb69a0-df22-4207-82b6-ec36ef13c779](data/lecture32/latex-c4cb69a0-df22-4207-82b6-ec36ef13c779.png), ![latex-e9d78c70-6d0a-46c1-875f-c08b2792fa1a](data/lecture32/latex-e9d78c70-6d0a-46c1-875f-c08b2792fa1a.png)
3. Public Key: ![latex-597fdd33-06f4-4387-a603-92c9c0fa918f](data/lecture32/latex-597fdd33-06f4-4387-a603-92c9c0fa918f.png), Private Key: ![latex-70fcc739-b195-4165-a508-fa688c6f01a6](data/lecture32/latex-70fcc739-b195-4165-a508-fa688c6f01a6.png)

Signature Generation: To sign a message ![latex-f17e0709-fedc-4de4-8084-6c5713b69348](data/lecture32/latex-f17e0709-fedc-4de4-8084-6c5713b69348.png)
1. Compute ![latex-aa5f599e-6e1d-4d12-9cd0-41bbedf992f4](data/lecture32/latex-aa5f599e-6e1d-4d12-9cd0-41bbedf992f4.png), call the bits of h: ![latex-6b2e3fa2-4797-4bea-a1c9-1f783cbef08d](data/lecture32/latex-6b2e3fa2-4797-4bea-a1c9-1f783cbef08d.png)
2. Let ![latex-f17c581b-1d53-420e-bbca-a0745bcdcae1](data/lecture32/latex-f17c581b-1d53-420e-bbca-a0745bcdcae1.png), ![latex-f7cf7ab7-3d5b-45d0-a29f-5c13ce888488](data/lecture32/latex-f7cf7ab7-3d5b-45d0-a29f-5c13ce888488.png)
3. Then the signature on the message M is, ![latex-6262ab28-5ad6-4065-9a68-b23c3a727b2e](data/lecture32/latex-6262ab28-5ad6-4065-9a68-b23c3a727b2e.png)

Signature Verification: Given ![latex-070c4df8-70f4-4c6b-9f98-44c6fc84613d](data/lecture32/latex-070c4df8-70f4-4c6b-9f98-44c6fc84613d.png) Bob does:
1. Bob obtains an authenticated copy of Bob's public key (recall: A vector of the y string pairs)
2. Compute ![latex-002160b1-ac49-4757-9eb0-93970bfdc1ef](data/lecture32/latex-002160b1-ac49-4757-9eb0-93970bfdc1ef.png), As before call the bits of h: ![latex-7bbdcb6b-3567-4d1c-b650-c7018eda68f9](data/lecture32/latex-7bbdcb6b-3567-4d1c-b650-c7018eda68f9.png)
3. Compute ![latex-e1d3d83b-eeea-4160-a0b1-75e1a811f248](data/lecture32/latex-e1d3d83b-eeea-4160-a0b1-75e1a811f248.png), for each i in ![latex-c0c23954-cfc7-4d44-a905-d64e213f6715](data/lecture32/latex-c0c23954-cfc7-4d44-a905-d64e213f6715.png)

In order to forge the signature, you would have to compute pre-images of G, which is in feasible as it is Preimage Resistance.

##### Notes
1. Each signature reveals half of the private key, therefore given enough captured signatures, an attacker can obtain the entire private key
  - Implication: Ideally you only use the key once.
  - **This is a one-time signature scheme**
  - Not Ideal
  - Can be alivieated using Merkel Trees
2. The signature is long
  - It is made up of 256 256-bit strings
3. Need lots of random bits (when generating the private key)
  - If it is not random, then problems
4. Public Keys are also large (256 256-bit strings), ![latex-0f73583a-33ce-4174-829e-c7154e48ff4d](data/lecture32/latex-0f73583a-33ce-4174-829e-c7154e48ff4d.png)
5. Private keys are large, ![latex-360a4e28-86c7-42a8-96cb-bfeef9ef3611](data/lecture32/latex-360a4e28-86c7-42a8-96cb-bfeef9ef3611.png)

##### Why is it secure (Classically)?
- You have a signed message, thus half of the private key is revealed
- Recall that G is preimage resistant, therefore it is infeasible to find the keys
- Recall that H is collision resistant, therefore it is infeasible to find hash values that are the same
