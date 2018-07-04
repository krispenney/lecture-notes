# Lecture 8 - July 3, 2018

## Strategies with options

- Stock plus option
- 2+ of the same type (a spread)
- 2+ of different types (a combination)
- Bond plus option to create principal protected note

### a: Covered Call
- Short call
- Own the underlying stock

### b:
- long call
- short underlying
- equivalent to a long put
- why not just buy the put?
  - you are typically trading against the market maker, they will probably put a larger spread on it.
  - by creating a synthetic put, you can be better off.

### c:
- long put
- own the underlying stock
- creates a synthetic long call position

### d:
- short underlying
- short put
- replicate a short call

### Bull Spread using calls
- Bullish on the underlying stock
- But don't want to risk in case things go bad
- short call, strike price ![latex-a16dfa9d-8876-427b-af39-69b648b59ce5](data/lecture8/latex-a16dfa9d-8876-427b-af39-69b648b59ce5.png)
- Use funds to buy long call with strike price: ![latex-efd74070-9326-45a6-94ec-b4ce6dbbf5a7](data/lecture8/latex-efd74070-9326-45a6-94ec-b4ce6dbbf5a7.png)
- Note: ![latex-1e1c350a-1cb4-46a9-90cf-701854a1e092](data/lecture8/latex-1e1c350a-1cb4-46a9-90cf-701854a1e092.png)
- Add the functions together
- Can add together the functions
- Basically produces 3 regions

### Bull Spread using Puts
- Basically the same as above

### Bear Spread using Puts
- Expect the underlying stock value to go down
- If the value drops too low then you could be better off with the long put, but everywhere else you're better off

### Bear Spead using calls
- Sell call with ![latex-ae0c723b-a349-4955-af0a-e9708d890eeb](data/lecture8/latex-ae0c723b-a349-4955-af0a-e9708d890eeb.png)
- Buy call with ![latex-96edcd9f-8bc3-4fa8-b613-d79efe3452f8](data/lecture8/latex-96edcd9f-8bc3-4fa8-b613-d79efe3452f8.png)

### A Straddle Combination
- Buy a call with a strike price ![latex-773b054b-6201-4c96-a644-45e8da7a6d9c](data/lecture8/latex-773b054b-6201-4c96-a644-45e8da7a6d9c.png)
- Buy a put with a strike price ![latex-365f141a-a274-4748-86a6-97c80d7f4800](data/lecture8/latex-365f141a-a274-4748-86a6-97c80d7f4800.png)
- In this strategy, you realize profits when the underlying goes extremely up or down
- Take advantage of the volatility of the underlying
- Better off as the stock moves away from the strike price
- **Note** An inverse straddle position is very risky, instead...

### Butterfly spread using calls
- Use 2 long calls ![latex-7993383c-3a2f-4049-9ad2-829a0f9408ea](data/lecture8/latex-7993383c-3a2f-4049-9ad2-829a0f9408ea.png)
- 2 Short calls with strike price ![latex-23669b24-8579-448e-b514-d15fda94bd68](data/lecture8/latex-23669b24-8579-448e-b514-d15fda94bd68.png)
- Use in the cases of Merger and Acquisition
  - The target typically goes up
  - Currently trading at ![latex-a067b740-721f-4b34-93fc-2b4a6ba48aa4](data/lecture8/latex-a067b740-721f-4b34-93fc-2b4a6ba48aa4.png), expect it to jump to ![latex-21cf09d8-27cb-4701-b81d-456d04002273](data/lecture8/latex-21cf09d8-27cb-4701-b81d-456d04002273.png)
  - since you're trading on rumors, you want to limit the potential losses

Can also build it using puts
- Really depends on the strike prices

### Strip and strap
- **Strip**: More profits when price goes down
- **Strap**: More profits when the price goes up

### Strangle Combination
- Straddle with two different strike prices
- Don't have much money
- Need a large move to start getting profits
- Try to limit the range in which the stock price will go

### Calendar Spread using calls
- Combine different maturities, match the strike prices

## Principal Protected Note

