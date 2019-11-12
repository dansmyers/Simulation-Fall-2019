# Quiz Review

## Matrix 2 Chain

Draw out the Markov chain corresponding to the following transition matrix.

```
                             to
 
                 state 0   state 1   state 2
      
      state 0      .40       .10       .50

from  state 1      .00        .90      .10

      state 2      .80        .00      .20
```

## Long-Run Probabilities

Draw out the Markov chain corresponding to the following transition matrix, then use the global balance equations to solve for the
long-run probability of being in each state.

```
                         to
 
                 state 0   state 1
      
      state 0      .00       1.0 
from  
      state 1      .50        .50
```

Tip:

The answers should be 1 / 3 and 2 / 3.

## M/M/1

Use a Markov chain analysis to show that the queue length distribution in the M/M/1 queue is

P(N = *k*) = *U*<sup>*k*</sup> (1 - *U*)

Tip:

This is the derivation that we did in class. This is an important result, so I want to make sure you know how the derivation works.

## Queue Length Distribution

Consider an M/M/1 queue with *U* = .90. What is the long-run fraction of time the queue contains more than 1 customer?

## Residual Service Times

Suppose a new customer arrives to a queue and finds someone already receiving service. The remaining time required for the customer in service is called the **residual service time**. In general, this quantity is hard to calculate, because we can't know how long the customer has been in service or what its eventual service time will be.

The M/M/1 queue, however, is a special case that's easy to analyze. What is the residual service time in the M/M/1 queue?

## M/M/*c*

Consider a queue with one waiting line and *c* servers. The first customer in line gets to enter service as soon as any of the *c* servers becomes available.

Suppose the service rate of each individual server is *μ*.

- When there is one customer in the system, one server is occupied, and the total service rate of the system is *μ*.

- When there are two customers in the sysetm, two servers are occupied, and the total service rate of the system is 2*μ*.

- When there are three customers in the system, three servers are occupied, and the total service rate of the system is 3*μ*.

- When there are *c* customers in the system, all *c* servers are occupied, and the total service rate of the system is *cμ*.

- When there are *c+1* or more customers in the system, all *c* servers are occupied, and the total service rate of the system is maxed out at *cμ*.

Draw out a Markov chain model for the M/M/*c* queue. You don't need to solve the model, just draw it out.
