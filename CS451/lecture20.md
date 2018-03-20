# Lecture 20 - March 20, 2018

## Back to graphs
- irregular structure
- irregular data access patterns
  - matrix
  - adjacency lists
- Algorithm iterations
  - iterate until algorithms converge
  - lots of ways to optimize

### Characteristics of Graph Algorithms
- Parallel graph traversals
  - local computations
  - pass messages along the edges
  - Recall:
    - Parallel BFS: Add 1 to distance, pass it on. Reducer: take the minimum distance. Each iteration expands the frontier by 1, until you've covered the whole graph
    - Pagerank: prob of random jump, Divide mass equally amoungst neighbours. Reducer sum everthing up
      - Additional map to handle the missing mass at the edges
- Iterations
  - MapReduce is expensive at each iteration, high startup time, wasteful checkpointing at each step
  - Spark: Keep RDDs in memory, pipeline results
    - recall that the adjacency list is static, cache this
    - Can join in the adjacency list with the pagerank vectors

## BigData processing in a nutshell
Lots of the same tricks, applied in different contexts

- partition
  - Hash partitioning on the verticies
  - Range Partition based on some underlying linearization (ex. lexicographic sort urls: `www.cnn.com` -> `com.cnn.www`)
    - Then say, split into 10 partitions.
    - All of the pages of the same domain are contiguous, many more itra-domain links than inter-domain links. Most of the destinations are on the same domain, therefore they will likely belong to the same partition.
      - For example, consider a navbar on a webpage.
      - Social Networks: Demographics, sort by the country that your from
      - Geodata: Use space filling curves
        - regular graph, geographical regions are connected by their neighbours
        - Space filling curve: Some way to go through the entire structure
        - Z-Order Curve: Traverse in a z shape. Popular because it's easy to implement (write out x and y in binary and interleve the digits it's the pattern you get)
        - Hilbert Curve: Similar idea, but harder to compute.
      - In the general case: hard problem
- replication
- reduce cross-partition communication

### Schimmy Design Pattern
- Implementations have 2 data flows:
  1. Messages
  2. Structure
- Basic idea: Merge join between the graph structure and messages
  - S and T have to be partitioned in the same way (copartitioned)
- Can work with the limitations of MapReduce

### How to partition a general graph?
- If you don't have some underlying property to rely on it's hard
- **graph Coarsening**: Try to compress the graph, merge dense areas together, but keep the general structure
  - This gives to a smaller graph
  - Do this iteratively, graph likely won't fit into memory, repeat until it does
  - Run whatever partitioning algorithm you want
  - uncoarsen
  - **Chicken-and-egg problem**
    - Need to know where the dense local regions are
    - to know this, you have to traverse the graph
    - but to traverse the structure efficiently, you need the local structure
      - Then nodes may be on different machines
    - but if i have the local structure, then the problem is solved!
- For industry: go for the easy solution that takes advantage of the specific domain
  - Or default to hash partitioning for the general case, as it's not worth the trouble

### Problem: Partitioning will break edges
- Partitions on separate machines will likely have edges going between them
  - Unless you have disconnected regions in your graph
- The local partitions are fast, but the results between the partitions will be slow
- Add a final tweak: For the state-of-the-art
  - Allow message passing to be async, communicate periodicly (without worrying about the other nodes)
  - The frequency of communiation will have effects on the performance and correctness of the algorithm
  - Determining this is domain dependant.

### Graph Frameworks

It's not naturally to think of graph as joins, Message idea and propogration is more intuitive. Frameworks have been developed to allow thinking like a vertex

#### Pregel: Computational Model
- in each step, recieve message from previous step
- execute some function at each vertex
- Write some vertex program that recieves messages
- Framework orchastrates the delivery of the mesages
- **Bulk Synchronous Parallel**:

##### Impementation
- Master-Worker
  - master is responsible for maintaining the clock cycle
  - points to checkpoint periodically (gives robustness)

### Giraph Synchronization
- Does not do the async iterations
- Giraph forces global synchronized communication
- The reason they don't do this is because they want to be a general purpose graph framework (And always be correct), in order to do async you have to decide frequency for correctness.
- Async frequency is always algorithm dependent.

### Alternated: GraphX
- Spark for Graphs
- Use RDDs! RDDs for the vertex, one for the edges
- Triplet: Vertex, Edge, Vertex
