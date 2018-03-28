# Lecture 34 - March 28, 2018

## Lamport-Diffie (LD) One-time Signature Scheme
- The public key should only used to sign a single message, as half of the private key bits are exposed each time.

### Scheme
- Alice's private key: ![latex-8d179a50-5e53-4325-ac80-d562807dfb5c](data/lecture34/latex-8d179a50-5e53-4325-ac80-d562807dfb5c.png)
  - Each ![latex-a4b81d2c-04aa-4f41-95bc-c9a59f1113fe](data/lecture34/latex-a4b81d2c-04aa-4f41-95bc-c9a59f1113fe.png) is 256-bits
  - ![latex-8483149e-c6df-4e0c-be68-e29a7b7a29ae](data/lecture34/latex-8483149e-c6df-4e0c-be68-e29a7b7a29ae.png) bits in total
- Alice's public key: ![latex-476736ff-27ad-4758-a1cd-16b8bb18223b](data/lecture34/latex-476736ff-27ad-4758-a1cd-16b8bb18223b.png)

To sign ![latex-b83897fa-f8f9-4b78-8c61-f9fc30082627](data/lecture34/latex-b83897fa-f8f9-4b78-8c61-f9fc30082627.png), Alice does:
- Compute ![latex-a90d1ab7-9785-4ae0-ba61-79e56ae748fe](data/lecture34/latex-a90d1ab7-9785-4ae0-ba61-79e56ae748fe.png)
  - note that H is collision resistant
- Signature is: ![latex-3941423e-5969-45cb-b20b-32aab21dc5a5](data/lecture34/latex-3941423e-5969-45cb-b20b-32aab21dc5a5.png)
  - where: ![latex-979e47a0-5301-4633-a0f8-59e5a0e965ee](data/lecture34/latex-979e47a0-5301-4633-a0f8-59e5a0e965ee.png) if ![latex-416d85ce-efd1-4f42-83c2-3a91c2f2643f](data/lecture34/latex-416d85ce-efd1-4f42-83c2-3a91c2f2643f.png)
  - ![latex-233cef02-3908-4200-8706-dda3ad6571d9](data/lecture34/latex-233cef02-3908-4200-8706-dda3ad6571d9.png) if ![latex-d0170594-5979-4475-acbb-8f5f6a1637d0](data/lecture34/latex-d0170594-5979-4475-acbb-8f5f6a1637d0.png)

### Security
The Adversary is given public key ![latex-dd6d354a-5b00-473e-bba6-a54222d34e03](data/lecture34/latex-dd6d354a-5b00-473e-bba6-a54222d34e03.png) and a signed message ![latex-cf363e85-4e34-4fe3-8dc9-e7c32b469277](data/lecture34/latex-cf363e85-4e34-4fe3-8dc9-e7c32b469277.png) for *one* message of the adversary's choosing. It's goal is to compute a valid signed message: ![latex-b9ef306d-b83f-4fff-8846-7d8a307782c9](data/lecture34/latex-b9ef306d-b83f-4fff-8846-7d8a307782c9.png) where ![latex-b2165a19-25fc-41e5-90e7-69c4a778230b](data/lecture34/latex-b2165a19-25fc-41e5-90e7-69c4a778230b.png)

Suppose the adversary can compute ![latex-27dc3776-3731-4d7d-a609-facf3167b827](data/lecture34/latex-27dc3776-3731-4d7d-a609-facf3167b827.png) efficiently.
- If ![latex-bad0e85f-fcd7-4c1b-a77b-bf578a786324](data/lecture34/latex-bad0e85f-fcd7-4c1b-a77b-bf578a786324.png), then you have found a collision for ![latex-dc0dd350-9ae2-45fb-8e61-28faa130d81b](data/lecture34/latex-dc0dd350-9ae2-45fb-8e61-28faa130d81b.png). But H is collision resistant, a contradiction.
- If ![latex-077b4e0a-62fe-44b3-822b-c23b6055b045](data/lecture34/latex-077b4e0a-62fe-44b3-822b-c23b6055b045.png), then ![latex-a81ae9a5-584b-42c1-8f54-30059b4b737a](data/lecture34/latex-a81ae9a5-584b-42c1-8f54-30059b4b737a.png) for some ![latex-dc3b38ae-b7d2-4839-8b9a-61d110bbedea](data/lecture34/latex-dc3b38ae-b7d2-4839-8b9a-61d110bbedea.png)
  - WLOG, suppose ![latex-2a0098bc-3da6-43aa-8af5-7d98e5d96bfd](data/lecture34/latex-2a0098bc-3da6-43aa-8af5-7d98e5d96bfd.png). The adversary knows ![latex-adf800f7-c0b1-43c1-826d-6ccff151aad1](data/lecture34/latex-adf800f7-c0b1-43c1-826d-6ccff151aad1.png). Then the adversary must have computed a preimage of ![latex-e142968a-9186-465b-a4ed-4a3fa7363230](data/lecture34/latex-e142968a-9186-465b-a4ed-4a3fa7363230.png), ![latex-ea5ae174-898c-426d-812b-c943447175c0](data/lecture34/latex-ea5ae174-898c-426d-812b-c943447175c0.png) where ![latex-77dfd6ce-4c43-4bd9-849f-71b0ea7cebd4](data/lecture34/latex-77dfd6ce-4c43-4bd9-849f-71b0ea7cebd4.png), but G is preimage resistant. A contradiction.
  - **Note**: ![latex-5fcdf3cf-2186-463d-9442-27cc74e02b70](data/lecture34/latex-5fcdf3cf-2186-463d-9442-27cc74e02b70.png) may not be equal to ![latex-33655fe9-6dec-430c-86cf-a6fa91a27f4c](data/lecture34/latex-33655fe9-6dec-430c-86cf-a6fa91a27f4c.png), as long as the hash value is the same the scheme will work.

### Facts
- The cheapest (classical or quantum) algorithm known for finding collisions of H is VW.
  - There is a faster quantum algorithm, but the massive space requirements make it not practical.
- The fastest/cheapest (classical or quantum) algorithm known for finding preimages of G is **Grover's Search**, in time ![latex-4f5ed2da-2b9d-4a1a-bb6d-5f3c49e3599a](data/lecture34/latex-4f5ed2da-2b9d-4a1a-bb6d-5f3c49e3599a.png) quantum time (operations).
  - Note that the fastest classical would be ![latex-2c021063-e4fd-4605-869b-658c7d0ebbdc](data/lecture34/latex-2c021063-e4fd-4605-869b-658c7d0ebbdc.png) (brute force)

### Drawbacks of the scheme
- Very large keys
- can only use the keys once, very hard to manage in practice.

### Fixing the Key Problem (Merkle's authentication trees)
- **Goal**: Make available large amounts of public data in a verifiable way.
- Pick a power of two public keys, ![latex-f537c399-69b5-44dc-bc36-288d5a631127](data/lecture34/latex-f537c399-69b5-44dc-bc36-288d5a631127.png)
- Build a binary tree, with the number of leaf nodes equal to the number of public keys
- each leaf node has a hash value corresponding to the hash of the public key
- The hash of each parent is equal to the hash of the concatentation of it's children.
- The root value is Alice's new public key.

![alt text](data/lecture34/board.jpg "Logo Title Text 1")

Suppose Alice signs a message wth her 5th key pair.
- Assume that Bob has an authenticated copy of R (through Certs, or embedded in browser)
- Bob now needs an authentic copy of ![latex-c30e88dd-229a-4b8d-b26d-5125ad17b44a](data/lecture34/latex-c30e88dd-229a-4b8d-b26d-5125ad17b44a.png), he obtains this by obtaining it from an untrusted public source.
  - Bob also needs the public keys belonging to the sister nodes, draw a path from the leaf to the roof, fill in the dependencies.
- Bob obtains ![latex-fbb53003-4114-4e05-a1f2-d74156bf74ef](data/lecture34/latex-fbb53003-4114-4e05-a1f2-d74156bf74ef.png) and computes ![latex-707d4f6f-e0dc-472e-9ef9-501cd707daf8](data/lecture34/latex-707d4f6f-e0dc-472e-9ef9-501cd707daf8.png)
- Check that ![latex-5513982d-8ea1-4c6b-a8eb-df56b9f1462e](data/lecture34/latex-5513982d-8ea1-4c6b-a8eb-df56b9f1462e.png)
  - Recall that H is collision resistant, then if ![latex-d63ee408-ad63-41c0-89eb-2f774fc2bf14](data/lecture34/latex-d63ee408-ad63-41c0-89eb-2f774fc2bf14.png) it must be the real R, otherwise you would have found a collision.
- There for the authenticity of ![latex-f01f8fad-7abd-4b76-953e-fd07f9b70bb2](data/lecture34/latex-f01f8fad-7abd-4b76-953e-fd07f9b70bb2.png)

In general, to make ![latex-0c1c8327-6510-425f-8104-59ce439d6d74](data/lecture34/latex-0c1c8327-6510-425f-8104-59ce439d6d74.png) LD keys available, the tree has height ![latex-469ac132-c3fb-455b-b911-12cc8659743a](data/lecture34/latex-469ac132-c3fb-455b-b911-12cc8659743a.png). And so one obtains authentic copies of a public key ![latex-dfaab840-a652-4fd7-ab6f-9620cf56438e](data/lecture34/latex-dfaab840-a652-4fd7-ab6f-9620cf56438e.png) by performing ![latex-f63679bb-6230-4ea5-8bfa-de9241dc0c2c](data/lecture34/latex-f63679bb-6230-4ea5-8bfa-de9241dc0c2c.png) hash computations.
- This gives you
