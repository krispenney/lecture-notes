# Lecture 17 - July 4, 2018

Tor / Onion Routing
- confidentiality: TLS
- Anonimous: Onion Routing

## The Nymity Slider

An organization collects various bits of information about users

- **Verinymity**: Very specific
  - government id, SIN, credit card, address
- **Persistent Pseudonymity**: Still some form of linkage to true identity
  - Blogs: don't want other people to know, use the same handle for each post. Allows readers to assume the same person wrote the article
  - Stephen King pseudonym
- **Linkable Anonymity**
  - Prepaid phone cards, loyalty cards
  - At the same place used your credit card, can cause a link.
- **Unlinkable Anonymity**: As long as there's no prior survaillence, hard to track
  - cash payments, Tor

If you're building a system with privacy and anonymity, collect as little information as possible

Note that it's much easier to collect more information than to collect less.
- Easier to add a credit card to a loyalty card / cash transaction
- Hard to remove identity information (i.e. pay with credit card)

## Application Layer Security and Privacy
- TLS provides encryption at the TCP socket level
  - At the transport layer
  - Provides protection for application level (HTTP), means application-level don't need to care about key exchange / other primitives
  - Is it good enough?
    - Maybe you need encryption at the application layer:
      - Don't trust the operating system
      - Google Drive / Dropbox: Storing a confidential file in the cloud, unencrypted. Can't rely on the transport layer alone, only protects while it's in transit.
        - Doesn't stop Google / Dropbox from reading the file once they have it
- Ideally want true end-to-end
  - very hard in practice: No way to ensure the machine is not infected with malware
  - Don't know who is accessing the current machine
  - Machine-to-machine is typically good enough

Applications:
1. Remote login (SSH)
2. Email (Anonymous)
3. Instant Messaging

### Remote Login (SSH)

#### Usage
1. Client connects to server
2. Server sends verification key
  - client should verify that it's the correct key
    - If we don't verify: man in the middle
  - Via digital signature scheme: Give authentication and integrity
3. Client and Server run a key exchange
  - Ex. Diffie-Helman
  - After this point, everything is encrypted
  - Also use Message Authentication Codes (MAC)
4. Client authenticates to server
  - via username and password
    - Server must know the hash of your password
    - Could also the same login information to be used
  - Sign a random challenge with your private key, the server verifies your public key
    - Not very usable for alot of users
    - More secure, users could pick bad passwords
      - assuming the user keeps their private key safe

### Pretty Good Privacy (PGP)
- First widely deployed form of public key crypto
- **Goal**: Protect contents of an email message
- public key crypto
  - encryption of email messages
    - hybrid encryption
  - digital signatures of email messages
    - hash then sign
- For Alice and Bob to communicate with PGP
  - Both need public / private key pairs, sign / verify key pairs
  - Encryption: Bob uses Public key to encrypt , Alice decrypts with her private key
  - Digital Signature: Alice signs message with her private key, Anyone can verify with Alice's public key
  - Alice sends the ciphertext and signature to Bob

#### Obtain keys
- Bob needs to get an authentic copy of Alice's public key in order to send encrypted messages
  - Bad idea to go to their website: The website could be compromised with a false key
  - Could get the key from the website, ask Bob directly if the key is correct
    - Difficult because the key is long, tedious to verify
- **Fingerprints**: Compute the hash of the key using a **cryptographic hash function**
  - Recall cryptographic hash functions are collison resistant
  - Therefore, very low likelihood to engineer key that creates a collision
  - Relies on a web of trust

 To exchange keys:
- Alice gets Bob's public key from his website
- Alice computes the fingerprint of the key
- Alice asks Bob of the fingerprints match
- **web of trust**
  - Someone else you trust has verified Bob's public key
  - You can go to them to verify

- **Key signing Party**
  - you accidently sign the key of someone you don't trust
  - then other people that you trust will trust this person

- **Plot Twist**
  - If Alice and Bob's encrypted communications are captured
  - Later, if one of their computers of key pairs are compromised, then the messages can be compromised
    - learn who sent the messages
  - Even if you're doing everything correctly
    - But it's hard to ensure everyone that you communicate with has done the right thing

### Casual conversations (**Of the record** conversations)
- no one else can hear (unless recorded)
- no one else knows what was said (unless told by Alice and Bob)
- Alice and Bob can't prove what was said
- legal support
  - consent to record people
- wiretapping generally illegal
  - need a warrent

#### Crypto Tools to provide

Suppose a whistleblower and journalists are communicating over a year, don't want others to know

Want to achieve **forward security**
- past messages can't be decrypted if the key is leaked later in the future

Want to achieve **Deniable Authentication**
- journalist doesn't want to be able to link information back to them

##### Perfect forward Secrecy
- future key compromise shouldn't reveal past communication
- utilize short-lived session keys
  - regular rotation (per day, per TCP connection, etc)
  - Worst case, if the session key is leaked then only information from that session is compromised
    - Solves the issue with PGP (which uses the same key for all sesssions)
- Discard session key after use

##### Deniable Authentication
- Don't want digital signatures: Non-repudiation good for legal, but unwanted for private conversations
  - Can be traced back to a specific person
- Do want authentication: Can't have privacy if attackers can impersonate our friends
- Use Message Authentication Codes (MAC)
  - Use some shared key `HMAC(M, K)`
  - The anyone who has the key can verify
  - But can't tell who created it
    - Anyone who has the key could have sent the message
- This allows Alice to deny
  - Anyone who can verify can also generate their own MAC
  - Therefore this is bad for transactions (ex. financial). Any party could say they sent money, when they didn't

##### Utilize Both
- make online conversations act like off-the-record private conversations
- Bad for email, good for instant messaging

Off The Record (OTR) Protocol
  - confidentiality: Only Bob can read messages Alice sends
  - keys (Ratchet)
    - Have some shared key as a seed, use pseudo-random number generator (PRNG) to derive session keys
  - **Perfect Forward Secrecy**: After Bob reads the message, unreadable to everyone everywhere
  - **Deniability**: Bob can be assured that the message came from Alice, but can't convince anyone else of that fact
    - Bob could also create forged chat logs that would pass as authentic
- Signal Protocol
  - Improved version of **Off the record (OTR)** protocol
  - Session keys via similar ratchet
    - use past session keys to generate Diffie Helman keys
    - Means the party would need to be there for the past sessions
  - forward secrecy
  - improved deniability (Triple Diffie-Hellman): idea
    - only need a user's public key to forge a message
    - by definition the public key is public, anyone could forge
