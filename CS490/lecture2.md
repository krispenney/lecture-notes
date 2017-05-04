# Lecture 2 - May 4, 2017

Software architecture: blueprint for the house
Infrastructure: Physical

### Host-Based architecture (Master Slave)
- Mainframe + dumb terminal
- Eventually split the workload between the client and the server
- Replaced by Peer to peer, no more server

### Application Layers
Any application can be split into three layers.
1. Presentation
2. Application processing
3. Data management

N - Tier: How many machines it takes to run a unit of processing

Metcafe's Law - Network Effect

Law of diminishing returns
- As you add more clients, the server can become backlogged
- P2P doesn't suffer from this.


Fat Client
- Con: Don't own the application logic
- Application logic runs on the client, makes updates harder


Thin Client
- Don't do anymore than I/O and present

App
- More features
- harder to maintain (multi-platform)

Website
- Easier to maintain
- Less convenient

