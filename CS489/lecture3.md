# Lecture 3 - January 8, 2018

## Simpler Neural Models
In a HH model, you need to solve a 4-D system. Instead, we can use 1 variable. Don't need to model the spike itself, just when it happens.

### Leaky Integrate and Fire (LIF) Model
- Simply records when the spike occurs (i.e. when the voltage reaches the threashold)

Let ![latex-044ea17c-260c-4c4d-a5c0-4ea2f800f0c1](data/lecture3/latex-044ea17c-260c-4c4d-a5c0-4ea2f800f0c1.png)
![latex-f0a4f224-b857-44e6-a39a-c795e106e830](data/lecture3/latex-f0a4f224-b857-44e6-a39a-c795e106e830.png)

**Eurler's Method for assignment 1**

If ![latex-fb159e14-edd3-43bc-81a9-574f42cf9c8d](data/lecture3/latex-fb159e14-edd3-43bc-81a9-574f42cf9c8d.png) the LIF neuron will spike.

![latex-1a9e38de-ac8f-48f4-8482-a0a3eb905b4c](data/lecture3/latex-1a9e38de-ac8f-48f4-8482-a0a3eb905b4c.png)


