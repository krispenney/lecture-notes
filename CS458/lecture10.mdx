# Lecture 10 - June 4, 2018

## Network Security

- All traffic is broken up into individual packets
- No way to know / no control the path that a packet will take across the Internet.

### TCP/IP

- TCP/IP is the dominant suite of protocols
  - defines what happens in case of packet loss, out of order, etc.

- Client Application <-> Server Application
- Link layer is the physical medium (Ethernet, Wi-Fi)
- origionally designed for universities, not designed with security in mind
  - parties that knew and trusted eachother
  - Design only addressed non-malicious errors (packet drops, out of order)

### Threats in Networks

#### Port scanning
- to distinguish between different applications running on the same machine, use ports
- Services typically run on ports that are predefined
- ex. web servers typically port 80

Attackers can query specific ports, try to determine which applications they're running. Bad if an attacker has a known exploit, wants to try to use it on other machines.
- Loose lipped applications, unnessary details that can help the attacker
- Non-malicious, non-confidential data. The attacker could eventually find them out anyway.
  - ex. version information
  - Password reset fields, give indications of real users
- Tool: `nmap` identify open ports

#### Intelligence Gathering
- social engineering:
  - exploit weaknesses in humans
  - ex. pretend to be someone else, try to get their information / get them to do something.
- find information of Facebook pages, Google
- Dumpster diving
  - data not destroyed, when things are thrown away
  - not shreading, wiping harddrives etc.

Attacker can continue to collect new information, go back to social engineering. Provide more, unnecessary information to be more convincing, get larger attacks.

#### Eavesdropping and Wiretapping
- owners of packets don't know the path a packet will take to it's destination
- owners of nodes could look at all of the traffic running through their nodes
  - modify / fabricate packets
  - bad for unencrypted packets
- bad before HTTPs
- eavesdrop on traffic going across links
- passive attacks
  - communication happens to be sent to an attacker
  - mistyped emails

##### Communication Media
- Copper cables
  - inductive properties allow data to be captured without physically modifying the cable
  - could also splice the cable
- Optical fibers
  - signal loss when splicing, could be detected.
- Wi-Fi
  - wireshark, attackers can read
  - special antennas allow long distance capturing

##### Misdelivered Information
- LAN
  - connects all computers on the same network (workplace, uni)
  - clients on the network might recieve packets that they weren't supposed to recieve. Network cards typically drop these by default.
    - use a packet sniffer

#### Impersonation
- impersonate someone by stealing their password
  - guess (devices with defaults)
    - Force users to change the default password
    - could change it to the network password
  - sniff it
    - especially unencrypted
  - social engineering: try to reset or change their password
- exploit trust between machines and accounts
  - remote accounts: specify remote users acting as local users without passwords
    - if an attacker breaks into machine y, can gain access to machine x without a password
    - private keys in memory
  - use biometrics to prevent
    - keystoke based method: each individual can have a specific typing signature. Difficult to copy.
  -

#### Spoofing
- some object acts as another
- URLs spoofing
  - typos, register urls (`uwaterlo.ca`)
  - ambiguous: add hypens, underscores
  - Use numbers
  - how to defend: public keys, organizations can register similar urls
    - password managers could spot it
- used for phishing attacks

##### Session Hijacking
- server maintains sessions for clients
- clients hold a cookie to maintain their session
  - If an attacker can steal this cookie, can use their session
- problems
  1. sequence numbers can be guessed by attackers
    - make them less predictable, use a sort of HMAC scheme.
  2. man in the middle
    - host C can send a reset packet, cancelling A's connection, C could sit in between A and B.

##### Traffic Analysis
- mere existance of communication (even encrypted) is sensitive
  - whistleblowers, military, CEOs
- You cannot encrypt the ip addresses of packets (need to know where to send the packets). This can aid analysis.
  - Provide additional information, to see who is communicating
- Use tech like Tor (later in the class)

##### Integrity Attacks
- Modify packets while their being transmitted
  - Can be detected using SSL/TLS
- replay previous packets
- DNS cache poisoning
  - map host names to numeric addresses
  - uwaterloo.ca -> 129.29.128.1
  - attacker can create false mapping
    - man in the middle: modify the DNS response
    - attacker acts as a website (Google), tells DNS servers that it's address has changed.
      - Typically need a signed certificate from the party

#### Protocol Failures
TCP/IP assumes all nodes implement protocols properly

- ask senders to slow down traffic, deal with network conjestion
  - attacker could ignore, send more, DDOS as server begins to drop packets
- Implementations may not check if a packet is not well formed, overflow systems
  - recall: Heartbleed
  - protocols are complex, rare cases may result in undefined behaviour

#### Web site vulnerabilities
- visiting a webserver returns HTML
- attacker can send bad inputs (incomplete mediation)
  - SQL injection, XSS, Buffer overflows
  - Get access to unauthorized data.
- HTTP is stateless
  - client may need to maintain some state (in URL params, cookies, forms)
  - attacker can try to modify the state (if no server mediation, only client-side)

