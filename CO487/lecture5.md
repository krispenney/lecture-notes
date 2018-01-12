# Lecture 5 - January 12

## Feistel Ladder
- ![latex-16072cdc-7ab5-4b46-b540-9c86475d91d1](data/lecture5/latex-16072cdc-7ab5-4b46-b540-9c86475d91d1.png)

### Chosen plaintext attack on NDS
**Scenario**: Alice and Bob share the secret key *k*
**Adversary's goal: Find *k*

**Adversary's capabilities:**
- Knows everything about the NDS (i.e. the algo), except for *k*
- Has an encryption oracle (wrt *k*)

**Main Observation:**
Let ![latex-adb9d528-9101-4b9d-ab6e-27f52e099602](data/lecture5/latex-adb9d528-9101-4b9d-ab6e-27f52e099602.png) denote one round of encryption (wrt *k*), so ![latex-eb5c411b-d000-41a7-bf48-c25d4cef5af9](data/lecture5/latex-eb5c411b-d000-41a7-bf48-c25d4cef5af9.png)

Let ![latex-7ef14c14-231c-4545-a356-66e4570f2a39](data/lecture5/latex-7ef14c14-231c-4545-a356-66e4570f2a39.png) denote the enryption function (i.e. all 16 rounds), meaning ![latex-5ba0704c-6ff4-4b97-9140-14aa2a3552d9](data/lecture5/latex-5ba0704c-6ff4-4b97-9140-14aa2a3552d9.png)

Then for all m 128-bit strings, we have:

![latex-330a5f61-3e5e-426c-8630-01518bd54a1b](data/lecture5/latex-330a5f61-3e5e-426c-8630-01518bd54a1b.png)
Therefore, we have the communitive property.

**Attack**:
Fix a byte r, we'll determine ![latex-02aa03bf-6a4b-4719-b280-8e484b68870b](data/lecture5/latex-02aa03bf-6a4b-4719-b280-8e484b68870b.png) as follows.
Select ![latex-0c52bf8e-152d-4331-a014-cd36b50b0e7d](data/lecture5/latex-0c52bf8e-152d-4331-a014-cd36b50b0e7d.png) such that:
  1. ![latex-0c620e9f-a023-4a10-be5f-7797eb120fc9](data/lecture5/latex-0c620e9f-a023-4a10-be5f-7797eb120fc9.png): First bit in every byte in ![latex-26d96106-e065-4b6c-b060-7f7fe7ba3c3a](data/lecture5/latex-26d96106-e065-4b6c-b060-7f7fe7ba3c3a.png)
  2. ![latex-3dfe747d-ab96-42e5-8f1d-910f2f908bb7](data/lecture5/latex-3dfe747d-ab96-42e5-8f1d-910f2f908bb7.png) for each j, 1 <= j <= 8.
Next, encrypt u (by asking the oracle) and recieve the ciphertext, ![latex-563969d9-2d93-431f-bbef-5b3549b669cd](data/lecture5/latex-563969d9-2d93-431f-bbef-5b3549b669cd.png)

**Note**: ![latex-165944ff-4862-4cb0-9b50-68cb823795dc](data/lecture5/latex-165944ff-4862-4cb0-9b50-68cb823795dc.png), we can't know the right half, since we can't do the encryption ourselves.
Hence, ![latex-85564aca-b02f-4dd5-8f30-a370a843b765](data/lecture5/latex-85564aca-b02f-4dd5-8f30-a370a843b765.png)

Now, let's guess that ![latex-342b052b-2dae-4cf6-b635-0b616dbc60f9](data/lecture5/latex-342b052b-2dae-4cf6-b635-0b616dbc60f9.png), where *t* is a byte.
Apply one round of encryption to u, assuming that *t* was guessed correctly. Call the result ![latex-8b80a440-bd54-4ea2-a9fa-62dc286cd61b](data/lecture5/latex-8b80a440-bd54-4ea2-a9fa-62dc286cd61b.png)
To check the guess, obtain the encryption ![latex-9b430961-46eb-42eb-b0b3-15eb4fcf9553](data/lecture5/latex-9b430961-46eb-42eb-b0b3-15eb4fcf9553.png) from the oracle: ![latex-afedbb37-8c44-4669-b59c-17e19a6f5b78](data/lecture5/latex-afedbb37-8c44-4669-b59c-17e19a6f5b78.png).
- If the guess was correct: then ![latex-f3c3996b-8004-4883-908d-a15101dbdde2](data/lecture5/latex-f3c3996b-8004-4883-908d-a15101dbdde2.png), so ![latex-ea980f3c-e35c-41eb-86dd-53ce9dfa05ad](data/lecture5/latex-ea980f3c-e35c-41eb-86dd-53ce9dfa05ad.png)
- If the guess was incorrect: Then ![latex-c60a75fe-323e-4dbe-91b3-10b0e119dcba](data/lecture5/latex-c60a75fe-323e-4dbe-91b3-10b0e119dcba.png) (by condition of selecting *u* above)

Hence, if we make the heuristic assumption that: F behaves like a random function, the probability that the left half (c) of ![latex-8672a515-cf55-4e5c-9751-2ed663f634ae](data/lecture5/latex-8672a515-cf55-4e5c-9751-2ed663f634ae.png) equals the left half of ![latex-2e32f893-745f-486b-92fe-2e43c45274a5](data/lecture5/latex-2e32f893-745f-486b-92fe-2e43c45274a5.png) is ![latex-54bd17e6-1458-45eb-be0e-12ded6d6fbca](data/lecture5/latex-54bd17e6-1458-45eb-be0e-12ded6d6fbca.png), which is neglidgibly small.
- If ![latex-b497da51-75cc-4870-ae80-031bdee9dcb4](data/lecture5/latex-b497da51-75cc-4870-ae80-031bdee9dcb4.png), then ![latex-48b666bc-b196-40db-b2d3-34c84ec2b1a0](data/lecture5/latex-48b666bc-b196-40db-b2d3-34c84ec2b1a0.png)
- If ![latex-392d09ee-412c-4bf7-94e3-de79820443bc](data/lecture5/latex-392d09ee-412c-4bf7-94e3-de79820443bc.png), then ![latex-b26e5bf5-3cec-4431-be87-bf57a89267c0](data/lecture5/latex-b26e5bf5-3cec-4431-be87-bf57a89267c0.png) with high probability.

Summary:
For each ![latex-32fafefc-2cef-41bf-968b-aa5c4a5e9669](data/lecture5/latex-32fafefc-2cef-41bf-968b-aa5c4a5e9669.png) for the following
  - Select ![latex-a1150727-c51a-4d31-a9e9-53f5922a4cd7](data/lecture5/latex-a1150727-c51a-4d31-a9e9-53f5922a4cd7.png) such that the conditions above are true
  - Obtain ![latex-735a4a36-3123-4c84-b52d-1b8e1b42b114](data/lecture5/latex-735a4a36-3123-4c84-b52d-1b8e1b42b114.png) from Alice
  - For each byte t do:
    - Compute ![latex-f51af627-3774-4479-8207-3957ca1e6703](data/lecture5/latex-f51af627-3774-4479-8207-3957ca1e6703.png), obtain ![latex-c0a1fc5e-6f80-42ca-8b7e-f0ca71c7ed52](data/lecture5/latex-c0a1fc5e-6f80-42ca-8b7e-f0ca71c7ed52.png)
    - If ![latex-c2836a33-2bc6-4011-84e4-7148fb1eaf97](data/lecture5/latex-c2836a33-2bc6-4011-84e4-7148fb1eaf97.png), then
      - ![latex-ff63b7ce-7a99-44e0-8129-82ad902d0f58](data/lecture5/latex-ff63b7ce-7a99-44e0-8129-82ad902d0f58.png)
      - goto the next r.
    - If ![latex-70b18426-3014-4e9d-9106-9ca791a146b8](data/lecture5/latex-70b18426-3014-4e9d-9106-9ca791a146b8.png), then
      - goto next r

Analysis:
- The number of chosen plaintexts is at most ![latex-84c76497-de67-470c-87b8-1e01a59757a6](data/lecture5/latex-84c76497-de67-470c-87b8-1e01a59757a6.png) iterations
- Note that this is a feasible number of iterations.

**Assignment 2: Is an MDS-like toy cipher.**
