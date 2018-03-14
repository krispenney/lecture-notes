# Lecture 28 - March 14, 2018

## Elliptic Curves
- Recall: ![latex-f9187384-6422-4971-ab72-f5515371f9b1](data/lecture28/latex-f9187384-6422-4971-ab72-f5515371f9b1.png)
- Addition rules
  1. ![latex-d142f66f-92ee-4ff8-8cc0-bfb54be3766d](data/lecture28/latex-d142f66f-92ee-4ff8-8cc0-bfb54be3766d.png)
  2. If ![latex-a7df22a4-2305-4f97-98de-d6742aca2856](data/lecture28/latex-a7df22a4-2305-4f97-98de-d6742aca2856.png), ![latex-258dab13-74f5-42c8-9f85-9bdb4d10524c](data/lecture28/latex-258dab13-74f5-42c8-9f85-9bdb4d10524c.png), then ![latex-7d30ffe8-8ea6-4fae-a25d-d29d1e9b70fe](data/lecture28/latex-7d30ffe8-8ea6-4fae-a25d-d29d1e9b70fe.png)
  3. If ![latex-997e6444-01a0-4247-b7d8-3d3d9f2e8366](data/lecture28/latex-997e6444-01a0-4247-b7d8-3d3d9f2e8366.png) and ![latex-96fa3f7c-445e-41c8-8931-00265479c896](data/lecture28/latex-96fa3f7c-445e-41c8-8931-00265479c896.png), ![latex-0585946a-2e85-4522-8ec3-3e2a1a6de067](data/lecture28/latex-0585946a-2e85-4522-8ec3-3e2a1a6de067.png).
    - ![latex-03f954a9-e9ea-4293-8b40-9e28dd810ad8](data/lecture28/latex-03f954a9-e9ea-4293-8b40-9e28dd810ad8.png)
  4. If ![latex-a4075598-a3b1-4f50-b33c-354220dd6b45](data/lecture28/latex-a4075598-a3b1-4f50-b33c-354220dd6b45.png) (<- case 2), then ![latex-e9c11863-007e-4539-9ac7-d58784fcd9b9](data/lecture28/latex-e9c11863-007e-4539-9ac7-d58784fcd9b9.png), where:
    - ![latex-4aa33e2d-6fc3-438a-bac7-4f01d69b7eff](data/lecture28/latex-4aa33e2d-6fc3-438a-bac7-4f01d69b7eff.png), ![latex-93cef2ea-2923-43cc-a9b9-ecc1af56b907](data/lecture28/latex-93cef2ea-2923-43cc-a9b9-ecc1af56b907.png), ![latex-0230fe85-7c9a-4f31-a929-2ae07396e431](data/lecture28/latex-0230fe85-7c9a-4f31-a929-2ae07396e431.png)
    - Note that ![latex-a0ef30a0-4110-4870-9e2f-250e3974fae9](data/lecture28/latex-a0ef30a0-4110-4870-9e2f-250e3974fae9.png), if it did then ![latex-2967b555-d73f-40fb-a320-d62c914a056c](data/lecture28/latex-2967b555-d73f-40fb-a320-d62c914a056c.png), which is covered by case 2.

### Proof of 3

The equation of ![latex-7efbaba9-8649-4f0d-b67d-01edb41a158d](data/lecture28/latex-7efbaba9-8649-4f0d-b67d-01edb41a158d.png) is ![latex-5896a161-eb5d-4aab-ab4d-ae9646ade530](data/lecture28/latex-5896a161-eb5d-4aab-ab4d-ae9646ade530.png), where ![latex-d1970454-b6b1-4bd8-b9b4-a7c087a439aa](data/lecture28/latex-d1970454-b6b1-4bd8-b9b4-a7c087a439aa.png):
- ![latex-51cbec59-b8ba-4734-b396-0e9a27b87447](data/lecture28/latex-51cbec59-b8ba-4734-b396-0e9a27b87447.png)
- ![latex-fcd10ef8-6064-4b41-9946-a0faa4d486e7](data/lecture28/latex-fcd10ef8-6064-4b41-9946-a0faa4d486e7.png)
- We know ![latex-aeb55ee3-7dae-429a-a64d-171b4c55f42f](data/lecture28/latex-aeb55ee3-7dae-429a-a64d-171b4c55f42f.png) are solutions to this cubic equation. Let ![latex-e780b965-8294-4d05-9629-024ff4e12787](data/lecture28/latex-e780b965-8294-4d05-9629-024ff4e12787.png) be the third solution.
- ![latex-d897a520-67d7-4ac2-9c89-f5b4b1a58fd0](data/lecture28/latex-d897a520-67d7-4ac2-9c89-f5b4b1a58fd0.png)
- Equate coefficients of ![latex-2ca79aef-1582-4643-bdfc-56865060d863](data/lecture28/latex-2ca79aef-1582-4643-bdfc-56865060d863.png)
- ![latex-c034d4fe-2e12-436f-aca2-983b05d72a7c](data/lecture28/latex-c034d4fe-2e12-436f-aca2-983b05d72a7c.png), solve for ![latex-498e23f9-2012-44f4-854c-6e7d3ed29646](data/lecture28/latex-498e23f9-2012-44f4-854c-6e7d3ed29646.png)
- ![latex-dc7a7798-9f4b-44d9-84a3-ac5c3fc38d4a](data/lecture28/latex-dc7a7798-9f4b-44d9-84a3-ac5c3fc38d4a.png)
- Note that there can only be one point of intersection (![latex-51ba72dd-c831-491b-9a42-cb400decb1f5](data/lecture28/latex-51ba72dd-c831-491b-9a42-cb400decb1f5.png))

- ![latex-847b680e-98e6-495e-a865-137472029bf4](data/lecture28/latex-847b680e-98e6-495e-a865-137472029bf4.png)
- ![latex-96a5ed97-45cc-46b8-a68a-c05099b994e3](data/lecture28/latex-96a5ed97-45cc-46b8-a68a-c05099b994e3.png)

### Some Facts

The addition satisfies pleasing properties:
1. ![latex-566df1a7-1e05-4ce6-98b4-d246f299bc19](data/lecture28/latex-566df1a7-1e05-4ce6-98b4-d246f299bc19.png)
  - Implies ![latex-98378c2b-91d7-4c8c-b972-5fa2e252e4ca](data/lecture28/latex-98378c2b-91d7-4c8c-b972-5fa2e252e4ca.png) is the 0 point, as per the definition (no proof required)
2. ![latex-57b51b32-eeaf-4be3-a0d8-aecb2f3ff690](data/lecture28/latex-57b51b32-eeaf-4be3-a0d8-aecb2f3ff690.png) such that ![latex-9ea1dac7-c2a0-421b-8fd8-8c11d8a1100c](data/lecture28/latex-9ea1dac7-c2a0-421b-8fd8-8c11d8a1100c.png)
3. ![latex-5104fddb-88e8-46db-95ce-2f0c3e2a0d93](data/lecture28/latex-5104fddb-88e8-46db-95ce-2f0c3e2a0d93.png)
  - Commutative
  - Recall the rule geometrically, a line through P and Q is the same through a line through Q and P.
4. ![latex-0026ba3f-4461-4cba-a6d7-37ebf132073e](data/lecture28/latex-0026ba3f-4461-4cba-a6d7-37ebf132073e.png)
  - We'll skip the proof

### Elliptic Curve Descrete Logarithm Problem (ECDLP)

Let ![latex-41d8da36-2358-4092-97b2-61f537b51025](data/lecture28/latex-41d8da36-2358-4092-97b2-61f537b51025.png) be a prime, ![latex-26a6dfdb-73d5-47c4-96c0-61c36f54fbc2](data/lecture28/latex-26a6dfdb-73d5-47c4-96c0-61c36f54fbc2.png), let ![latex-bc4f147e-ccac-4bbc-8619-bd81a66087b8](data/lecture28/latex-bc4f147e-ccac-4bbc-8619-bd81a66087b8.png), let n be the number of points (n is prime, if not try again until it is)
- Fact: Let ![latex-3374c2aa-814f-4d85-974e-ca4f36683459](data/lecture28/latex-3374c2aa-814f-4d85-974e-ca4f36683459.png), then ![latex-2b378a75-48b8-4c8a-b9c5-8a52b1e0582b](data/lecture28/latex-2b378a75-48b8-4c8a-b9c5-8a52b1e0582b.png) is pairwise distinct is equal to ![latex-c18b7bfb-5482-4f92-965d-7f878758c1c2](data/lecture28/latex-c18b7bfb-5482-4f92-965d-7f878758c1c2.png) (all of the points on the curve).
- Lastly, ![latex-69fa7740-2c74-4d04-ae0c-d1746276a6ac](data/lecture28/latex-69fa7740-2c74-4d04-ae0c-d1746276a6ac.png), note ![latex-b38432de-d8f1-461c-a5fd-c08767531e3e](data/lecture28/latex-b38432de-d8f1-461c-a5fd-c08767531e3e.png), therefore a cycle.
- P is called a generator of the set of all points (![latex-cf833175-5477-44ef-adab-599e5bb86227](data/lecture28/latex-cf833175-5477-44ef-adab-599e5bb86227.png))

**Problem Definition**: Given ![latex-2aa78c45-7ab1-4ff3-8e92-2317ceae3fed](data/lecture28/latex-2aa78c45-7ab1-4ff3-8e92-2317ceae3fed.png), ![latex-bd2ce70e-eab5-43e1-87a3-53831127c48f](data/lecture28/latex-bd2ce70e-eab5-43e1-87a3-53831127c48f.png) and ![latex-c91b77b4-cb65-41b6-963b-b7fd6ba46a7f](data/lecture28/latex-c91b77b4-cb65-41b6-963b-b7fd6ba46a7f.png). Find ![latex-3f3efaed-132b-485d-83d2-1632d5e29cc4](data/lecture28/latex-3f3efaed-132b-485d-83d2-1632d5e29cc4.png) such that ![latex-33cb59cd-4dde-486d-a7f4-0e03c51b310d](data/lecture28/latex-33cb59cd-4dde-486d-a7f4-0e03c51b310d.png).
- We say that ![latex-3ae96588-7876-4b14-8835-7061f194bf3e](data/lecture28/latex-3ae96588-7876-4b14-8835-7061f194bf3e.png)
- When n is very large, this is a hard problem.

#### Input Size
- ![latex-5177ff34-a08f-4e3d-ac24-e37036494c31](data/lecture28/latex-5177ff34-a08f-4e3d-ac24-e37036494c31.png) bits
- Everything is mod p, so all are ![latex-7752fb38-5e0c-4f95-86da-d339bc483095](data/lecture28/latex-7752fb38-5e0c-4f95-86da-d339bc483095.png) bits.
- ![latex-049ee94c-fd14-448d-a2ab-af2d150bdb53](data/lecture28/latex-049ee94c-fd14-448d-a2ab-af2d150bdb53.png) bits

#### Known Attacks
1. **Brute Force**: Add P to itself until you get Q.
  - You will eventually get Q as P generates all points
  - Run time is ![latex-216f4386-3899-4839-9282-2ab4ba2e4ba3](data/lecture28/latex-216f4386-3899-4839-9282-2ab4ba2e4ba3.png) point additions. Since n is roughly p (recall rounds), ![latex-6d2aadeb-3008-43b9-95be-e7f848e9a300](data/lecture28/latex-6d2aadeb-3008-43b9-95be-e7f848e9a300.png) additions, which is not polynomial time.
2. **Shanks' Attack**: Write ![latex-ca0036b1-c91e-4a1e-87db-1c6d5b774d9a](data/lecture28/latex-ca0036b1-c91e-4a1e-87db-1c6d5b774d9a.png) ![latex-6720e88a-0363-4e89-ac83-8e69bb9615b9](data/lecture28/latex-6720e88a-0363-4e89-ac83-8e69bb9615b9.png), where ![latex-333fa21a-4410-4b5c-99a4-e1ab8aefb279](data/lecture28/latex-333fa21a-4410-4b5c-99a4-e1ab8aefb279.png)
  - Then ![latex-d338de07-1437-4380-9dc1-01ef901f808a](data/lecture28/latex-d338de07-1437-4380-9dc1-01ef901f808a.png)
  - ![latex-e126b110-0a2b-47de-abc6-434016b2b44f](data/lecture28/latex-e126b110-0a2b-47de-abc6-434016b2b44f.png)
  - ![latex-240823b8-6e54-4e49-b0dd-a9e14e321d92](data/lecture28/latex-240823b8-6e54-4e49-b0dd-a9e14e321d92.png)
  - **Meet in the middle attack**
  - ![latex-b7d46cc5-948a-4519-aa59-555c3ebae658](data/lecture28/latex-b7d46cc5-948a-4519-aa59-555c3ebae658.png) are on opposite sides of the curve
  - Each have ![latex-f2f55e0d-2e6d-499e-9013-59b4ddc1dff8](data/lecture28/latex-f2f55e0d-2e6d-499e-9013-59b4ddc1dff8.png) possible values
  - **Algorithm**
    1. For a table of points ![latex-79e4fc7a-56ec-4d04-bd33-7a435631648f](data/lecture28/latex-79e4fc7a-56ec-4d04-bd33-7a435631648f.png) (sorted by first entry)
    2. Compute all possible ![latex-d6c1788e-05a4-43a9-a95e-a57de735ab28](data/lecture28/latex-d6c1788e-05a4-43a9-a95e-a57de735ab28.png) and look it up in the table.
    3. If ![latex-e518a24e-fc4c-4e76-8905-b70ac06690b8](data/lecture28/latex-e518a24e-fc4c-4e76-8905-b70ac06690b8.png), then output ![latex-ca480c3f-3218-4022-9f0c-8e70fb93fefb](data/lecture28/latex-ca480c3f-3218-4022-9f0c-8e70fb93fefb.png)
    - ![latex-99deec95-5028-46e0-851d-2abcb1a55099](data/lecture28/latex-99deec95-5028-46e0-851d-2abcb1a55099.png) (elliptic curve operations)
    - Again not polynomial, but better than brute force.
    - **Drawback**: High space requirements, ![latex-97382479-4a4e-428c-8441-c2d4b0900f46](data/lecture28/latex-97382479-4a4e-428c-8441-c2d4b0900f46.png)
      - Similar to Double-DES Attack, there's a trade-off (see next class).
  - How to compute ![latex-e58ee0b7-8627-458f-b3bb-e62a197002c4](data/lecture28/latex-e58ee0b7-8627-458f-b3bb-e62a197002c4.png)?
    - Add P to itself k times, efficiently
    - "Repeated square and add" (see A5), analogus to ![latex-4307bbac-65ab-4af3-9c38-7a456442ed62](data/lecture28/latex-4307bbac-65ab-4af3-9c38-7a456442ed62.png)
