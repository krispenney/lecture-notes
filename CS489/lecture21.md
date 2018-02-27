# Lecture 21 - February 26, 2018

## Midterm
- Everything upto and including variational autoencoders and Maps
- pre-reading week

## Assignment 3
- For dropout, no need to touch `Backprop`.
- As a result, it only needs to work on 1 hidden layer.

## Hubel and Wiesel Cat
- Monitor a few neurons in the cat's visual corex
- See what those neurons encode

## Neural Coding
- Recall LIF, If input current is fixed and above the threshold
- neuron encodes a quantity if the neuron's activity changes as the value changes
  - i.e. manupilating lights on a screen

### Population Coding
- Neurons react to some external environmental variable
  - reacting to light, brightness, etc
- Can build tuning curves of the neurons
- Then, given states of the neurons, you can reverse-engineer the state on the brain
  - Read the mind
  - Where was the cat looking

#### Linear coding
- Use a linear remapping to approximate all of the intermediate processes
  - There are many different processes between the input and the neuron
  - i.e. eye-ball -> a bunch of neurons -> the neuron that we're monitoring
  - ![latex-cfaec920-ee94-4b13-9e84-01ec285dd872](data/lecture21/latex-cfaec920-ee94-4b13-9e84-01ec285dd872.png)
  - ![latex-232ad2b0-eb9d-4fbb-a34f-18f2942e0e4f](data/lecture21/latex-232ad2b0-eb9d-4fbb-a34f-18f2942e0e4f.png): gain, positive real number
  - e: The encoder: $$e \in \left\{-1, 1\right\}
  - ![latex-f6d96e9a-3020-4a11-9d26-782aefbe7f0c](data/lecture21/latex-f6d96e9a-3020-4a11-9d26-782aefbe7f0c.png): Bias, real number

![latex-f7245767-ab9a-44fb-8489-a45e3359dc43](data/lecture21/latex-f7245767-ab9a-44fb-8489-a45e3359dc43.png) is the current entering the neuron for stimulus x, LIF neuron characterised by:
1. ![latex-be86bf65-31b1-4ee2-8cbf-dbe02d380ac3](data/lecture21/latex-be86bf65-31b1-4ee2-8cbf-dbe02d380ac3.png): Threshold (we just set it to 1)
2. ![latex-69a7bea4-09de-46d3-be26-b15cbaf7f6f2](data/lecture21/latex-69a7bea4-09de-46d3-be26-b15cbaf7f6f2.png): Membrane time constant
3. ![latex-ff316d2b-e3cf-4814-b70c-bf27d05b428e](data/lecture21/latex-ff316d2b-e3cf-4814-b70c-bf27d05b428e.png): refactory period
4. ![latex-eb68e0cd-1640-4184-8a16-17ac5744c756](data/lecture21/latex-eb68e0cd-1640-4184-8a16-17ac5744c756.png): Gain
5. ![latex-4387f605-5ff0-43e9-8a31-16bf288e4d2b](data/lecture21/latex-4387f605-5ff0-43e9-8a31-16bf288e4d2b.png): Bias
6. ![latex-b6a79a61-c823-4e52-ab26-396f019a75d4](data/lecture21/latex-b6a79a61-c823-4e52-ab26-396f019a75d4.png): Encoder

##### Decoding Excersice
- ![latex-46345f58-b315-41fa-999d-c40254eedcaf](data/lecture21/latex-46345f58-b315-41fa-999d-c40254eedcaf.png): Input must be around ![latex-5de5ce11-ec0a-472a-adf7-8415ffddb62a](data/lecture21/latex-5de5ce11-ec0a-472a-adf7-8415ffddb62a.png)Hz
- [1, 2]: Around 0hz
- [2, 3]: Around -1hz
- [3, 4]: Around 2hz

In reality each neuron has a stochastic element, therefore you want to have a higher number of neurons to improve stats.

##### Optimal Linear Decoding
- ![latex-a656c3f1-6346-4dfd-8a04-12e5edbd3716](data/lecture21/latex-a656c3f1-6346-4dfd-8a04-12e5edbd3716.png) is a column vector containing P x-values (inputs)
- ![latex-7dac5711-ef82-4b61-8b5f-573cb0c5da74](data/lecture21/latex-7dac5711-ef82-4b61-8b5f-573cb0c5da74.png) is a PxN matrix with each row containing the activities (firing rates) of N neurons for the corresponding input value.
