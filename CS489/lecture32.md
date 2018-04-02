# Lecture 32ish - April 2, 2018

## Word2Vec
- embedding words, one-hot encoding ignores the semantic relationships between words
- Word2Vec: Autoencoder type structure, compress to a smaller space, reproject to predict nearby words. Co-occuring words.
  - hidden layer -> embedding space

- Similar to Self-Organizing Map (SOM)
  - Similar words organize themselves into a closer topological space
  - Words with similar meaning likely will occur with the same set of words, so the network should produce similar output. Therefore, the embedding (hidden) representation should also be similar.
  - We care about the embedding activations (i.e. throw away the output layer), use the embeddings as features in some other model (instead of the actual words)

Typical loss function: cosine proximity, the angle between two vectors

## Equilibrium Propogation
- Biologically realistic way of doing backprop
- way of doing backprop without knowing the gradients themselves
- Internal Energy: ![latex-fb4b8406-d034-47e4-ad5c-7ee51bd7e5cf](data/lecture32/latex-fb4b8406-d034-47e4-ad5c-7ee51bd7e5cf.png)
  - coactivation: When both nodes are active at the same time
  - W is symmetric
- ![latex-4fa75349-ab5f-40b0-aeea-e190c3e6f2dd](data/lecture32/latex-4fa75349-ab5f-40b0-aeea-e190c3e6f2dd.png)
  - similar to RBMs
- Output Loss: ![latex-7865d22e-a1ea-4253-b569-51ae37d52b4e](data/lecture32/latex-7865d22e-a1ea-4253-b569-51ae37d52b4e.png)
- Total Energy: ![latex-7c9766f3-253c-418b-9edb-82e31135e234](data/lecture32/latex-7c9766f3-253c-418b-9edb-82e31135e234.png)
  - if ![latex-47339301-fafb-4df3-b7b7-f1726676b52e](data/lecture32/latex-47339301-fafb-4df3-b7b7-f1726676b52e.png): energy ignores the targets
  - if ![latex-47039028-bb2d-43e7-8854-2d6d4b778f83](data/lecture32/latex-47039028-bb2d-43e7-8854-2d6d4b778f83.png): energy includes the output loss
- Network behaviour governed by: ![latex-462b50a4-8083-4b5a-ad6f-3f74f18ddf8d](data/lecture32/latex-462b50a4-8083-4b5a-ad6f-3f74f18ddf8d.png), where ![latex-9235143e-cb3b-45bb-9073-de6e7c25dd06](data/lecture32/latex-9235143e-cb3b-45bb-9073-de6e7c25dd06.png)
- Rewrite F: ![latex-9c5d6167-05e2-4bbb-984a-8281e5c6260c](data/lecture32/latex-9c5d6167-05e2-4bbb-984a-8281e5c6260c.png)
  - ![latex-9ca48820-f76c-4e9f-8243-189869384b03](data/lecture32/latex-9ca48820-f76c-4e9f-8243-189869384b03.png)
    - similar to a leaky integrator node
  - ![latex-238dc0f2-a1ed-4689-954c-257e90cc8e2e](data/lecture32/latex-238dc0f2-a1ed-4689-954c-257e90cc8e2e.png)
  - ![latex-c1833a94-becb-44df-96a4-59956ef5ffcf](data/lecture32/latex-c1833a94-becb-44df-96a4-59956ef5ffcf.png)
- ![latex-d9f6ebf3-46a6-468f-923c-3e60e26f78f0](data/lecture32/latex-d9f6ebf3-46a6-468f-923c-3e60e26f78f0.png)
