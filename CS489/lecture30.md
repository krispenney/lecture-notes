# Lecture 30 - March 19, 2018

## LSTMs: Long-Short Term Memory Networks
- RNNs are bad at handling long term dependencies
- RNNS suffer from exploding / vanishing gradient problems
  - Multiplication of many terms above / under 0

### Architecture
- forget gate: how much from previous time steps
  - ![latex-8ba4996a-6176-4f86-88d4-9f0133898d22](data/lecture30/latex-8ba4996a-6176-4f86-88d4-9f0133898d22.png)
- input gate: how much of current time step we care about
  - ![latex-19ebb4a2-0964-4a54-8d53-a2bea65ed771](data/lecture30/latex-19ebb4a2-0964-4a54-8d53-a2bea65ed771.png)
  - ![latex-f8d85f42-c911-4cd6-9f48-e9aa9d1cba5c](data/lecture30/latex-f8d85f42-c911-4cd6-9f48-e9aa9d1cba5c.png)
- output gate:
  - ![latex-114e69f9-f001-4389-92d1-e834dab8e6ea](data/lecture30/latex-114e69f9-f001-4389-92d1-e834dab8e6ea.png)
  - ![latex-2968e1a2-a943-4a46-8933-25d451fd5252](data/lecture30/latex-2968e1a2-a943-4a46-8933-25d451fd5252.png)
- cell state: combination of previous cell state and the candidate of current state
  - ![latex-fa13eca5-1e5a-4027-a67a-c583b18909f1](data/lecture30/latex-fa13eca5-1e5a-4027-a67a-c583b18909f1.png)
  - Gradient is a constant term, helps to avoid vanishing gradient

### Backprop in LSTM
- want the error with respect to the previous state
-
## LSTM variant: Gated-Recurrent Unit (GRU)
- Similar gating mechanisms, but no cell states

## Open Questions
- Avoid vanishing / exploding gradient problem
  - Use RELU: gradient is linear
  - Regularization
  - Weight initialization
    - Research into using RNNS with proper weight initialization, can produce similar results to LSTMs with 4x fewer params.
