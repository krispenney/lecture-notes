# Lecture 7 - June 26, 2018

## Excercise solution

This is with annual compounding:
- ![latex-09692c82-df4d-491a-9035-0842407e264f](data/lecture7/latex-09692c82-df4d-491a-9035-0842407e264f.png)
- ![latex-d824031d-525c-4be2-bda1-8548637541cc](data/lecture7/latex-d824031d-525c-4be2-bda1-8548637541cc.png)

- Current 1 year LIBOR: 3%
- LIBOR forward 1 to 2 year period: 3.2%
- 3 year (annual payments): 3.2%
a. Find the LIBOR forward rate for 2-3 year period
  - ![latex-4eec3685-5428-45ef-add4-463298a83c6b](data/lecture7/latex-4eec3685-5428-45ef-add4-463298a83c6b.png)
  - Just solve for ![latex-110cf0fb-af80-49aa-b79b-aa48794c035e](data/lecture7/latex-110cf0fb-af80-49aa-b79b-aa48794c035e.png) (recall that we can compute each ![latex-dbe8cc42-349e-4a98-82d0-0b80c8be8271](data/lecture7/latex-dbe8cc42-349e-4a98-82d0-0b80c8be8271.png))
b. Value a 3 year swap, 4% recieved, LIBOR paid on principal of $100 million
  - Take the cash flows and forward rates
  - Note that 4% is the 1 year rate
  - ![latex-c62ea425-7c42-4191-9add-7de4a5ae4676](data/lecture7/latex-c62ea425-7c42-4191-9add-7de4a5ae4676.png) is 100 million
  - We know the forward rates for (1-2, 2-3), use the swap LIBOR rate from part a (3.4)
  - ![latex-b20f3950-45b0-4f49-956a-500e8a685ada](data/lecture7/latex-b20f3950-45b0-4f49-956a-500e8a685ada.png)
c. If the 3-4 forward rate is 4.1%, what should be the swap rate for a 4-year swap contract?
  - Compute Present values for each, weighted average of the rates
  - ![latex-8305c843-6dbb-465f-bd9c-70cc805dce5a](data/lecture7/latex-8305c843-6dbb-465f-bd9c-70cc805dce5a.png)
  - solve for the swap rate
  - ![latex-91744545-467b-460e-a94d-ced4bf589445](data/lecture7/latex-91744545-467b-460e-a94d-ced4bf589445.png)

### Question 3

Airbus
- borrow at 11% fixed rate
- or: LIBOR + 1 floating rate

Bombardier
- borrow at 10% fixed rate
- or: LIBOR + 3% floating rate

How can you bring both companies together in an interest swap that would make both better off:
- Note: Although Airbus has a better credit rating than Bombardier, Bombardier has a better fixed rate because it is supported by the federal government.

Solution
- Airbus goes for the floating rate, enter into a swap rate with Bombardier, who uses their fixed rate
- 3% that can be distributed between the companies (assume equal parts, i.e. benefit both by 1.5%)
- Airbus
  - recieve LIBOR + 0.5%, pay 9% to Bombardier. ![latex-fcec3996-3330-4e30-a512-2f849f09ef9e](data/lecture7/latex-fcec3996-3330-4e30-a512-2f849f09ef9e.png) implies better off their fixed rate by 1.5%
  - Borrow at fixed rate, pay LIBOR + 0.5%, recieve a fixed rate of 9%. ![latex-8561ed03-2a19-468d-abe2-49d2b4770bce](data/lecture7/latex-8561ed03-2a19-468d-abe2-49d2b4770bce.png)

## Options: General Aspects
- Rights to perform action at a price

### Types
Suppose ![latex-30c847f4-d792-47ee-8307-db399676a911](data/lecture7/latex-30c847f4-d792-47ee-8307-db399676a911.png) is the strike price

- **call**: option to buy
  - value at which you can buy is called the **strike price**
  - Decision to exercise is dependent on the price of the underlying (don't want to loose out when you can just buy)
  - Payoff at maturity (Euro): ![latex-c3a8e20f-6a88-4077-95b7-63b0c02972e3](data/lecture7/latex-c3a8e20f-6a88-4077-95b7-63b0c02972e3.png)
- **put**: option to sell
  - Payoff at maturity (Euro): ![latex-dcb23e40-5150-4c68-b386-fc6e86a7483a](data/lecture7/latex-dcb23e40-5150-4c68-b386-fc6e86a7483a.png)
- **European**: Can only excerised at the end of it's life
- **American**: Can be excerised at any time, until maturity

Options are traded on the market
- The price is related to their payout

### Long call
- Expect the market to go up
- In practice, you pay to own the option
- breakeven point: Underlying price = Strike price + option price
- make money when ![latex-91b316c8-bc30-457f-98d5-940771a20336](data/lecture7/latex-91b316c8-bc30-457f-98d5-940771a20336.png)

### Short call
- expect the market goes down
- Very risky, can have unlimited losses
- make money when $$underlying < strike price - option price

### Long Put
- expect the market goes down

### Short Put
- Expect the market to go up

### Specifics of exchange traded options
- Expiration date: T
- Strike Price: K
- option class: call or put
- Lot size is typically for 100 shares

**Moneyness**
- At the money: ![latex-550d6698-f3ea-4d16-a4a2-2a8294c4bf8e](data/lecture7/latex-550d6698-f3ea-4d16-a4a2-2a8294c4bf8e.png)
- In the money: Make money
  - call ![latex-1cd71790-d4ab-40be-b44e-c7fe6438f654](data/lecture7/latex-1cd71790-d4ab-40be-b44e-c7fe6438f654.png)
  - put  ![latex-b5571bbd-22b3-46f1-acd6-016b7dd99cfe](data/lecture7/latex-b5571bbd-22b3-46f1-acd6-016b7dd99cfe.png)
- Out of the money: Loose money
  - call ![latex-718179b1-79df-4186-8e2e-802418d3ab98](data/lecture7/latex-718179b1-79df-4186-8e2e-802418d3ab98.png)
  - put ![latex-f206146f-994a-4e9f-8cb0-2df943da04f2](data/lecture7/latex-f206146f-994a-4e9f-8cb0-2df943da04f2.png)

**Option Class**: call or put
**Option series**: Specific contract over time
**Intrinsic VAlue**: payoff from an immediate exercise, always use the current value of the underlying
- Call: ![latex-63900152-48e6-4a07-8fe2-b3fc3112897a](data/lecture7/latex-63900152-48e6-4a07-8fe2-b3fc3112897a.png)
- Put: ![latex-932ddc17-2790-4a24-aef6-b3e0130a66c4](data/lecture7/latex-932ddc17-2790-4a24-aef6-b3e0130a66c4.png)

**Time Value**: Different possible values at maturity
  - intrinsic and time value converge as time approaches maturity

### Dividends and stock splits
- recall that trading an option on an exchange is in bundles of 100
- If there's a stock split, your contract must change as a function of this split
- Suppose there is an n for m stock split
  - The value of the position won't change
  - the number of shares changes
  - ![latex-591b6bc8-6421-484d-b6e7-342accec1e3a](data/lecture7/latex-591b6bc8-6421-484d-b6e7-342accec1e3a.png) (decreases)
  - Number of shares is: ![latex-d74551da-0545-4fb1-935b-d03bebb75e61](data/lecture7/latex-d74551da-0545-4fb1-935b-d03bebb75e61.png) (increases)
- For dividends
  - If it's paid in dollars, no change
  - if it's stocks, then it must be changed (as the amount of stock is effected)
    - 5% stock dividend => 21-for-20 split: option to buy 105 shares at $19.05

### Market Makers
- party that is behind the bid and ask prices

#### Margin

In the case of short selling options, need margin to cover potential losses (which can be very large)

when a naked option is written, margin is the larger of:
- A total of 100% of proceeds of sale, plus 20% of the underlying share price less the amount out of the money
- 100% of proceeds of the sale plus:
  - call: 10% of underlying share price
  - put: exercise price
- **Example:** ![latex-985897f3-a60b-4eae-b270-f4747259bfb5](data/lecture7/latex-985897f3-a60b-4eae-b270-f4747259bfb5.png)
  - Note that we're in the money
  - 12 + 0.2(100 - 0) = 12 + 20 = 32
  - 12 + 0.1(100) = 22

### How firms can hedge
- compared to a futures strategy, the option strategy only protects in the cases where losses can occur

| | futures strategy | option strategy |
|-|-|-|
| intends to buy; concerned about price increase | long futures | purchase call option |
| intends to sell; concerned about price decrease | short futures | purchase put option |

## Test 2
- 30% is multiple choice
- 70% is calculations
  - show work
- See online
