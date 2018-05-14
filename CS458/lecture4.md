# Lecture 4 - May 14, 2018

## Ransomware
- exploit some existing vulnerability on your machine.
- Typically encrypts your files, asks the victim to send them money to decrypt.
  - demands some sort of ransom to regain access
- scareware
  - scare people into taking some action
  - You download pirated software, you recieve an email threatening to take you to court unless you pay a fee.

## Logic Bombs
- Malicious code hiding in software on your computer
- written by insiders
- Triggered sometime in the future when a particular trigger goes off
- Design to cause damage.

### Triggers
- Allows the insider to gain access in the future
- Special pin codes
- A specific time

### Spotting Trojan Horse and Logici bombs
- Hard to spot: you can warn the user, but they may want to see the material ("The dancing pigs")
  - Difficult to develop signatures
  - Typically not public domain code
- prevention
  - Don't run from untrusted sources
  - Internal Code reviews

## Other Malicious Code
- back doors
- priviledge escalation
- rootkit

Typically tools that are included in payloads

### Web Bugs

Small object (1x1 transparent image) embedded in a web page, fetched from a different server than the hosting server.
- You information is sent off to a 3rd party without your consent.
- Sent to advertisers
  - IPs
  - cookies
  - Other info

Issue of privacy, more than security. Typically it's not an action that you would expect a website / browser to do.

#### Leakage of your Identity
- cookies let advertisers learn what website an individual is interested in.
- Typically no link to your true identity until they appear on your social network.

### Back Doors
- Developer leaves some instructions to bypass normal authentication allow access to anyone who knows that the back door exists.
- sometime innocent: left in for debugging purposes
- important to make sure toolchains (compilers) don't modify the code to add backdoors
- Port knocking
  - a particular sequence of packets that are sent to specific ports, from the same ip addresses. Launch a root shell.

### Salami Attack
- Made up of many smaller attacks, each part is inconsequential by itself.

### Privilege Escalation
- run arbitrary code, get root access
- Exploit a program that runs with root access, exploited to launch a shell which has root access.
  - assignment 1
- example: Buffer overflow attack
  - obtain session id/cookie/password of another user to gain access to their priviledges

### Rootkits
- Hide the attacks tracks
- Parts
  1. Method for getting unauthorized root access on a machine
    - Exploit some known flaw on the system.
    - Often leaves behind a back door so the attacker can get back in, even if the flaw is patched.
  2. A means of hiding it's own existance.

- Stealth capabilities
  - clean up log messages
  - modify `ls` and `ps` so they don't report files / processes belonging to the rootkit
  - modify the kernel so that user programs can't learn about the root kit
- Sony XCP
  - Rootkit by Sony to protect their Cds from being ripped

Is it possible to detect a rootkit which uses zero-day vulnerabilities?
- It's very hard
- means you can't trust the output of any command
- no idea if it's actually been infected

### Keylogger
- log all of the user's keyboard inputs
- send the log back to the attacker

#### Application Specific
- Record only keystrokes associated with a particular app

#### System keyboard loggers
- record all keypresses
- anything on the system

#### Hardware keyboard loggers
- Works for any operating system
- limitation: need physical access to the machine

### Interface Illusions
- Assumptions that you make when you use a particular system
- Mental model can be exploited to make users do things that they didn't want.
  - Conflicker worm: Look like windows explorer icon, actually install the worm
  - Scroll bars: drag a progrm to the users startup directory (as well as scroll the page)
- How to defend against?
  - software / OS design decisions
  - **CTRL+ALT+DELETE**: always show the login screen, otherwise someone could write software to look like the login screen.
  - **Mobile OSs**: Android allows you to overlay anything on an app, iOS doesn't

### Phishing
- Looks like your visiting a legit website, but your not.
- Check the address bar + TLS/SSL cert
- Unusual emails and URLs

### Man-in-the-middle attacks
- individual that your communicating with isn't actually who you think it is.
- Someone could sit in the middle, intercept your communications, and pass it off to who ever you want.
- Could modify the packet contents to make the user do things that they don't want to do (without them knowing)

## Nonmalicious Flaws

### Covert Channel
- Creates a capability to transfer information through a channel that was never supposed to transmit that information
  - Coughing to cheat on an exam
  - use the number of spaces to encode binaries (2 spaces is a 1, 1 is a 0)
  - File allocation table: like a linked list
    - read the table, if you link to the next block then it's 1, if you skip: it's a zero.
    - Gives the person plausibile denyability, fragmentation actually occurs, could have just ended up that way.
  - Timing: add some delay for 1.

### Side Channels

> In computer security, a side-channel attack is any attack based on information gained from the implementation of a computer system, rather than weaknesses in the implemented algorithm itself (e.g. cryptanalysis and software bugs). Timing information, power consumption, electromagnetic leaks or even sound can provide an extra source of information, which can be exploited.

- watch how a system behaves when processing a particular piece of data.
- An attacker can learn information.
- Suppose it is faster to XOR `0001` than `abab` when encrypting a piece of data.
  - The time to encrypt can give the attacker information related to the key
- Checking passwords
  - check character by character
  - The farther you go into the loop, the longer it takes, the more characters correct.
