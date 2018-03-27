# Lecture 22 - March 27, 2018

## Real Time Analytics
- Recall: OLTP -> ETL -> Data Warehouse
  - analysts are working with delayed data
- Twitter wanted it real time query suggestion / completion
  - co-occurences within query sessions, overtime learn what queries go together. **Problem**: Delayed suggestions, potentially suggest irrelevant topics, be too late.
  -

### Real-time vs. Online vs. Streaming
- these terms get mixed-up
- Real-time: Low latency
  - differs depending on the applications
  - seconds or minutes could be good enough for your application
- Online: Contrast with batch processing
- Stream: Nature of the data that arrives
- Could have real-time without streaming
  - get a batch of 10 records every minute
  - real-time, but not really a stream.

### Data Stream
- Some sequence of tuples
- Could have a schema
- Usually ordered
  - implicit: The time they arrive
  - Explicit timestamps
- May not be able to store everything

### Semantics
- you want to do a group-by and then aggregation. When do you stop grouping and aggregate?
- Join a stream and static source
  - just do a lookup
- Join of two streams?
  - how long do you wait, when do you stop?
- join 2 streams, group by, and aggregate
  - when do you stop joining and continue?

#### **Solution**: Windows
- Defined in 3 ways
    1. Some ordering attribute: ex. time
    2. Counts
    3. explicit markers

##### Windows on Ordering Attributes
- Most natural is time
- Sliding window: current time + some offset, overlap
- Tumbing window: next window starts at the end of the current window

##### Windows on Counts
- Ex. Call a window once 10 elements have been seen
- Variable window sizes

##### Windows from "Punctuations"
- Some application defined end-of-processing
- Ex. The end of a user session
  - some are long, some are short
  - Frontend inserts some punctuation to say the user has explicitly logs out

#### Stream processing Challenges

- inherent
  - Latency requirements (time)
  - Space
- System Challenges
  - Bursty Behaviour and load balancing
    - Steve jobs dies! Sudden spike
    - how to balance the load to react to these effects
  - Out of order message delivery and on-determinism
    - Lots of message sources, no idea when they will arrive
    -
  - Consistency: Important to declare what it is respect to
    - At most once
    - at least once
      - Individually all packets get there, but could be dropped / lost along the way
    - exactly once
      - Packet delivery (`scp`): all the packets made it end to end
      - Only 1 file is transfer

### Stream Processing Frameworks

#### Producers and Consumers
- Producer pushes to the Consumer (callback)
- Consumers pulls the Producers (polls)

Problem: In a large system, lots of systems may want information from one source, as more sources are added it gets complicated.
Solution: **Introduce a Broker**
- Broker acts as a buffer (guarantees robustness)
  - If a consumer goes down they can get the data that they missed
  - Queue: Producers take data, gets removed from the queue
  - Pub/Sub: Lots of subscribers (Kafka)
    - Kafka: Consumers
- Producer sends data to Broker
- Consumer gets data from the Broker

#### Storm and Heron
- Storm: Real time distributed stream processing system
- Heron: From scratch, API-compatible re-write of Storm
  - By Twitter

##### Topologies
- Storm Topologies: start a job, runs until you kill it
- topology is a computational graph
  - verticies: computation
  - Edges: How the tuples flow
- processing sementices
  - At most once: without acknowledgments
  - At least once: With acknowledgments
    - Exactly once: You de-dup the data yourself
- Spouts: emit tuples
- Bols: Processing tuples
  - Typically have some bolt that writes out the data
- physical plan: how many instances of spouts and bolts are run? Load balancing?

##### Stream Grouping
- under the developers control
- Shuffle grouping: randomly to different instances
- Field grouping: Use some field as a key, determine where in the next set of bolts a tuple goes
- Global Grouping: Send everything to a single bolt

#### Heron Architecture
- Heron gives you the plumbing, you have to assemble things yourself.

#### Spark Streaming
- Spark is really good at batch processing
- Take the stream, chop it into pieces, create RDDs, then we're good!
- Their justification: most people don't actually need tuple by tuple, extremely low-latency
- Get the rest of Spark for free!
- Fault Tolerance: Everything is an RDD
  - input data stored in memory
  - If you loose an intermediate result, can recompute it.

```scala
val tagCounts = hashTags.window(Minutes(10), Seconds(1)).countByValue() # this is stupid
val tagCounts = hashTags.countByValuesAndWindow(Minutes(10), Seconds(1))
val tagCounts = hashTags.reduceByKeyAndWindow(Minutes(10), Seconds(1))
```
- Note that the first way is stupid!
- Lots of wasted work: sliding window drop off the first, add the last
- Solution: Spark API allows you to provide an aggregation operation and an inverse operation
  - Agg: Addition
    - For new values entering the window
  - Inverse: Subtraction
    - Values that leave the window

##### Problems: Event-time vs. processing time
- event-time: When a particular tuple was generated
- processing-time: When a particular tuple was actually processed
  - This is all Spark does
  - Chops up Tuples as they arrive
  - No way to compute in event time ordering (when a tweet was made)
- Everything is in terms of when tuples arrive at the spark streaming job
  - Want number of users who visited the website in the last hour
  - But spark gives us when they arrive in spark

#### Apache Beam
- Google donated the API to Apache, under the hood Google CloudDataflow
- Exactly once processing semantics
- Like Spark
  - apply a set of operations as a pipeline
- Watermark: system's notion when all data in a window is expected to arrive
  - At the end of an hour, I expect all results from that hour to arrive in the next 5 minutes.
    - could be a heuristic
    - Could have some guaranteed absolute
  - Process the window at the watermark
    - In Beam: **Trigger** when you actually materialize the window
    - Notion of early firings
      - have some slow upstream processing, watermark is 30 minutes after the hour
      - can fire early at 10 minute intervals (panes) and give me intermediate results.
    - Notion of late firings
      - system crashes, is restarted and has messages to send
      - rollup staggaling messages
    - How to refinements of results relate?
      - can throw away panes
      - accumulate: running sum
      -
