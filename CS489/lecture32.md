# Lecture 32 - March 26, 2018

## Adversarial Inputs
- To create inputs that are malicious to NNs
- Can go gradient ascent, pull it away from the correct class
- Can do gradient decent, but compare it to the wrong target. Thereby pulling it towards a different class.
  - Find the smallest bit (in terms of changes) of random noise that causes the incorrect classification

## Generative Adversarial Networks
- Adversarial networks + descriminitive networks
- Both compete against eachother, try to fool eachother
- adversarial network
  - Take some random noise, produce some output
  - ex. take some noise, produce an image
  - Job is: fool the discriminator to misclassify fake inputs
  - Want to minimize 1-disriminator output, minimize probability that generated images are fake.
- descriminator
  - Classifies
  - ex. take an image, produce a label
  - Job becomes, identify real or generated (fake) images
  - want to maximize probability of discriminator when input is real (close to 1), minimize (close to 0) if fake.
