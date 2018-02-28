# Lecture 22 - February 28, 2018

## Population Coding

### Linear Coding

Goal is to find a set of decoding weights ![latex-b01c41e9-e6b3-4515-b6ec-1afd4ef35a0c](data/lecture22/latex-b01c41e9-e6b3-4515-b6ec-1afd4ef35a0c.png), such that ![latex-880ba17e-a106-43ec-8b6f-fc34ccc42c21](data/lecture22/latex-880ba17e-a106-43ec-8b6f-fc34ccc42c21.png).
- Or ![latex-f19d427b-e5b7-4865-8f21-7ee63bd2cc2b](data/lecture22/latex-f19d427b-e5b7-4865-8f21-7ee63bd2cc2b.png)

#### Least Squares

##### Method 1: Normal Equations
- The columns of A have to be linearly independent in order to have a unique solution.
- This method is efficient to compute, but may not be numerically stable.

![latex-369d8724-8aa8-4052-b095-58219c0364f7](data/lecture22/latex-369d8724-8aa8-4052-b095-58219c0364f7.png)
![latex-28729aec-1a9c-46ff-b1f2-1406b5ca1c9a](data/lecture22/latex-28729aec-1a9c-46ff-b1f2-1406b5ca1c9a.png)
![latex-fbe3d0ff-8b46-4c27-9c74-63c98e983255](data/lecture22/latex-fbe3d0ff-8b46-4c27-9c74-63c98e983255.png): Normal Equations
![latex-c7d9ff25-86a6-4fbc-908d-b17a028658dc](data/lecture22/latex-c7d9ff25-86a6-4fbc-908d-b17a028658dc.png)

##### Method 2: SVD
- A more computationally expensive method, but more numerically stable

Let $$U \sigma V^T = A$
- ![latex-72ac8fec-fb97-43ad-999a-e77ca0c73faf](data/lecture22/latex-72ac8fec-fb97-43ad-999a-e77ca0c73faf.png) are orthogonal matricies
- ![latex-ecc6f5e7-0c8d-481e-9715-8152209774c2](data/lecture22/latex-ecc6f5e7-0c8d-481e-9715-8152209774c2.png): diagonal matrix

![latex-b366c166-b384-4c34-a720-92836659d02e](data/lecture22/latex-b366c166-b384-4c34-a720-92836659d02e.png)
![latex-010eab51-9fd9-47f3-8bb4-ad9163b7672f](data/lecture22/latex-010eab51-9fd9-47f3-8bb4-ad9163b7672f.png)
![latex-f921ee5f-e485-432d-acbc-7f46d8aff6ee](data/lecture22/latex-f921ee5f-e485-432d-acbc-7f46d8aff6ee.png)
![latex-01f9453e-41ce-4ec6-b943-33a167ced8e0](data/lecture22/latex-01f9453e-41ce-4ec6-b943-33a167ced8e0.png)


