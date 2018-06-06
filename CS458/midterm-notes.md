# Midterm Notes

## What is Security

A computer system is typically deemed to be secure if it meets the following:
- **Confidentiality**: Access to systems is limited to trusted parties
- **Integrity**: When data is recieved, it is the right data
- **Availability:** The system or data is there when you want it

**Privacy**: You get to control the information about you (**informational self-determination**)
- Who gets to see it
- who gets to use it
- what they can use it for
- who they can give it to
- PIPEDA: Personal Information Protection and Electronic Documents Act

### Adversaries
- Murphy
- Amateur
- Script Kiddies
- Crackers
- Organized Crime
- Government Cyberwarriors
- Terrorists

#### Assets

Something we want to protect
- hardware
- software
- data

#### Vulnerabilities

A weakness in a system that can be exploited to cause loss or harm.
- file server that doesn't authenticate users

#### Threats

A loss or harm that can befall a system
- users files may be revealed to the public

Types of threats
1. Interception
2. Interruption: Interupt a real user's service
3. Modification
4. Fabrication: Pass off fake data as real

**Threat Model**: Set of threats we are defending against

#### Attacks

An action which exploits a vulnerability to execute a threat
- ex: telling a fileserver that you are a different user in order to read or modify their files

#### Control / Defence

Removing or reducing a vulnerability. You control a vulnerability to prevent an attack to defend against a threat.

Methods of Defence
- **Prevent it**
  - Immobalizer on car
- **Deter it**: Make the attack more difficult / expensive
  - Store the car in a secure facility
- **Deflect it**: make yourself less attractive to the attacker
  - Sticker mentioning car alarm, hide valuables
- **Detect it**: notice that the attack is occurring (or has)
  - Car alarms, Onstar
- **Recover from it**: Mitigate the effects of an attack
  - Insurance

**Defence in Depth**: Do many things to defend against the same attack.

**Principal of Easiest Penetration**
- System is only as strong as it's weakest link
- Attackers go after the easiest

**Principal of Adequate Protection**
- Economics
- Don't spend $100,000 to defend a system that can only cause $1,000 in damage.

## Program Security

Why is it hard to write secure programs
- **Murphy's Law**: All programs have bugs
- Security relevant programs have security bugs

### Flaws, Faults, and Failures

**Flaw**: Problem with a program
- **Security flaw**: problem that effects security in some way (CIA)
- Types
  1. **Fault**: A mistake behind the scenes
    - An error in the code, the programmer's view
    - a potential problem
  2. **Failure**: When something actually goes wrong
    - A derivation from the desired behaviour (the specification may be wrong)
    - login to a website, see someone else's account
    - The user's view

#### Find and Fix Faults

- If a user experiences a failure, work backwards to find the fault
- Think like an attacker: try to cause failures, proceed as above
- Once faults are found, fix them
  - Via patches, penetrate and patch
  - Patching can make things worse, devs get tunnel vision, don't do the right solution, cause other faults, create inconsistencies.

Unspecified behaviour
- spec lists what the program should do
- Implementations don't typically care if it can do additional things as well, Extra behaviour can be bad for security.
- Consider "and nothing else" as being added to the spec.

#### Types of Security flaws
- **Intentional / Inherent**:
  - **malicious**, inserted intentionally to be exploited later.
    - If targetting a specific system: **Targeted malicious flaw**
  - **non-malicious**: features intended to be there, correctly implemented, but can be exploited by an attacker.
- Most flaws are caused **Unintentionally**

##### Heartbleed
- when a client connects to a web server, sends a heartbeat to keep the connection alive.
- Send random data and a payload length
- **Issue**: No length checks, causing data to be leaked.

#### Types of unintentional flaws

##### Buffer Overflow
- functions / developers often don't check that the data being copied into a buffer will fit into the buffer.
- Can overwrite stack elements, including the return address. Causing arbitrary code to be executed.

Varients
- Off-by-one
- overflow buffers on the heap
- jump to other parts of the program, libraries

How to defend
- Check bounds!
- The compiler can insert a **canary** onto the stack, between the data and the return address. Check if the canary has been tampered with.
- Make memory pages exclusively executable or writeable
- Stack randomization

##### Integer Overflows
- Programs may assume that a signed integer will always be positive, overflow can violate that.
- Program cast a large unsigned int to a signed int, causing overflow

##### Format String
- `printf(buffer)` instead of `printf("%s", buffer)`

##### Incomplete mediation
- mediation: ensure all requests made are reasonable
  - incomplete mediation: the application accepts invalid data
- enter bad data (invalid emails, phone numbers)
- If we don't validate, possibilities for buffer overflow, SQL injection, etc.
- Always need to perform server-side
  - Javascript can be disabled, bypassing client side authentication
  - use client side for better UX

##### TOCTTOU (Time of Check to Time of Use)
- race conditions

1. User asks to perform an action
2. System checks if the user can perform the action
3. System perform the action

Problem in time between 2 and 3, what if system state changes in such a way that the user wouldn't be allowed to do?
- `symlink` to `/etc/passwd`

How to defend?
- Ensure that system state remains static between authorization check and use
- keep a private copy of the request, not allowing it to be modified unintentionally
- Use locks

#### Malware

Types of software written with malicious intent. Needs to be executed in order to cause harm. Execute via:
- User actions
- exploiting another (existing) flaw

Types
- **Virus**: Malicious code that adds itself to benign programs
  - code to spread + the actual attack
  - infects other non-malicious files
  - try to evade detection
  - spreads between computers by unknowning users accidently sharing infected files
- **Worms**: Spreading with little to no user interaction
  - Use security flaws in widely deployed systems
  - try to affect other vulnerable computers on the network
- **Trojans**: Malicious code hidden in seemingly innocent programs
  - Exploits users: they want to see the dancing pigs. scare users into taking some action
- **Logic Bombs**: Malicious code that's hidden in existing programs on your machine.
  - Waiting for some trigger to go off
  - typically written by insiders, execute later when they leave

How to check for viruses
- **Signature Based**:
  - maintain a list of known viruses, store signatures of each
  - See if these signatures exist in other files
  - **Polymorphism**: to evade, viruses make imperfect copies of themselves. Could encrypt the virus code, on copy choose a new key
  - **problem**: You can only scan for viruses that are in the list, new ones introduced every day
- **Behaviour Based**
  - look for suspicious patterns in behaviour
  - could run the code in a sandbox, see if it does something bad

Need to be mindful of false positives and false negatives
- FP: false alarms, annoying to the user
- FN: Miss infected files

**Salami Attack**: An attack composed of many smaller, unrelated attacks.
**Interface Illusions**: we expect standardized behavirour. Malicious code can trick us into taking the wrong action.

#### Non-Malicious

**Covert Channel**: Transmit information through a channel that isn't supposed to transmit information
**Side Channel**: Eve watches how Alice's computer behaves while processing the sensitive data

## Operating Systems

Access Control
1. Check every access: Access could be revoked at any time
2. Enforce Least Priviledge: grant programs access to the smallest number of objects required to perform the task.
3. Verify acceptable use: Limit the types of activity that can be performed on objects

Access control Matrix
- set of protected objects (database, files)
- set of subjets (users)
- set of rights
- Every entry of matrix is a set of rights for (O, S) pair
- rarely done in practice: too big, many objects to keep track of.

Access control lists
- column-wise view: each object has a list of subjects
- allows users of object: easy, run through the list
- determine set of objects a user can access: harder have to go through all objects
- revoke users rights to an object: easy
  - all objects: hard

Capabilities
- row-wise view of matrix
- subjects have access to objects
- A capability is an unforgeable token that gives its owner some access rights to an object
  - unforgebel enforced by the OS, cryptographic

Role-Based Access Control
- user's role within an organization influences what they can access
- When some changes their job, don't need to update everything
- extensions
  - Hierarchical
    - a manager is also an employee
  - Users can have multiple roles, differing depending on assigned tasks.
  - Separation of duty
    - payment order has to be signed by manager and accountant, different people.

User Authentication
- Identification: who are you
- Authentication: prove it
  - Factors: Combine multiple classes
    - something they know
    - something they have
    - something they are
    - something about the context
      - where they are, nearby devices

Password guessing attacks
- offline attack: The attacker has an encrpyted password file,
- online attack: attacker might want to guess your banking password, log in as you
  - are detectable by the web site

Trusted Operating Systems
- policy: a set of rules outlining what's secured and why
- model: model implements the policy, reasoning about it
- design: spec of how the OS implements the model
- trust: OS is implemented according to design

Trusted Software
- functional correctness: works correctly
- enforcement of integrity: Wrong inputs don't impact correctness
- Limited Privilege: Access rights limited and passed onto others
- Appropriate Confidence Level: rated as required by the environment

Security Policy
- From military
- Subject and objects have clearance levels (Top secret, secret), also compartments (russia, germany)
  - could have multiple
  - **need to know rule**: different departments have trade secrets
- Subject s can access object o iff $$level(s) \ge level(o)$$ and $$compartments(s) \subseteq compartments(o)$$.

Chinese Wall Policy
- only access the information of a single company of a given kind.
- for consulting, legal
- Access rights change over time
- **ss-property**: Subject s can access object o iff each object accessed by s belongs to the same company as o, or each object access by s is of a different kind of company than o.
- **\*-property**: for write access to o by s, ensure that all objects readable by s either belong to the same company as o or have been sanitized

Models - Lattices
- unique lowest upper bound: for any a and b there exists a u which dominates both a and b.
- unique greatest lower bound: For any a and b there exists a l which is dominated by both a and b

Bell-La Padula confidentiality Model
- Regulates the flow of information
- **information can only flow up**
- ss-property: no read up. s should have read access to o only if s dominates o
- \*-property: no write down, s should have write access to o only if o dominates s

Biba integrity model
- prevents inproper modifications to data
- write access: s can modify o only if s dominates o
  - unreliable person can't modify files containing high integrity information
- read access: s can read o only if o dominates s
  - unreliable information cannot contaminate a subject
- Low Watermak property: used to deal with the restrictive nature of Biba. Subjects can never read lower integrity information. Integrities are always falling
  - subject low watermark property: if s reads o, then l(s) = glb(l(s), l(o))
  - object low watermark property: if s writes to o, then l(o) = glb(l(s), l(o))

Trusted OS design
- security should be part of design from the start
- design principals
  1. Least privilege: Operate using fewest privileges possible
  2. economy of mechanism: protection should be simple and straight forward
  3. Open Design: no security by obscurity, use secret keys and password, algorithms should be public.
  4. complete mediation: every access should be checked.
  5. permission safe / fail based defaults: default access should be denial
  6. separation of privilege: 2+ conditions should be met to gain access
  7. Least common mechanism: every shared mechanism could be used as a covert channel
  8. Ease of use: protection mechanisms need to be easy, otherwise no one will use them.

Mandatory Access Control: Central authority, Chinese Wall, Bell-La Padula, Biba
Descretionary Access control: owners of objects have some control over who can access
Role-based: subject's role defines what they can access

Trusted computing base
- necessary to enforce a security policy
- could be a seperate security kernel: Easier to test
- Placed throughout OS code
- Reference monitor: Part of TCB
  - collection of access controls
  - tamperproof, unbypassible

Virtualization
- provide logical separation
- Virtual Memory: page mapping gives illusion that process owns all of the memory
- Virtual Machine: Virtualize IO, devices
  - can limit attacks on a program to the VM
  - Problem: The OS itself could be placed in a VM by a rootkit

Application Insulation
- memory encryption to shield from other apps,
- Partition app into trusted and untrusted code
  - communicate with eachother via an API
- trusted code is encrypted by a hardware secure enclave
