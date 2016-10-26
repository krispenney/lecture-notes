# Lecture 13 - Oct 25, 2016

## Two Level Paging
* Instead of a single page table to map entire virtual memory, split the page table into multiple smaller page tables. Add a page table directory.
  * If all Page Table Entries in a smaller table are invalid, avoid creating that table entirely.

* Virtual Address has three parts (p<sub>1</sub>, p<sub>2</sub>, o):
  1. Level one page number: used to index the directory
  2. Level two page number: used to index a page table
  3. Offset within the page

### Address Translationwith two-level paging
* MMU's page table base register points to the page table directory for the current process.
