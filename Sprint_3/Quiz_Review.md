# Sprint 3 Quiz Review

## Topics

- Using the exponential CDF and CCDF to solve lifetime problems
- Using the memoryless property with the exponential CDF and CCDF to solve lifetime problems
- Using Little's Law and the Utilization Law to calculate system performance measurements
- Applying the inverse CDF method to derive an expression for generating random variates from a given distribution
- Generating values from a linear congruential pseudorandom number generator

## Problems

### Lumos, Pt. I

Consider a bulb that has an expected exponentially-distributed lifetime of 2000 hours. What is the probability that the bulb survives for between 1000 and 3000 hours?

### Lumos, Pt. II



### Lumos, Pt. III: Deluminator

To save money, I like to buy discount lightbulubs from Crazy Pavel's House of Illumination. Pavel's bulbs are terrible and burn out
after an average of only 25 hours.

How many bulbs would expect to go through before finding one that survives for more than 100 hours?

Tip: this is like a geometric trial where the probability of success can be calculated by the expoenntial distribution.


### LCPRNG

Generate a full period from a linear congruential PRNG with parameters

- *a* = 5
- *c* = 1
- *m* = 8
- *x*<sub>0</sub> = 0

### Gumbel

The Gumbel distribution is an odd distribution with an interesting application to modeling extreme events. It has one of the all-time best CDFs:

*F(x)* = *e*<sup>-*e*<sup>-(*x* - *μ*) / *β*</sup></sup>

*μ* is the mean and *β* is a scale parameter.

Use the inverse CDF approach to derive an expression for generating Gumbel-distributed random variates.

### Hyperexponential Distribution

A *hyperexponential distribution* is created from a probabilistic mixture of exponential distributions. The two-stage hyperexponential has three parameters: *μ*<sub>1</sub>, *μ*<sub>2</sub>, and *p*.

To generate values from the distribution, use the following rule:

- With probability *p*, generate an exponential random variable with parameter *μ*<sub>1</sub>
- With probability *1 - p*, generate an exponential random variable with parameter *μ*<sub>2</sub>

Write a Python method to generate two-stage hyperexponential random variates.

```
def randHyperExp(mu_1, mu_2, p):

    # TODO: code goes here
```
