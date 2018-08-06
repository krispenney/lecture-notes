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
