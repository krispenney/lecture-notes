# Lecture 4 - January 16, 2018

## Why PerfectX?

### Funnel / Traffic analysis
Examine how people navigate a particular website.
- Go through the query log and see where people went.
- What do people do after they see a tweet (retweet, profile, reply)?

## MapReduce Algorithm Design
Have to express everything wrt. Mapper, Reducers, Combiners, and Partitioners.
- Both a blessing and a limitation
  - **Pro:** Don't have to think about anything
    - The framework takes care of all the behind the scenes actions.
  - **Con:** Don't have to think about anything!
    - Where are mappers / reducers running?
    - When do things start and finish?
    - Which key is a particular reducer processing?

- Any design patterns?

## Tools for Synchronization

### Tips

**Avoid Object Creation**
- Expensive!!: imagine `1,000,000,000` items to process, needs to create objects for all
- Garbage collection: may halt excecution to clean up
  - less of a problem in newer versions of JVM

**Avoid Buffering**
- Don't store results in some buffer (think reducers)
- Will run out of memory for large datasets.

**Combiners can run 0, 1, or multiple times**

### Local Aggregation

#### Recall:
Most expensive part is the distributed group-by

- High communication, expensive! Limit communication
- Most scalable way to do group by: **sort**
  - Merge sort
  - Load a bunch of data in memory, sort it, write it out to a file (spills)
  - Bunch of sorted files, merge the spills together
  - Reducers (r total) pull the data from the Mappers
  - A reducer pulls data from **m** Mappers
  - In total `m * r` copies, we want to limit network traffic. Solution: **Combiners**
  - Combiners work on the spills, works on the local nodes to try to perform some intermediate aggregation.
  - Combiners also apply on the Reducer side, a reducer pulls it's data from `m` mappers, try to reduce more.

#### Word Count Baseline Example
- Initial: Mappers emit `total_word_count` (k, v) pairs
- With the combiner, upper bound of the vocab size (number of unique words) * number of mappers
  - Is this buffering? Depends, in the worst case the mapper has the vocab size (k, v) pairs for that particular document.
  - Are combiners still needed? **Yes**, need to do it across multiple maps
    - Why doesn't `Map` example improve running time? Combiners are doing all of the work and object creation + gc overhead add up. Network is the bottleneck.

### Preserve state in mappers and reduces
- Note the `setup` and `cleanup` methods on `Mapper` and `Reducer`.
- Can instead initialize state objects across the object lifecycle, emit results on the Mapper cleanup.
- Note combiners are still needed on the reducer side.
- **In-Mapper Combining**: Fold function of combiners inside the Mapper.
  - Wins here come from the reduction of spills to disk. The number of (k, v) pairs emitted are the number pushed across the network.
  - Since we don't emit unit the cleanup, fewer spills needed.
  - Have to be concious of memory usage (i.e. can the vocab size fit into memory)

### Data structures bring partial results together
- Places more onus on the developer vs the framework.
- Find out where your bottleneck is
  - Lots of small objects, high network traffic
  - Fewer complex objects, lower traffic, higher overhead.
  - Maybe harder to serialize/deserialize complex object
  - Implementation details of complex objects

#### Algorithm Design: Term co-occurrence matrix
- `NxN` matrix (N = vocab size)
- ![latex-2ba8b405-d47a-403b-91bc-49dd2a93d721](data/lecture4/latex-2ba8b405-d47a-403b-91bc-49dd2a93d721.png): number of times word i and j appear in the same context (ex. same sentence)

##### Basic Approach:
- Mappers generate partial counts
  - Each take a sentence, generate counts with (word_i, word_j) as the key
  - **Note**: default partition behaviour is to hash the pair mod the numbers of reducers
  - In this case, custom partitioner to only operate on the left side of the pair.
- Reducers aggregate partial counts

##### Stripes Approach
- map to associative array, with intermediate counts
- Reducers perform an element-wise summ on the associative array.
- Cons: Harder to implement, more complex objects
- **The Stripe needs to fit in memory**
  - Depends on your domain / application

### Define custom sort order of intermediate keys
Take advantage of sorted key order in the reducers in order to sequence computations.
- Emit special tokens in the mappers (i.e. marginal values), use sorting to make them show up first.

