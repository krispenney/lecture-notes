# Lecture 20 - February 16, 2018

## RSA
Note that to avoid collisions, make sure m is strictly less than n. Avoid mod n information loss.

### Key Generation

- Alice's Public Key: ![latex-2aa865ce-921c-43ab-8b1c-e824f408adfb](data/lecture20/latex-2aa865ce-921c-43ab-8b1c-e824f408adfb.png)
- Alice's Private Key: ![latex-b2c05e75-8f6a-4144-8361-f918a4b7b6fd](data/lecture20/latex-b2c05e75-8f6a-4144-8361-f918a4b7b6fd.png)
- Encryption: ![latex-21a2ff41-762d-4ca3-bc2b-10e09ee17424](data/lecture20/latex-21a2ff41-762d-4ca3-bc2b-10e09ee17424.png)
- decryption: ![latex-65e45604-3d30-4298-9e17-eb4648662d21](data/lecture20/latex-65e45604-3d30-4298-9e17-eb4648662d21.png)
- ![latex-f02a23ea-78d3-46b3-ada0-7a6e0edf9edb](data/lecture20/latex-f02a23ea-78d3-46b3-ada0-7a6e0edf9edb.png)
- ![latex-cf455253-876a-4684-9635-b1d82552839e](data/lecture20/latex-cf455253-876a-4684-9635-b1d82552839e.png)
  - ![latex-d2416830-e8d5-446c-b6a3-838be1f9eed6](data/lecture20/latex-d2416830-e8d5-446c-b6a3-838be1f9eed6.png), ![latex-39670662-f408-43da-8b11-90f3b7d05003](data/lecture20/latex-39670662-f408-43da-8b11-90f3b7d05003.png)

### Security

1. If Eve can factor ![latex-3775e05a-293d-41b4-bb3c-458ea39033aa](data/lecture20/latex-3775e05a-293d-41b4-bb3c-458ea39033aa.png)n, then Eve can compute ![latex-e28f9c8a-1519-4074-8c6b-657cbe1e89ae](data/lecture20/latex-e28f9c8a-1519-4074-8c6b-657cbe1e89ae.png) efficiently, and thus totally break RSA. So, hardness of factoring ![latex-fcfd08cf-07f3-4246-a67f-c070aca1970b](data/lecture20/latex-fcfd08cf-07f3-4246-a67f-c070aca1970b.png) is *necessary* for RSA security.
2. **Fact**: Computing ![latex-21603ea8-d0fb-4a85-86b5-5c71c22c429e](data/lecture20/latex-21603ea8-d0fb-4a85-86b5-5c71c22c429e.png) from ![latex-bae28013-5b9b-47b3-8307-d842c671d54b](data/lecture20/latex-bae28013-5b9b-47b3-8307-d842c671d54b.png) is *equivalent* to factoring ![latex-ed99ba93-a840-4594-9dd6-12dc8684c353](data/lecture20/latex-ed99ba93-a840-4594-9dd6-12dc8684c353.png).
3. The probem of finding ![latex-9ea2c0eb-f592-47a6-b592-997c5bedf7f8](data/lecture20/latex-9ea2c0eb-f592-47a6-b592-997c5bedf7f8.png) root modulo ![latex-772c81ad-d088-41cb-8807-fc1260e1f4ac](data/lecture20/latex-772c81ad-d088-41cb-8807-fc1260e1f4ac.png) (the "RSA problem"). Which must be hard if RSA encryption is to be secure.
4. It is **believed** that finding ![latex-aabea236-22c8-49e7-829e-b147654b7a0e](data/lecture20/latex-aabea236-22c8-49e7-829e-b147654b7a0e.png) roots mod n is equivalent to factoring n. So, hardness of the RSA problem is **necessary** for security of RSA encryption.
  - Very important to note that this is a belief.
5. RSA encryption as described above is **insecure**
  - See below

#### Attacks

##### Dictionary Attack
Suppose that the plaintext message, m, belongs to a small and easily predictable set of messages
- Encrypt all possible m's in the message space, when the ciphertext matches, know the plaintext.
- simply lookup ciphertexts in the table

###### Salting
This attack can be defended against by appending a random string to the start (or end) of the plaintext, before encrypting. This is called **a salt**.

##### Chosen Ciphertext Attacks
- The attacker (Eve) has a decryption oracle available
- Eve is given a challenge ciphertext which she has to decrypt
- Any ciphertext can be decrypted, except c.
- **Goal**: Learn something about the plaintext for c.
  - Other than it's length

**Attack**: Select ![latex-8a1d1a03-36a2-495b-8c6e-82896168ff4f](data/lecture20/latex-8a1d1a03-36a2-495b-8c6e-82896168ff4f.png) with ![latex-3bd19516-b4bf-4088-8ec1-1c5dfb409035](data/lecture20/latex-3bd19516-b4bf-4088-8ec1-1c5dfb409035.png)
- **Note**: If ![latex-aa557c92-f6e3-44d5-8452-d2414230e011](data/lecture20/latex-aa557c92-f6e3-44d5-8452-d2414230e011.png), then *stop*. You have factored n and totally broken the encryption.
- Compute ![latex-dce84db0-de7b-436c-944f-4c5a86121af2](data/lecture20/latex-dce84db0-de7b-436c-944f-4c5a86121af2.png), where ![latex-209db30b-0890-4e58-a873-1dc1db2aa64b](data/lecture20/latex-209db30b-0890-4e58-a873-1dc1db2aa64b.png)
- Give ![latex-5ac67ac4-58d1-4e82-ac9e-8d8d2b639afe](data/lecture20/latex-5ac67ac4-58d1-4e82-ac9e-8d8d2b639afe.png) to the decryption oracle, and obtain ![latex-e7595f88-6d0b-4f3e-b862-1f6dbe314e9b](data/lecture20/latex-e7595f88-6d0b-4f3e-b862-1f6dbe314e9b.png)
- **Note**: That ![latex-c136f246-a8ac-4d50-b0c3-c7e9448c54e4](data/lecture20/latex-c136f246-a8ac-4d50-b0c3-c7e9448c54e4.png)
- Compute ![latex-0c751df7-473f-4855-ae74-ce9f2aeaaf31](data/lecture20/latex-0c751df7-473f-4855-ae74-ce9f2aeaaf31.png)

###### Are these attacks feasible?
- Chinese mobile browser case study
- browsers track users, where they are, and what they are doing
- QQ browsers WUP encryption
  - Randomly generate a 128-bit AES session key $$k = i || j$
  - Encrypt k with the server's RSA public key
  - encrypt m using AES-ECB
  - send ![latex-8fcc8a9c-7ad2-414e-81d8-da457a3f7770](data/lecture20/latex-8fcc8a9c-7ad2-414e-81d8-da457a3f7770.png) to the server
- Server decrypts:
  - uses it's RSA private key to decrypt ![latex-f59c6b15-e2bf-4faf-a555-c102cce0562b](data/lecture20/latex-f59c6b15-e2bf-4faf-a555-c102cce0562b.png) to get k
  - Use k to decrypt ![latex-7ec9ed63-b862-4351-a4c0-d7d7a1dc8e08](data/lecture20/latex-7ec9ed63-b862-4351-a4c0-d7d7a1dc8e08.png)

**problem**: ![latex-88e3a488-b07c-426b-be04-2b1d0c3e5eaf](data/lecture20/latex-88e3a488-b07c-426b-be04-2b1d0c3e5eaf.png), n is 128-bits, meaning p and q are 64-bit, which is feasible to compute.
- The same ![latex-dc81d674-7ccb-4aa4-bd02-5feedc54872d](data/lecture20/latex-dc81d674-7ccb-4aa4-bd02-5feedc54872d.png) was embedded in 500-million cell phones.
- The number of possible k's is ![latex-e0d1941a-d51d-4662-8f42-a6cc3b2336a9](data/lecture20/latex-e0d1941a-d51d-4662-8f42-a6cc3b2336a9.png)
- ECB mode is also bad
- no authentication
-
