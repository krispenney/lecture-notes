# Lecture 6 - June 19, 2018

Recall that a forward rate agreement allows us to lock in an interest rate for the future

### Eurodollar Futures
- underlying is always a 3 month LIBOR rate
  - **always**, no matter the maturity
- If you are afraid of interest rates going up, what position will you take?
  - short
  - The price is inversely correlated with the interest rate
  - Interest rate going up implies the price is going down.

#### Example (Slide 19)
- 11 basis point change between Nov 1 and 2
- ![latex-1615a8f4-dbe3-4fe2-9224-0c85251076dc](data/lecture6/latex-1615a8f4-dbe3-4fe2-9224-0c85251076dc.png)
- From november 1 to 2 the implied interest rate decreased
  - note that the price went up
- From november 2 to 3, the quote dropped, interest rates went up

#### Implicit Rate in an ED Future Quote
- Note that the example is working with percentages (i.e. why the 10,000 instead of 1,000,000)
- ![latex-16b6a936-5b6b-4dc4-840c-93776cb03ae1](data/lecture6/latex-16b6a936-5b6b-4dc4-840c-93776cb03ae1.png)
  - November 1: ![latex-c20a4107-1596-47b9-bf0b-059b529bcfb9](data/lecture6/latex-c20a4107-1596-47b9-bf0b-059b529bcfb9.png)
  - November 2: ![latex-aa06b965-a370-440b-8a61-101a218aebd8](data/lecture6/latex-aa06b965-a370-440b-8a61-101a218aebd8.png)
  - ![latex-df33a65d-5bec-408d-bf42-995ade404ccd](data/lecture6/latex-df33a65d-5bec-408d-bf42-995ade404ccd.png)
- Notice that this result is exactly the same as the previous calculation.

![latex-8fd40442-83f0-4204-a2bd-e4b001a05eac](data/lecture6/latex-8fd40442-83f0-4204-a2bd-e4b001a05eac.png)
- Quote price is linear in the interest rate (![latex-0e6890f7-698b-47aa-91b0-193c3e666d87](data/lecture6/latex-0e6890f7-698b-47aa-91b0-193c3e666d87.png))

### Exercise on ED-Futures
- 50 basis points (bps) is the spread, what has to be paid on top of the LIBOR rate (which is only available to banks)

a. What is the rate that we will lock in
  - ![latex-1123047d-87d6-4a03-b0bc-d5bb40786763](data/lecture6/latex-1123047d-87d6-4a03-b0bc-d5bb40786763.png)
  - Disney can lock in ![latex-8489f55b-6795-45ef-b544-56ae4d54ef39](data/lecture6/latex-8489f55b-6795-45ef-b544-56ae4d54ef39.png)
  - Therefore the rate it pays is ![latex-96eeceb3-8d60-45ce-b94a-1598b4f21349](data/lecture6/latex-96eeceb3-8d60-45ce-b94a-1598b4f21349.png)
b. how to profit if interest rates go up?
  - take a short position
  - You will be hedging the possibility of interest rates going up.
  - Take a short position of 50 contracts
c. If interest rates were 1.3 what is the quote?
  - ![latex-a0b282a1-e079-4c58-8f78-a641dfd7926c](data/lecture6/latex-a0b282a1-e079-4c58-8f78-a641dfd7926c.png)
d. The futures contract is settled in September, interest rates are paid 3 months later.

## Conventions

### Day Count

Defines the time to which the interest rate applies. The period of time used to calculate accrued interest (relevant when it is bought or sold).

- Treasury Bonds: Actual/Actual
- Corporate Bonds: 30/360
- Money Markey Instruments: Actual/30

**Note**: When you change the country, these conventions will change.

#### Example: Treasury Bond

- Coupon: 8%
- Payment days: March and September 1
- How much interest earned between March 1 and July 3?
  - ![latex-8b766a77-f231-43ef-8d65-f31a4c3d6ee0](data/lecture6/latex-8b766a77-f231-43ef-8d65-f31a4c3d6ee0.png)
  - Number of days between march and july / march and september


#### Example: Corporate Bond

![latex-dfc679ac-ae40-4bd0-8fc4-a47cd29023d1](data/lecture6/latex-dfc679ac-ae40-4bd0-8fc4-a47cd29023d1.png)

#### Example: commercial paper

![latex-c8032078-d522-4eae-9c15-be048d31e595](data/lecture6/latex-c8032078-d522-4eae-9c15-be048d31e595.png)

Dirty price = quoted price + accrued interest
- Cash price == dirty price, the price that you actually pay

### Treasury Bond futures
- underlying asset: is any government bond with maturity between 15 to 25 years on the first day of the delivery month
- Quotes are in dollars and 32-nds of a dollar per 100 dollar face value

cash price recieved by short position = most recent settlement price * Conversion factor + accrued interest
- Conversion factor accounts for the fact that different bonds will have different interest
- Accrued interest is for the underlying bond

#### Example: Cash recieved by short position
- settlement price: 90
- conversion factor of the bond delivered: 1.38
- Accured interest of bond: 3
- ![latex-9a094f00-4e4b-4a29-ac9d-ab79d3be4a30](data/lecture6/latex-9a094f00-4e4b-4a29-ac9d-ab79d3be4a30.png)

#### Conversion Factor
- Semi annual compounding
- typically from CNE, Bloomburg, etc

#### Choosing the Cheapest to deliver bond
- Delivery cost = cost to purchase - cash price recieved by party with the short position
- Have a pool of available bonds, compute the delievery cost of each, choose the one with the lowest delivery cost
  - that's the one to choose if your taking the short position

#### Steps to compute treasury bond futures price quotes
- Know the cheapest to deliever bond

1. Obtain cash price of the bond
2. Compute forward price of that bond ![latex-f9505284-392a-4b0f-ace5-9f88cc86b719](data/lecture6/latex-f9505284-392a-4b0f-ace5-9f88cc86b719.png)
3. Subtract the accrued interest from the future price, to obtain the quote price
4. Divide by the conversion factor

Basically the steps in reverse.

##### Example (Slide 13)

1. Obtain the cash price for the underlying bond
  - Quoted price: 115
  - Accrued interest: ![latex-0ec066e0-483e-425e-9574-6d530ca92991](data/lecture6/latex-0ec066e0-483e-425e-9574-6d530ca92991.png)
  - Cash price: ![latex-abaa0a1e-27a3-4d1a-ae0b-cdf79ac5d586](data/lecture6/latex-abaa0a1e-27a3-4d1a-ae0b-cdf79ac5d586.png)
2. Compute Future price
  - ![latex-5cbe325e-8590-4bb8-9803-9264bcafcff8](data/lecture6/latex-5cbe325e-8590-4bb8-9803-9264bcafcff8.png)
    - Present value of all coupons recieved
  - ![latex-a26c64b9-d7dd-4f4b-93b6-75f1a3aff49b](data/lecture6/latex-a26c64b9-d7dd-4f4b-93b6-75f1a3aff49b.png)
3. Compute Clean Future Price
  - ![latex-c352e625-a5fb-4e0b-aebc-262d2b13617e](data/lecture6/latex-c352e625-a5fb-4e0b-aebc-262d2b13617e.png)
4. Remove the conversion factor
  - ![latex-00237a82-11fc-453c-b70b-ef9dda3e2d3b](data/lecture6/latex-00237a82-11fc-453c-b70b-ef9dda3e2d3b.png)

## Swaps
- Swap is an arrangement to exchange cash flows at specified future times according to certain rules.
- floating cash flows vs. fixed
- Payments sent/recieved depend on the LIBOR rate, set on the specified day.

### Uses of an Interest Rate swap
- Converting a liability from:
  - floating rate -> fixed rate
    - recieving a variable rate, want to get a fixed rate
  - fixed rate -> floating rate
    - Currently paying LIBOR, want to pay a variable rate instead

- Converting an investment from:
  - floating -> fixed
    - recieving a variable rate, exchange for fixed LIBOR with a spread
  - fixed -> floating
    - recieve LIBOR (spread), recieve a variable rate

### The Comparative Advantage Argument
- AAACorp wants to borrow floating
  - better credit rating, has a lower cost
- BBBCorp wants to borrow fixed
  - lower credit rating than AAA

AAA can borrow at the fixed rate, start a swap with BBB.
- Pay LIBOR and recieve 4.35
- BBBCorp borrow at floating: LIBOR + 0.6

This is a better deal for both companies than just using the rates alone:
- AAACorp ends up paying: LIBOR - 0.35
  - Notice that LIBOR - 0.1 is a higher rate
- BBBCorp ends up: 4.95
  - The alternative fixed rate is 5.20

In reality, this is difficult for companies to do alone. They don't know eachother exist
- Instead, introduce an investment bank, who sets up indepentent swaps with each company.
- The investment bank introduces a spread between the two rates, their fee to provide the service.

### Valuation of an interest rate swap
- initially interest rate swaps are worth close to 0
  - Present values of fixed and variable are the same at the beginning

Recall that this is just a generalization of Forward Rate Agreements
- do so as a portfolio of Forward rate agreements

1. Calculate LIBOR forward rates
2. Calculate the swap cash flows that will occur if LIBOR forward rates are realized
3. discount the swap cash flows at OIS rate
  - Present values

#### Example: Evaluating an Old Swap
- 3 month: 2.8 -> ![latex-ccc9a056-3ada-468e-b14f-6e348d3bf02f](data/lecture6/latex-ccc9a056-3ada-468e-b14f-6e348d3bf02f.png)
- 9 month: 3.2:-> ![latex-42e2cd05-9cec-4ef7-b39a-b179c02cc2da](data/lecture6/latex-42e2cd05-9cec-4ef7-b39a-b179c02cc2da.png)
- 15 month: 3.4:-> ![latex-b9315193-f7fa-4f9a-8392-2b1a200cb33e](data/lecture6/latex-b9315193-f7fa-4f9a-8392-2b1a200cb33e.png)

Fixed cash flow rate: ![latex-b1a9e3b1-25ae-4fd8-a36b-f5b2466b8870](data/lecture6/latex-b1a9e3b1-25ae-4fd8-a36b-f5b2466b8870.png)

### Pricing A Swap

![latex-ef63ce7d-dd61-4e8b-beb2-df66435774a5](data/lecture6/latex-ef63ce7d-dd61-4e8b-beb2-df66435774a5.png)
- ![latex-1c461c9e-d115-45d4-8773-c0629cf56c64](data/lecture6/latex-1c461c9e-d115-45d4-8773-c0629cf56c64.png): LIBOR forward rate associated with period ![latex-cb7eb4ce-37b4-451e-bfa2-0fcc92083341](data/lecture6/latex-cb7eb4ce-37b4-451e-bfa2-0fcc92083341.png)
![latex-68aa9ecc-8931-42b5-89c6-7161f18c2dc3](data/lecture6/latex-68aa9ecc-8931-42b5-89c6-7161f18c2dc3.png)
- ![latex-06aeee50-663e-49c2-b15c-be9dc6b12846](data/lecture6/latex-06aeee50-663e-49c2-b15c-be9dc6b12846.png) present value of 1 dollar accrued for period ![latex-abcc3c58-5a36-4284-9477-434aa2510bd5](data/lecture6/latex-abcc3c58-5a36-4284-9477-434aa2510bd5.png)

#### Bootstrapping Forward rates example
- We know everything for the first 3 periods
- final period don't know the forward rate, easy to solve for it
