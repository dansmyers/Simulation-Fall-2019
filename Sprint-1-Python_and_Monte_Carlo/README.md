# Sprint 1: Python and Monte Carlo Simulation

## Overview

## Learning Outcomes

At the end of this sprint, you will be able to

- Write small to moderately-sized programs in Python using standard programming features: variables, conditionals, loops, functions, lists, etc.

- Use a Python development environment.

- Work with files in Python.

- Use `matplotlib` to visualize the results of simulations.

- Calculate standard summary statistics: mean, median, standard deviation, variance.

- Design and implement a simulation that uses randomness to estimate the outcome of a complex calculation or process.

- Be able to use Python's `random` library and functions for generating uniform random variables and random integers.


## Deliverables

Write Python programs to perform the following simulations.

### Passe-Dix

French for "pass ten", passe-dix is a gambling game of ancient origin. Some early gambling books claim it was the game played by Roman soldiers to divide Jesus's clothes at the Crucifixion.

The rules are simple: the player rolls three six-sided dice. If the sum is ***strictly greater than ten***, he wins. If not, he loses.

Use a Monte Carlo simulation to estimate the probability of winning at passe-dix.

Your program should have two functions:

- A `simulate` method that simulates one round of the game. The method should use the Python `random` module to roll three dice, check their sum, and returns `True` or `False` to indicate whether the player wins or loses.

- A `main` method containing a loop that calls `simulate` a large number of times (at least 1000), counting up the number of `True` responses. At the end of the loop, calculate the fraction of trials that resulted in `True`: this is the estimated winning percentage. Print this number as your final output.

Submit your code in a program called `passe_dix.py`.

### Craps

One of the most popular dice games in American casinos, craps is famous for an extensive array of bets players can make. The most common
is called the "pass" bet, and it works as follows:

- A player (the "shooter") rolls two six-sided dice.

- If their sum is 7 or 11, the bet immediately wins. If the sum is 2 ("snake eyes"), 3, or 12 ("boxcars" or "midnight"), the bet immediately loses.

- If the sum is any other number, that number becomes the *point*.

- The shooter continues rolling the dice with the goal of rolling the point value again before rolling a 7. If the point comes up first, the bet wins; if a 7 comes up first, the bet loses. The shooter will re-roll as many times as required until either a point or 7 comes up.

Write a simulation program to estimate the probability of winning the pass bet in craps. Use the same guidelines as the previous problem. Remember that your `simulate` method should return the result of *one complete round of the game*.

Submit your code in a program called `craps.py`.

### The Martingale



## Resources

I've given you several notes and example programs to help you get started:

- The `Notes` directory contains some background telling you how to set up Python, the differences between Python and Java, and some tips for writing Python programs.

- The `Examples` directory contains example simulation programs and some practice questions.

For general Python background I recommend Allen Downey's *Think Python*, which is [available free on the web](https://greenteapress.com/wp/think-python/). It contains a good overview of essential elements of Python programming. For our purposes, the most important chapters are the ones on variables, iteration, conditionals, functions, and lists. We'll get into the material on tuples, dictionaries, and objects later in the class.
