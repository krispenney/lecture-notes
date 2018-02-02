# Lecture 14 - February 2, 2018

## Daum-Lucks Attack
- Attack on MD5 for PostScript files
- Pick some preamble, that is a multiple of the block length
- Use this to falsify messages
- Can use 1 useless collision to generate any file with the same hash.
- extendible to arbitrary binary programs

### Protection
- A user could inspect the postscript file, but in reality no one does this

## Message Authentication Code Schemes (MAC)
- MAc scheme is a family of functions, mapping arbitrary-bit strings to n-bit strings
- has a parameter k, which is an l-bit string
- ![latex-1b5870a8-0f60-42b8-8ec7-28bb3e3f855d](data/lecture14/latex-1b5870a8-0f60-42b8-8ec7-28bb3e3f855d.png), outputs the tag of x with key k.
- allows a scheme for providing data integrity and data origin auth

### Applications
1. Alice and Bob establish some secret key
2. Alice computes the tag, sends the message and tag to Bob
3. Bob verifies the tag

- Integrity: since the attacker doesn't know the secret key, the tag won't match
- origin: again doesn't know the secret key, tag won't match, probably not from alice
- No confidentiality or non-repudiation
  - Message is open
  - Bob could just generate some key and tag and say that it came from Alice
    - Can't distinguish between tags that Alice generated or Bob generated
- Doesn't prevent against replay attacks
  - use some sort of sequence
  - timestamp

### Security
- Assume the attacker knows everything about the MAC scheme, except for the secret key
- **Goal of the attacker**: Eve needs to convince Bob that a message she sent was from Alice.
  - i.e. correct a message x and tag without knowing the secret key
  - Eve is able to collect pairs of messages and tags
  - **Chosen Message Attack**: Eve may be able to pick messages for Alice to tag.
    - Harmless messages for Alice (i.e. contract worth $1) is all Alice will sign
      - Whatever Alice will tag for you
    - Goal: Eve needs to tag harmful messages for Alice
      - Whatever Alice won't tag for you
    - Compute the tag on any message

#### To be secure
- The MAC scheme must be existentially unforgeable against chosen-message attacks
- **Assignment 3, Q3**
  - First 3 problems from todays lecture

### Ideal MAC Scheme
- **Propery**: For any l-bit key, the function ![latex-44249c6a-e141-4d20-b47c-9ae19cb8fb5b](data/lecture14/latex-44249c6a-e141-4d20-b47c-9ae19cb8fb5b.png) is a random function.
- Note: this is useless in practice since we can't program a random function
  - analysis purposes

#### Generic Attack on MAC scheme
- select a random tag, assume it is the tag
- since H is random, each guess has Probability of correctness of ![latex-05357bde-0f9c-456f-8e76-80e6af25322c](data/lecture14/latex-05357bde-0f9c-456f-8e76-80e6af25322c.png)
- **Note**: Guesses can't be directly computed
  - Can't check offline
  - Online: few guesses, limited time
- This is realistic for small n.
- In reality use ![latex-3c16928c-717a-4f35-85db-e8aabb3f4bae](data/lecture14/latex-3c16928c-717a-4f35-85db-e8aabb3f4bae.png)

#### Generic Attack 2
Exhaustive key search

- Given r known message tag pairs
- ![latex-d969cbd9-7ee8-48ee-a69d-6675d6e078d7](data/lecture14/latex-d969cbd9-7ee8-48ee-a69d-6675d6e078d7.png)
- Expected number of steps: ![latex-12681241-5b82-4964-859c-622afa92d084](data/lecture14/latex-12681241-5b82-4964-859c-622afa92d084.png)

### MACs based on Block Cipher (CBC-MAC)
- Assume that all plaintext messages all have lengths that are multiples of n
1. Divide x into r n-bit blocks
2. Compute the tag
3. For each block compute ![latex-fa7e6cdd-17c4-49a1-974e-81b3e6bbc69d](data/lecture14/latex-fa7e6cdd-17c4-49a1-974e-81b3e6bbc69d.png)
4. Then ![latex-22c14ec3-7311-4155-bf3d-87ea1fd2e115](data/lecture14/latex-22c14ec3-7311-4155-bf3d-87ea1fd2e115.png)

#### Security
- Provided by theroem
- Makes the assumption that ![latex-769d28be-86f8-49cd-a594-be1bfab9fa5d](data/lecture14/latex-769d28be-86f8-49cd-a594-be1bfab9fa5d.png) is an ideal encryption scheme (block cipher)
  - It may not actually be.
- Need to used fixed-length inputs.

#### Attack if arbitrary lengths
1. attacker picks a block
2. obtain the tag for the message
3. encrypt it
4. obtain the tag of the tag
5. this tag is also the tag of the 2-block message `(x, 0)`

Note: While this attack is silly, it **still** breaks the notion of security as defined. Thus, the MAC scheme is insecure if arbitrary length.

##### Fix Encrypted CBC-MAC
- CBC-MAC as before
- Encrypt the last block under a second key s
- **Theorem:** If E is ideal, then this MAC is secure for inputs of any length

### MACs based on Hash Values
- Problem: Public fixed function, with no secret key
- `H`: An iterated n-bit hash function, without the length block
- Note the compression function
- keys are n-bit strings
- Block K is key padded with ![latex-78b5a3d6-0383-4330-b509-bd47a459f6ad](data/lecture14/latex-78b5a3d6-0383-4330-b509-bd47a459f6ad.png) 0's

#### Secret Prefix Method
- Use K as the first block
- hash the message blocks
- if ![latex-e012f224-893e-4827-9350-d436f5b387ac](data/lecture14/latex-e012f224-893e-4827-9350-d436f5b387ac.png) is known
- Can compute ![latex-15e81b8f-8a8a-4dd0-abb3-1554674e1eab](data/lecture14/latex-15e81b8f-8a8a-4dd0-abb3-1554674e1eab.png)

#### Secret Suffix Method
- Add the key block to the end of the message
- Previous attack doesn't work, appending y means Key is in a different place
- If there is a collision then finding a collision for the tags means the tag will work for the second message
- Security relies on the hash function being collision resistent
