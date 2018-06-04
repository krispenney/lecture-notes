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
- **Worms**: Spreading with little to no user interaction
- **Trojans**: Malicious code hidden in seemingly innocent programs
- **Logic Bombs**: Malicious code that's hidden in existing programs on your machine.
