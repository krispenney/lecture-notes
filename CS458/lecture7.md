# Lecture 7 - May 23, 2018

## User authentication
- Systems often have to identify and authenticate users before authorizing them to access the system.
- **Identification**: Who are you?
- **Authentication**: Prove who you are
- easy to identify and authenticate people when they know eachother in the same local area.
- However, remotely this is difficult. The person on the other end could be pretending to be someone else.

### Authentication Factors
1. something they **know**
  - password, pin, secret questions
2. something they **have**
  - badge, card, cookie, key
  - could be a uniform, but these are easy to forge, steal, etc.
3. something they **are**
  - biometrics
4. something about their **context**
  - location, time, nearby devices

You can combine these factors to achieve more solid authentication (two-factor, multi-factor)
- The factors should be from different classes, meaning if one factor is compomised then the other should be safe.
- Note: "something you have" can become "something you know"
  - tokens can be duplicated
  - token generation scheme could be discovered, allowing an attacker to gain access to the token.

### Passwords / Pins
- oldest, but most dominant scheme
- `uid, password` pairs
- usability problems
  - inconvenient
  - complicated rules
  - forgotten passwords
- security problems
  - someone could give out their password
  - keyloggers
  - password re-use
  - easy to guess

### Password Guessing attack
- **brute-force**: use exhaustive search to try all combinations
- problem if the system doesn't limit the authentication attempts
- brute forcing passwords is exponential
  - adding one more character exponentially increases the complexity to solve
  - good to make users have a longer password

Exhaustive search assumes that individual's choose passwords randomly, but people typically don't select a random password, there are patterns.
- helps attackers make better guesses
- dictonary attacks, select root passwords, add common prefixes and suffixes to the word

Should we just give up on passwords?
- There's a reason they're so dominant: you don't need any specialized hardware

**Offline Attack:** Attacker can try as many attempts as they want
- could be a website that doesn't check attempts
- attacker has access to an encrypted document or password
- This type of attack is more favourable to attackers.

**Online Attack**: Attacker has a limited number of attempts
- could be locked out after n failed attempts
- try to login to a website that checks
- How can attackers be better
  - try n-1 times
  - cycle the passwords through multiple users.
  - Increase the probability that one user has chosen one of these passwords
  - can effect **availability**: attacker purposly locks someone out of their account

#### Password Hygiene (as a user)
- Use a password manage to create and store passwords
  - prevents password reuse across websites
  - issue: all passwords are located in one place.
  - problem if you go to a different machine
  - bad if password manager has bugs
- pass-phrases
  - phrase of randomly chosen words
  - avoid using common phrases, slogans
- don't re-use passwords
- don't share passwords
  - problems with studies that show people give out passwords
    - reserachers can't actually check that the users weren't lying
    - no ground truth

#### Password Hygiene (for developers)
- no composition rules
- don't allow common passwords
  - have a blacklist

Recall information leakage in the following case
```C
if (stored_password[i] != supplied_password[i]) break;
```
Timing information can be leaked depending on where the mismatch is.

- don't force users to periodically change their password
  - they might just cycle passwords through different websites
  - might just add a counter to the end
- Support multi-factor authentication
  - SMS based should be avoided due to vulnerabilities in SMS technology

#### Attacks on password files
- storing passwords in plaintext is dangerous
  - system admin might have access to the file, try to impersonate others
  - The file could be leaked
- store a **digital fingerprint** (using a cryptographic hash function)
  - when logging in, the system computes the fingerprint using the supplied password, compares to the stored fingerprint
  - Note that cryptographic hash functions are preimage resistant (one way), meaning an attacker is not able to reconstruct the plaintext with high probability.
  - still allows for an offline guessing attack in case the password leaks
    - can take dictionary list, run it through the same hash function. check if the real hash is in the list.
  - **salting**: The system generates a random string, appends it to the end of the password, hash it
    - store the hash and salt
    - to check, use the plaintext, add the salt, hash, compare to stored
    - now it's much harder to create the table, need to append the salt to all dictionary words, and only works for one user
      - doesn't allow for multiple users in parallel (but can do targeted by creating a single dictionary)
    - Means two users with the same passwords will have different hashes, as the salts will be different. (with high probability)
- defend against dictionary / guessing attacks
  - don't use a standard cryptographic hash
  - the typical crypto hash functions (SHA-256/512) are public and designed to be fast.
  - Instead use an iterated hash function that is expensive to compute (bcrypt), and maybe uses lots of memory (scrypt)
  - limits the bandwidth of an attacker, while users who use the system will not notice.
    - significantly slows down attackers over many guesses
- Alternative is to use a MAC scheme, instead of hashes
  - in the salted-hash example, if the passwords are leaked the salts are also leaked.
  - MAC includes a secret key to compute the fingerprint
  - If the fingerprints leak, guessing attacks aren't effective (as the secret key is safe)
  - Protect secret key in secure enclave in the CPU
- Password recovery
  - can't typically be recovered when using fingerprints
  - the system could set a temporary password
  - this email could be sent in plaintext, could be intercepted

#### Adobe Password Hack
- 130 million encrypted passwords leaked
- Using ECB mode (bad)
- storing unencrypted password hints.

#### Interception Attacks
- attacker intercepts password while it is communicated from client -> server
- one-time passwords make intercepted password useless for later logins
  - Fob
  - challenge-response protocols
    - the server sends a random challenge to the client
    - client uses challenge and password to compute a one time password
    - send one-time password to server, check the response is valid
    - problem: if the attacker obtains the challenge and response they could brute force
      - especially if the number is too small
- Lots of SSL/TLS adoption, safe over the network
  - passwords are transported in plaintext
  - digital fingerprints
  - don't prevent against attacks on the client (malware, keylogger)

#### Graphical Passwords
- alternative to text-based passwords
- user has to select something from a graphical environment
  - select three points on a map
  - select three "secret" faces
- Problem: shoulder surfing can be easier
- Problem: Hotspots
  - people choose the same locations
  - people choose the same faces / parts of faces

#### Server Authentication
- user should also authenticate the system it's communicating with
- opens the door for phising
  - you think your talking to your bank, but it's fake
- implementations
  - some banks will show you a picture and caption (that you selected), after entering your user-id, before password
  - `CTRL-ALT-DELETE` to login on Windows, can't override

#### Biometrics
- authenticate users based on physical characteristics
  - fingerprints, iris, voice, handwriting
  - behavioral biometrics: use some aspect of the user's behaviour
- if observed trait is sufficiently close to the truth, accept
  - doesn't need to be an exact match
  - observed sample will never be exactly the same as the stored

##### Local vs remote Authentication
- biometrics work well for local, can make sure you're using your own fingerprint

##### Identification vs. Authentication
- Auth: does a captured trait correspond to a particular stored trait
- Identification: does a captured trait correspond to any of the stored trait
- False positives are bad
  - false negatives: real users are rejected
  - false positives: false users are accepted
- problem: boy who cried wolf
  - too many false negatives, then people will ignore the true positives. loose trust in the system

##### Other Problems
- privacy
  - can't change your fingerprint if they leak
  - why should they have a copy?
- Accuracy: false negatives are annoying
  - what if there's no other way to authenticate
- secrecy: some biometrics aren't secret
  - Fingerprints: best place to look is on the fingerprint sensor
- legal protection
  - can refuse to give away your password
  - but could make you put your finger on the scanner
