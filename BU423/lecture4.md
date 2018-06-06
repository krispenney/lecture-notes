# Lecture 4 - June 5, 2018

## Technical Test
- next week
- multiple choice
- chapter 2, 3, 5
- go through the excersices (in the book and given)

Last Weeks Quiz
- answer was d: 75,648
- (15 + 10 * 0.24)exp(10% * 10/12) = 18.91 for one contract
- Multiply the price per contract by 2

## Forwarding Prices

### Futures Prices and Expected Future Spot Price
- let k be the expected return required by the investor
  - can't use the risk free directly, need to incorporate the expected return
- ![latex-3ed57699-03b2-4aeb-a39c-32858e450af6](data/lecture4/latex-3ed57699-03b2-4aeb-a39c-32858e450af6.png)
  - ![latex-6c0ee76f-9ff3-4b87-92e2-dea31b392f3c](data/lecture4/latex-6c0ee76f-9ff3-4b87-92e2-dea31b392f3c.png): Expected spot price at the time of maturity
- ![latex-e65a1b46-1d30-4471-8b64-1d838d6c9810](data/lecture4/latex-e65a1b46-1d30-4471-8b64-1d838d6c9810.png)

- If there is systematic risk: ![latex-751289c0-064c-4e68-9dd8-28797e122ed1](data/lecture4/latex-751289c0-064c-4e68-9dd8-28797e122ed1.png)
  - Future price will be higher, prices are going to converge from above.
  - comphensation related to the systematic risk
- ![latex-21760d15-353a-4924-8b15-2d4669a6dcd4](data/lecture4/latex-21760d15-353a-4924-8b15-2d4669a6dcd4.png)
  - futures prices selling at a discount
  - the asset has negative systematic risk.

Positive systematic risk: stocks
Negative systematic risk: gold

## Hedging

- Futures are typically traded to preexisting hedge risk in some line of business
- man selling sunglasses and ubrella
  - when sunny, sell sunglasses
  - when raining, sell umbrellas
  - prepared for any state of the world
  - **natural hedge**: Inverse behaviour of assets
- hedging can reduce risk in fluctuations
  - example: farm wants to lock in the price, lock into a contract to mitigate changes in price.

### Benefits of corporate hedging
1. hedging locks in a future price
  - example: farmers locking stable prices, plan production and marketing accordingly
2. hedging premits forward pricing of products
  - example: airlines hedge fuels prices
    - want to offer vacations, they know the cost of fuel, can negotiate with hotels, can offer a price knowing their margins

### Perfect Hedge

This is the optimal scenario, hard to get in practice.
- have a contract which provides you with a contract that exacly covers the loss (eliminates spot-price risk). Best case scenario.

There are requirements that effect the optimality:
- the futures contract is written on the commodity being hedged.
- the contract matures when the hedger is planning to lift the hedge
- the size and other characteristics of the futures contract fit the hedger's need.

**Imperfect / Cross-hedges** occur when these conditions are not met

### Long Hedges
- When you are going to purchase something in the future and you want to lock in the price.
- You want protection in case prices rise.
- finance the purchase with gains from the future contract.
- Suppose your in vancouver, the future is in Montreal. Instead close out the position on maturity (i.e. don't settle) and buy from the local manufacturer.

### Short Hedge
- Use when you need to sell an asset, afraid of prices going down

### Basis Risk

Dealing with imperfections

- basis: the difference between spot and futures prices
- basis = spot price of hedged asset - futures price of contract used.
- basis risk arises because of the uncertainty about the basis when the hedge is closed out.
  - suppose you can't find a future that matures when you want

- ![latex-247eadce-9059-45d9-8ef2-7a0614ccd227](data/lecture4/latex-247eadce-9059-45d9-8ef2-7a0614ccd227.png): futures price at the time hedge is set up
- ![latex-ffc27206-16fd-4430-8de1-d1421c92dbb2](data/lecture4/latex-ffc27206-16fd-4430-8de1-d1421c92dbb2.png): futures price at the asset is purchased
- ![latex-9e533e76-c611-4e1b-bd89-1c860ea36964](data/lecture4/latex-9e533e76-c611-4e1b-bd89-1c860ea36964.png): asset price at the time of purchase
- ![latex-7acf4426-0df0-4263-88c3-1cb7e508f28e](data/lecture4/latex-7acf4426-0df0-4263-88c3-1cb7e508f28e.png): basis at time of purchase
- Cost of asset ![latex-c4ab5fa2-3d5c-4a04-a599-4c16cee793d5](data/lecture4/latex-c4ab5fa2-3d5c-4a04-a599-4c16cee793d5.png)
- Gain/loss on futures: ![latex-5cc51c9c-7924-427d-8e96-f19208f21cba](data/lecture4/latex-5cc51c9c-7924-427d-8e96-f19208f21cba.png)
- Net amount paid: ![latex-e6ca8b15-d258-4c8b-9728-a423c8c725cd](data/lecture4/latex-e6ca8b15-d258-4c8b-9728-a423c8c725cd.png)
  - Note: In the case of a perfect hedge: ![latex-414624f8-0996-4295-9433-f3bf46628eed](data/lecture4/latex-414624f8-0996-4295-9433-f3bf46628eed.png)

if you don't hedge, then you pay ![latex-afa7def3-4f9e-4838-bb43-91d1e41f5df0](data/lecture4/latex-afa7def3-4f9e-4838-bb43-91d1e41f5df0.png). If you hedge, you gain / loss factors in.

As the basis widens ie ![latex-e5cbb5cd-6a33-4d06-802c-6178333c075e](data/lecture4/latex-e5cbb5cd-6a33-4d06-802c-6178333c075e.png) increases: you end up paying more for the asset.

### Choice of Contract
- choose a delivery month that is as close as possible to, but later than, the end of the life of the hedge.
- when no ftures contract on the asset, choose a contract where the future price is highly correlated
  - Bitcoin and Etherum
- ![latex-a20dea7b-53e2-47f8-ba61-e08d29410161](data/lecture4/latex-a20dea7b-53e2-47f8-ba61-e08d29410161.png)

#### Cross Hedging - Minimum variance hedge ratio
- compute deltas on the 2 assets over time
- Bitcoin and Ethereum
- do simple regression: ![latex-eecca9e1-8e1d-4890-bcc1-a70307dd364a](data/lecture4/latex-eecca9e1-8e1d-4890-bcc1-a70307dd364a.png)
  - also compute ![latex-4025a302-d324-40d0-86e2-f901447ddec8](data/lecture4/latex-4025a302-d324-40d0-86e2-f901447ddec8.png), how effective is the hedging we are going to use. Want highest possible ![latex-59d41ef8-8377-4ef3-a3a2-1b1155fdc7e0](data/lecture4/latex-59d41ef8-8377-4ef3-a3a2-1b1155fdc7e0.png)
- ![latex-a0cff457-6419-492e-9641-2132f5781a99](data/lecture4/latex-a0cff457-6419-492e-9641-2132f5781a99.png)
  - sigmas are std deviation.
- optimal number of contracts : ![latex-5e6030c4-b1be-4f97-afb7-982383caf6bc](data/lecture4/latex-5e6030c4-b1be-4f97-afb7-982383caf6bc.png)
- Market value of the quantity: ![latex-0dc84050-8e50-4f81-8fc9-dab43bd598a1](data/lecture4/latex-0dc84050-8e50-4f81-8fc9-dab43bd598a1.png)

### Hedging using index futures
- we want to get rid of systematic risk
- one possibility, sell of the portfolio, buy back later, but high transaction fees
- number of contacts that should be shorted is: ![latex-a722a27c-00c3-4c93-a89f-bfcd3884b0e7](data/lecture4/latex-a722a27c-00c3-4c93-a89f-bfcd3884b0e7.png)
  - ![latex-5e123bb2-35d4-45da-9a16-8359bb70022e](data/lecture4/latex-5e123bb2-35d4-45da-9a16-8359bb70022e.png) is the value of the portfolio
  - ![latex-fa729cef-115d-467a-a8f8-515dc9283b73](data/lecture4/latex-fa729cef-115d-467a-a8f8-515dc9283b73.png) is the current value of futures: price times
- ![latex-6680201d-c77b-43d9-952b-a96921f38e61](data/lecture4/latex-6680201d-c77b-43d9-952b-a96921f38e61.png) as the systematic risk has been eliminated.

### Changing beta of a portfolio
- ![latex-c3f0f47a-520a-4200-8258-11168d7ab240](data/lecture4/latex-c3f0f47a-520a-4200-8258-11168d7ab240.png) short position of ![latex-7d20fe89-6a2d-4978-998b-38a4bd0b6df6](data/lecture4/latex-7d20fe89-6a2d-4978-998b-38a4bd0b6df6.png)
- ![latex-7454cc90-7503-4fd5-a79f-233c8279a2bb](data/lecture4/latex-7454cc90-7503-4fd5-a79f-233c8279a2bb.png) long position of ![latex-c5f7f575-3031-490a-84b6-c9c4001e6eab](data/lecture4/latex-c5f7f575-3031-490a-84b6-c9c4001e6eab.png)

Examples:
1. 6.82, short
2. 4.5, long

### Why Hedge Equity Returns
- you may want to exit the market, but avoid all of the transaction fees

### Stack and Roll
- roll futures contracts forward
- as maturity approaches, close position, get new futures
