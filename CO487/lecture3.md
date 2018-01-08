# Lecture 3 - January 8, 2018

## Symmetric Key Encryption Scheme
- Alice and Bob communicate some secret key over a secure channel
- Can use the key to encrypt / decrypt communications

### When is it secure?
When it is semantically secure against chosen plaintext attack by a computationally bounded adversary.

### One Time Pad
A key is a random string of letters that is at least as long as the message.
- This is secure, given a cyphertext, no matter how much computation you do, you can't derive any other information abount the plaintext. Only it's length.
- **Problem**: You can only use the key a single time. Example: XOR-ing 2 cyphertexts that have been encrypted with the same key produce the XOR-ed plaintexts.

### Stream Cipher
Secret key is now the seed to a psuedo-random number generator (PRBG).
- **Problem**: No longer perfectly secret, depends on the properties of the PRBG.

Requirements:
- The keystream must look like a random string
- If an adversary knows part of a plaintext and a corresponding cyphertext, then XOR-ing them together will yeild part of the keystream. This could potentially be usful to help generate the remainder, thus breaking the encryption.

**Note**:
- Don't use UNIX random number generators (`rand`, `srand`) for cryptographic purposes. Can predict once the seed is known.

### RC4
Very popular stream cipher.

Pro:
- Simple
- Fast
- variable key size
- no terrible weaknesses found

Cons:
- Design criteria are proprietary

**Key scheduling algorithm**
- Example: Key is 128-bits or 16 bytes long (i.e. ![latex-6af92097-94bd-476b-b09b-ae48ea199abc](data/lecture3/latex-6af92097-94bd-476b-b09b-ae48ea199abc.png)).
- ![latex-af97b2f9-5c45-47f2-a808-4ada1c4295c2](data/lecture3/latex-af97b2f9-5c45-47f2-a808-4ada1c4295c2.png) is just the secret key, repeated enough times to fill the array (256 bits)
- Iterate over the repeated key and S, perform 256 swaps to produce the a random looking permutation of ![latex-198a6f9f-2b60-4a2c-a4c5-efb0ad3d93e7](data/lecture3/latex-198a6f9f-2b60-4a2c-a4c5-efb0ad3d93e7.png)

**Keystream generator**
- For each byte of the plaintext, select a keystream byte (see slides), XOR with the plaintext.
- The keystream should only every be used once.
  - This is hard to achieve in practice, collisions are likely when sending many messages.

### Wireless Security
WI-FI introduced many new security concerns.
- More attack opportunities (no physical access)
- Far distance.
- No trace that you broke in.

**WEP** == Wired Equivalent Privacy
- Only protects from the client devices to the access points.

**Goals**:
  1. Confidentiality: prevent eavesdropping
  2. Data Integrity: Prevent tampering
    - This has been broken
  3. Access Control: Protect access
    - Throw away packets that aren't correctly encrypted / formatted

**Protocol**:
- Key size either 40 or 104 bits long
  - 2 keys because of US government regulation on crypto
- Mobile station needs to share key with access point
  - Everyone on the network uses the same secret key.
- Messages are divided into packets of some fixed length
- Select a 24-bit Initialization Vector (IV)
  - Meaning every packet would have a separate secret key.
  - Either random or The IV is set to 0 and incremented by 1.
    - Bad because the IV is short, only ![latex-68c73d12-75d4-4f03-8f49-ed24758afce6](data/lecture3/latex-68c73d12-75d4-4f03-8f49-ed24758afce6.png) possibilities, eventually collisions.
- `CRC` is the checksum function, allows use to tell if a packet has been tampered with.

**Does it achieve it's goals / is it secure?**
- Many attacks have been found, breaking WEP.

**IV Collisions**
- On a high traffic network, since the IV is only ![latex-e5f350aa-5c49-4f9e-978a-716a0be4e4dd](data/lecture3/latex-e5f350aa-5c49-4f9e-978a-716a0be4e4dd.png) bits long, eventually they will collide.
- Counter actually provides better repition than random selection -> birthday paradox ![latex-22695118-cc28-4006-8dad-abb58ba9a449](data/lecture3/latex-22695118-cc28-4006-8dad-abb58ba9a449.png) packets for a collision.
- Then it is possible to XOR to ciphertext's together to get their plaintexts.
- Doesn't totally break things, doesn't reveal the secret key.

**Checksum is linear**
- Attack on data integrity
- The attacker can create a delta vector and calculate it's checksum, XOR-ing this with the ciphertext (and it's checksum) a valid message with changes

Proof ![latex-4982febf-57f9-4a22-851a-2775b6398fb1](data/lecture3/latex-4982febf-57f9-4a22-851a-2775b6398fb1.png) will be accepted:

![latex-a3440ed6-f7e5-47b3-ab28-c689ed13bdcd](data/lecture3/latex-a3440ed6-f7e5-47b3-ab28-c689ed13bdcd.png)$$$$
c' = c + (\delta || CRC(\delta)) = RC4=(v||k) + (m||S) | (\delta || CRC(\delta)) \
\implies RC4(v || k) + (m + \delta || CRC(m) + CRC(\delta)) \
\implies RC4(v || k) + (m + \delta || CRC(m + \delta)) \
\implies RC4(v || k) + (m' || CRC(m + \delta)) \
\therefore RC4(v || k) + (m' || CRC(m'))
![latex-977da3f6-0ab4-4a4c-bd5a-0aa20f3df8fd](data/lecture3/latex-977da3f6-0ab4-4a4c-bd5a-0aa20f3df8fd.png)$$$$

**Integrity function is unkeyed**
- Attack on access control
- Suppose an attacker learns the plaintext corresponding to a single encrypted packet ![latex-c78507d7-510f-40f8-86b3-76c640ef98e3](data/lecture3/latex-c78507d7-510f-40f8-86b3-76c640ef98e3.png)
- Then, the attacker can compute the RC4 keystream.
- The attacker can compute a valid encrypted packet for any plaintext `m'`
