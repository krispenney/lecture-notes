# Lecture 22 - February 28, 2018

**OAEP**: Optimal Asymmetric Encryption Padding

## RSA-OAEP
- Recall salt is added to prevent dictionary attacks
- Chosen ciphertext attack are prevented via the padding
  - The attacker has some valid ciphertext c, they would try to modify it (or create one). Since the random functions are applied it is likely that the resulting plaintext will be garbage.

### Example
- $$G_1(r) = SHA256(1 \mid\mid r) \mid\mid SHA256 (2||r) || SHA256(3 || r) || \ldots

### Notes
1. RSA-OAEP is **plaintext aware**: If any party computes a valid ciphertext ![latex-a1d7c0d4-47cd-494b-a420-a00dd723ac60](data/lecture22/latex-a1d7c0d4-47cd-494b-a420-a00dd723ac60.png), then that party must know the plaintext ![latex-5119e03a-f56f-4cd9-ae8b-59dce8b84a43](data/lecture22/latex-5119e03a-f56f-4cd9-ae8b-59dce8b84a43.png).
  - Just picking ciphertexts are likely to be garbage
  - If you know the plaintext and ciphertext, then there's no point using the decryption oracle
2. **Theorem (Bellare & Rogawey)**:
  - Suppose finding ![latex-0a66d0fa-51d5-40e8-9c2b-0edf7142b8df](data/lecture22/latex-0a66d0fa-51d5-40e8-9c2b-0edf7142b8df.png) roots mod n is hard (RSA relies on this, otherwise you could just find the roots).
  - Suppose ![latex-1c76136e-30ef-42b2-b1ef-5867ab959944](data/lecture22/latex-1c76136e-30ef-42b2-b1ef-5867ab959944.png) are random functions
  - Then RSA-OAEP is **secure** (semantially against chosen-ciphertext attacks against an adversary)
    - Proven using the power of math
    - This is what the QQ browser should have used, not possible to do chosen ciphertext attacks.
3. We *believe* that finding ![latex-cab56ef3-c4de-4926-9519-5bd1c721b4fe](data/lecture22/latex-cab56ef3-c4de-4926-9519-5bd1c721b4fe.png) roots mod n is equally as hard as factoring n
  - We can't prove this
4. In practice ![latex-553ac978-5fe4-4866-9b83-2d5366b14fa4](data/lecture22/latex-553ac978-5fe4-4866-9b83-2d5366b14fa4.png) are pseudorandom functions (i.e. not truely random)

**Problem**: The theorem has no value in practice. As ![latex-02b3f31b-b9f7-4e28-9f1f-f957de70dd47](data/lecture22/latex-02b3f31b-b9f7-4e28-9f1f-f957de70dd47.png) are pseudorandom then the theorem isn't applicable.
- Nonetheless, the theorem does prove security against attackers who treat ![latex-bedb0ca2-7b03-48e6-83e6-6b76ad4ac51e](data/lecture22/latex-bedb0ca2-7b03-48e6-83e6-6b76ad4ac51e.png) as random functions.

In any case, a proof with artifical assumptions is better than no proof at all.
- maybe.....

**Shoup in 2000 discovered that the poof was wrong. Shoup patched the proof**

RSA-OAEP is included in the latest version of TLS 1.3, March 2018.

## Status of Integer Factorization
- Crutial for the security of RSA

### Little-o
![latex-4f0d7fa2-0ebf-4323-8d1b-46d241fe0f7c](data/lecture22/latex-4f0d7fa2-0ebf-4323-8d1b-46d241fe0f7c.png)
- g dominates f as n gets large

### Polynomial Running Time
- ![latex-8ddbaebc-005f-4b87-834b-411672f6c4e1](data/lecture22/latex-8ddbaebc-005f-4b87-834b-411672f6c4e1.png)
- n is input size
- c is a constant

### Exponential
- Not polynomial
- fully exponeital of the form ![latex-f6348887-420e-4482-92b6-ec4b0a08397b](data/lecture22/latex-f6348887-420e-4482-92b6-ec4b0a08397b.png)
- Subexponential: of the form ![latex-198a8b85-b68b-4f61-9c45-8be96ac5abfd](data/lecture22/latex-198a8b85-b68b-4f61-9c45-8be96ac5abfd.png)
  - ![latex-21a893b9-06bf-4ea0-b0a3-5837caabc23a](data/lecture22/latex-21a893b9-06bf-4ea0-b0a3-5837caabc23a.png)

### Trial Division
- Trial divide n by the primes ![latex-e25e4152-8a80-4fe7-8bbf-f4bb0e738e4f](data/lecture22/latex-e25e4152-8a80-4fe7-8bbf-f4bb0e738e4f.png)
- ![latex-34bff862-c56a-49c9-9ee6-47b665031543](data/lecture22/latex-34bff862-c56a-49c9-9ee6-47b665031543.png): not n is not the input size
  - ![latex-41340959-8feb-427e-a2f7-c3d250a322a3](data/lecture22/latex-41340959-8feb-427e-a2f7-c3d250a322a3.png): exponential in the input size

### Subexponential Time
- ![latex-20c2217e-f4da-4f58-99b9-2e1fd08928a0](data/lecture22/latex-20c2217e-f4da-4f58-99b9-2e1fd08928a0.png)
  - Subexponential if ![latex-c05ba68a-c536-4e5c-a7f8-434ae711ece9](data/lecture22/latex-c05ba68a-c536-4e5c-a7f8-434ae711ece9.png)
- ![latex-01cae9f9-0025-459c-882d-83f5d90acf8c](data/lecture22/latex-01cae9f9-0025-459c-882d-83f5d90acf8c.png), polytime
- ![latex-68c3eff5-4165-4ffd-8ac2-5db4c429ec75](data/lecture22/latex-68c3eff5-4165-4ffd-8ac2-5db4c429ec75.png), which is fully exponential

### Special Purpose Factoring
- Slow in general
- But fast if the number is of a special form
- Example: Trial division is fast when the factors are all very small

### General Purpose Methods
- Work on any n
- running times do not deend of any properties of the number being factored
-
