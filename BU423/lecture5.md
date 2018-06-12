# Lecture 5 - June 12, 2018

## Interest Rate Derivatives

### Types of Rates
- **Treasury Rate**: rates on instruments issed by governments in it's own currency
  - risk free for good economies (US, Canada)
- **ICE LIBOR**: Rate of interest by which a AA bank can borrow from another bank, unsecured
  - LIBOR: ask all banks, remove top and bottom quantile, average the rest
    - every day rates for different maturities and currencies are posted
  - changed the entity in charge of computing the rate, result of 2008 scandels
- **Overnight Rate**
  - unsecured interbank rate of interest
  - central bank regulates the flow of money in an economy
  - Allows the bank to maintain reserves at the central bank
  - excess reserves are given to other banks, recieve interest.
- **Repo Rate**
  - related to short selling, need to borrow and pay back
  - sell a security for X, buy it back in the future for some higher price Y.
- **Swap Rate**
  - LIBOR is swapped for a fixed rate
  - remove variability across time
- **Overnight Index Swap(OIS) Rate**
  - Overnight rates over some period is exchanged for the geometric average ![latex-4b7fe0e0-c55a-4a0d-82ba-3f83e76f1a93](data/lecture5/latex-4b7fe0e0-c55a-4a0d-82ba-3f83e76f1a93.png)

### Risk Free Rate

considered to be artifically low:
- banks aren't required to hold capital for Treasury Investments
- high demands for bonds
- Favourable tax treatment, increasing the demand.

OIS now used as a proxy for risk-free rates

**Rate Spread**: same maturities, look at the difference
- TED Spread: LIBOR against the treasury rate
  - during the financial crisis the spread dramatically increased.
  - acts as a proxy for risk in the financial market

### Bootstrap

How to extract interest rates from quotes.

Suppose you purchase a 3 month T-bond
- buy for 97.5, in 3 months recieve 100
- There's an implicit rate here

![latex-0704aad4-4f3d-4b4a-8cfd-dc6399b5d256](data/lecture5/latex-0704aad4-4f3d-4b4a-8cfd-dc6399b5d256.png) with quarterly compounding
- from here, can change the compounding period (continuous, 6 months, ...)
- ![latex-27a20571-99e3-4c3e-8bf4-4a290c9540be](data/lecture5/latex-27a20571-99e3-4c3e-8bf4-4a290c9540be.png) - solve for R
- For discounting, we will use continuous compounding

Always match the correct rate to the correct maturity period

What happens if you have 0.75?
- Interpolate between the neighbouring values
- average the previous and following period
- **For this class, we will always have the values we need**

If a security pays dividends
- Match the interest rate compounding period to the payment period
- just compute the present values
- Iterative process to compute the rates for each period

### Forward Rates
- When the market quotes zero-rates, they allow us to extract forward rates


![graph-b963aaa6-6c8f-4cbc-8398-35c56065393c](data/lecture5/graph-b963aaa6-6c8f-4cbc-8398-35c56065393c.svg)

![latex-7e6b2faa-5537-4a15-b2b8-4465d5c4d7e1](data/lecture5/latex-7e6b2faa-5537-4a15-b2b8-4465d5c4d7e1.png) - Solve for ![latex-90cca527-4f3f-43b8-8c9f-22f09e47bd9a](data/lecture5/latex-90cca527-4f3f-43b8-8c9f-22f09e47bd9a.png)
![latex-a82264ca-f8a6-42f8-bca9-e64a8181408a](data/lecture5/latex-a82264ca-f8a6-42f8-bca9-e64a8181408a.png) (ln)

Forward rate between ![latex-c4d6da25-5ac0-4ace-b4f1-7a48b38e96c7](data/lecture5/latex-c4d6da25-5ac0-4ace-b4f1-7a48b38e96c7.png)
![latex-aee5ae1f-d8c4-4faf-b0a5-434df3cabf3f](data/lecture5/latex-aee5ae1f-d8c4-4faf-b0a5-434df3cabf3f.png)

### Forward Rate Agreement (FRA)

Lock in an interest rate for some period of time.
- Over the counter agreement
- borrowing or lending
- Payoff at maturity: ![latex-81bda419-f7e6-42de-a90a-52c780f86c42](data/lecture5/latex-81bda419-f7e6-42de-a90a-52c780f86c42.png)
  - long: pay the fixed rate, ![latex-0d15d8e4-6e22-42f0-b3ff-5d1a586f4747](data/lecture5/latex-0d15d8e4-6e22-42f0-b3ff-5d1a586f4747.png) is the borrowing rate.
  - short: Recieve the fixed rate, ![latex-d8ea4cad-a166-4873-8e13-9a4724d35fe3](data/lecture5/latex-d8ea4cad-a166-4873-8e13-9a4724d35fe3.png) is the lending rate

#### Example
- 5x8:
  - In 5 months you will know the rate
  - In 8 months you will have to pay


