# Lecture 8 - May 25, 2017

- Windows block size 4kb

### Harddrive Times
- Seek: 4ms
- Rotate: 60/7200/2 = ~4ms
- Time: 4kb/750MB ps = 0.004ms

### Datastriping
- Use multiple drives
- Store the blocks of a file across each of the drives
- **Con**: Loose one drive, you have data loss
- Binomial distribution

### RAID 1
- Uses mirroring
- Creates redundancy
- Doesn't have any performance improvements
- Guranteed to have no data loss for one drive
  - For up to n/2 failures, it is possible that there's no data loss
- **Con**: Not an efficient use of resources

### RAID 5
- Use striping and parity
- **Parity Bits**: Store a parity block, Are there odd or even number of ones?
  - 0101 -> Parity: 1

### Storage Area Network
- Share RAID array across multiple drives
- File management done on the application servers
- Much faster (due to fiber network)
- Much more expensive

### Archieval Backups
- Done at the end of the day
- Stored offsite
- To tape (or some medium)
- Can only backup to some point in the past

### Difference between Server application and server machine
- application: the software itself
-
