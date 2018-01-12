# Lecture 2 - January 12, 2018

## Logistic Regression

![latex-0b81c32f-5136-4ab5-996c-cf2e2f0903d0](data/lecture2/latex-0b81c32f-5136-4ab5-996c-cf2e2f0903d0.png)
![latex-816c01f1-04a8-495a-a5ee-2728eb83a2fa](data/lecture2/latex-816c01f1-04a8-495a-a5ee-2728eb83a2fa.png)

The goal is to find optimal params ![latex-f7cd4718-d00e-4fbc-bcf2-09b1a15edd22](data/lecture2/latex-f7cd4718-d00e-4fbc-bcf2-09b1a15edd22.png) to optimize log likelihood

### Explanetory context
Example: What is causing someone to where a jacket
- Interperet results as a probability.
- ![latex-bc0c7617-2067-4592-9f5a-5b5ef6f66d12](data/lecture2/latex-bc0c7617-2067-4592-9f5a-5b5ef6f66d12.png)
- **Parametric assumption**: Follow sigmoid shape, low-high or high-low

### Odds Ratio

![latex-670c1759-1721-45d2-9e23-dffdc0cd88bb](data/lecture2/latex-670c1759-1721-45d2-9e23-dffdc0cd88bb.png)

Example: The horse has ![latex-aa4aad65-52cd-42ab-bf40-0425d451532c](data/lecture2/latex-aa4aad65-52cd-42ab-bf40-0425d451532c.png) odds of winning the race, probability of winning is 5/7.

### Linear Log odds ratio

![latex-d3f1ef44-0681-4d9f-8b3b-97880448f083](data/lecture2/latex-d3f1ef44-0681-4d9f-8b3b-97880448f083.png)

## Pilgrim Bank Case A

### Industry
- Retail banking: 2001
  - Dot-com era, pre crash, pre 911
  - Internet big new thing, new oppourtunities
- B2C, lots of small consumers
- Not always clear what drives profits
  - Depends on amount of fees paid
  - Services used
- Customers are pretty loyal, not trivial to switch banks

- Alan Green
  - analyst
  - online banking group
- Bank isn't sure about which business model to use for their online banking channel
  - should they charge a fee for online banking?
  - analysis should provide evidence to support some claim

- Intuitively:
  - reasons for no
    - may cause customers to leave for another bank
    - cheaper for the bank, don't have to use physical banks, employees
  - reasons for yes
    - more profit for online users
    - Not many people have computers yet

### Questions to guide analysis
- Is being online associated with higher profits?
  - Descriptive question
- Does the online channel cause higher profilts?
  - explanatory question

What is the true relationship?

![graph-1974e5f3-3487-465d-b8ca-75f256b36e6b](data/lecture2/graph-1974e5f3-3487-465d-b8ca-75f256b36e6b.svg)

or maybe?


![graph-79d4e38e-ffea-427c-9119-412c46cd2e57](data/lecture2/graph-79d4e38e-ffea-427c-9119-412c46cd2e57.svg)

There could be some other variable(s) that effect both online and profits, for example:


![graph-1cdec1e3-6976-4ab7-9314-4e0f9ad8ca9c](data/lecture2/graph-1cdec1e3-6976-4ab7-9314-4e0f9ad8ca9c.svg)


