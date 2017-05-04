# Lecture 2

Confidentiality
Integrity
Avaliability

- Deturrence increases the difficulty to attack
- Deflection decreases the attractivness of an attack

- Analyze code from the prespective of an attacker

### Principal of Easiest Penetratino
- The advarsary will always try to attack the weakest link
- Always focus on strengthening the weakest links

### Principal of Adequate Protection
- Security is economics
- Don't spend $100,000 in security for a system that can only cause $1,000 in damage.

### Defences of systems
- Software controls
  - passwords
  - virus scanners
  - OS Sandboxing
  - Ensure quality in source code development
- Hardware controls - protect physical access to systems
  - fingerprint readers
  - physical tokens (ex. keycards)
  - security systems
- Physical controls: Protect the hardware itself
  - locks
  - guards
  - off-site backups
- Non-Technical: People / Administrative staff -> Subject to social - engineering
- Cryptography
  - authentication via digital signatures
  - integrity of stored data
  - improve privacy of user's
- Policies and Procedures
  - Rules about changing passwords
  - Device network access
  - train in security best practices

## Program Security
- Murphy axiom: Programs have bugs
  - Security relevant programs will also have bugs

### Flaw, Faults, and Failures
- Flaw: A problem with a program
  - security flaw: a flaw that effects security (CIA)
  1. Fault
    - a potential problem
    - only visible from the inside
  2. Failure
    - when something actually goes wrong

How do you find a fault?
- repeat user steps
- intentionally try to cause failures
- once you find them fix them, **penetrate and patch**

Problems with patching
- Could make things worse (in other parts of the system)
- Create new bugs

**Fuzzing**
- Use automated tools to find faults in the system
- brute force bad inputs
- More intelligent state-machines base solutions
- Should be done early in the development process

**Unexpected Behaviour**
- Most programs typically have a specification
- From a security prespective, don't want to deviate from spec
- It's usually impossible to check for every possible case

**Types of Security Flaws**
Categories
1. Intentional
  1. Malicious
    - If you conciously write a virus
  2. Non-Malicious
    - Just a property of the system
    - Example: Cache is faster than HDD. Attackers can to a time analysis to infer which memory is accessed. But we still want this behaviour
2. Non-Intentional
  - Bugs

**Unintentional Flaws**
- Heartbleed
  - Broke SSL/TLS connections on all servers
  - Missing a bounds check in the code, HAT(500 letters)

- Buffer Overflows
  - Possible to write more into a buffer than it's size
  - **Smashing the Stack for Fun an Profit**
    - Write through the stack (i.e. the return address)
    - Possible to redirect to an address of the attacker's choice
    - Targets: programs with su privileges

``` C
// Example 1

void writeBuf(char *str) {
  char buffer[16];
  strcpy(str, buffer);
}

// Attacker writes 20 'A's
// Return address is now 'AAAA', which will probably crash
// Worst Case: return to a location of the attacker's choice
writeBuf('AAAAAAAAAAAAAAAAAAAA');

// Stack
// buffer: 16 bytes
// return address: 4 bytes

// Example 2
// Set the return address to the address after the authentication check
int x = 0;
writeBuf(input);
x = 3;
int y = x;

while(y > 0){
  // Some secure authentication check
  --y;
}

// Safe
```

**Kinds of buffer overflows**
- Off-by one errors
- Overflow of heap buffers instead of the stack
- jump to other parts of the program, or parts of standard libraries, instead of shellcode

**Defences against buffer overflows**
- Use a programming language with bounds checking (and be sure to catch the exceptions)
- Compiler: Place padding between the data and return address (canaries)
  - Detect if the stack has been overwritten before the return from each function
  - i.e. check that the canaries are still intact
- Non-Executable stack: W XOR X, memory page is either writable or readable
- OS can place the return address at a random virtual location.

