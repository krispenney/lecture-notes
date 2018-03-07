# Midterm Notes

## Fundamental goals of Crypto

1. Confidentiality: Keep data secret from all but those who are authorized to access it.
2. Data integrity: Ensuring data has not been altered by unauthorized parties.
3. Data Origin Authentication: Corroborating the source of data
4. Non-Repudiation: Preventing an entity from denying previous actions or commitments

## Attacks

### Assumptions of Adversary

- Information theoretic security: The adversary has infinite computational resources
- Complexity-theoretic security: The adversary has a "polynomial time turing machine"
- Computational Security: The adversary has 10,000 Intel Xeon CPUs.

### Goal of the Adversary

1. Recover the secret key
2. Systematically uncover plaintext from ciphertexts
  - May not actually need/have the secret key to accomplish this.
3. Learn some partial information about the plaintext (other than it's length)

If an adversary can achieve **1 or 2**, then the encryption scheme is said to be totally insecure.

If the adversary cannot learn any partial information about the plaintext from the ciphertext, then the encryption scheme is said to be semantically secure.

### Passive

- Ciphertext only attack: The adversary knows some cipher text
- Known plaintext attack: The adversary knows some plaintext, ciphertext pairs.

### Active

- The adversary can choose some plaintexts to be encrypted and obtain the ciphertext (via some oracle).

## Symmetric Key Encryption Scheme
- A symmetric key encryption scheme is said to be secure if it is semantically secure against chosen-plaintext attacks by a computationally bounded adversary.

To break a symmetric key encryption scheme, the adversary must accomplish:
1. The adversary is given a challenge ciphertext
2. The adversary can select plaintexts and can obtain the ciphertext from the oracle.
3. After a feasible amount of computation, the adversary obtains some information about the plaintext corresponding to the ciphertext.

### Desirable Properties

1. Efficient algorithms should be known for computing ![latex-90c43c8f-274a-4465-be42-dae1796d8029](data/midterm/latex-90c43c8f-274a-4465-be42-dae1796d8029.png) and ![latex-6d0a13fd-b2f7-4a27-a668-f7cfc5b07173](data/midterm/latex-6d0a13fd-b2f7-4a27-a668-f7cfc5b07173.png)
2. The secret key should be small, but large enough to prevent exhaustive key search.
  - Note that ![latex-66ca56e0-968b-4397-b3e9-1edab95f1dac](data/midterm/latex-66ca56e0-968b-4397-b3e9-1edab95f1dac.png) operations is considered infeasible.
3. The encryption scheme should be secure.
4. The scheme should be secure against even the designer of the system.

## Security Levels

A cryptographic scheme is said to have a security level of l bits if the fastest known attack can be performed in ![latex-1ec86575-20ff-453b-83a4-7647d073d683](data/midterm/latex-1ec86575-20ff-453b-83a4-7647d073d683.png) bits.
- A security level of at least 128 bits is desired in practice.

## Stream Ciphers

Use a pseudorandom bit generator (PRBG) to generate "random" keystream bits.
- The seed for the PRBG is the secret key between Alice and Bob.
- The security depends on the quality of the PRBG

### Security requirements of the PRBG
- The keystream should be indistinguishible from a random sequence (the **indistinguishability requirement**)
- **Unpredictibility Requirement**: Given portions of the keystream, an adversary should not be able to learn anything about the rest of the keystream.

## RC4 Stream Cipher

### Key Scheduling Algorithm

Given the secret key, generate a random looking permutation of ![latex-aaf6c9ee-f231-4bc1-86b3-8db0fe026a26](data/midterm/latex-aaf6c9ee-f231-4bc1-86b3-8db0fe026a26.png).

### Keystream Generator

Given the random permutation (from the scheduler), generate keystream bytes. The keystream bytes are then XOR-ed with plaintext blocks.

## WEP (Wired Equivalent Privacy)

1. Confidentiality: Prevent Eavesdropping
  - RC4 is used for encryption
2. Data Integrity: Prevent tampering with transmitted messages
  - Integriy checksum is used
3. Access control: Protect access to wireless network infrastructure
  - Discard all packets that are not properly encrypted using WEP

The mobile client shares an either 40-bit or 104-bit secret key with the access point. Messages are divided into packets of some fixed length.

Each packet uses a per-packet 24 bit initialization vector, the standard does not specify how IVs are managed
- A random IV is generated for each packet
- The IV starts at 0 and is incremented by 1 for each use (counter)

### Protocol

#### Client side

1. Select 24-bit IV
2. Compute a 32-bit checksum, ![latex-f51a2319-770f-4716-bd68-da3b83281dc0](data/midterm/latex-f51a2319-770f-4716-bd68-da3b83281dc0.png)
3. Compute ![latex-6df432b3-8411-4ee2-9c7b-6bd14fdbd6c0](data/midterm/latex-6df432b3-8411-4ee2-9c7b-6bd14fdbd6c0.png)
4. Send ![latex-0cffa100-cba2-4033-ac0a-548811b2512c](data/midterm/latex-0cffa100-cba2-4033-ac0a-548811b2512c.png) over the wireless channel.

#### Reciever

1. Compute ![latex-0d6f8e84-e49e-441c-afff-4dcaa6b25d63](data/midterm/latex-0d6f8e84-e49e-441c-afff-4dcaa6b25d63.png)
2. Compute ![latex-d0655c25-69f8-4958-a263-b01166100e63](data/midterm/latex-d0655c25-69f8-4958-a263-b01166100e63.png), reject packet if ![latex-360d6d71-95bf-4b2f-9eb1-3e4e93b82126](data/midterm/latex-360d6d71-95bf-4b2f-9eb1-3e4e93b82126.png)

#### Problems

##### IV Collisions
**WEP doesn't provide a high degree of confidentiality**

There's only ![latex-7ece7144-0789-4ebc-9b36-fc301758b950](data/midterm/latex-7ece7144-0789-4ebc-9b36-fc301758b950.png) possible IVs, eventually they will be repeated.
- then all encrypted packets contain ![latex-b72a2cdc-c325-4ad3-8c98-c7f43c17912b](data/midterm/latex-b72a2cdc-c325-4ad3-8c98-c7f43c17912b.png), can XOR them together, if either plaintext is known the plaintext can be extracted.

By the birthday paradox, if IVs are randomly expected then a collision should be expected after ![latex-3b5c5656-66e9-4454-ba62-e83815720509](data/midterm/latex-3b5c5656-66e9-4454-ba62-e83815720509.png)

##### Linear Checksum
**WEP does not provide data integrity**

It's possible to make controlled changes to encrypted packets, that are still valid.

##### Integrity function is unkeyed
**WEP does not provide access control**

If an attacker can obtain the plaintext of some encrypted packet ![latex-313ff7d3-1a27-41aa-98e9-daeb7fb2c4ee](data/midterm/latex-313ff7d3-1a27-41aa-98e9-daeb7fb2c4ee.png), then they can compute:
![latex-13d141c2-dbc1-4220-aedf-04b5b3d1d276](data/midterm/latex-13d141c2-dbc1-4220-aedf-04b5b3d1d276.png)
Therefore, the attacker can compute a valid encrypted packet for any message of their choice.

## WPA

- Uses a master key from which 128 bit session keys are periodically generated
- session key combined with 48-bit IV to form the RC4 key.
- A Message Authentication Code (MAC) algorithm is used instead of CRC.

## WPA-2

- Uses AES instead of RC4

## Block Ciphers

A block ciphers is a SKES the breaks of the plaintext into blocks of fixed length and encrypts it one block at a time.
- in Contrast, a stream cipher encrypts the plaintext one bit at a time.

### Desirable Properties of Block Ciphers

#### Security
- Diffusion: each ciphertext bit should depend on all of the plaintext bits
- Confusion: the relationship between key and ciphertext bits should be complicated
- Key length: should be small, but large enough to guard against exhaustive key search.

#### Efficiency
- Simplicity: Easy to implement and analyze
- high encryption and decryption rate
- Suitability for hardware or software

### Feistel Ciphers
- Block length n
- h rounds
- l: key length
- M is 2 blocks
- A key scheduling algorithm is used to determine subkeys for each round.
- **Encryption**: ![latex-64d73a79-cf46-4255-868c-585556fa7f37](data/midterm/latex-64d73a79-cf46-4255-868c-585556fa7f37.png)
- **Decryption**: ![latex-3bc0a1cd-42ee-49a1-8c92-64ad418da79a](data/midterm/latex-3bc0a1cd-42ee-49a1-8c92-64ad418da79a.png)

### New Data Seal (NDS)
- n = 64, h = 16
- key maps 8 bits to 8 bits
  - ![latex-aca56a97-b65f-4615-9ce9-f5ad94c3a501](data/midterm/latex-aca56a97-b65f-4615-9ce9-f5ad94c3a501.png) possible keys
  - 256 slots in the array, each with a value of 256

#### Chosen plaintext attack
- Can obtain the secret key after 32,000 plaintexts
- Try to bruteforce the value for k(r)

### Data Encryption Standard (DES)
- Feistel cipher: n=32, h=16, l=56
- Using the secret key, selects 16 48 bit subkeys
- S-Boxes: Security of DES depends on their choice

#### Problems
- Exhaustive key search is feasible (![latex-fa11fb75-6bb5-4ec3-8829-a373c092965f](data/midterm/latex-fa11fb75-6bb5-4ec3-8829-a373c092965f.png) steps) and can be easily parallelized
- If plaintext blocks are distributed uniform random, then by birthday paradox the expected number of encrypted blocks before a collision occurs is ![latex-49df2739-a34e-4b06-9008-6cdbbdee8718](data/midterm/latex-49df2739-a34e-4b06-9008-6cdbbdee8718.png)

#### Double DES meet in the middle attack
- foreach possible ![latex-54d08ab7-2cf2-4c26-8616-55991e128292](data/midterm/latex-54d08ab7-2cf2-4c26-8616-55991e128292.png), perform 1 round of DES decryption, save results in a table.
- foreach possible ![latex-489b92be-0126-4455-a09d-890055d3d8d1](data/midterm/latex-489b92be-0126-4455-a09d-890055d3d8d1.png), encrypt the plaintext see if the result is in the table
  - IF it is, check the other 2 plaintext, ciphertext pairs
  - IF not, it's not correct, move on.

### Electronic Cookbook Mode (ECB)
- Encrypt blocks independently, one at a time
- ![latex-e9973666-f37b-4a40-96c5-0705ca135973](data/midterm/latex-e9973666-f37b-4a40-96c5-0705ca135973.png)
- **Problem**: IDentical plaintext blocks produce identical ciphertext blocks.

### Cipher Block Chaining Mode (CBC)
- ![latex-609f2ef5-b83e-4122-997f-e07958136d30](data/midterm/latex-609f2ef5-b83e-4122-997f-e07958136d30.png)
- ![latex-904302ce-1a1d-4509-a97e-1489beaa8861](data/midterm/latex-904302ce-1a1d-4509-a97e-1489beaa8861.png) is a random non-secret IV.
- Each ciphertext block feeds into the next.

## Hash Functions
- Map inputs of arbitrary bit length to a fixed length, n.
- H can be efficiently computed for any length

### Properties of Hash functions

#### Preimage resistance
- Given a hash value y, it is not computationally feasible to find an x such that ![latex-03d84911-50ce-40f6-9d33-d9f39ee9d01f](data/midterm/latex-03d84911-50ce-40f6-9d33-d9f39ee9d01f.png)
- x is called a preimage of y
- **Application**: Password protected systems, store (user id, H(password)) in db.

#### 2nd Preimage Resistance
- Given an input x (and it's hash value), it is computationally infeasible to find an ![latex-e00dfb62-f579-46fe-9bf2-51c5ba26f4b4](data/midterm/latex-e00dfb62-f579-46fe-9bf2-51c5ba26f4b4.png) such that ![latex-74b545d8-5d81-41a9-a4de-4efc32c1cce2](data/midterm/latex-74b545d8-5d81-41a9-a4de-4efc32c1cce2.png)
- **Application**: Modification detection codes, prevent a message m from being modified by unauthorized means.

#### Collision Resistance
- It is computationally infeasible to find two distinct inputs ![latex-32fcd8a8-b0c4-414f-a909-3e4f4fa903a2](data/midterm/latex-32fcd8a8-b0c4-414f-a909-3e4f4fa903a2.png) such that ![latex-5a8e8f7c-7c11-47e9-9379-f829ba567df8](data/midterm/latex-5a8e8f7c-7c11-47e9-9379-f829ba567df8.png)
- **Application**: Message digests for digital signature schemes, if collisions exist, Alice could sign x but actually send x'.

#### Relationships between properties

Collision resistance implies 2nd preimage resistance
- Proof: Suppose H is not 2nd preimage resistant. Then, given an input x it is computationally feasible to find a distinct input x' such that ![latex-64d889b4-c068-45f8-a764-bafc5726a88f](data/midterm/latex-64d889b4-c068-45f8-a764-bafc5726a88f.png).
  - (x, x') is a collision, meaning H is not Collision resistant.
  - Therefore, if H is collision resistant, then it is 2nd preimage resistant.

2nd preimage resistance does not guarantee Collision resistance.
- Proof: Hash function where H(1) = H(0), can't find 2nd preimage given (potentially any) x, but easy to find a collision.

Collision Resistance does not guarantee preimage resistance.

### Hash Function Terminology

- A preimage resistant hash function is called a One Way Hash Function (OWHF)
- A hash function that is both preimage resistant and collision resistant is called **a cryptographic hash function**

### Generic Attacks on Hash functions
- A generic attack does not exploit the properties of any particular hash function
- For analysis purposes, H is viewed as a random function (however this isn't the case in practice)

#### Generic attack to find preimages
- Given a hash value y, select arbitrary inputs x until ![latex-eebd8edb-f346-42a8-ae87-8402c49a928a](data/midterm/latex-eebd8edb-f346-42a8-ae87-8402c49a928a.png)
- Brute force
- Expected number of hash evaluations: ![latex-53f98bf6-0f6a-43d2-b13b-2eefa49ca8c0](data/midterm/latex-53f98bf6-0f6a-43d2-b13b-2eefa49ca8c0.png)
- **This is the optimal generic attack for finding preimages**

#### Generic Attack to find Collisions
- Select arbitrary inputs x, insert into a table ![latex-13fa36e8-090b-4231-aebf-24e50364f6ec](data/midterm/latex-13fa36e8-090b-4231-aebf-24e50364f6ec.png) (sorted by the hash value)
- Repeat until you find x' such that ![latex-c1a52fba-6f8c-40b7-ba82-2754a6817d34](data/midterm/latex-c1a52fba-6f8c-40b7-ba82-2754a6817d34.png) is in the table, with a distinct x.
- Expected number of evaluations ![latex-c92dac2f-eef5-4010-ab13-deb50f03f2ab](data/midterm/latex-c92dac2f-eef5-4010-ab13-deb50f03f2ab.png), by birthday paradox.
  - Expected space requirements is ![latex-77602d3c-1057-4e63-b6d8-4f31c0d197f1](data/midterm/latex-77602d3c-1057-4e63-b6d8-4f31c0d197f1.png)
- This attack is infeasible if ![latex-9f84cab2-8b2f-4d78-93d4-35a51737f052](data/midterm/latex-9f84cab2-8b2f-4d78-93d4-35a51737f052.png)
- This attack is optimal in terms of hash function evaluations.

#### VW Parallel Collision Search
This attack is easily parallizable and can be modified to find meaningful collisions.

- A more efficient implementation of the generic birthday attack, hash neglidible space requirements.
- Only need to store **distinguished points**, points with some easily testable property.
  - ex. A point is distinguished if the 32 most significant bits are 0s.
- Compute the sequence of hash values, store the distinguished points in a table
- If you see the same distinguished point again, you know that you have found a loop in the sequence from values b to d.
- Compute hash values forward from b, backward from d until the collision is found

##### Parallizable
- Can be computed in parallel
- Each thread has a different starting point in the sequence
- When results are combined, if a distinguished point has already been seen then the collision exists.

### Davies-Meyer (Based on Block Ciphers)
- m-bit block size
- Break up ![latex-15166fdc-eded-4c44-9618-5959de1a4cd5](data/midterm/latex-15166fdc-eded-4c44-9618-5959de1a4cd5.png) into t m-bit blocks (pad with 0s)
- ![latex-a2caa332-f6bf-4556-a2c7-4678309a7451](data/midterm/latex-a2caa332-f6bf-4556-a2c7-4678309a7451.png)
- ![latex-503e13e9-a332-4cee-bcca-d7e580d9afcb](data/midterm/latex-503e13e9-a332-4cee-bcca-d7e580d9afcb.png)
- ![latex-7f8afc62-cb5e-4fed-9444-dc6d2dc06f43](data/midterm/latex-7f8afc62-cb5e-4fed-9444-dc6d2dc06f43.png)
- ![latex-328ab7bc-0bec-441d-884d-4a2d767e4729](data/midterm/latex-328ab7bc-0bec-441d-884d-4a2d767e4729.png)

### Iterated Hash Function (Merkel Meta-Method)
- n-bit IV
- n+r-bit -> n-bit compression function.
- break up x into t r-bit blocks
  - ![latex-ccd30490-91ae-4fca-961a-1b6915a507d9](data/midterm/latex-ccd30490-91ae-4fca-961a-1b6915a507d9.png) is defined to be a length block
- ![latex-82c65f4d-55dd-4b45-a995-8aef7954d777](data/midterm/latex-82c65f4d-55dd-4b45-a995-8aef7954d777.png)
- ![latex-c3d6db1f-250f-4b41-a069-fd3609415c97](data/midterm/latex-c3d6db1f-250f-4b41-a069-fd3609415c97.png) for i > 0
- ![latex-bc7fbb8c-186a-4939-8a2b-b07a2af13aa6](data/midterm/latex-bc7fbb8c-186a-4939-8a2b-b07a2af13aa6.png)
- **Theorem**: If the compression function is collision resistant, then the hash function is collision resistant.

## Message Authentication Schemes
MAC schemes are a family of functions ![latex-06a5d0a3-bd89-4da1-8c72-f5a5443cc554](data/midterm/latex-06a5d0a3-bd89-4da1-8c72-f5a5443cc554.png), with an l-bit secret key k.
- Can be efficiently computed
- Used for providing data integrity and data origin authenticity
  - Note: May not provide, confidentiality of the message or non-repudiation.

### Security Definition
- Let k be shared key
- The adversary does not know the key, but can obtain message signatures from Alice or Bob.
- **Goal**: Obtain the signature for any new message, i.e. not signed by Alice or Bob.
- A MAC scheme is secure if given some MAC tags it is computationally infeasible to compute a message tag pair for any new message x.
  - Must existentially unforgebale from chosen message attacks
  - If secure, a MAC scheme can provide data integrity and data origin authentication.

### Generic Attacks on MAC Schemes

#### Random Guessing
- Select a y and guess that ![latex-559fc941-a9cb-44bc-8ed5-8b1d796c359f](data/midterm/latex-559fc941-a9cb-44bc-8ed5-8b1d796c359f.png)
- If random function, then probability that it's correct is: ![latex-db1a709e-0b6c-4ca9-affe-62ce9101f706](data/midterm/latex-db1a709e-0b6c-4ca9-affe-62ce9101f706.png)

#### Exhaustive Search on the Key Space
- Given r known message-tag pairs
- Can guess values for k, check if ![latex-39d6a017-e682-41a5-a849-6470d06bcbb4](data/midterm/latex-39d6a017-e682-41a5-a849-6470d06bcbb4.png)

### MAC based on Block Ciphers

#### CBC-MAC
- Divide x into r n-bit blocks
- ![latex-6186a6a6-018e-4923-a0e4-32a952a4d2a1](data/midterm/latex-6186a6a6-018e-4923-a0e4-32a952a4d2a1.png)
- ![latex-6912d7db-b054-4759-8ae6-f129837c2d4d](data/midterm/latex-6912d7db-b054-4759-8ae6-f129837c2d4d.png) for 2 <= i <= r
- ![latex-f3015b24-ca6e-4f66-a1cd-488037a393ef](data/midterm/latex-f3015b24-ca6e-4f66-a1cd-488037a393ef.png)
- **Theorem**: Sps E is an ideal encryption scheme (each result is "random"), then CBC-MAC with fixed length inputs is secure.
  - If variable length inputs, then chosen message attack is possible.

#### Encrypted CBC-MAC (EMAC)
- CBC-MAC, but encrypt the last block under a different key.
- ![latex-a3149d21-d42d-44c0-b471-16a78cdae872](data/midterm/latex-a3149d21-d42d-44c0-b471-16a78cdae872.png)
- If E is an ideal encryption scheme, then it is secure for inputs of any length.

### MACs based on Hash functions
- Let H be an iterated hash function
- let compression function f map n+r bits to n-bits
- Let the key be padded with 0s (to be bit-length r)

#### Secret Prefix Method
- ![latex-6fc5ff69-f323-4828-a0b9-3a6d6344230a](data/midterm/latex-6fc5ff69-f323-4828-a0b9-3a6d6344230a.png)
- Possible to perform a length extension attack, can compute the tag of ![latex-4ffc957a-3e07-423f-b44c-799547e3210e](data/midterm/latex-4ffc957a-3e07-423f-b44c-799547e3210e.png) by retrieving ![latex-d4063b21-a1ea-4fb5-bb1f-4ac0a4225eed](data/midterm/latex-d4063b21-a1ea-4fb5-bb1f-4ac0a4225eed.png), then continue to compute the hash function. No knowledge of k required.

#### Secret Suffix Method
- ![latex-b2e23a47-3e34-4b1d-ac9f-20de69c09b3d](data/midterm/latex-b2e23a47-3e34-4b1d-ac9f-20de69c09b3d.png)
- Secret prefix attack doesn't work here
- If H is not collision resistant, then it is possible to find a collision ![latex-4ceba3f0-848a-42b3-ba07-37cb699c8a8d](data/midterm/latex-4ceba3f0-848a-42b3-ba07-37cb699c8a8d.png), then ![latex-582a69d9-706e-4257-ba28-4d556ed44554](data/midterm/latex-582a69d9-706e-4257-ba28-4d556ed44554.png)

#### Envelope Method
- ![latex-e23feeea-d29d-4536-bf02-d75477886146](data/midterm/latex-e23feeea-d29d-4536-bf02-d75477886146.png)
- Seems to be secure

#### HMAC
- ![latex-30a79d9f-52ec-4dae-a886-2c559845518a](data/midterm/latex-30a79d9f-52ec-4dae-a886-2c559845518a.png)
- Relies on compression function, secret IV to be secure.

### Authenticated Encryption
- Encryption scheme provides confidentiality
- A MAC scheme provides authentication (data origin authentication and data integrity)

#### Encrypt - AND - MAC
- Alice sends ![latex-74e68f3b-dd78-461f-b505-fe95a61838b1](data/midterm/latex-74e68f3b-dd78-461f-b505-fe95a61838b1.png) to Bob
- Bob decrypts c and checks that the signature is correct
- Problem: H may leak information about the plaintext, no confidentiality requirement.

#### Encrypt-Then-MAC
- Alice sends ![latex-8f5dde23-3d54-4802-99fc-81162aae18b4](data/midterm/latex-8f5dde23-3d54-4802-99fc-81162aae18b4.png) to Bob.
- Bob first checks the signature of the ciphertext, then decrypts if it matches

#### AES-GCM
- Can have header information that is authenticated, but not confidential.

### Public Key Crypto
- Symmetric key crypto requires sharing a secret key over some secure channel
  - The key must get to Bob without anyone else gaining access.
  - Bob and Alice must both keep the key safe
- Key management problem
  - In a network of n users, they must hold n-1 keys
  - Total number of secret keys: n choose 2 = ![latex-6aa45293-cf79-4edd-ae54-13bcdca1c68a](data/midterm/latex-6aa45293-cf79-4edd-ae54-13bcdca1c68a.png)
