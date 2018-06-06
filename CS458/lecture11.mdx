# Lecture 6 - June 8, 2018

## website vulnerabilities
- user inputs can influence the execution of a web server (XSS, SQL injection, CSRF)
- CSRF: cause the user to take an action on a different web site, if they are logged in

### DoS Attack
- cut wire, jam signal
- overload network capacity
- point is to overload resources of the victim
- ping flood: nodes recieving a ping packet are expected to reply, overload the node
- ping of death: a malformatted ping packet, designed to crash the victem's computer
  - i.e. cause a buffer overflow
- smurf attack: spoof source address of ping packet, responses are redireted to the victim
  - broadcast this packet to all computers on the LAN, all responses will go the victim
- SYN Flood: exploit 3 way handshake
  - only perform the first 2 steps of the handshake
  - the client never ACKs, therefore a poorly implemented server may maintain the previous handshakes for a period of time
  - flood the server
- Fragmentation
  - take a large packet, divide into smaller fragments.
  - only send some of the fragments to the server, make it wait for the rest to arrive
- Craft packets so that they will fall into the same bucket of a hash table

For these attacks, the victim never gets the packets:
- black hole attack / packet drop attack
  - packets routed to their destination
  - packets take a series of hops, no way to know the route a packet will take.
  - routers communicate their cost to send a packet to a particular host, want to minimize this
  - malicious router can advertise a path with a low cost to the victim, simply drop all traffic going there.
- DNS attack
  - recall the malicious modification of DNS entries (cache poisoning)
  - this can cause packets to be redirected to the wrong host

Defences
- spoofing an IP address: check that the packet is well formed, correct packets
  - make sure source ip is within a particular range
  - but, you can simply spoof IPs within the range
  - policy related problem: difficult to take people off of the internet

#### Reflection and Amplication DDoS (Distributed)
- generate as little traffic as possible, create more traffic from unsuspecting nodes
- Amplification: a network node runs a service which responds with much more data than the query itself
- Reflection: Attacker spoofs the source address of the queries to the victim recieves the response

hard to combat:
- how to prove traffic is coming from innocent nodes
- hard to identify the true source because of spoofing

Most of the attacking machines don't know that they're doing it
- attack breaks in using trojan, some other exploit
- machine becomes a **zombie/bot** waits for command from attacker
  - A collaction of zombies is a **botnet**
- how to take out a classic botnet (one central command node)
  - kill the central command node
    - remove it's DNS entry
    - simply drop that traffic
- modern botnets
  - more complex: botnets are rented out for money, owners want to have income

- how to keep bots alive
  - use P2P architecture
  - have multiple bots designated to distribute updates
  - issue: bots generate alot of traffic
    - Domain Generation Algorithm: generates a large list of changing domain names, distribute to a subset of machines
      - way to cycle through domains, code to do this is inside the infected machines
    - to stop, have to take control of many domains
    - purposes is redundancy
  - Attacker can set the domain to expire after a short time, reregister the domain name with a new IP.

Do captchas help
- can bypass the captcha by other API
- still use techniques to exhaust the resources of the server

## Module 3 Review
- classification levels: Top secret, secret, confidential, unclassified
- For a valid lattice
  - partially ordered
  - lower upper bound
  - greatest lower bound
- Bell-La Padula
  - confidentiality
  - no read up
  - no write down
  - need to know rule: you can only know what you need to know, to prevent contamination
    - idea is to prevent leaks in the case of capture
  - Example 1
    - Subject: Top secret, (A, B)
    - Object: Top Secret, (A, B, C)
    - write: yes, not leaking any confidential information
    - read: no, the object has additional information about C
  - Example 2
    - Subject: Top secret, (A, B)
    - Object: Top Secret, (A)
    - Read: Yes
    - write: no, could leak information about B
  - Example 3
    - Subject: Top secret, (A, B)
    - Object: Secret, (A)
    - read: yes
    - write: no, leak top secret information
- Biba
  - integrity
  - opposite direction
  - no read down, no write up
  - example 1
    - Subject: Top secret, (A, B)
    - Object: Secret, (A, B)
    - Read: no
    - write: yes
  - example 2
    - Subject: Top secret, (A, B)
    - Object: Top Secret, (A, B, C)
    - Read: no
    - write: no
