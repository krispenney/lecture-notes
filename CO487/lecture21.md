# Lecture 21 - February 26, 2018

## Chosen-Ciphertext attack on Revised WUP

- k: 128 bits
- ![latex-5547c20e-4e34-426d-9d8e-a06018de1779](data/lecture21/latex-5547c20e-4e34-426d-9d8e-a06018de1779.png): 1024 bits
- ![latex-8e084ffe-7c4f-4c36-be82-7433d0ebe64a](data/lecture21/latex-8e084ffe-7c4f-4c36-be82-7433d0ebe64a.png): 1024 bits
  - The rightmost 128-bits should be ![latex-8d30d1ca-5863-4838-82c7-78a728a96a01](data/lecture21/latex-8d30d1ca-5863-4838-82c7-78a728a96a01.png)
  - The rest are all 0's
- **Flaw:** They don't check the formatting (i.e. they only extract ![latex-40fcb1c5-c80b-49b0-9864-20c3d79c23ef](data/lecture21/latex-40fcb1c5-c80b-49b0-9864-20c3d79c23ef.png))

### Restricted Chosen Ciphertext attack on QQ Browser (6.5.0.2170)
- **Given**: Target ![latex-3bdddcf4-66ee-41ff-9c58-b36afad2c6ea](data/lecture21/latex-3bdddcf4-66ee-41ff-9c58-b36afad2c6ea.png)
- **Goal**: Compute ![latex-a83bdc8b-5abd-4a4f-9ac5-f07d74f92fba](data/lecture21/latex-a83bdc8b-5abd-4a4f-9ac5-f07d74f92fba.png), and then ![latex-811d9af2-3414-4493-8c65-feb9c230940d](data/lecture21/latex-811d9af2-3414-4493-8c65-feb9c230940d.png)
- **Restricted Oracle**: If you give an improperly formatted ciphertext, then the server will reject the message
  - You learn the ciphertext / plaintext was not properly formatted.
- **Attack**: We'll learn the bits of ![latex-77e902c4-b75f-4c9a-8d76-e09f2dcb6344](data/lecture21/latex-77e902c4-b75f-4c9a-8d76-e09f2dcb6344.png), one at a time:
  - $$k = k_{127} \mid\mid \ldots \mid\mid k_2 \mid\mid k_1

#### To Find k

- Compute ![latex-aa8c99c9-80b8-4ac2-bf4d-c581b0f1697a](data/lecture21/latex-aa8c99c9-80b8-4ac2-bf4d-c581b0f1697a.png)
  - i.e. ![latex-7219b3b7-4057-4131-8a7d-a4755971367d](data/lecture21/latex-7219b3b7-4057-4131-8a7d-a4755971367d.png) are the server's public key
  - **Note**: ![latex-d7790e32-f5b2-4faa-b998-7dc97c109e22](data/lecture21/latex-d7790e32-f5b2-4faa-b998-7dc97c109e22.png)
  - ![latex-a85cfab9-e560-479d-933a-6d21d1dd5c84](data/lecture21/latex-a85cfab9-e560-479d-933a-6d21d1dd5c84.png)
    - ![latex-f0fd854c-ff8e-4cc5-a6dc-742b13d63845](data/lecture21/latex-f0fd854c-ff8e-4cc5-a6dc-742b13d63845.png) shifted by 127 bits
    - ![latex-12335da8-e6a0-4995-8292-8a9d2ed9a135](data/lecture21/latex-12335da8-e6a0-4995-8292-8a9d2ed9a135.png): 255 bits, n is 1024 bits
  - first 128 k, 127 are 0's
- Note that the server decrypts ![latex-c517a31b-1c0d-41c1-a8fd-07d9404bc35c](data/lecture21/latex-c517a31b-1c0d-41c1-a8fd-07d9404bc35c.png) and obtains ![latex-6c39cd05-4ee0-4805-b30e-fa220c51908e](data/lecture21/latex-6c39cd05-4ee0-4805-b30e-fa220c51908e.png)
- Don't know if $k_0$ is 1 or 0
  - Guess that $k_0 = 1![latex-80abb296-8826-44b9-b304-692763f782d7](data/lecture21/latex-80abb296-8826-44b9-b304-692763f782d7.png)k' = 1 \mid\mid 0 \ldots 0$$
  - Select ![latex-730ae54d-c539-485f-bac6-1360b6fb85d0](data/lecture21/latex-730ae54d-c539-485f-bac6-1360b6fb85d0.png) and compute ![latex-bc48aa2b-14a7-4804-996c-df119679889c](data/lecture21/latex-bc48aa2b-14a7-4804-996c-df119679889c.png)
- Send ![latex-ccb1ef97-8098-458b-9e46-2016b97326c9](data/lecture21/latex-ccb1ef97-8098-458b-9e46-2016b97326c9.png) to the QQ server
- The server decrypts ![latex-fc13b9c5-736c-4cbf-addd-1f0643109403](data/lecture21/latex-fc13b9c5-736c-4cbf-addd-1f0643109403.png) to get ![latex-4f46dcfb-da8d-4b74-957e-226697eb4a19](data/lecture21/latex-4f46dcfb-da8d-4b74-957e-226697eb4a19.png)
- Note: If ![latex-5ac01e56-cb18-49b7-9d1c-8fd1061dc890](data/lecture21/latex-5ac01e56-cb18-49b7-9d1c-8fd1061dc890.png), then ![latex-fbb8608d-d639-4d55-a8c1-8f1ba7773e4e](data/lecture21/latex-fbb8608d-d639-4d55-a8c1-8f1ba7773e4e.png), so ![latex-a22b0809-bc60-4401-a355-3d5ce6892105](data/lecture21/latex-a22b0809-bc60-4401-a355-3d5ce6892105.png) is properly formatted
  - If ![latex-b2a1d701-23de-4fdc-8856-be2bdbc11f76](data/lecture21/latex-b2a1d701-23de-4fdc-8856-be2bdbc11f76.png), then so ![latex-2e2ec73f-5175-4b25-b479-5365cc0ac9cb](data/lecture21/latex-2e2ec73f-5175-4b25-b479-5365cc0ac9cb.png) is likely garbage. And therefore, the server won't respond
- You learn ![latex-9f8343ca-2dba-4ff4-a77f-c1316337f88c](data/lecture21/latex-9f8343ca-2dba-4ff4-a77f-c1316337f88c.png) depending on the response recieved from the server.
  - If it responds, you guessed correctly: ![latex-35614699-d1a3-4e0a-acd1-d404eaf15ed3](data/lecture21/latex-35614699-d1a3-4e0a-acd1-d404eaf15ed3.png)
  - If it doesn't respond, you guessed wrong: ![latex-6ff422d4-eb46-433c-941e-c49d012f708c](data/lecture21/latex-6ff422d4-eb46-433c-941e-c49d012f708c.png)
- Proceed similarly for ![latex-5a6cd548-6c4f-4dab-91e6-b252ae48b465](data/lecture21/latex-5a6cd548-6c4f-4dab-91e6-b252ae48b465.png), shifting k by ![latex-294d0b90-29b8-416c-81f1-98646b3a06e4](data/lecture21/latex-294d0b90-29b8-416c-81f1-98646b3a06e4.png) using your previous guesses.

## How to defend against chosen ciphertext attacks in practice
- **Definition:** A public-key encryption scheme is secure if it is semantically secure against chosen-ciphertext attack by computationally bounded adversaries.
  - Given access to a decryption oracle

### Approach 1: RSA PKCS 1 V1.5 Encryption
- **PKCS**: Public Key Cryptographic Standard, 1993
  - Used in SSL

#### Encryption


![graph-16315777-44e9-4716-933e-596a6174cc6b](data/lecture21/graph-16315777-44e9-4716-933e-596a6174cc6b.svg)

#### Decryption


![graph-6c0fc3e5-3fd8-4dbf-9d3d-ef4a7d81147a](data/lecture21/graph-6c0fc3e5-3fd8-4dbf-9d3d-ef4a7d81147a.svg)

#### Formatting
- Have a formatted plaintext ![latex-8d687878-c991-4c27-82a2-7f3e75598f49](data/lecture21/latex-8d687878-c991-4c27-82a2-7f3e75598f49.png) that is t-bytes long
- ![latex-a0c22eaf-f0ce-4cbf-b6c9-ed3b8207f13c](data/lecture21/latex-a0c22eaf-f0ce-4cbf-b6c9-ed3b8207f13c.png) the byte length of n
- Set ![latex-57b9c0f0-a635-40bb-bb63-d0c9c9ba6c4f](data/lecture21/latex-57b9c0f0-a635-40bb-bb63-d0c9c9ba6c4f.png) (the real plaintext) to the right
- ![latex-5944d0cb-8fa6-44c0-8d70-0c5b95a6895b](data/lecture21/latex-5944d0cb-8fa6-44c0-8d70-0c5b95a6895b.png)
- xx's -> The salt: Non zero-bytes random to fill in the space (at least 8 consecutively)
  - **Why random?**: Prevent a dictionary attack

### Approach 2: RSA-OAEP Encryption (1994)
- Let ![latex-3d1353b4-6927-4cae-8a9d-22d794bfe3ee](data/lecture21/latex-3d1353b4-6927-4cae-8a9d-22d794bfe3ee.png) be the **bit** length of the modulous, n (ex. ![latex-7c4b6cfe-488d-466a-af28-66b0103157da](data/lecture21/latex-7c4b6cfe-488d-466a-af28-66b0103157da.png))
- Salt ![latex-bbd53567-dd4e-40e7-9977-7e3629afbcea](data/lecture21/latex-bbd53567-dd4e-40e7-9977-7e3629afbcea.png)

#### Formatting and Encryption
  - ![latex-a34932fb-5e33-4f06-9cd8-e495b4c2988b](data/lecture21/latex-a34932fb-5e33-4f06-9cd8-e495b4c2988b.png)
  - ![latex-37c60a16-9d54-46ef-9184-d6a2b0a6d2f5](data/lecture21/latex-37c60a16-9d54-46ef-9184-d6a2b0a6d2f5.png): Length of M + 256 0's
  - ![latex-5d154f7d-0c26-46cf-bb8b-6300b47481ca](data/lecture21/latex-5d154f7d-0c26-46cf-bb8b-6300b47481ca.png)
  - ![latex-3bd6b741-64ca-4fc9-8608-0124f8dc3d8e](data/lecture21/latex-3bd6b741-64ca-4fc9-8608-0124f8dc3d8e.png)
  - ![latex-30996b93-e64b-4167-bdf7-659e54ad5bb9](data/lecture21/latex-30996b93-e64b-4167-bdf7-659e54ad5bb9.png) and ![latex-3f5f0a84-13ad-4410-ad2d-5bf44f5f4b62](data/lecture21/latex-3f5f0a84-13ad-4410-ad2d-5bf44f5f4b62.png) are random functions implemented with hash functions
  - ![latex-4e8bd17c-6ecf-47dc-90c0-cbe478d32bd8](data/lecture21/latex-4e8bd17c-6ecf-47dc-90c0-cbe478d32bd8.png)
  - ![latex-934a2268-eb98-467a-a7de-b25799d6426a](data/lecture21/latex-934a2268-eb98-467a-a7de-b25799d6426a.png)
    - The point of this is to discuise the salt and plaintext
    - **Think**: Similar to a 2-step feistel network

#### Decryption (given c)
- Compute ![latex-b2fd9ba7-1cde-4a92-822c-339394648f7e](data/lecture21/latex-b2fd9ba7-1cde-4a92-822c-339394648f7e.png)
- Parse m: ![latex-fc2d9721-61ef-4818-9a06-bd5782f78c6c](data/lecture21/latex-fc2d9721-61ef-4818-9a06-bd5782f78c6c.png)
- Check that ![latex-249b1948-d6b7-4467-842a-a071215fbada](data/lecture21/latex-249b1948-d6b7-4467-842a-a071215fbada.png)
- Go backwards:
- Compute: ![latex-06a624c1-ca4b-45c4-bd9e-aa108a385eac](data/lecture21/latex-06a624c1-ca4b-45c4-bd9e-aa108a385eac.png)
- Compute: ![latex-bde327ab-a204-4182-89ac-7dd8c576dd5c](data/lecture21/latex-bde327ab-a204-4182-89ac-7dd8c576dd5c.png) and parse to get ![latex-d2426dfa-b6b6-403d-98d6-f310a152fe2d](data/lecture21/latex-d2426dfa-b6b6-403d-98d6-f310a152fe2d.png)
  - a should be 256 bits long
- Check that ![latex-2bdceee6-6e05-419f-b173-7bcdf7097c94](data/lecture21/latex-2bdceee6-6e05-419f-b173-7bcdf7097c94.png) is 256 0's
- Then the plaintext is ![latex-5415ce20-601a-453a-a4ec-db4a59895f66](data/lecture21/latex-5415ce20-601a-453a-a4ec-db4a59895f66.png)

#### Why is this secure?
- Provable by theorem.
- See next class
