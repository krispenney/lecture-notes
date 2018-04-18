# Final Notes

## MapReduce Algorithm Design

### Common Theme

Parallelization challenges come from (sharing state):
- Need to communicate partial results
- Need to access shared resources
- **Layer of abstraction**: The datacenter is the computer
  - Allow the developer to avoid system level details.
  - dev specifies the computation that needs to be performed
  - framework handles the actual execution
- Scale out, not up
- assume that components will break
- move processing to the data, code is much smaller
- process data in sequential order, avoid random access (which is expensive)

### MapReduce Runtime
- handle scheduling: assign workers to map and reduce tasks
- move processes to data
  - Start up worker on nodes that hold the data.
- handles synchronization
- handling errors and faults
- gotchas
  - avoid object creation (expensive)
  - get data to maps and reducers
    - via job config params
    - Side data: distributed cache, read from HDFS in setup.

### Business Intelligence
Organizations should retain data resulting from carrying out it's mission. Exploit those insights to benefit the organization.

#### Virtuous product cycle: Generate revenue
1. a useful service
2. analyze user behaviour to extract insights (data science)
3. transform insights into actions (data products)
4. feedback

### Cloud Computing
- Utility computing: computing resources as a metered service, pay as you go
- cloud makes it easier to start companies that generate big data, avoid ownership of the data
- everything as a service

### Namenode Responsibilities
- managing the file system namespace
- coordinating file operations
- maintaining overall health

files are divided into many splits, RecordReaders act as a cursor, passed to the Mappers.
- the splits can be arbitrary, down the middle of a record
- RecordReaders always start reading from a complete block, may keep reading over the edge of a split to capture the last record.

### Distributed GroupBy in MapReduce

#### Map side
- map outputs are in memory in a circular buffer
- when buffer reaches threshold, contents spilled to disk
- spills are merged into a single partitioned file (sorted by partition)
- combiners run during merges

#### Reduce Side
- map outputs are copied over to reducers
- sort is a multi-pass merge of map outputs (in memory, on disk)
- combiner runs during the merges
- final merge pass goes directly into reducer

#### Design Patterns
- all algs must be expressed in m, r, c, p
- no idea when things run, what order, which input a worker is processing
- avoid: object creation, buffering
- local aggregation: synchronization kills communication, kills performance, reduce the number of intermediate pairs that need to be processed.
  - in-mapper combining: fold combiner into the mapper, preserve state across multiple map calls.
    - pros: speed
    - cons: need to explicitly manage memory, order-dependent bugs
- combiners are optional optimizations, may br run 0, 1, or multiple times
  - should not impact correctness

##### Pairs vs. Stripes
- **Pairs:** Utilize the key as a pair, secondary sorting
  - pros: easy to implement + understand
  - cons: lots of intermediate pairs, combiners dont really work
  - may need custom sort order, have certain pairs show-up first `(a, *)`
    - pull values as part of the key for proper sorting
- **Stripes:** Group pairs into associative array
  - pros: less sorting and shuffling, can use combiners (element-wise operations)
  - cons: harder to implement, more complicated object, data structure manipulations,

tradeoffs:
- developer code vs. framework (sorting, grouping)
- number of kv pairs
- size + complexity of each kv pair: de/serialization overhead

| Pairs | Stripes |
|-|-|
| more kv pairs | less |
| less combining | more combining |
| more sorting | less sorting + shuffling |
| simple reduce aggs | complex (slower) aggs |

### Pig
- write in a higher level language, run a series of MapReduce jobs.

Common model:

``` pig
LOAD # load from HDFS
FOREACH ... GENERATE # per tuple processing
FILTER # discard unwanted tuples: (map)
GROUP / COGROUP # group tuples
join # relational join (reduce)
STORE # write back to HDFS
```

- extend PIG via user defined functions (UDFs) in any language

### Problems with MapReduce
- always have to go back to HDFS
- slow
- Dryad: Graph processing framework
  - abstractions for vertex-to-vertex communication

## Spark
- based on **Resilient Distributed Datasets (RDD)**
  - immutable, partitioned
  - perform transformations, lazy
  - actions, trigger the execution
- RDDs don't have to be written back to HDFS, can chain operations
- fault tolerance: RDDs can be regenerated from the operations

- why does it work
  - associativity: group operations in any way: `1 + 3 + 2 = (1 + 3) + 2`
  - commutativity: swap order of operands however you want: `(2 + 1) + 3 = 3 + (2 + 1)`

### Monoids
- semigroup: (M, operator)
  - ![latex-59267102-e735-4833-acf7-81c6f5ce04ae](data/final_notes/latex-59267102-e735-4833-acf7-81c6f5ce04ae.png)
- monoid: Semigroup + identity operation
  - ![latex-a52425e5-7fc0-44e4-b72d-6e641c61b452](data/final_notes/latex-a52425e5-7fc0-44e4-b72d-6e641c61b452.png)
- commutative Monoid: monoid + commutativity
  - ![latex-0715c96e-cbe7-46c0-8331-7f98b9e73a9b](data/final_notes/latex-0715c96e-cbe7-46c0-8331-7f98b9e73a9b.png)
- when you can't utilize monoids: sequence computations by sorting

## Analyzing Text

- Language Models: ![latex-7c16207a-fe5c-4b87-84bf-f121734bbd01](data/final_notes/latex-7c16207a-fe5c-4b87-84bf-f121734bbd01.png)_
- Use Markov Assumption to limit history to a fixed number of words: ![latex-a2d8accd-53b4-4afb-bd4c-d6be9064e44a](data/final_notes/latex-a2d8accd-53b4-4afb-bd4c-d6be9064e44a.png)
- ![latex-0d72a8cb-f85f-45c3-abad-e8cc4f2a2a51](data/final_notes/latex-0d72a8cb-f85f-45c3-abad-e8cc4f2a2a51.png) unigram language model, ![latex-e3a76a33-8713-4fe3-8998-452737079b0a](data/final_notes/latex-e3a76a33-8713-4fe3-8998-452737079b0a.png): bigrams
- Compute **Maximum likelihood estimates (MLE)** (count + divide)
  - ![latex-435e345d-bd50-4702-a5c0-544349b3576f](data/final_notes/latex-435e345d-bd50-4702-a5c0-544349b3576f.png)
- **Smoothing**: Want to avoid zero probabilities
  - Laplace: add 1 to all counts
  - Jelinek-Mercer smoothing: weighted linear combination of lower-order models.
  - Kneser-Ney: discounted model with special continuouation n-gram model. Number of different contexts ![latex-4cb665ab-0a1b-4d1a-af07-4476d40a9fb8](data/final_notes/latex-4cb665ab-0a1b-4d1a-af07-4476d40a9fb8.png) has appeared in.
  - Stupid backoff: use the higher order language model if greater than zero, otherwise fallback to lower order models.
    - Solve the problem by throwing lots of data at it.
- Bayes rule: ![latex-042a1eff-605e-4889-86bc-ad4988601c96](data/final_notes/latex-042a1eff-605e-4889-86bc-ad4988601c96.png)

## Document Retreival
- **ranked retrieval**: Order documents by how likely they are to be relevant.
- Partitioning: Scalability
- Replication: Redundancy
- Caching: Speed
- Routing: Load Balancing

### TF.IDF Term Weighting
- term weights consist of 2 parts: document and collection
- high weights for terms that appear many times in a document, terms that appear in many documents should get low weights.

![latex-9af68197-14b2-4f93-91df-1d0ff824aa78](data/final_notes/latex-9af68197-14b2-4f93-91df-1d0ff824aa78.png)

## Graphs
- hard: irregular structure, irregular access patterns
- typical alg: local computations at each node, propogate results along the edges

Representations:
- **Adjacency Matrix:** nxn square matrix, n=number of verticies, ![latex-2167e5f4-e623-48bf-864c-0dcbf7fbe057](data/final_notes/latex-2167e5f4-e623-48bf-864c-0dcbf7fbe057.png)_ iff there is an edge from i to j.
  - intuitive to iterate over rows and columns
  - lots of wasted space, for sparse graphs. easy to write, hard to run computations
- **Adjacency List:**
  - Less wasted space, possible to compress. Easy to compute using outlinks (just iterate over the list foreach edge)
  - hard to compute over inlinks
- **Edge List:** Explicitly enumerate all of the edge pairs
  - easy to add new edges, just add a pair to the list
  - waste alot of space.

Store undirected graphs, do one of:
1. store both edges, make sure the algorithm de-dups
2. store as one edge, alg needs to recognize it goes in both directions.

Manipulations
- Invert: `flatMap` and `regroup`
- Adjacency list -> edge list: `flatMap` over adjacency list and emit tuples
- Edge list -> adjacency list: `groupby`

Single Source Shortest Path
- Recall: **Dijkstra**, start at source node, expand the field until the destination is reached.
- Define inductivly
  - `DistanceTo(s) = 0` b is reachable from a if b is on adjacency list of a
  - `DistanceTo(p) = 1` For all nodes p reachable from s
  - `DistanceTo(n) = 1 + min(DistanceTo(m), for m in M)`: For all nodes n reachable from some other set of nodes M

Parallel BFS
- For all nodes except the start, ![latex-f747f1b9-0bf2-4427-9a20-d22c0eec91b8](data/final_notes/latex-f747f1b9-0bf2-4427-9a20-d22c0eec91b8.png)
- **Mapper**: For each m in adjacency list, emit `(m, d+1)`, emit the distance to yourself
- **Sort/Shuffle**: group distances by reachable nodes
- **Reducer**: Select the minimum distance path for each reachable node, additional book-keeping needed to keep track of the actual path.
- Multiple Iterations: each MapReduce job expands the frontier by one step

```scala
class Mapper {
  def map(id: Long, n: Node) = {
    emit(id, n)
    val d = n.distance
    emit(id, d)
    for (m <- n.adjacenyList) {
      emit(m, d+1)
    }
  }
}

class Reducer {
  def reduce(id: Long, objects: Iterable[Object]) = {
    var min = infinity
    var n = null
    for (d <- objects) {
      if (isNode(d)) n = d
      else if (d < min) min = d
    }
    n.distance = min
    emit(id, n)
  }
}
```
- run job, check for convergence, try again
- MapReduce explores all possible paths in parallel, lots of wasted space, we only do useful work at the frontier.

Single Source with weighted edges
- add weight w for each edge in adjacency list
- in mapper emit `(m, d+w)` instead of `(m, d+1)`
- need to go through the entire graph

Multiple Source shortest Path
- have an array of sources
- Mapper emits an array of distances wrt each source
- Reducer finds the minimum for each element in the array

Generic Recipie:
- represent graph as adjacency list
- perform local computations in the mapper
- pass along partial results via outlinks, use the desination node as the key
- perform aggregation in the reducer on inlinks to a node
- iterate until convergence, external driver
- pass the graph structure between iterations

PageRank
- Based off of random walks around the web
- Given page x with n inlinks
  - ![latex-28925682-0abd-4b2b-b2e7-697b63605862](data/final_notes/latex-28925682-0abd-4b2b-b2e7-697b63605862.png) is out-degree of t
  - ![latex-331ccd78-73c0-46d9-bbc2-c0a14960e56f](data/final_notes/latex-331ccd78-73c0-46d9-bbc2-c0a14960e56f.png) is the prob of a random jump
  - ![latex-9885251a-83c8-403b-9c32-692941c0246e](data/final_notes/latex-9885251a-83c8-403b-9c32-692941c0246e.png) total number of nodes in the graph
  - ![latex-36a397eb-f8a2-4de5-b096-ab7f2917b0c8](data/final_notes/latex-36a397eb-f8a2-4de5-b096-ab7f2917b0c8.png)
  - Second pass for dangling nodes: ![latex-fe7a4646-a055-4165-99ad-4fe272d1c8e6](data/final_notes/latex-fe7a4646-a055-4165-99ad-4fe272d1c8e6.png)
    - ![latex-53845c53-282e-423b-91ca-5cd4402c5295](data/final_notes/latex-53845c53-282e-423b-91ca-5cd4402c5295.png) is previous pagerank mass
    - ![latex-561b5b24-0620-46b3-a1df-3efa4aa0a35b](data/final_notes/latex-561b5b24-0620-46b3-a1df-3efa4aa0a35b.png) is the missing PageRank mass
- Convergence criteria
  - iterate until PageRank values don't change
  - Iterate until PageRank rankings don't change
  - Fixed number of iterations
- Use log probabilities to avoid small values

- weighted PageRank
- Personalized PageRank
- Spark: `join`, `flatMap`, `reduceByKey`
  - cache the adjacency list
  - Join with PageRank vector

## Analyzing Relational Data



Database Workloads
- **OLTP**: Online Transaction Processing
  - user facing, real-time, low-latency
  - Application users want fast applications
    - Typical access patterns
    - random access
    - writes on small amounts of data
    - small amounts of data per query
- **OLAP**: Online Analytical Processing
  - Business intelligence, data mining
  - batch workloads, less concurrency
  - Analysts want to be able to analyze large amounts of data
    - Full table scans
    - lots of joins
    - large amounts of data per query
- Hard for OLTP and OLAP to exist together
  - poor memory management
  - conflicting data accessing patterns
  - variable latency
  - **solution** Build a separate data warehouse
  - OTLP -> ETL -> OLAP
    - Run ETL on some frequency (ex. every night)
    - **Implication**: Analysts are working on old data
    - Extract
    - Transform
      - Data cleaning and integrity checking
      - schema conversion
      - field transformations
    - Load
- **OLAP cubes**: Join tables together, perform operations
  - slice and dice
    - slice the cube into areas that your interested in
    - ex. take a time slice, only care about the last month
  - roll-up /down
    - Dimensions have heirarchial structure: time is composed of hours / days / years
    - Specific products categories / sub-categories
    - drill down: Stores in Ontario -> Stores in Southern-Ontario -> Stores in Waterloo
  - pivot
    - Rotate the cube
    - Sales figures for products and stores, rotate to see changes by month
    - Perform aggregation along some different axis
  - Cube materialization
    - lots of joins, group-bys and aggregations
    - pre-compute parts of the cube
    - trade-off between time and space

What do you do with the data?
- Report Generation
- Dashboards
- Ad-hoc analyses
  - Descriptive: What happened / what is happening
  - Predictive: predict future, unknown events
- Data products

Why databases (known unknowns)
- great for structured data, can use schemas!
- data is clean
- know what queries you want to run on it

Why Not databases (unknown unknowns)
- little to no structure in data
- data is messy and noisy
- don't know what your looking for
- behavioural data

Advantages of Hadoop (dataflow language)
- don't need to know a schema ahead of time
- raw scans are the most common operations
- many analyses are better formatted imperitevely
- much faster data injest rate


Utilize both to gain the most benefits and flexibility:
**Data Lake**: Store of raw data
**Data Warehouse**: Structured data

Future: **HTAP**: Hybrid Transactional Analytical Processing
- avoid the ETL process
- Let's analysts work with realtime data

### MapReduce algorithms for relational data

- Projection (![latex-cb67c2cf-5053-4c3c-aecd-881d63a2c4ba](data/final_notes/latex-cb67c2cf-5053-4c3c-aecd-881d63a2c4ba.png))
  - Select particular fields for each tuple
  - Need to keep track of field positions after projections
- Selection (![latex-2bbc5cfa-f1fa-4bfe-9f0f-f26e168ceb69](data/final_notes/latex-2bbc5cfa-f1fa-4bfe-9f0f-f26e168ceb69.png))
  - Process each tuple, emit those that meet some criteria
  - Pipeline with projections
  - Performance limited by HDFS throughput
    - speed of encoding/decoding tuples is important
    - take advantage of compression
- Groupby ... Aggregation
  - Some aggregation function
  - Map over dataset, emit tuples, key by the group by attribute. **Framework handles the actual grouping**
  - Compute the aggregation function in the reducer
  - Optimize with combiners, IMC
- Joins
  - Reduce side (repartition, shuffle join)
    - map over both datasets
    - emit tuple value with join key as the intermediate key
    - framework brings together
    - perform join in reducer
  - Map Side (sort-merge)
    - both datasets must be copartitioned (partitioned in the same way), allows for parallelization
    - Map over one dataset, read from the other corresponding partition
    - no reducer needed
  - Hash (broadcast, replicated)
    - Load one dataset into memory, keyed by the join key
    - Read the other dataset, probe for the join key
      - Store R in DistributedCache, progate to all workers
      - no reducers necessary
    - Need `R << S` and R must fit into memory
    - variants
      - R and S are co-partitioned: only need to build hash maps for the corresponding partition
      - striped: If R doesn't fit into memory
        - Divide R into n groups, such that each fit into memory
        - Perform a hash join for all n
        - Union the results together
      - Use a global key-value store (Memcached), prob the key-value store
  - Preferences (Most, ... ,Least): Hash > Map > Reduce

Limitations of Joining
| Hash | Map | Reduce |
|-|-|-|
| Memory | Sort order and partitioning | General purpose |

Running SQL-on-Hadoop
1. Build logical plan
2. optimize logical plan
3. select physical plan

Hadoop Dataware house designs
- Joins are expensive
- Ultimately a time-space trade-off
  - Have more redundant data around in order to save on later joins (save time, waste space)
- normalization: factor out redundancy
- denormalizations: pre-join to the Facts table in order to save the cost of later joins
  - Denormalize can occur during the ETL process

Row vs. column Stores
- Row store: `(a, b, c), (a, b, c), ....`
  - Easy to modify a record, in place updates
  - May need to read un-necessary data during processing
- Column store: `(a, a, a, a..., ), (b, b, b, ...), (c, c, c, ...)`
  - only read the necessary data when processing
  - tuple writes require multiple operations
  - tuple updates are complex
  - better compression, read efficiency, vectorized execution, compiled queries

Physical Representation
- Use binary representations (parqueet, protobuf)
- define schemas for binary
- Use an index to speed up hadoop, InputSplits on contain blocks that match selection crtieria. Instead of processing everything and thowing away most. Implement at the RecordReader level.

### Predictive Analytics
- Descriptive Analytics: Describe what is currently happening
- Predictive Analytics: Predict future values
- Classification: output draw from labels
- Data -> Features -> Model -> Optimization

Features
- Dense: most samples contain the features
- Sparse: messages that contain specific terms
- Gathering labelled data can be a bottleneck
  - crowdsource
  - Bootstrapping, semi-supervised techniques
  - Exploiting user behaviour logs: emojis for sentiments
- Supervised Binary Classification: restrict output label to binary
  - Extend to multi-class with multiple classifiers
    - 1 vs. rest: A or not, B or not, ...
    - Classifier Cascading: A or Not -> B or Not -> ...
      - Keep going until success
- Minimize some loss function, gradient descent, lower loss over time
  - Gradient descent is first order techniques, use higher order derivatives
- **Logistic Regression**:
  - Set equal to one: ![latex-bc327dae-28de-4d64-aaa0-1ca0c8d4ad31](data/final_notes/latex-bc327dae-28de-4d64-aaa0-1ca0c8d4ad31.png)
  - ![latex-c8600452-1129-407b-8d64-a04c90a29b87](data/final_notes/latex-c8600452-1129-407b-8d64-a04c90a29b87.png)
  - ![latex-b3ba0531-cdf8-43e5-89ea-0e2d4089c850](data/final_notes/latex-b3ba0531-cdf8-43e5-89ea-0e2d4089c850.png)
  - ![latex-dc753f49-f634-48f3-947b-0b865ea29946](data/final_notes/latex-dc753f49-f634-48f3-947b-0b865ea29946.png)
    - Minimize the log likelihood
  - ![latex-dc8e4dd7-a681-49fa-be44-01a6d4f82bc0](data/final_notes/latex-dc8e4dd7-a681-49fa-be44-01a6d4f82bc0.png)
    - Utilize the gradient to update weights

![Gradient Descent](gradient.png)

```scala
val points = spark.textFile(...).map(parsePoint).persist()
var w = // random initial vector
for (i <- 1 to ITERATIONS) {
  val gradient = points.map{ p =>
    p.x * (1/(1+exp(-p.y*(w dot p.x)))-1)*p.y
  }.reduce((a,b) => a+b)
  w -= gradient
}
```

Batch Learning: Update the model after considering all training instances
Online Learning: Update the model after considering each randomly selected training example.
  - stocastic gradient descent
- Randomly shuffle the training samples
- Mini-batching as a middle ground

Ensemble Learning: Use multiple independent models to make a prediction
- Train classifiers on distinct partitions of the data
- Combining Predictions
  - Majority Voting: Take the class that most models pick
  - Simple Weighted Voting: Apply some weights to each prediction
  - Model Averaging
- This works as long as the models are independent. If the errors are uncorrelated then the chances of multiple classifiers being wrong is less likely.
