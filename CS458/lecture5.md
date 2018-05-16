# Lecture 5 - May 16, 2018

## Spectre / Meltdown

The CPU may execute some instructions out of order, this allows for slower instructions to be executed first.

```asm
jmp ...
mov ..., ...
rcx = 0x..... # Somewhere in kernel space
mov l, byte[rcx]
```

When the CPU tries to access the kernel address, an exception will be raised. Because of out of order execution, these values could be saved in the cache allowing later access by a malicious actor.
How fast the cpu returns the result can give insights into what has been saved in the cache.

## How to Write More Secure Code

How can we follow better software engineering practices in order to stop security flaws from being created during development time.
- security controls should be considered throughout all phases.

### Design

How can we design programs so that they're less likely to have security flaws.

#### Modularity
- break the main problem into multiple, smaller, sub-problems
- single purpose, small, and independent modules.
- makes it easier to understand what any given module is doing, at a glance.
- low coupling between modules
  - shouldn't be dependent on too many other components

#### Encapsulation
- have modules be self-contained
- helps with understanding, just look at the published api. Less likely that developers will make bad, assumptions.

#### Infomation Hiding
- The internals of one module should not be visible to other modules.
- prevent the reliance on undocumented behaviour that isn't specified in the API
- reduces chances of other developers from taking malicious actions.
  - reduce salami attacks (lots of smaller, inconsequential attacks)

#### Mutual Suspicion
- Modules should check that their inputs are sensible before acting on them.

#### Confinement
- Sandboxing, if Module A has to call an untrustworthy Module B, it can confine it to a sandbox.
  - run it in a limited environment, which reduces the resources that it can access to only those required.
  - ex. code downloaded from the internet
- what would be the effect if untrusted code were run this way?
  - there's a performance penalty associated with the sandbox environment
  - recent research into running untrusted code in the cloud, where performance is better. This could protect local machines

### Implementation

When your actually coding, what can you do?

- Better programming languages, languages with bounds checking, safeties
  - use bounds checking in C
  - learn about security

#### Static Code Analysis
  - tools which analyze your code, that look for various security concerns.
  - point out buffer overflows and TOCTTOU
  - need to construct a call graph,
    - can be time consuming, lots of functions calling eachother
    - Function pointers, just using static code analysis, you'll never know which function is actually being run. You'll likely miss things, or get false positives.


![graph-1b74231d-a3b3-4d7c-87d9-08022b93e7c5](data/lecture5/graph-1b74231d-a3b3-4d7c-87d9-08022b93e7c5.svg)

#### Formal Methods
- mathematically prove that the code does what it is supposed to do.
- impossible to do in general
- programmer may have to mark up code with assertions / hints to help the theorem proving program.
  - time consuming
  - spend your effort once

#### Genetic Diversity
- worms and virus are able to spread so quick is because many machines are running the same vulnerable code.
  - inspired by argiculture
- Could have lots of different machines, running different versions
  - more work to deploy, maintain
- not security via obscurity
  - just because people don't know about something, doesn't provide additional defence

#### Learn More About Software security
- Books
  - "Building Secure Software - How to Avoid security problems the right way"

### Change Management
- large software projects may have hundreds of developers
- frequent turnover, people may leave the company, new people join
- if a flaw enters the program, trace how it got introduced.
- Version Control
  - Linux backdoor was detected because the commit didn't have a valid approval.

### Code Review
- most effective may to detect. other people can critically look at the code, and potentially spot bugs.
- kinds
  - **Open Source Model**: reviewers are just given the code.
  - **Guided**: The person who developed the code is going to explain the code to the reviewers.
    - justifies design decisions
    - reviewers can easily give feedback, lead to changes
  - **Easter Egg**: Reviewers constantly looking at code from the same people, they become complicit. The programer can insert explicity flaws in the program.
    - should keep reviewers on watch
    - Important: you should take the flaws back out of the program. Avoid inserting backdoors

### Testing
- Goal: make implementation match the specification.
- Remember: The specification includes "And Nothing Else"
- Strategies
  1. try to make the program do unspecified things just be doing unusual, attacker-like things to it.
  2. Try to make the program do unspecified things by considering the design and implementation

#### Black-Box Testing
- Testing where you have access to a completed object.
- what kind of things can you do to make it misbehave, see how it operates?
- Pass null values, overflows, etc..

#### Fuzzing
- Supply completely random data to the object
  - as input
  - data file
  - network data
- This will often cause the program to crash
  - therefore effecting security, recall availability.
- The goal is for the program to never crash
  - could give indications for additional assertions

#### White-Box Testing
- Testing conformance to the specification, given knowledge of the implementation
- good for regression testing
  - make comprehensive sets of tests, make sure the program passes
  - when the next version of the program is released, make sure the tests still pass the old tests.
  - doesn't break anything.

#### Documentation
- write down the design decisions that you made, the reasoning behind them.
- document what you tried and didn't work.
- note things to be careful of (checklists for other developers).
  - subtle, non-obvious interactions between different components.

### Maintenance
- hope that once the program is released, there are no more issues.
  - ...but probably not
- Maintain code when on the consumers pc, patches will probably have to go out.

#### Standards, processes, and audit
- within a company, have rules / standards about how things are done at each stage of the software lifecycle.
- formalize how each standard should be implemented in practice.
- How audits to ensure that these processes are followed.
  - could be an external third party.
- Doesn't guarantee flaw-free code

what to consider for patching?
- IOT devices, small, low performance devices. Alot of them can't be patched.
- means many devices are exposed.
- engineering costs associated with patching.
  - A version of a car will likely exist for 10-15 years.

End of module 2

# Module 3: Operating Systems Security

