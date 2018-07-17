# Lecture 10 - July 17, 2018

## Synthetic calls
- recall that we can synthesize a call by constructing a portfolio

## Developing the Binomial Model

### Assumptions
- no market frictions
  - no bid ask spreads
- no credit risk
  - no possibility of bankrupcy
- competitive and well-functioning markets
- no intermediate cash flows
  - no lump sum dividends
- no arbitrage oppourtunities
- no interest rate uncertainty
  - constant with continuous compounding

### Binomial Process
- S is the current stock price
- The next periods stock price is modelled by:
  - Up factor: ![latex-72d6b90c-7c37-42b2-af85-9b7ec2e98eb8](data/lecture10/latex-72d6b90c-7c37-42b2-af85-9b7ec2e98eb8.png) gives ![latex-577b8aed-8b27-42ad-bba0-9afe2f152037](data/lecture10/latex-577b8aed-8b27-42ad-bba0-9afe2f152037.png)
  - Down factor: ![latex-ad6f01fc-864c-4f01-bd54-930f45906b55](data/lecture10/latex-ad6f01fc-864c-4f01-bd54-930f45906b55.png) gives ![latex-5d202580-b6db-4eda-a735-899f01262efb](data/lecture10/latex-5d202580-b6db-4eda-a735-899f01262efb.png)
  - Assumption: ![latex-ef73420e-b848-4f34-b4ae-958692b00a0d](data/lecture10/latex-ef73420e-b848-4f34-b4ae-958692b00a0d.png)
    - no arbitrage oppourtunities
- Let ![latex-b639fad7-c0ee-4c6a-81f5-dcb8eb95b1a6](data/lecture10/latex-b639fad7-c0ee-4c6a-81f5-dcb8eb95b1a6.png) denote the probability of the stock going up

#### Replicating Portfolio - Binomial Model
- Portfolio construction: purchase ![latex-9e684068-7ef4-45e6-bdcc-2126ff19d7c0](data/lecture10/latex-9e684068-7ef4-45e6-bdcc-2126ff19d7c0.png) units of the underlying, b units invested in money market account
  - b earns the risk free rate
- Initial value of portfolio: ![latex-a4d9f1b6-14d1-4b3b-a4f4-2a34f0ff887b](data/lecture10/latex-a4d9f1b6-14d1-4b3b-a4f4-2a34f0ff887b.png)
- At maturity: ![latex-c7c235c1-0773-490f-8125-770347f9c684](data/lecture10/latex-c7c235c1-0773-490f-8125-770347f9c684.png)
  - ![latex-3c8ed8ea-d165-4bbb-8f58-e9e5a2daba1d](data/lecture10/latex-3c8ed8ea-d165-4bbb-8f58-e9e5a2daba1d.png)
  - ![latex-ebfa7550-b072-45ba-8fc3-b29a77d6af0c](data/lecture10/latex-ebfa7550-b072-45ba-8fc3-b29a77d6af0c.png)

We can then derive the values for ![latex-89e5ade6-09ef-4357-aba5-9c32af084f11](data/lecture10/latex-89e5ade6-09ef-4357-aba5-9c32af084f11.png) and b:
- ![latex-e08c5698-9fdc-4ca7-acb5-2d8820501811](data/lecture10/latex-e08c5698-9fdc-4ca7-acb5-2d8820501811.png)
  - Just subtract both equations
  - ![latex-8ddfb495-c936-4468-b5ef-badc48de79f9](data/lecture10/latex-8ddfb495-c936-4468-b5ef-badc48de79f9.png) becomes similar to the hedging ratio
- ![latex-93107877-8720-4290-949c-167e7b0852d0](data/lecture10/latex-93107877-8720-4290-949c-167e7b0852d0.png)
  - Can use either equation, just use the relevant position

#### How to find the value of the option?
- The value of the portfolio V is equal to the value of the option c at any time, ![latex-41265425-669f-4b84-974d-3e2ee8cce52a](data/lecture10/latex-41265425-669f-4b84-974d-3e2ee8cce52a.png)
- ![latex-e03c9ebb-e5cb-4b10-8494-c978ae1096fc](data/lecture10/latex-e03c9ebb-e5cb-4b10-8494-c978ae1096fc.png)
  - ![latex-fe6d548e-d494-473f-947c-d523b2135cf5](data/lecture10/latex-fe6d548e-d494-473f-947c-d523b2135cf5.png)
- Let ![latex-106495b3-a155-4559-80be-148a5a7588a9](data/lecture10/latex-106495b3-a155-4559-80be-148a5a7588a9.png)
- Then, ![latex-68726a43-7bc6-42ac-b55b-7ac6828c5abc](data/lecture10/latex-68726a43-7bc6-42ac-b55b-7ac6828c5abc.png)

#### Risk neutral valuation of the principal
- Interpret ![latex-01b31064-fbb2-4e3a-bd8d-c9341248fb35](data/lecture10/latex-01b31064-fbb2-4e3a-bd8d-c9341248fb35.png) as probability
- As an expectation: ![latex-399fb3b1-2815-4f98-bd2e-049b6fbd7dd6](data/lecture10/latex-399fb3b1-2815-4f98-bd2e-049b6fbd7dd6.png)

#### Example: Pricing a call option
- YBM's stock price is 100 today
- after one year
  - ![latex-04846467-4193-4541-b791-865df2f2c963](data/lecture10/latex-04846467-4193-4541-b791-865df2f2c963.png)
  - ![latex-bf3fd4ed-83d5-49a5-98b1-83806a3c87b7](data/lecture10/latex-bf3fd4ed-83d5-49a5-98b1-83806a3c87b7.png)
  - ![latex-d210651d-0b38-485a-bae7-3c63d9242450](data/lecture10/latex-d210651d-0b38-485a-bae7-3c63d9242450.png)
- ![latex-10f08190-1c6b-4d12-a56e-27accd756fd2](data/lecture10/latex-10f08190-1c6b-4d12-a56e-27accd756fd2.png)
- With strike price 110
  - ![latex-26f7b355-075d-4263-9d08-29e0c3f644b7](data/lecture10/latex-26f7b355-075d-4263-9d08-29e0c3f644b7.png)
  - ![latex-83139149-b08f-4433-aaa6-3ba4afade4dc](data/lecture10/latex-83139149-b08f-4433-aaa6-3ba4afade4dc.png)
  - ![latex-1730fa5f-48dd-41c1-8b9e-305ea8a6a2b5](data/lecture10/latex-1730fa5f-48dd-41c1-8b9e-305ea8a6a2b5.png)

The expected return follows the risk-free rate if investors are risk neutral

We can add additional periods by adding intermediate layers

#### Two-Step Binomial Trees
- update state is always: ![latex-1e02b705-b455-49da-aef3-e087a21064e2](data/lecture10/latex-1e02b705-b455-49da-aef3-e087a21064e2.png), down is always ![latex-ced92868-e84d-4395-b2ba-3c59e2a452cf](data/lecture10/latex-ced92868-e84d-4395-b2ba-3c59e2a452cf.png)
- Just multiply by the proper probabilty as you traverse through the tree
  - Number of nodes grows exponentially, too much work to do by hand
- Need a structure to allow for many periods, without exponential properties
  - **REcombining**: Note that `down, up` is the same as `up, down`
    - For this property we need ![latex-785747a3-a64e-4ac3-b7f5-9c5cc57fb70e](data/lecture10/latex-785747a3-a64e-4ac3-b7f5-9c5cc57fb70e.png)
    - Then the number of nodes in each layer is linearlly proportional to the layer
      - ![latex-f6c98151-2204-421f-a122-b87e6b9ab89d](data/lecture10/latex-f6c98151-2204-421f-a122-b87e6b9ab89d.png)
- Periods are always the same distance from eachother
  - ![latex-57b882cd-9e41-43be-b6ce-7937b4d568e4](data/lecture10/latex-57b882cd-9e41-43be-b6ce-7937b4d568e4.png) defines the length of each individual timestep
  - Total length is T
    - Sum of all periods: ![latex-6aac38f5-598b-45fb-a36c-8b080f3d129e](data/lecture10/latex-6aac38f5-598b-45fb-a36c-8b080f3d129e.png)

#### How to price option
1. Build the tree
2. Compute value of the derivative for each node in the second layer
  - Use the strike price and derivative type
  - Ex: for a put with strike price 52: ![latex-1ad0a89c-7295-4b35-901d-ccc1062786e0](data/lecture10/latex-1ad0a89c-7295-4b35-901d-ccc1062786e0.png)
3. Work backwards computing the option values
  - Need ![latex-03df8bd0-0d01-4dd4-93fe-71513c5b37b5](data/lecture10/latex-03df8bd0-0d01-4dd4-93fe-71513c5b37b5.png)
  - ![latex-1c54eaa3-ab8e-410b-8dcf-da96aec223e8](data/lecture10/latex-1c54eaa3-ab8e-410b-8dcf-da96aec223e8.png)
  - ![latex-5e9f9126-fe3f-4de0-ae63-c9322350b419](data/lecture10/latex-5e9f9126-fe3f-4de0-ae63-c9322350b419.png)
4. Then find C
  - Note that ![latex-aca615a3-dec2-48cf-b2e9-ee54cb63d604](data/lecture10/latex-aca615a3-dec2-48cf-b2e9-ee54cb63d604.png) doesn't change
  - ![latex-7f56d9df-5a2d-4a08-87ea-306f821a99db](data/lecture10/latex-7f56d9df-5a2d-4a08-87ea-306f821a99db.png)

Then to compute: ![latex-454f0c31-9be8-43a0-8994-730671f40f8d](data/lecture10/latex-454f0c31-9be8-43a0-8994-730671f40f8d.png) **(for european case)**
- C(T) can take on multiple values
- sum of the probabilities, just look at path in the tree
- **For american** have to work through the iterative approach
  - Can exercise at any point in time
  - The payoff is the max of present value (keep holding), or the intrinsic value
  - This has implications for the present value of the option, because of the possibility to exercise in the future

#### How to Choose U and D?
- ![latex-5e9d741e-e8fa-460d-9cea-27febd9e1925](data/lecture10/latex-5e9d741e-e8fa-460d-9cea-27febd9e1925.png)
  - ![latex-d212a9f0-23c2-4a0d-9496-70b4d8cb3917](data/lecture10/latex-d212a9f0-23c2-4a0d-9496-70b4d8cb3917.png) is the volatility of the underlying stock's price
- ![latex-fa793e92-b8cb-4ea9-b10e-bf806633eb31](data/lecture10/latex-fa793e92-b8cb-4ea9-b10e-bf806633eb31.png)

#### Increasing the number of steps
- A smaller time step gives a better approximation of the true
