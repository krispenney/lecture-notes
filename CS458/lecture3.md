# Lecture 3 - May 9, 2018

## Format String Vulnerabilities
- Recall format control characters: `printf("%s", buffer);`.
- Problem: `printf(buffer)`, will parse the buffer for `%s` characters, potentially causing data to be leaked (ex. off of the stack).

### Slide 2-28 Example
- First `snprintf` got `%48d+` into the buffer
- This will cause us to read past the end of the buffer, hopefully onto the return address

### Incomplete Mediation
- Inputs are often specified by intructed users
- Ex: Bad inputs `sroos#uwaterloo.ca`
- **Incomplete Mediation**: When an app accepts incorrect data from the user.

Why do we care? **Sanitized Data**
- Unsanitized data could cause issues (code execution, SQL injection)
- Need to make sure user inputs are well-specified values, known to be safe
- `; DROP TABLE users; --`

### Client-side Mediation
- Javascript routines doing mediation on the client side
- Problem: JS can be turned off, browser may not support Javascript.
  - Client may somehow bypass your JS, pass whatever they want to you.
- Therefore, you should do server-side validation. Maintain state on the server (Sessions)

### Defenses against incomplete-mediatino
- Client-side for nice UI
- always check on the server side
- sanitize user input values
  - Could contain arbitrary data
- Ensure that the client hasn't modified state in any way.

### TOCTTOU Errors
- Time-Of-Check To Time-Of-Use
  - Race conditions
- Example
  1. User makes a request of a system
  2. The system verifies the user is allows to perform the action. i.e. correct permissions.
  3. The System performs the action
- If you can change the system state between 2 and 3 bad things can happen
- Symbolic Link Example
  1. User makes a symlink to a log file
  2. User tries to write a string to the log file
  3. The system checks that the user can write to the log file
    - Between 2 and 3, the user would try to change the symlink to point to a different file (`/etc/passwd`)
- Solution
  - Don't let the user modify the state
  - Use locks
    - May not be needed, transactional filesystems may give atomic operations.
  - The OS could request that the user provide the true file name
  - The kernel could keep a private copy of the required information. Check if the user modified on their end.

## Malicious Code: Malware
- **Malware**: Software written with malicious intent.
  - Common characteristic: Need to be executed in order to cause harm
  - Could be launched by user actions (downloading and running a file) or by exploiting an existing flaw in a system (buffer overflows)

### Types of Malware
- **Virus**
  - Malicious code that adds itself to a benign program
  - code to spread + code for the actual attack
  - **requires user involvement in order to spread / infect**
- **Worms**
  - Malicious software that spread with **no involvement from the user**
- **Trojan**
  - Advertised as an innocent program, but it's malicious
- **Logic Bombs**
  - Malicious code that hidden in existing programs on your machine.

#### Virus
- Typically executed when the host program is executed
- Not only limited to binary files, could be in Office macro, PDFs
- They want to maximize coverage, when run will try to spread itself.
  - infect other files on the system
  - attempts to spread to other computers, a user may accidentally give the infected file to another user.

**Infection**

| Binary File |
|-|
| Entry Point |
| Machine Instructions |
| Virus Instructions |

- A virus may append it's code to the instructions, change the entry point to the file to virus code. Then jump back to the original entry point when it's done.
  - return to the host program
- Opening / executing the file will turn control over to the file
- How to defend?
  - Some anti-viruses just check the ends of files (for performance reasons)
  - Some virus just overwrite the file's instructions in an arbitrary location and hope it gets executed.
- The virus may eventually spread so that it is executed when the machine is booted
  - infected applications that autorun on boot
  - previously, could infect the boot sector of the HD.
- **Goal of a virus**: Evade detection
  - Try not to overwrite the original source

**Spreading**
- Sending infected files to friends
- Infected files on networks
- emails, USBs, Torrents

**Payload**
- Payload will likely cause something bad to happen
  - Erase files, keylogger, attack some particular targets


##### How to look for viruses
- signature-based protection
  - Keep a list of known viruses
  - for each virus in the list, store some characteristic features
    - machine instructions
    - Use features of both the payload and the infection code
  - Other features
    - Where they try to hide (tmp files)
    - check autorun / startup
  - **Polymorphic**
    - Some viruses will make imperfect copies of itself in order to evade detection
    - for example, insert `nop` instructions
    - Different compilers will generated different machine code, different optimizations used.
    - Encryption can be used to modify the virus, when it spreads use a different decryption key.
      - Virus scanners would try to detect the encryption routine
    - To catch: Try to execute the code in a virtual environment, see the meaningful effects.
  - **limitation**: You can only identify viruses in the signature database
- behaviour-based protection
  - look for suspicious patterns of behaviour, rather than some specific signature
  - Try to run in a sandbox first
    - some viruses can detect that their running in a sandbox and behave.

Virus scannars can have errors in detection
- false positive: claim a file is a thread, when it is not
- false negatives: Claim a file is safe, when it is not
  - i.e. fail to identify a threat
- signature-based: fewer false positive
- behaviour-based: fewer false negatives

Base Rate fallacy (why false positives can be bad)
- Suppose a breathalyzer reports false drunkness in 5% of cases, never fails to decect true drunkuness
  - false positive rate: 5%
  - false negative rate: 0%
- Base rate: suppose 1 in 1000 drivers are drunk.
- If a breathalyzer test of a random driver indicates that the driver is drunk, what is the probability that they are?
- In virus scannar, more false positive than true positives meaning the true positives may be ignored.

#### Worms
- Worms is a self-contained piece of code that can be replicated with little user involvement
- often use security flaws in widely deployed systems
- The Morris Worm
  - Buffer overflow in the finger daemon
  - Backdoor in sendmail
  - Try to use a dictionary attack against the local user's passwords, spread to other machines they can access (without a password)
- The Code Red Worm
  - Buffer overflow in Microsoft IIS
  - patch was available for ~month, some admins decided not to update
  - infected machine would
    - deface it's home page
    - launch attacks on other web servers (whether or not it was IIS)
    - launch a targetted DDOS attack
    - install a backdoor in order to gain later access
- Slammer Worm
  - Microsoft SQL server
  - spread extremely fast, 90% of vulnerable hosts in 10 minutes
  - a machine could be infected with a single UDP packet
    - no handshake in UDP
- Stuxnet
  - Targetted Iranian uranium enrichment program
  - 4 zero-day vulnerabilities, not widely known to public
- WannaCry
  - ransomware
  - NSA knew about vulnerability, but didn't tell anyone.

#### Trojan Horse

- Software that looks like an innocent program, but does something malicious
- everyone like dancing pigs, the user would like to execute the program and will bypass any warnings

##### Scareware
- Scare the user into taking an action that they think that they want to do.
- Scare them into installing some program (anti-virus, CRA)
