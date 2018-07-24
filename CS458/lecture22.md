---
title: CS 458 Lecture 22
author: Kris Penney
---

## Risks

A risk is a potential problem that a system or it's users may experience.

characteristics:

- **probability**: What is the probability that the risk will occur
- **Impact**: If the risk occurs, what is the harm it will cause? Typically measured in terms of money.

### Risk analysis

It's impossible to completely eliminate risk, risk analysis is performed to determine if the risk is worth the potential benefit.

1. Identify assets
  - Main assets we want to protect: hardware, software, data
  - Additionally:
    - People: skills needed to run the business
    - Documentation: of hardware and software, also security plans, business continuity, indicent response
    - supplies: paper, forms, things that play a supporting role in running the business.
2. Determine vulnerabilities
  - for each type of asset
  - do some kind of threat modelling
  - threats that target: Confidentiality, integrity, availability + privacy
    - both technical and non-technical, ex. phishing and social engineering attacks
  - Want to determine the correct monetary amount of potential harm, to ensure that the proper controls are implemented
3. Likelihood of exploitation
  - Difficult to estimate the probability of each risk, especially if it's never happened before
  - **Frequency analysis**: How often has this attack happened in the past?
  - Example: Probability that Windows Vista is infected by a virus is 10% for enterprise users
    - Could be different for regular users (i.e. enterprise may restrict certain features; have stronger security)
  - Take the existing controls into account, as well as their probabilities of failing
4. Compute risk exposure
  - identify the impact of the risk, utilize the likelihood of the risk being exploited
  - $risk\ exposure = prob * impact$
  - Examples
    - need to consider legal obligations of users wrt. confidentiality, integrity, etc
    - Penalities for failing to provide a service (i.e. a disruption of availability)
      - Cost to offload data processing to a third party if availability of your systems are effected (ex. offload to AWS if your servers go down)
    - Could the release of an individual's data cause harm to them?
5. Survey applicable controls
  - Foreach vulnerability think of technical and non-technical means to control it
  - classify controls to how they protect each vulnerability
    - Could be better for one vulnerability, but make others worse
6. Project savings due to controls
  - Expected cost of not controlling the risk (risk exposure)
  - cost of each control is it's direct cost (ex. buying equipment, training), plus the exposure of the controlled risk
    - most controls aren't perfect, but they should reduce the probability of a threat occuring
  - Savings = risk exposure - cost of control
    - should have a positive benefit

### Physical Security

- firewalls don't protect the physical hardware
  - ex. someone just walking in and stealing a laptop

#### Classes of physical threats

- Nature
  - fire, flood, blackout
  - physically located
  - hard to predict
  - can only impact availability
- Human
  - theives
  - targeted attackers (have intention)
  - can target any of CIA

> What are the major differences in the security controls needed to protect against these two classes?

- humans can be held responsible (ex. legal action, taken to court), can be used as a detturrent.

#### Types of Human threats

- Vandals
  - some human attacks don't care about the data
  - just want to cause harm
  - how to control?
    - use offsite backups, systems
- Thieves
  - They are typically after the physical hardware
  - control:
    - lock computers down
    - guard systems
- Targetted Attackers
  - thieves are targetting a particular individual
  - After data / information that you have access to / know
  - How to control
    - encrypt your data

#### Protecting Offline Data

Data sitting on a shelf:
- printouts / reports
- backup tapes / HDDs

An attacker could walk in and grab the medium off of a shelf

- **This is very hard to detect**
- have physical guards

This is attractive to the attacker
- Backups may not be encrypted
- Backups contain files which have no permissions, no protection provided by the OS
  - Tapes have an unlimited time to access

Theives and insiders would be able to get physical access to this data
- need to have physical security, guards, lock it down
- Proper disposal of data
  - Paper: Shredder
  - Magnetic (Tapes / HDD): First encrypt the entire drive, then zero it out
    - Completely destroy it
  - Optical Media: break it

#### Testing that controls are correctly implemented

- Penetration testing
  - hire people to try to break into your systems
  - tell you what's wrong

#### Legal Protections

How to defend against a threat

- Prevent it
- deter it
- deflect it
- detect it
- recover from it

There's also legal defences

- Most obvious: stolen physical hardware

##### Overview of Intellectual Property

IP differs from real property by:

- It is **non-depletable**
  - If a laptop is stolen from you, you no longer have it
  - If IP is stolen, you still have it (but so does the theif)
- It is **replicable**
  - copy of a song / painting
- It has **minimal marginal cost**
  - Producing the first copy of IP is expensive
  - After this it can be applied / used for basically nothing

Types of IP for this course

1. Trade secrets
  - You don't want anyone else to own (ex. your competitors)
    - Coke formula
  - Just don't tell anyone (who doesn't need to know), call it a trade secret
  - You get legal protection if that person passes it on
    - NDA
  - No duration for a trade secret
  - No need to register trade secrets / NDAs
  - Threat: Reverse Engineering
    - take a finished product, take it apart to figure out how it works
    - If someone can do this, you've lost your trade secret, but there's nothing that you can do about it.
2. trademarks
  - Ownership of a particular name, brand, logo
  - legally file the trademark, allows you to sue the others who use your trademark in a confusing mannar
  - **Cyber-swapping**: register a similar domain name, but provide similar (legal) services
    - `anazon.com`
  - Domain names are typically protected under trademark law
3. patents
4.

They all cover

1. Different kinds of intangibles
2. Convey different rights
  - licences that define usage
3. Different duration
4. Have different registration requirements
