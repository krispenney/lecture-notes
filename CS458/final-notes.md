# Final Exam Notes

## Network Concepts

### Characteristics of the Internet
- No single source controls
- Traffic flows through nodes owned by various entities as it travels from source to destination
  - End notes can't control through which nodes traffic will flow
  - Traffic is divided into individual packets
  - each packet could be routed along different paths
- Different types of communication links
  - wired vs. wireless
- TCP/IP protocols
  - packet format
  - routing of packets
  - deal with packet loss

#### TCP/IP Protocol Suite
- Application Layer
  - HTTP, FTP, email, SSL
- Transport Layer
  - TCP or UDP
- Network Layer
  - IP
- Link
  - Ethernet, Wi-Fi

Transport and network layers were designed in the 70s to connect different universities together, who knew and trusted each other. Therefore, the original design addressed non-malicious errors (ex. dropped packets), but not malicious errors.

## Threats in Networks

### Port Scan
- To run multiple (networked) applications on the same server, run each of them on a different port.
- An attacker could attempt to identify which applications/services are running on a particular machine by sending queries to a series of ports.
  - can identify based on loose-lipped applications (which tell you what they are) or how a particular protocol is implemented.
  - Loose-lipped systems reveal non-confidential information, which could facilitate an attack.
    - reveal info about the system's OS
    - reveal if a particular user id is valid
      - Different error messages for valid user-id and non-existant user id (ex. Forgot Password form).
    - web server version information
- **Goal of attacker**: is to find an application with remotely exploitable flaws.
  - ex. Early versions Apache web server were known to be vulnerable to buffer overflows

### Social Engineering
- Attacker gathers sensitive information from a person, often by impersionating someone within the organization who needs help "solving a problem".
  - Exploit the other person's willingness to help
  - "I forgot my password"
- Dumpster Diving
  - literally see what people discard
- Eavesdropping on oral communciation
- Google it
  - see what people post publically on the Internet
- Look at the victim's Facebook profile

### Eavesdropping and Wiretapping
- Owner of an Internet node can monitor the packets flowing through it
  - **Passive wiretapping**: eavesdropping
  - **Active Wiretapping**: involves the modification or fabrication of communication
- Can also eavesdrop while packets are flowing across a link
- The victim initiates accidental communication with the attacker's node
- **Rule of thumb**: assume that your communication is wiretapped

### Communication Media

Each of the following attacks are feasible, but require the attacker to be physically present:

- Copper cables
  - a physically close attacker can eavesdrop without making physical contact (inductance)
  - the cable can also be cut and a secondary cable can be spliced in
- Optical Fiber
  - no inductance
  - signal loss by splicing is likely detectable
- Microwave/Satellite communication
  - signal path at receiver tends to be wide, so an attacker close to the receiver can eavesdrop

- **Wi-Fi**
  - Can be intercepted by anyoone with a mobile device, no need for suspicious additional hardware

#### Misdelivered Information
- Local Area Network
  - Connect all computers within a company or organization
  - A packet may be sent to multiple nodes, not just the intended receiver
  - By default, a network card should ignore wrongly delivered packets
  - Using a **packet sniffer**, an attacker can capture these packets
- Email
  - wrongly addressed emails
  - accidently Reply-to-all

### Impersonation

An individual can be impersonated online by stealing their password
- guessing attack
- Exploit default passwords that haven't been changed
  - routers
- sniff password packets as they are being transmitted between network nodes
- obtain it / reset it via social engineering

Exploit trust relationships between machines / accounts
- A machine says that users on different machines can login to it as a particular user:
  - Example: ssh keys
  - Attackers can break into the other machine and then login to your machine
    - Or masquerade as the other machine

### Spoofing

An object masquerades as another one
- node
- person
- web page
- etc...

They are often used in phishing attacks, session hijacking, and man-in-the-middle attacks

#### Session Hijacking

The TCP protocol sets up state at the sender and reciever end nodes and uses this state while exchanging packets:
- ex. sequence numbers for detecting lost packets
- an attacker can hijack such a session and masquerade as one of the endpoints

Web servers sometimes have client hold a cookie to re-identify the client for future visits
- The attacker can sniff or steal the cookie and masquerade as the client

**Man-in-the-middle** attacks are similar, expect the attacker becomes a stealth intermediate node, not an end node.

### Traffic Analysis

Sometimes, the existence of communication between two parties is sensitive, and therefore should be hidden
- whistleblower
- military environments

Traffic analysis is made simple due to the fact that TCP/IP specifies that packets contain unique addresses for a packet's sender and reciever nodes.
- An attacker can learn these addresses by sniffing packets

### Integrity Attacks

An attacker could modify pacets while they are being transmitted, by:
- changing the payload
- change source/destination addresses
- replay previously sent packets
- delete/create packets

**Note**: Integrity can also be effected due to non-malicious causes
- line noise, network congestion, software errors
- TCP/IP will likely detect environmental problems, but fail to detect the presence of an active attacker

DNS cache poisoning
- DNS maps host names -> ip addresses
- `www.uwaterloo.ca` -> `129.97.128.40`
- An attacker can create an incorrect mapping

### Protocol Failures

The TCP/IP protocol assumes that all nodes implement the protocol faithfully
- Example: The protocol specifies a mechanism where the sender node should slow down if the network is congested. A malicious node could simply ignore these requests for Denial of Service

Some implementations may not check that a packet is well formed
- Ex: Not checking if the packets true length differs from it's declared length could lead to a buffer overflow.

These can be disastrous if all implementations are from the same vendor or based on the same code base.

**Note**: Due to the complexity of these protocols, behaviour is special cases may have undefined behaviour.

It's also worth mentioning that some protocols themselves are fundamentally flawed, even if the implementation of them is perfect.
- WEP

### Website Vulnerabilities

When a user visits a web server (via a URL), HTML is often returned which tells the browser how to display the web page, as well as how to interact with the web server.
- An attacker can also examine this code for vulnerabilities

An attacker could send a malicious request to a web server via an unconventional URL
- Try to trigger a buffer overflow (really long URL)
- Invoke a shell / other programs
- manipulate a server side script (`www.google.com/../../../../etc/passwd`

The HTTP protocol is stateless, therefore a web server will often require the client to store a cookie to maintain state (ex. for authentication purposes).
- An attacker could attempt to submit modified state information
- This is bad if the web server fails complete mediation (checking validity)

Cross-site Scripting (XSS) or Cross-site request forgery (CSRF)
- code injection
- **XSS:** The attacker inserts their own HTML code into someone elses web page. For example, by submitting the to comments section of a website. This could be to potentially steal the cookie of anyone who views that comment (`http://attacker.com/cookie=...`)
- **CSRF**: Code attempts to perform malicious actions at some web site that the user may be logged into (ex. tries to transfer money to their bank)

### Denial of Service (DOS)

Disrupt availability:
- Cut a wire, jam a wireless signal
- Flood a node by overloading it's internet connection / processing capacity
- **Ping Flood**: A node which recieves a ping packet is expected to generate a reply, an attacker could overload a victim's ability to generate replys.
- **Ping of Death**: Attempt to crash the victim's machines via a malformatted packet.
- **Smurf Attack**: Spoof the source address of a sender node in a ping packet by setting it to the victim's address.
  - Broadcast the ping packet to all nodes on a LAN.
- **SYN Flood**
  - TCP initializes state by having both nodes exchange packets (SYN, SYN-ACK, ACK)
  - Server enqueues SYN from the client and dequeues it when the corresponding ACK is received.
  - Attacker: Send many SYNs, no ACKs
- **Black Hole Attack** (Packet drop attack)
  - Each router informs other routers of it's cost to reach a set of destinations
  - A malicious router can announce a low cost for victim destinations and just drop thoses packets
- **DNS Attacks**
  - DNS cache poisoning can lead to packets being routed to the wrong host
- **reflection and Ampliciation DDoS Attack**
  - Attack where the victim is flooded with legitimate looking traffic that originates from unsuspecting network nodes on the internet
  - **Amplification**: A vulnerable network node runs a service that responds to queries with significantly more data than the query itself
  - **Reflection**: The attacker can spoof the source address of the queries to be a victim's so the large responses are reflected back to them

#### Distributed DoS
- If there's one machine, then it would be possible to identify and drop it's packets.
- Instead, have lots of attacking machines. Have them participate without knowledge of their owners
  - Break into machines uing Trojans, buffer overflows, or etc. and install malicious software
  - Turn the target machine into a **zombie/bot**, waits for attack commands from the attacker.
    - Bots are used for different purposes (spam, DDOses)
  - **botnet**: A network of bots
    - Old botnets were made mostly for fame
    - Modern are used for profit (ex. via renting them out)
  - Hard to stop
    - Viruses/worms/trojans propogate, spread to new machines
    - hide from owners of the computer
    - Code modifications make them difficult to detect (ex. via signatures)
  - Distributed, dynamic, redundant control structure
    - P2P system for updates
    - **Fast Flux**: Single host name maps to hundreds of addresses of infected machines, machines proxy to the mothership, and are constantly swapped in and out to avoid detection.
    - Domain generation: infected machine generates a large set of domains (change every day), contact a random subset of names for updates. To stop, authorities would have to take control of a large amount of constantly changing domain names.

### Active Code

To reduce the load on a server, it may ask clients to execute code on it's behalf
- Java, JS, Flash
- Can be dangerous for the client if the code is malicious
- **Privileged code**: App will run with unrestricted access
- **Sandboxed code:** limit what an application can access, intention is to protect your computer + data
  - But this code still takes up CPU cycles
  - If an app can break out of the sandbox (i.e. trick the user into giving you permission), can do whatever it wants.

## Network security Controls

- Use controls against security flaws.
- Perform complete mediation, always check inputs, trust nothing from clients
  - Favor whitelists over blacklists

### Segmentation and separation

Don't invoke all servers on a single machine, then if one machine is broken into only some services will be affected

### Redundancy

Avoid single points of failure, ensure that important services are deployed in a redundant way on multiple machines, ideally with different software to have **genetic diversity**
- Redundant servers should be kept in-sync so backup servers can easily take over

### Access Controls

Maintain access control lists for routers
- All traffic of a company typically goes through a single router
- A router ACL can drop packets in case of a flooding attack
- **Firewalls:** designed to filter traffic, also taking into account other information than just packet addresses

## Firewalls

All traffic in and out of a company has to go through a small number of gates,
- Wireless access points should be outside of the firewall
- **Choke Points**: examine traffic (especially incoming), may refuse access
  - Whitelist vs. Blacklist strategy
- **Note**: Firewalls don't protoect against attacks on company hosts that originate from within the company.

### Packet Filtering Gateways
- Make decisions based on the header of a packet (ignore the payload)
- Drop spoofed traffic: any packet that originates from UW whose source address doesn't match

### Stateful Inspection Firewalls
- Keep state to identify packets that belong together
  - When client from inside the company opens a TCP connection to a server outside the company, firewall must recognise response packets and let only them through.
- Much more expensive than Packet filtering
- IP layer can fragment packets, meaning the firewall must re-assemble packets in order to inspect

### Application Proxy
- Client talks to the proxy, the proxy talks to the server
- Proxy blocks all traffic except for the required application
- **Forward Proxy**: User within the company wanting to access server outside the company.
- **Reverse Proxy**: User outside the company wants to access sever inside the company
- Can perform strong user authentication

### Personal Firewalls
- Run on an individual's computer
- Typically whitelist approach: block everything unless explicitly allowed
- Protect against attacks on servers running on the computer

### Demilitatized Zone (DMZ)
- Subnetwork that contains an organization's external services (accessible to the internet)
- Have internal and external firewalls
  - External: Protect DMZ
  - Internal: Protect the internal network from attacks originating from within the DMZ

## Honeypots / Honeynets

Setup a trap to try to catch attackers in the act.
- System has no production value, so any activity is suspicious
- Observe how to attacker attempts to attack your system, stop them from attacking the real system
- Attacker shouldn't know that the system they're attacking is fake
- **Low Interation**: Emulates multiple hosts, running different services
  - limited amount of information gathering possible
  - easy to maintain, but easier for an attacker to detect
- **High Interaction**: Deploy real hardware and software, install keylogger
  - harder to deploy, but provides better logging capabilities

## Intrusion Detection Systems (IDS)
- Firewalls don't protect against inside attackers or insiders that make mistakes, IDS are the next line of defense
- IDS monitors activity to identify malicious or suspicious events
  - monitors sensors
  - analyze
  - potentially take action
- **Host Based**
  - Run directly on a host to protect that host
  - exploit lots of information
  - but, miss out on information available to other (attacked) hosts
  - **Note**: If the host is subverted, the IDS is also compromised
- **Network Based**
  - Run on a dedicated node to protect all hosts on the network
  - can only use information available in packets
  - harder to compromise
- **Signature Based**
  - Known attacks have a signature, try to detect them
  - Fails for new attacks, or modified versions of existing attacks (polymorphic)
- **Heuristic/Anomaly Based**
  - Look for behaviour that is out of the ordinary
  - False positive / negative rate

## Cryptography
- **Cryptography**: Secret writing. Turn plaintexts into ciphertexts
- **Cryptanalysis**: Breaking secret messages, recover the plaintext from ciphertext

Components:
- **Confidentiality:** prevent Eve from reading Alice's messages
- **Integrity**: Preventing mallory from modifying Alice's messages without being detected
- **Authenticity**: Prevent Mallory from impersonating Alice

**Kerckhoffs' Principal**: The security of a crypto system should not rely on a secret that's hard to change
- Make the class public information
- The system is at most as secure as the number of keys
- Eve can try them all until she finds the right one
- **Strong Cryptosystem**: Best attack is bruteforce

### Secret Key Encryption (symmetric)

Alice and Bob use the same key to encrypt and decrypt their messages

**Perfect Secret Key: One Time Pad**
- Generate a random bit string, as long as the message, encrypt and decrypt are just XOR.
- Must only use each key once, and truely random

**Computational Security**: It is certain that they can be broken, given enough time.
- At worst, the attacker has to try every key (this can take a very long time)

#### Stream Ciphers

Same as a one time pad, but use a pseudorandom keystream instead of truely random.
- Can be very fast, good to send lots of data securely
- If you change a single bit of the plaintext, that bit will change in the ciphertext

#### Block Ciphers

Operate on blocks of bits (64 or 128 bits)
- Key needs to be as long as a block
- Don't use ECB mode (exposes patterns in the plaintext)

### Public Key Crypto

- Every party has a public and private key
- Allows parties to exchange information without needing to establish a prearranged shared secret
- Needs a longer key (2048+ bits) to obtain security
- Slower for longer messages

#### Hybrid Crypto
- Use public key crypto to establish a session key
- Use a block cipher using the session key

## Integrity

Use a cryptographic checksum to tell if a message has changed in transit.

### Cryptographic hash functions

A hash function accepts an arbitrary length string `x` and computes a fixed length string `y = h(x)` <- this is called a **message digest**

Properties
- **Pre-image resistance:** given `y = h(x)` it should be infeasible to find `x`.
- **second pre-image resistance**: given `(x, h(x))` is should be infeasible to find an `x'` such that `x != x && h(x) == h(x')`.
- **Collision resistance**: Infeasible to find distinct `(x, x')` such that `h(x) == h(x')`

**Note**: Hash functions can only provide integrity guarantees when there is a secure way of sending and storing the digests.
- on paper

### Message Authentication Codes

Have a symettric key that is used to compute a signature of a message. If a message is changed by an unauthorized party, they should not be able to compute the MAC.
- Encrypt-Then-MAC: send `(E(M), MAC(E(M)))` to Bob

**Repudiation**: Deniability of having sent a message
- using a MAC scheme Bob could sign an arbitrary message and claim that Alice had signed it. Likewise, Alice could sign a message, but deny doing so.

### Digital Signatures

Digital signature schemes provide non-repudiation, can't deny having sent a message.
- similar to public key crypto
- Private signing key, public verification key
- This is slow for large messages, instead Alice can sign the hash of a message.

The (signature, verification) pair is long lived, while the (encryption, decryption) key pair is short lived.
- Provides forward secrecy: If ciphertexts compromised in the future, this gives the ability to not leak all of the plaintexts as they use different encryption keys

### Key Management

Key management is difficult, need to ensure that you have an authenticated copy of the message recipient's public key (encyption or verification).
- **Manual Keying**: Can know it personally
- **Web of Trust**: Trust a friend to tell you
- **Certificate Authority**: Trusted third party
  - Everyone has a copy of a CA's verification key in their browser
  - Alice sends her public keys to the CA who signs it with their verification key
  - Need the verification key of the root CA in order to verify the certificate chain

## Security Controls using Cryptography

Any secrets need to be available to real users, but not to adversaries.
- secret key crypto is problematic because if an attacker obtains a key they can decrypt/send messages.
- Public key: devices can only hold te public key for encryption and verification. e.x. devices (iOS or BlackBerry) will only install / execute code if it's signed by the manufacturer.

**Encrypted Code**: Research into allowing processors to execute only encrypted code, decrypt the instructions before executing them.

**Encrypted Data**: HDD encryption protects lost or stolen devices.
- doesn't protect against users who have legitimate access to device / someone who installs malware
- Someone could also extract the decryption key from memory

Primary usage of cryptography is in **Network security and privacy**
- People who you can only interact with over a network are less trustworthy, may not be who they claim to be
- Encryption is used throughout the network stack for both security and privacy.

### Link Layer Security: Protect Local Area networks

- WEP wireless protocol
  - Intended to provide (failed on all):
    - **Confidentiality**: Prevent an attacker from learning the contents of your wireless traffic
    - **Access control**: Prevent adversaries from using your wireless network
    - **Integrity**: Prevent unauthorized modifications to data sent on the network
  - IV was 24-bits long: can easily be guessed
  - Checksum used was linear: `c(M ^ D) = c(M) ^ c(D)`
    - An attacker can generate modifications, compute the checksum independently and XOR it to the message checksum (still a valid checksum)
  - By obtaining a single plaintext/ciphertext pair, the attacker obtains the IV, can generate modifications, compute the checksum and XOR with `RC4(v, k)`
    - The authentication protocol gives this pair for free, watch someone else complete the handshake
- WPA protocol
  - Short-term replacement for WEP
  - Increased length of IV
  - Changed checksum function to a real MAC
  - Frequent key changes
- WPA-2 protocol
  - replacement for WPA
  - Uses AES for authenticated encryption

### Network Layer Security: Want security across networks

Ideally want end-to-end encryption, typically accomplished with VPNS
- connect two+ networks that are physically isolated, make them appear to be a single network
- Attacker between the networks should not be able to read or modify traffic flowing across the VPN
- One host on each side is the **VPN gateway**
- traffic designated for the other network is sent to the local VPN gateway
- local gateway encrypts traffic with integrity, sends to the remote gateway (via **tunnelling**)
- remote gateway decrypts the message and sends it to it's appropriate destination.

#### Tunnelling

Sending of messages of one protocol inside messages of another protocol as the payload. Outside of the usually nesting sequences
- TCP-over-ip: **NOT TUNNELLING**
- IP-over-TCP: **TUNNELLING**

#### IPsec

One method of setting up a VPN

Modes
1. **Transport Mode**: Useful to connect a single laptop to home network, only contents of the original packet are encrypted and authenticated.
2. **Tunnel mode**: Useful to connect two networks
  - The contents and the header of the original packet are authenticated and encrypted, result is placed inside a new packet which is destined for the remote VPN gateway.

#### Transport-Layer Security and Privacy: Send individual packets securely from one network to another

Transform arbitrary TCP connections to add security

**Main transport layer security mechanism**: TLS
- Client connects to server, indicates it's speaking TLS,
- server sends it's certificate to the client and selects the ciphersuite to use
- Client validates the server's certificate
- Client and server run a key agreement protocol
- communication proceeds using the chosen symmetric and MAC schemes.

Security properties provided by TLS
- Server authentication
- Message integrity
- Message confidentiality
- Client authentication (optional)

Very successful: comes installed in browsers, no user requirements

**Main transport layer privacy mechanism**: TOR
- Also want to protect the metadata of messages
  - Who is sending the message
  - hide the existance of a message
- Tor nodes -> **onion routers**
- Alice establishes a connection with a Tor node, does a key exchange
  - Alice tells node 1 to connect to another node (via tunneling), does another key exchange
  - Alice tells node 2 to connect to another node (via tunneling), does another key exchange
  - The final node connects to the website
- Alice has: `(k1, k2, k3)`
  - to send a message send `E(E(E(M, k3), k2), k1)`
  - Node 1 decrypts and sends to the next node
  - node 2 decrypts and sends to node 3
  - node 3 decrypts and sends to the website
- Replies are sent in reverse from the website back to Alice, node send backwards and encrypt.
- **Note** The connection between n3 and the website is unencrypted, to obtain this end-to-end should also be used (HTTPs)

Tor provides **anonymity** in TCP connections
- **unlikably**: long term
  - no long term identifier for Tor users
  - Connections from a Tor server today and tommorrow, can't tell if they're the same person
- **likably**: short term
  - two connections in quick succession from the same Tor node are likely the same person

#### Nymity Slider

Transactions can be placed on a continuum according to the level of nymity
- **Verinymity**: Gov ID, SIn, credit card
- **Persistent Pseudonymity**: many blogs
- **Linkable anonymity**: prepaid phone cards, loyalty cards
- **Unlinkable anonymity**: cash payments, Tor

Easy to modify a system to have a higher levl of nymity, hard to lower
- It's easy to collect more information (add a loyalty card to cash)
- Design systems with a low level of nymity, raise if needed

## Application Layer Security and Privacy
- Many applications want true end-to-end encryption (machine-to-machine)

### Remote Login (ssh)

