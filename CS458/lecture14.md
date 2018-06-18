# Lecture 14 - June 18, 2018

## Public Key Encryption

### Key Exchange

Alice and Bob need to exchange a secret key in order communicate.

Use public key crypto to share a shared secret (session key), then use a symettric scheme (AES)
- RSA requires large keys (2048+ bit) to be secure, slow, expensive.
- AES 128-ish bit keys are sufficient, much faster
- **Hybrid Cryptography**

### Properties of secure hash functions
- Preimage resistance: Given H(x), infeasible to find x
- Second Preimage resistance: Given ![latex-09bb9948-8752-4db9-9992-c2a35e8c8c63](data/lecture14/latex-09bb9948-8752-4db9-9992-c2a35e8c8c63.png), infeasible to find x' s.t ![latex-3b728432-09ee-4c78-8edd-ad78c867055b](data/lecture14/latex-3b728432-09ee-4c78-8edd-ad78c867055b.png) and ![latex-43b1b09d-9995-407d-974e-c508198788f0](data/lecture14/latex-43b1b09d-9995-407d-974e-c508198788f0.png)
- Collision resistant: It is infeasible to find ![latex-7caeee7a-ad60-4800-8f12-17ba97ec471a](data/lecture14/latex-7caeee7a-ad60-4800-8f12-17ba97ec471a.png) st. ![latex-9ddf2451-d8c9-497c-bb43-3d6440d7985b](data/lecture14/latex-9ddf2451-d8c9-497c-bb43-3d6440d7985b.png) and ![latex-482d977e-fbe8-409f-a4e9-a99536ced81d](data/lecture14/latex-482d977e-fbe8-409f-a4e9-a99536ced81d.png)
