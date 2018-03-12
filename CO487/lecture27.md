# Lecture 27 - March 12, 2018

## DigiNotar
- was a CA, root CA embedded in all browsers.
- Issed hundreds of false certificates (including for `*.google.com`)
- Directed 300,000 iranian gmail users to a false site.

### Dealing with CA Breaches
- Browser developers (Apple, Google, Mozilla), want users to trust their browsers, as well as the websites they visit.
- **Extended Validation:** Root CA's must now meet stricter requirements (doing so gives you the green bar)
- **Certificate Transperancy**: CA's publish all of the certificates that they publish
  - Append only, they can't remove past certs

## Methods of Establishing Shared Secrets
- Use of RSA is decreasing
- Now being replaced with Eliptical Curve Diffie-Helmen

## Ellpitic Curve Cryptograhy (ECC)
- Public-key crypto scheme
- alternative to RSA
- Developed in 1985
- **Definition**: Let ![latex-fee70da5-1901-445e-a201-e50a436a26be](data/lecture27/latex-fee70da5-1901-445e-a201-e50a436a26be.png) or ![latex-d085f4d8-7b96-4794-8b33-894e0db2d900](data/lecture27/latex-d085f4d8-7b96-4794-8b33-894e0db2d900.png) (integers modulo p ![latex-5a023c70-8f58-41d9-8c29-3e5b874683c8](data/lecture27/latex-5a023c70-8f58-41d9-8c29-3e5b874683c8.png)
  - If ![latex-b80b5f9b-cee7-43cd-b6ec-e0de978abf01](data/lecture27/latex-b80b5f9b-cee7-43cd-b6ec-e0de978abf01.png)
  - ![latex-6fae50d8-637c-4317-9d14-d6bc912bd555](data/lecture27/latex-6fae50d8-637c-4317-9d14-d6bc912bd555.png)
  - ![latex-5fe2e44c-80ff-41d9-ba48-a4002e1e3eda](data/lecture27/latex-5fe2e44c-80ff-41d9-ba48-a4002e1e3eda.png)
- An **elliptic curve** E over F is defined by:
  - ![latex-4d4ccfe9-deae-44ab-8062-b7e905978662](data/lecture27/latex-4d4ccfe9-deae-44ab-8062-b7e905978662.png)
  - ![latex-b1e4fb9a-2641-4db5-b686-d0e3955cc5a6](data/lecture27/latex-b1e4fb9a-2641-4db5-b686-d0e3955cc5a6.png)
  - ![latex-4d914409-e169-4578-9503-3f80ba00f19b](data/lecture27/latex-4d914409-e169-4578-9503-3f80ba00f19b.png)
- In practical applications, we typically work with the integers mod p (it's hard to work with infinite sets!)
  - Elliptical curves over the reals give better geometric intuition.
  - Map this geometric intuition (over the reals), to algebra (over ints mod p)
- The set of **F-rational points on E**:
  - ![latex-52927536-3dcb-47ab-9bf7-a37ca38fdfdf](data/lecture27/latex-52927536-3dcb-47ab-9bf7-a37ca38fdfdf.png)
  - Where ![latex-e63b3268-6709-46b7-aae2-a207e1455c1c](data/lecture27/latex-e63b3268-6709-46b7-aae2-a207e1455c1c.png) is the point of **infinity**
  - ![latex-c30b164c-d81e-42e3-bac4-e72eae9cb02b](data/lecture27/latex-c30b164c-d81e-42e3-bac4-e72eae9cb02b.png)
  - ![latex-2d005490-e9e3-4738-ac4f-28b155560bf1](data/lecture27/latex-2d005490-e9e3-4738-ac4f-28b155560bf1.png)
    - Always have ![latex-21d2a118-6c73-41d4-8a8e-97fa76b2243b](data/lecture27/latex-21d2a118-6c73-41d4-8a8e-97fa76b2243b.png), find the others by trial and error.
    - Example: No solution for ![latex-bbd3c60c-fd4f-49a9-9d19-94e22c37ef69](data/lecture27/latex-bbd3c60c-fd4f-49a9-9d19-94e22c37ef69.png)
    - Note that this is a finite set, there are only so many possible x values.
  - **Note**: Let ![latex-d96e5c31-ffbe-479b-8f02-a2a69bae4fec](data/lecture27/latex-d96e5c31-ffbe-479b-8f02-a2a69bae4fec.png)
    - Then ![latex-111dcf1a-d112-4a88-adfe-c73f2efcb3a5](data/lecture27/latex-111dcf1a-d112-4a88-adfe-c73f2efcb3a5.png)
      - Always have the infinite point
      - At most, every x value has a solution, meaning 2 points + inf point.
      - **Hasse's Theorem**: Gives ![latex-d51f83f4-b737-4e71-be02-06e3b074880a](data/lecture27/latex-d51f83f4-b737-4e71-be02-06e3b074880a.png)
        - Notice that when p is very large, the size of the set is ![latex-99c315d4-0d4f-4fb0-96ec-d053755b7ffc](data/lecture27/latex-99c315d4-0d4f-4fb0-96ec-d053755b7ffc.png)
    - The size of this set is what will determine the security of the system

### Addition Rule
- Given two points ![latex-8537a267-3745-46b7-aa67-a99423c7435e](data/lecture27/latex-8537a267-3745-46b7-aa67-a99423c7435e.png), define a point ![latex-00dc2d5a-ed8a-488a-89b3-297666ea1f10](data/lecture27/latex-00dc2d5a-ed8a-488a-89b3-297666ea1f10.png)

#### Chord Case
- Geometrically (in the reals): Draw a straight line through the points, the line will intersect the curve at a third point. The negation of that point is the addition.

#### Tangent Rule: Add a point to it's self
- Draw the tangent line of the point P
- Reflect the point of intersection

#### Vertical Case
- Drawing a vertical line, doesn't intersect the curve
- Define this case to ![latex-29f9baff-f308-4e1c-a848-5f716794ef08](data/lecture27/latex-29f9baff-f308-4e1c-a848-5f716794ef08.png)

#### Algebraic Definitions
Given ![latex-2b7ddf67-2faf-4bb9-ae57-09de1c1a541d](data/lecture27/latex-2b7ddf67-2faf-4bb9-ae57-09de1c1a541d.png) over a general field

1. ![latex-4f785c65-48e9-473d-806d-a51848003fa3](data/lecture27/latex-4f785c65-48e9-473d-806d-a51848003fa3.png)
2. If ![latex-d9ec6411-489c-46fa-8e75-d132a3aa4bcb](data/lecture27/latex-d9ec6411-489c-46fa-8e75-d132a3aa4bcb.png) and ![latex-077e2dcc-d9fa-437c-a833-8be16e23c6eb](data/lecture27/latex-077e2dcc-d9fa-437c-a833-8be16e23c6eb.png), then ![latex-a62db2be-8479-4771-8059-e4e89e64d39e](data/lecture27/latex-a62db2be-8479-4771-8059-e4e89e64d39e.png)
  - We write ![latex-1ca5f6a1-72a3-4a54-8038-a84cd921f1ea](data/lecture27/latex-1ca5f6a1-72a3-4a54-8038-a84cd921f1ea.png)
  - ![latex-7f3f8e7d-c42d-4e11-bd14-199f89200bbe](data/lecture27/latex-7f3f8e7d-c42d-4e11-bd14-199f89200bbe.png)
  - Sideeffect: ![latex-e8a63923-2981-4aa0-9163-bd4831afef61](data/lecture27/latex-e8a63923-2981-4aa0-9163-bd4831afef61.png)
3. If ![latex-56f2fdff-b3a7-4f0c-9ebe-af4047810907](data/lecture27/latex-56f2fdff-b3a7-4f0c-9ebe-af4047810907.png) and ![latex-11d178f6-655a-4937-97df-f2346d4a9eaa](data/lecture27/latex-11d178f6-655a-4937-97df-f2346d4a9eaa.png)
  - Chord case
  - Want ![latex-e34d7399-12d7-4bc8-8772-56916a6759b1](data/lecture27/latex-e34d7399-12d7-4bc8-8772-56916a6759b1.png) and ![latex-2fb3302b-d32b-4ba5-8b21-053f10631fd6](data/lecture27/latex-2fb3302b-d32b-4ba5-8b21-053f10631fd6.png)
  - ![latex-ab7fdc51-e1f3-40b2-9b0c-24baa4ce43a7](data/lecture27/latex-ab7fdc51-e1f3-40b2-9b0c-24baa4ce43a7.png)
    - ![latex-7a203cd9-f4b1-4111-952f-045d0a3e7495](data/lecture27/latex-7a203cd9-f4b1-4111-952f-045d0a3e7495.png)
    - ![latex-076ed3ad-4713-4970-8dcf-203e81886dda](data/lecture27/latex-076ed3ad-4713-4970-8dcf-203e81886dda.png)
    - ![latex-cc64c665-9977-457d-b09e-4d02b239afbb](data/lecture27/latex-cc64c665-9977-457d-b09e-4d02b239afbb.png)
  - Note that this is always defined (not equal cases)
