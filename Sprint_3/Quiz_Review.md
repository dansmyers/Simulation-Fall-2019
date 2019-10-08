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

Answer: about .3834.

### Lumos, Pt. II

Consider two bulbs that have mean exponentially-distributed lifetimes of 500 hours each. What is the probability that one bulb survives for more than 1000 hours and the second fails before reaching 100 hours?

Tip: the bulbs are independent, so you need to multiple their individual probabilities to get the joint probability.

Answer: about .02453.

### The Basics

Suppose you have a queue with the following parameters:

- *U* = .50
- *s* = 5 minutes
- *N* = 2 customers

Use the Utilization Law to calculate the arrival rate to the system.

What is the average residence time of a customer in the queue?

Answer: 20 minutes.

### Another Unbalanced Load Problem

(I have tried to be as precise as possible in explaining how this problem is set up).

Suppose we have a computer system that contains two disks labeled *A* and *B*. Job requests come into the system and spend time moving through different processing phases before eventually existing.

During a trip through the system, the average job request makes two non-consecutive visits to disk A and one visit to disk B.

Disk A is the component with the highest load, so it is the *bottleneck* for the system: the maximum throughput for the entire system must be kept low enough to prevent disk A from being overloaded.

Suppose each disk access takes an average of 10 ms. What is the maximum throughput that can be sustained by each disk? What does that imply about the maximum throughput of the system as a whole?

Tip: the utilization at each disk must be less than 1.0.

Tip-tip: remember that the visits to disk A are non-consecutive. Each customer passing through the larger system vists A twice, so λ<sub>A</sub> = 2λ<sub>system</sub>.

Answer: Disk throughput must be less than 100 customers / sec. Total system throughput must be less than 50 customers / sec.

### Faster Disks?

Suppose we replaced disk A in the previous problem with a higher performance disk that has an average access time of only 6 ms. What is the maximum possible system throughput under this configuration?

Tip: use the Utilization Law to calculate the improved max throughput at disk A.

Answer: about 83 customers / sec.

### Balanced Loads?

Suppose we keep the original disks with 10 ms service times, but re-design the system so that each customer makes 1.5 vists to A on average and another 1.5 vists to B on average.

What is the impact of this change on the maximum possible system throughput?

Answer: about 66 customers / sec.

### Lumos, Pt. III: Deluminator

To save money, I like to buy discount lightbulubs from Crazy Pavel's House of Illumination. Pavel's bulbs are terrible and burn out
after an average of only 25 hours.

How many bulbs would expect to go through before finding one that survives for more than 100 hours?

Tip: this is like a geometric trial where the probability of success can be calculated using the expoenntial distribution.

Answer: about 54.59 bulbs, on average.


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
