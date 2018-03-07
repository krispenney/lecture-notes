# Lecture 25ish - March 9, 2018

## Neural Decoding Overview

1. behavioural sampling
  - A bunch of input stimulus are recieved
  - Brain accepts input and processes it
  - We can sample these neural activities.
  - Choose X, use simulation to get A (activities of the neurons)

2. Compute Decoders
  - Use data from behavioural experiment to solve:
  - ![latex-11817bc1-3c91-4871-8d25-1d8ea3328a91](data/lecture25/latex-11817bc1-3c91-4871-8d25-1d8ea3328a91.png)
  - Decoding list is how to interperete neural activities
3. Decode neural activity
  - Now you can decode further neural activitty
  - i.e. given ![latex-10c05d60-f2da-4363-9000-d38ed67cb862](data/lecture25/latex-10c05d60-f2da-4363-9000-d38ed67cb862.png) you can estimate ![latex-99b62f3a-0b36-4007-aadb-12d8fd6a1917](data/lecture25/latex-99b62f3a-0b36-4007-aadb-12d8fd6a1917.png)

## Neural Transformations
- In the brains, populations of neurons send their activities to other neurons.

### Encoders and Decoders
- Given 2 populations A and B can we simply copy the weights from A to B
  - No, it's unlikely that both A and B are of the same dimension (number of neurons)
- Can use an autoencoder:
  - Decode input from A
  - Re-interpret results into B

1. Encode input x into A
  - ![latex-d59049d1-210c-4b96-946b-d0b344ebb152](data/lecture25/latex-d59049d1-210c-4b96-946b-d0b344ebb152.png)
    - J input current
    - G is activation function
    - X is 1xK vector
    - ![latex-3aa5958c-5f53-4550-8dfb-feac6cb7bfa9](data/lecture25/latex-3aa5958c-5f53-4550-8dfb-feac6cb7bfa9.png): KxN
    - ![latex-b6892e82-35ee-42b6-9042-55c0ae823f5e](data/lecture25/latex-b6892e82-35ee-42b6-9042-55c0ae823f5e.png): NxN diagonal matrix
    - Bias for each neuron (1 x N)
    - A is a 1xN vector, giving the activity for N vectors
2. Decode the value from A
  - ![latex-416ac5b4-359e-4d05-9b8c-687a9189cb7f](data/lecture25/latex-416ac5b4-359e-4d05-9b8c-687a9189cb7f.png)
  - the indentity decoding weights
  - Recall that the decoding weights are created from solving the least squares problem
3. RE-encode into B
  - ![latex-6d40c771-e261-404d-8acd-e89d9c2be6c7](data/lecture25/latex-6d40c771-e261-404d-8acd-e89d9c2be6c7.png)
  - ![latex-27511b3a-d0ff-4149-8dfd-062882c00339](data/lecture25/latex-27511b3a-d0ff-4149-8dfd-062882c00339.png) is 1xk
  - ![latex-f707dc68-14e6-472e-9512-15bf5d097abd](data/lecture25/latex-f707dc68-14e6-472e-9512-15bf5d097abd.png): is kxM
  - ![latex-319bb6f1-2a55-4ac0-af8f-6cb016df4ff2](data/lecture25/latex-319bb6f1-2a55-4ac0-af8f-6cb016df4ff2.png): is MxM diagonal matrix
  - Rewrite as ![latex-a7c45599-618f-448a-829b-2765a607d428](data/lecture25/latex-a7c45599-618f-448a-829b-2765a607d428.png)
    - Notice that the product: ![latex-9b0d017f-621a-4d81-bcde-0e6605561cc2](data/lecture25/latex-9b0d017f-621a-4d81-bcde-0e6605561cc2.png) is NxM
    - Call this product W.
4. Decode from B if desired
