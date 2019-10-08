# Sprint 3 Quiz Review

## Topics

- Using the exponential CDF and CCDF to solve lifetime problems
- Using the memoryless property with the exponential CDF and CCDF to solve lifetime problems
- Using Little's Law and the Utilization Law to calculate system performance measurements
- Applying the inverse CDF method to derive an expression for generating random variates from a given distribution
- Generating values from a linear congruential pseudorandom number generator

## Problems

### LCPRNG

Generate a full period from a linear congruential PRNG with parameters

- *a* = 5
- *c* = 1
- *m* = 8
- *x*<sub>0</sub> = 0

### Gumbel

The Gumbel distribution is an odd distribution with an interesting application of modeling extreme events. It has one of the all-time best CDFs:

F(x) = *e*<sup>-*e*<sup>-(*x* - *μ*) / *β*</sup></sup>

*μ* is the mean and *β* is a scale parameter. Use the inverse CDF approach to derive an expression for generating Gumbel-distributed random variates.
