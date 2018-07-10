# Lecture 18 - July 9, 2018

## Database integrity

### Logical Integrity of Database
- db is typically stored as sometype of file
- Only authorized users can modify the database, run `INSERT`/`UPDATE` queries

### Physical Integrity
- Hardware failures, power outages
- backups
- Write ahead log

### Element Integrity
- Ensure correctness of database elements
- `(Name, Household Income)`
- Use **Access Control** to limit who can update elements
- **Element Checks** to verify correctness
  - business logic
  - Income can't be less than 0
  - unique fields
  - Triggers that run everytime a modifiaction is made.
- **Change Log**: allows erroneous changes to be reverted
  - Redundency in case access control or element checks fail
  - need additional storage space
  - **Accountibility:** Useful to know who and when made a change
    - helps with auditing
- **Error Detection Codes**: Detect corruption incase of hardware / OS failures
  - RAID

### Integrity: Two Phase updates
- Transactions: All or none actions are performed
  - rollback in the case of a failure
- First Phase: Use shadow fields to gather data that needs to be changed
  - Don't make any changes
  - safe to repeat in case of failure
- Second Phase: make the changes permenant
  - lock the real fields, commit the updates

### Integrity: Concurrent Updates
- Multiple threads are operating on the database
- Multiple reads can cause integrity errors
- Need to perform operations / transactions atomically

### Referential Integrity
- Every table has a primary key, minimal set of fields that uniquely identify a tuple
  - `id`
- may have multiple forign keys, primary keys of other tables
- **referential integrity**: Ensure that there are no dangling foreign keys
  - in the user table, there is always a corresponding entry in the postal code table

### Auditability
- Keep audit log of all database accesses
  - reads and writes
- Need to decide on the granularity of logs
  - too much, lots of wasted space, harder to search through
  - too little, may miss important events

#### Access Control
- much harder than OS access control
- many types of queries: Need to perform access control for each, all fields
- Inference Problem: Relationships between database objects can be inferred without actually looking at the relationship
- Access control could consider past queries
  - the current query, and past queries could reveal sensitive information
  - iteratively querying whether element is in set ultimately leaks the set

### Types of Data Disclosure
- Exact Data
- Bounds
  - sensitve value is smaller than H, but bigger than L
  - Use binary search to decrease range
- Negative Result
  - knowing that a person has zero felony convications is sensitive, even if the number is hidden
- Existence
  - know that some data exists can be sensitive
- Probable Value
  - sensitive data has value x with probability y

### Security vs. Presicion trade off
- **Security**: Forbid any queries that access sensitive data, even if aggregated results are no longer sensitive
- **Precision**: Aggregated data should reveal as much non-sensitive data as possible

#### Statistical Inference Attacks
- Sum
  - Get sum of all
  - Sum of all except items you care about
- Mean
  - sum = count * mean
- Median
  - intersecting medians may leak sensitive information

#### Tracker Attack
- Some query C that the DBMS refuses to answer
- matches fewer than k or more than N-k and less than N rows
  - N records in database
  - why more than N-k:
- Tracker T: Query that matches between ![latex-fcd183f4-e6f5-48d6-83ad-b81e30c6cc70](data/lecture18/latex-fcd183f4-e6f5-48d6-83ad-b81e30c6cc70.png) and ![latex-9ef2e3a9-6f3b-469f-89fb-e2b2acb32946](data/lecture18/latex-9ef2e3a9-6f3b-469f-89fb-e2b2acb32946.png) results
  - DBMS will answer T and the query not T

