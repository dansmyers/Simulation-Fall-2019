# Sprint 6 Quiz Review

## PASTA and Poisson Process

PASTA stands for *Poisson Arrivals See Time Averages*. Explain, in your own words, the meaning of this statement.

Write down expressions for the following:

- The probability that the server is occupied at the instant of a Poisson arrival
- The expected number waiting in the queue but not being served at the instant of a Poisson arrival

Give an example of a system where the Poisson process would be a useful arrival model. Give an example of a system where the Poisson process **would not** be a useful arrival model.

## Derive

Use the tagged customer method to show that the residence time in the M/M/1 queue is

```
       s
R = ------- 
     1 - U
```

## M/G/1

Consider a queue with hyperexponential service times and Poisson arrivals.

The arrival rate is 100 customers per second.

The average service time is 5 ms and the variance in the service times is 150.

Use the M/G/1 residence time equation to calculate the expected residence time in this queue.


## Compare

For the system in the previous problem, which design improvement would have a larger impact?

1. Reducing the average service time to 2 ms while keeping the variance at 150.

2. Keeping the average service time at 5 ms while reducing the variance to 20.


## Shake

Shake Shack is a restaurant where people go to wait in line and sometimes get milkshakes and other food.

The Shack uses a dual-queue system to process orders:

1. One line serves only milkshakes.

2. Another line serves the complete menu.

Suppose that 20% of people visiting Shake Shack only want a milkshake and the other 80% want to order off the full menu. Shake Shack serves 50 customers per hour during peak loads.

Suppose that the time to fulfill a milkshake order is effectively **deterministic** and *s*<sub>*milkshake*</sub> = 3 minutes.

- What fraction of time is the milkshake line empty?
- What is the maximum service time that the full-menu line can tolerate?
- What is the total expected residence time required to get a milkshake?
- Suppose you arrive at the milkshake queue at a random moment in time. How many customers do you expect to find in the queue in front of you, on average? Hint: use the M/G/1 residence time equation and Little's Result.
