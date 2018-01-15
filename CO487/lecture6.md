# Lecture 6 - January 15, 2018

## New Data Seal (NDS)

### Chosen Plaintext Attack (continued from lecture 5)
- Find the table *k* (mapping of values between ![latex-6f25c961-96e2-4721-87bc-000ef218dad3](data/lecture6/latex-6f25c961-96e2-4721-87bc-000ef218dad3.png) to function values)

Foreach $$r \epsilon {0, 1}^8 do:
- Pick *u* and obtain ![latex-d1ed6a2f-37b4-468c-98b2-499f76ba9a24](data/lecture6/latex-d1ed6a2f-37b4-468c-98b2-499f76ba9a24.png)
- For each possible byte *t*, check if ![latex-a6ff34e3-fded-4890-b490-1bb4946297c8](data/lecture6/latex-a6ff34e3-fded-4890-b490-1bb4946297c8.png)
  - obtain the encryption ![latex-92efcd1e-bba6-47a8-bd8d-5b3cf706dca2](data/lecture6/latex-92efcd1e-bba6-47a8-bd8d-5b3cf706dca2.png)
  - Check if the guess is correct (i.e. ![latex-b8254db5-fb13-4ce4-93c7-00b831c5af79](data/lecture6/latex-b8254db5-fb13-4ce4-93c7-00b831c5af79.png))

Note that the total number of chosen plaintexts is ![latex-4aec5f2e-f3a0-4eaf-839e-8837fd5e6d42](data/lecture6/latex-4aec5f2e-f3a0-4eaf-839e-8837fd5e6d42.png)
- Alternatevly, the expected number of chosen plaintexts is ![latex-be42f9a0-f4b0-4209-8580-94bcc561948c](data/lecture6/latex-be42f9a0-f4b0-4209-8580-94bcc561948c.png), in this case randomly guess *t*'s, on average you'll need to guess half of them.
- **Excercise**: Modify the attack so that the number of chosen plaintexts is ![latex-ff833d71-e25f-4755-b4f6-6f76b1d57718](data/lecture6/latex-ff833d71-e25f-4755-b4f6-6f76b1d57718.png). This approach check each bit of *t*.
  - Make reasonable assumptions about ![latex-19af6c3c-98c3-4884-8b3c-eec66a511853](data/lecture6/latex-19af6c3c-98c3-4884-8b3c-eec66a511853.png) (substitution functions)
- **Harder Excercise**: Reduce this to 556 chosen plaintexts.

Is this feasible?
- Note that Alice and Bob probably aren't real people, think devices.
- Try to get a secret key off of someone's computer, automate the generation of ciphertexts.

## Data Encryption Standard (DES)
- Designed by IBM mid-70's
- US government and banking standard.
- Falling out of use.
- 16-round Feistel ladder.
  - Made use of subkeys, each round in the ladder uses a different key.
  - Avoids the attack of NDS.
- Designed with hardware in mind.

### Problem 1
The key size is too small (only 56-bits).

### Problem 2
The block size is too small.
- Example: Imagine encrypting a large file, on average collisions will occur after about ![latex-d10b85ce-9a40-49b0-af67-07c3e5b7ec5e](data/lecture6/latex-d10b85ce-9a40-49b0-af67-07c3e5b7ec5e.png) blocks.
  - An attacker can examine the blocks and look for repeats.

### Sophisticated Attacks on DES

1. Differential Cryptanalysis
  - Not practical because of key rotation, would be able to obtain enough `(m, c)` pairs
2. Linear Cryptanalysis
  - Requires fewer `(m, c)` pairs.
  - Key rotation still a problem

## Multiple Encrpytion
- Since DES was implemented in hardware, it made it more difficult to switch away from.
- Goal was to find a way to use DES, without upgrading hardware.
- Solution: Re-Encrypt ciphertext one or more times. Hope that this increases the effective key length.
- Doesn't always result in a better ciphertext.

## Double DES
- Run DES twice, with 2 keys.
- ![latex-a4080f8b-08ab-485a-b5fa-4d80b7b3c68e](data/lecture6/latex-a4080f8b-08ab-485a-b5fa-4d80b7b3c68e.png), 2 56-bit keys.
- Encryption: ![latex-e09a9efd-fff3-4cc0-a25a-b32c78aaf4f7](data/lecture6/latex-e09a9efd-fff3-4cc0-a25a-b32c78aaf4f7.png)
- Decryption: ![latex-8230dfa1-3bd5-49b1-b2cc-a215beb8a775](data/lecture6/latex-8230dfa1-3bd5-49b1-b2cc-a215beb8a775.png)

### Problem: Meet in the middle attack
![latex-e3d54b50-78af-47a4-8158-b356eb26d9a5](data/lecture6/latex-e3d54b50-78af-47a4-8158-b356eb26d9a5.png)

Generate a guesses ![latex-95aeaae5-0067-4ff0-9ab0-bd88aa1d9c95](data/lecture6/latex-95aeaae5-0067-4ff0-9ab0-bd88aa1d9c95.png) for ![latex-52106325-22de-4b06-bccb-a832a5858879](data/lecture6/latex-52106325-22de-4b06-bccb-a832a5858879.png), apply ![latex-dbea4436-773f-4767-b0ec-c5b7f1293d1e](data/lecture6/latex-dbea4436-773f-4767-b0ec-c5b7f1293d1e.png) to *c*, Store them in a table.
Do the same for ![latex-b0c933db-93b7-40a5-9e83-061182145574](data/lecture6/latex-b0c933db-93b7-40a5-9e83-061182145574.png), see if there are any matching pairs. For each match, compare to the other pairs.
- If it is a match for both, then it is a match with high probability.
- If not, then it is not a match.
