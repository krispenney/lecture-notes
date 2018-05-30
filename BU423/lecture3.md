# Lecture 3 - May 29, 2018

## Determination of Forward Prices (The Principals)

- Consumption assets: help for consumption
  - copper, oil
  - need the assets for your business
  - part of your costs
- investment assets: held purely for investment purposes
  - gold, silver

### Short Selling
- Selling securities that you do not own.
- You broker borrows the securities from another client, sells them in the market. You must eventually buy the securities so they can be replaced in the account of the client.
- You must pay dividends and other benefits to the owner of the security

#### Example
- short 100 shares, current price per share is 100, close short position in 3 months when the price is 90. Pay a dividend of 3 per share.
- profit for short
  - buy ![latex-36c42b2e-84db-400b-b33b-7e7f86fa96c7](data/lecture3/latex-36c42b2e-84db-400b-b33b-7e7f86fa96c7.png),
- loss for long

### A cost-of-carry approach

cash-and-carry argument.
1. buy the underlying commodity in the spot market with borrowed cash, hold it until forward maturity date. carry to the future.
2. pay various costs of carry (carrying charges)
3. Hash the same payoff at maturity as the forward. They must be equal or else arbitrage would occur.

arbitrage:
- If Walmart sells an item for 5 and Costco for 3
- Borrow money and pay 0.25 cents interest
- go sit outside of Walmart, sell for 4.
- 0.75 cent profit without any risk for yourself.

law of one price:
- if you have 2 assets with the same cashflows, they have to be worth the same.
- If not, then there is an arbitrage oppourtunity.

#### Assumptions
- work in a frictionless market: no bid and ask prices, no credit risk.

#### Example
- january 1
- 1 year forward contract on YBM stock.
- No cashflows today because the forward price is the fair price.
  - Costs nothing today
  - maturity: stock worth S(T), buy them for F dollars.

##### Alternative 1
- Buy YBM and carry it into the future (i.e. buy it directly, no future)
- at time 0, pay 100
  - borrow 100, pay back the loan at maturity (in 1 year)
- pay back loan ![latex-84fcc015-e772-4840-972c-66c79fcf9510](data/lecture3/latex-84fcc015-e772-4840-972c-66c79fcf9510.png)
- This has to be the same as the future oppourtunity, otherwise there is an arbitrage oppourtunity.
- Has to be the case that ![latex-29f52343-ff81-4fa7-950b-7d99392030f0](data/lecture3/latex-29f52343-ff81-4fa7-950b-7d99392030f0.png)
  - Here we only have a borrowing cost, realistically you would have additional costs for assets (storage). But the value would become a function of those costs.

In this example, any gains would happen at the end

##### Alternative 2
- borrow the present value of the future (![latex-a4c4735f-6ca1-411c-b043-abf02c3edcc1](data/lecture3/latex-a4c4735f-6ca1-411c-b043-abf02c3edcc1.png)), then short sell the asset.
- Cashflow at time 0: ![latex-9dd3f337-8942-4f76-980c-e85a1f20b7b1](data/lecture3/latex-9dd3f337-8942-4f76-980c-e85a1f20b7b1.png), if it's not zero there's an arbitrage oppourtunity
  - ![latex-8de858bc-2885-453a-8411-ca47e70b41e7](data/lecture3/latex-8de858bc-2885-453a-8411-ca47e70b41e7.png)

### Forward vs. Future Price
- When maturity and asset price are the same, forward and future price are the same
- slightly different when interest rates are different.
  - high positive correlation: future prices higher than forward price
  - high negative correlation: future prices lower than forward price.

### Forward Price
- ![latex-af87da38-3c5f-4af7-94c5-97427a24d5fa](data/lecture3/latex-af87da38-3c5f-4af7-94c5-97427a24d5fa.png)
  - T years
  - r interest rate

continuous compounding: ![latex-d7704462-9b0c-44be-824f-118a3df05978](data/lecture3/latex-d7704462-9b0c-44be-824f-118a3df05978.png)

### How to exploit an arbitrage oppourtunity
- Forward price greater than true, establish a short position and long position.

Action now:
1. enter into forward contract, sell in 3 months for 43
2. borrow 40 at 5% for 3 months
3. buy the asset

Action in 3 months:
1. Sell asset for 43
2. use 40.50 to repay the loan.

Profit of 2.50 is realized in 3 months.

### excercise 1

> An asset that does not pay any cash flow is currently trading at $40. An errant trader
wants to trade a forward on that asset for $39. The maturity of the contract is 0.25.
Assume that the interest rate is 5% for all maturities.

- Is there an arbitrage opportunity? What would be the profit?
  - Yes, there is.
  - The price of the forward is lower than the current spot price.
- Describe the steps that you have to follow in order to secure this opportunity.
  - Short the bond, future value is: ![latex-ca1ff60b-8d1d-48c7-97bd-5df3b5cae2c7](data/lecture3/latex-ca1ff60b-8d1d-48c7-97bd-5df3b5cae2c7.png)
  - purchase the forward today for 39, using the proceeds
  - in 3 months buy the asset, closing out your short position.

part 2

> What is the effect of increasing interest rates on forward prices?
- Price increases, higher cost of borrowing higher price.

> Are forward prices increasing or decreasing with maturity? Why?
- Increasing. Projecting further into the future.

> Are forward prices increasing or decreasing with spot prices?
- Increasing.

For this example, there is no benefit other than the price.

### When an Investment provides a known dollar income

![latex-a589a68c-229f-49d4-9ac2-87da321b17a4](data/lecture3/latex-a589a68c-229f-49d4-9ac2-87da321b17a4.png)
- I is the present value of the income during the life of the forward contract (i.e. up to the maturity of the contract).

#### Example

| r | T |
|-|-|
| 3% | 4 |
| 4% | 9 |

- ![latex-5affa476-e681-4e5f-8bd2-a7affd4b1c51](data/lecture3/latex-5affa476-e681-4e5f-8bd2-a7affd4b1c51.png)
- ![latex-6b254eed-b188-486f-b64c-144fc1a56ada](data/lecture3/latex-6b254eed-b188-486f-b64c-144fc1a56ada.png)
- $$I = 40 e^{-3% * \frac{4}{12}}
- ![latex-e4aac4da-c0a3-405c-b7d2-a76128bcffd9](data/lecture3/latex-e4aac4da-c0a3-405c-b7d2-a76128bcffd9.png)

In this example, there's only one payment prior to maturity.

Suppose we are quoted 910, overpriced. Short sell this contract, use the proceeds to make a long position (replicating the forward)

now
1. enter into forward to sell asset in 9 months (short)
2. borrow 900: 39.6 for 4 months, 860.4 for 0 months
  - Match the loan payments to the payments of the underlying asset
3. Buy one unit of the asset

in 4 months
1. recieve 40 of income from asset
2. replay first lean

in 9 months
1. sell asset for 910
2. use 886.6 to replay second loan

If quoted lower, short the bond

action now
1. enter into forward contract, buy
2. short 1 unit of asset to realize 900
3. invest 39.6 for 4 months, 860.4 for 9 months

4 months
1. recieve 40 from investment
2. pay income

9 months
1. recieve 886
2. buy asset for 870
3. close short position.

### When an investment asset provides a known yield
- ![latex-7b15deb0-b0eb-403a-a4f0-c08253fde969](data/lecture3/latex-7b15deb0-b0eb-403a-a4f0-c08253fde969.png)
- q is the average yield during the life of the contract (assume continuous compounding)
- Note: ![latex-7551fd74-ba70-43d3-a5c0-a4af1d70221f](data/lecture3/latex-7551fd74-ba70-43d3-a5c0-a4af1d70221f.png) prices increase for longer dates, costly to hold the asset for longer time.
- Note: ![latex-47f30653-50f4-4cc9-81c2-b68e023398bf](data/lecture3/latex-47f30653-50f4-4cc9-81c2-b68e023398bf.png) price decrease for longer dates many benefits to hold the asset

#### Index Arbitrage:
![latex-9948a2e2-3fbb-4f91-96d5-ddc9b8f396cf](data/lecture3/latex-9948a2e2-3fbb-4f91-96d5-ddc9b8f396cf.png)
- buy the stock underlying the asset and sells the futures
- But this often means you need to replicate the entire portfolio, need low transaction costs

![latex-e1a62e9c-1647-4291-895a-1369e253fb8d](data/lecture3/latex-e1a62e9c-1647-4291-895a-1369e253fb8d.png)
- buy futures and short / sell the underlying asset

### Futures and Forwards on Currencies
- forward exchange rate

![latex-6ae068b8-bfff-4fcb-aa0b-5f474b5ad406](data/lecture3/latex-6ae068b8-bfff-4fcb-aa0b-5f474b5ad406.png)
- ![latex-900d26e7-f0ae-43ba-9ad7-89b3430f67d4](data/lecture3/latex-900d26e7-f0ae-43ba-9ad7-89b3430f67d4.png) is the forign risk-free exchange rate.
- Always take the perspective of the US investor

#### Example
- A
  - ![latex-b61325f7-093a-4518-8464-79914e57c4a7](data/lecture3/latex-b61325f7-093a-4518-8464-79914e57c4a7.png)
  - $$1000 * F_0 * e^{r_f * T} = 812s$
  - 808
- B
  - ![latex-ef39836c-2af8-4512-88a9-a64775c6a112](data/lecture3/latex-ef39836c-2af8-4512-88a9-a64775c6a112.png)
  - ![latex-d439c234-116f-4421-981d-6cff653db674](data/lecture3/latex-d439c234-116f-4421-981d-6cff653db674.png)

Use the cheaper one as funding, invest in the more expensive one.

### Futures on Commodities: Storage is Negative Income

we have to pay extra in order to store the underlying asset.

![latex-a347733c-7293-4040-81f1-b94d6c3222c8](data/lecture3/latex-a347733c-7293-4040-81f1-b94d6c3222c8.png)
- u Storage value per unit of time
- ex. 5% every year

![latex-b3079b0a-ee54-4cd1-8103-cbb20b101ffb](data/lecture3/latex-b3079b0a-ee54-4cd1-8103-cbb20b101ffb.png)
- U is present value of storage costs
- U is 2 per year

#### Example: Goal future price
- How do storage costs effect the arbirage oppourtunity.
- futures price too high
  - borrow money to buy gold
  - short the future
  - you have to pay storage costs
- future price too low
  - short gold
  - enter the future contract for delievery
  - don't have to pay storage costs, don't have to hold the formula for a year

### Cost of Carry
- c is the cost of carry (storage costs + interest - income earned)
- investment asset: ![latex-80f5f413-5158-4c63-ab0f-837b088b7169](data/lecture3/latex-80f5f413-5158-4c63-ab0f-837b088b7169.png)
- consumption asset: ![latex-f85c95ba-5ed4-4281-8794-b8b6dd36635b](data/lecture3/latex-f85c95ba-5ed4-4281-8794-b8b6dd36635b.png)
  - ![latex-06cce368-901d-4fc7-8426-a80ec0b4a7fa](data/lecture3/latex-06cce368-901d-4fc7-8426-a80ec0b4a7fa.png)

### Markig-to-market a forward contract
- forward contract woth 0 when it's negotiated
- later could be positive or negiatve
- value of long forward contract: ![latex-710020f2-9267-4c6b-93a1-1b3eb37a167e](data/lecture3/latex-710020f2-9267-4c6b-93a1-1b3eb37a167e.png)
- value of short forward contract: ![latex-a4d56f47-f565-484c-9fcb-b09980b5ee40](data/lecture3/latex-a4d56f47-f565-484c-9fcb-b09980b5ee40.png)
- Intermediate cashflow: ![latex-5364ebd5-e746-4db0-a62a-83ab390c5c29](data/lecture3/latex-5364ebd5-e746-4db0-a62a-83ab390c5c29.png)

### Exercise 2

Part 1

Fair value of the contract:
- 51 dollars

Suppose a trader is quoting for 50 dollars (underpriced), how to exploit?
- enter into the futures contract for 50 dollars
- short sell the asset, invest the present values of income for 3, 6, and 9 months. Invest the remainder for 10 months
- Pay the dividends as required

