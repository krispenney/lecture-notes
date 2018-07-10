# Lecture 9 - July 10, 2018

## Excercise Strategies - Question 3
Short Strangle
- underlying price needs to stay close to the strike price
- betting against high volatility
- max loss: infinite. If the underlying price keeps rising
- Breakeven points: 1799-5 and 1949+5
  - Profits in between

## Option Properties

### Effects of variables on Option Price
- slide 2: First 2 columns -> European Options, Last 2 -> American
  - Both c->call, p->put

- **Current Stock Price:** ![latex-ea124440-6bb7-4729-b6e1-814d62608667](data/lecture9/latex-ea124440-6bb7-4729-b6e1-814d62608667.png)
  - Draw the graphs
  - notice that as the price increase, for calls: move closer to being in the money, puts: moves farther away
  - Same for american and euro
- **Strike Price**: ![latex-a5deacf7-af27-4d9b-ab1f-37d4aa705f08](data/lecture9/latex-a5deacf7-af27-4d9b-ab1f-37d4aa705f08.png)
  - again: draw the graphs
  - For calls: Notice that a lower strike prices increases your chances of being in the money
    - Negative correlation on price
  - For puts: Lower strike price decreases your chances of being in the money
    - positive correlation on price
  - Same for american and euro
- **Maturity**: ![latex-c1399be6-7651-450b-8ee2-70c684982c9a](data/lecture9/latex-c1399be6-7651-450b-8ee2-70c684982c9a.png)
  - Recall the difference between American and European options, American: can excercise at any point.
  - Euro: can't do anything until maturity
    - Therefore maturity has no effect on the price of an option
  - American: Can excercise at anypoint during the lifecycle of the option
    - Have an increased oppourtunity of observing a profitable scenario.
    - American options are higher priced
  - **American** options can never be priced less than an equivalent **European** bond
- **Volatility**: ![latex-6468eb7b-a9ce-4d70-96e6-f2cfbc1e5314](data/lecture9/latex-6468eb7b-a9ce-4d70-96e6-f2cfbc1e5314.png)
  - Call/Put and Euro/American doesn't matter
  - probability of possible values that the underlying price could take on
  - lower volatility: (assuming a normal distribution) the expected value is much clearer, lower standard deviation, lower odds of being in the money
  - higher: higher standard deviation, potentially increasing your chances of being in the money
- **Risk Free Rate** ![latex-d17f4fe2-20f0-4dd4-833f-617851da0d92](data/lecture9/latex-d17f4fe2-20f0-4dd4-833f-617851da0d92.png)
  - Examine CAPM: $$E[r_i] = r + \beta(E[r_n] - r)
  - With a higher risk free rate, faster rate of appreciation, end up in the money sooner.
  - With a call (euro/american) increases price
  - With a put: decreases prices
- **Dividend Payments**: ![latex-139387fa-235b-454c-bf75-3abdad0da342](data/lecture9/latex-139387fa-235b-454c-bf75-3abdad0da342.png)
  - Price goes down when a dividend is payed
    - we are removing money from the company
  - Call: Negative relation
    - decreasing the value of the underlying, decreasing likelihood of being in the money
  - Puts: Positive relation

#### Replication with Options

We want to find a way to price options

Recall that pricing forwards is a linear relationship
- Via the no-arbitrage principal

With options, need additional information to determine the price
- How the stock price will evolve

##### Put-Call Parity (PCP)
A combination of options and the underlying can produce a call or put option

- combination of a short call, long underlying
- combination of call + underlying
  - short put
- long put + long call
  - long call

![latex-47581d0b-af88-4374-b735-fd383cb9fa5d](data/lecture9/latex-47581d0b-af88-4374-b735-fd383cb9fa5d.png)
- Long call = Long put + long stock - short bonds
- ![latex-7f3332be-ea04-4bb2-9d02-e9a0afd85615](data/lecture9/latex-7f3332be-ea04-4bb2-9d02-e9a0afd85615.png) are today's price of Euro calls and puts
  - Strike price K, expiration T
- ![latex-2485cbaa-412f-4e49-aa3d-cdce558d8c26](data/lecture9/latex-2485cbaa-412f-4e49-aa3d-cdce558d8c26.png): today's price of zero-coupon bond ![latex-71e96b14-ed0e-4cdc-8fb1-75cd71cbf9cd](data/lecture9/latex-71e96b14-ed0e-4cdc-8fb1-75cd71cbf9cd.png)
- ![latex-601e641a-8bdb-42fa-8a9d-7ad983077e2d](data/lecture9/latex-601e641a-8bdb-42fa-8a9d-7ad983077e2d.png): Underlying price today

If this equality does not hold, there is an arbitrage oppoutunity to be exploited

###### Establishing PCP by Payoff Diagram
- Long put: Strike Price 20
- fund the purchase of a long call
- funded transaction: Not you're money
  - that's why the minimum payoff is ![latex-dbe20ec8-e43e-4267-8f6f-4083ada318fc](data/lecture9/latex-dbe20ec8-e43e-4267-8f6f-4083ada318fc.png)
- Combined effect: a long call
  - "It's not really a call"
  - a real call would have minimum payoff of 0
- To get a true call
  - Need to be worth ![latex-e4f9645f-696d-41d5-b327-354f406c6b5e](data/lecture9/latex-e4f9645f-696d-41d5-b327-354f406c6b5e.png) no matter the value of the underlying
  - short sell 20 zero-coupon bonds
- If this porfolio has a different value to an actual call, then there is an arbitrage oppourtunity.

###### Slide 11 Example:
- IBM Stock: $22.50 today (![latex-7a5deb2c-88d8-4bce-a5e1-11ad6e189775](data/lecture9/latex-7a5deb2c-88d8-4bce-a5e1-11ad6e189775.png))
- options have Strike price of $20, mature in 6 months
- put price is $0.50
- ![latex-2460e41f-89e6-4559-8ffd-213422fc19db](data/lecture9/latex-2460e41f-89e6-4559-8ffd-213422fc19db.png) per year
- ![latex-8e407a3e-22f0-463d-aa16-e2dbb59f7d22](data/lecture9/latex-8e407a3e-22f0-463d-aa16-e2dbb59f7d22.png)
- no dividends
- ![latex-bc845824-ca10-426d-929e-c76c06c176ea](data/lecture9/latex-bc845824-ca10-426d-929e-c76c06c176ea.png)
- real call price: $4
- Short real, long synthetic
- Profit of ![latex-e84912a8-77a2-407e-9756-d16302c3296c](data/lecture9/latex-e84912a8-77a2-407e-9756-d16302c3296c.png)
- Columns in the table on slide 13 is comparing Stock price to the strike price

IF the call price is $3
- The we need to create a synthetic short call
- The call is underpriced: Profit is ![latex-c646966b-79c3-4ee5-9007-685cd7db6ff1](data/lecture9/latex-c646966b-79c3-4ee5-9007-685cd7db6ff1.png)
- short put, short stock, buy bonds
  - as always, short case is just the equation * -1

## Binomial Tree for Valuing Options
- Build a binary tree over time, outcomes of events are branches
  - each level in the tree is a period
  - Some probability of taking each branch, i.e. the world ending up in some state
- "State of the world up" vs. "State of the world down"
  - do we win or loose
- ![latex-3796258d-382f-42ca-9bd8-8d882a0b2ab1](data/lecture9/latex-3796258d-382f-42ca-9bd8-8d882a0b2ab1.png)
- ![latex-5990a543-e449-4b88-b541-fd0d0d2adda7](data/lecture9/latex-5990a543-e449-4b88-b541-fd0d0d2adda7.png)

### Example: Euro Call Pricing

Asset A:
- Current price: ![latex-43f92780-8573-4eff-b368-c29b359c845f](data/lecture9/latex-43f92780-8573-4eff-b368-c29b359c845f.png)
- In one year
  - go upto $120 (suppose probability ![latex-276f6d2d-4ca5-44d0-9ac5-d61ebf1134b9](data/lecture9/latex-276f6d2d-4ca5-44d0-9ac5-d61ebf1134b9.png))
  - go down to $90.25

Asset B:
- Dollar invested in money market account grows to $1.0513

Consider a Euro call option, ![latex-9e9652f9-174a-45dd-b0dd-de4040d9e8b0](data/lecture9/latex-9e9652f9-174a-45dd-b0dd-de4040d9e8b0.png), maturity in 1 year
- ![latex-61a54ba6-70b3-4744-9b3c-9a28407ac220](data/lecture9/latex-61a54ba6-70b3-4744-9b3c-9a28407ac220.png)
  - Upside: ![latex-b8a67ff6-d140-4e10-ad69-e7c3a99ccbda](data/lecture9/latex-b8a67ff6-d140-4e10-ad69-e7c3a99ccbda.png)
  - Downside: ![latex-bfd2828a-2580-4817-9e69-cbf5ae73b33c](data/lecture9/latex-bfd2828a-2580-4817-9e69-cbf5ae73b33c.png)

How much to pay?
- Come up with a portfolio that looks like the call options (i.e. that has the same payoff)
  - Build it using asset A and B

- Let ![latex-bbe3e333-e8cb-49b3-93ca-9369700cb291](data/lecture9/latex-bbe3e333-e8cb-49b3-93ca-9369700cb291.png) be the number of underlying units purchased
- Let ![latex-1788385c-df34-4366-b407-11cfd4e0ab1b](data/lecture9/latex-1788385c-df34-4366-b407-11cfd4e0ab1b.png) be the number of units put into the money market account
- ![latex-fe0f4ed1-982e-45c0-bdef-ea2cf66f3d06](data/lecture9/latex-fe0f4ed1-982e-45c0-bdef-ea2cf66f3d06.png)
  - Want ![latex-5be53ea6-d4b7-4f54-a43e-1b314565a15b](data/lecture9/latex-5be53ea6-d4b7-4f54-a43e-1b314565a15b.png) such that payoff at time 1 matches the call
  - upside: ![latex-0329c193-9fe5-4430-a7cc-2fe9eae2259c](data/lecture9/latex-0329c193-9fe5-4430-a7cc-2fe9eae2259c.png)
  - downside: ![latex-08d4cd94-3897-4551-8d60-b00194b04c48](data/lecture9/latex-08d4cd94-3897-4551-8d60-b00194b04c48.png)
  - ![latex-5e2aaa1f-da09-4657-aead-ca757caa9021](data/lecture9/latex-5e2aaa1f-da09-4657-aead-ca757caa9021.png)
  - Solve for b, ![latex-62154d42-3fff-40ea-b207-b0101cfac109](data/lecture9/latex-62154d42-3fff-40ea-b207-b0101cfac109.png)

To construct the portfolio:
- Time 0: Need to buy ![latex-11cf0471-a467-48b3-b01a-3945c0a33f0f](data/lecture9/latex-11cf0471-a467-48b3-b01a-3945c0a33f0f.png) units of underlying, borrow ![latex-4ba11a46-bfba-43a4-8e77-b84ba9429ca3](data/lecture9/latex-4ba11a46-bfba-43a4-8e77-b84ba9429ca3.png) dollars
  - ![latex-c09c408e-23bf-467d-b90f-e9be38dc9aa0](data/lecture9/latex-c09c408e-23bf-467d-b90f-e9be38dc9aa0.png)
  - This price must be the same as the price of the call, otherwise there is an arbirage opportunity

Arbitrage:
- suppose a trader quotes $7 for the call
  - sell the overpriced traded call for $7
  - construct the synthetic call for $4.76 (as above)
  - immediate profit of ![latex-68b6128a-86e9-4e12-a12a-3d1bd5863cab](data/lecture9/latex-68b6128a-86e9-4e12-a12a-3d1bd5863cab.png)
- suppose the quote is $3
  - buy the call for $3
  - short the portfolio, rebuild the portfolio with reversed positions

**Euro put Example**

Payoff:
- upside: max(110 - 120, 0) = 0
- Downside: max(110 - 90.25, 0) = 19.75

![latex-e00a759a-a9df-455b-97a7-4542f241c831](data/lecture9/latex-e00a759a-a9df-455b-97a7-4542f241c831.png)
![latex-ef4a69e6-36c1-4d66-8007-2b4a2bcd26ef](data/lecture9/latex-ef4a69e6-36c1-4d66-8007-2b4a2bcd26ef.png)
