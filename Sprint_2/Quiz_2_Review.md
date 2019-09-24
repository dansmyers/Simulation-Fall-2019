# Quiz 2 Review

## Topics

- Expected values
- The geometric distribution
- The binomial distribution
- Bayes' Rule
- Conditional probability

## Practice Problems

### Family Planning

Suppose a newly married couple has decided to keep having kids until they have one girl and then stop.

What is the probability they end up with more than two kids? You can assume the probability of having a girl is always .50, independent of any previous children.


### *Les Poissons*, *Les Poissons*! How I Love *Les Poissons*!

<img src="les_poissons.jpeg" width="50%" />

A Poisson random variable is often used to model the occurence of random events over time. Its first application was, allegedly,
modeling the incidence of deaths by horse kicks in the Prussian Army (but that's probably not true).

Its distribution is discrete and has a single parameter, *λ* > 0, which is called the *rate*. Very shortly, we’ll study
the Poisson process, which is closely related to the Poisson distribution and has several nice properties that
are useful in analyzing queueing systems.

The basic application of the Poisson distribution is modeling the number of events that occur in a fixed time period if the events occur at constant rate *λ*. The probability of $k$ events in the period is given by the Poisson pmf:

<img src="poisson_pmf.png" width="15%" />

Show that the expected value of the Poisson distribution is simply *λ*.

Tip: start by writing down the definition of the exponential.

<img src="poisson_exp_value.png" width="15%" />

Notice that the first term of the summation is zero, so it's okay to start the sum with *k* = 1.

Tip-tip: use the fact that 

<img src="exp_def.png" width="10%" />

(This is one of the definitions of the exponential function.)

### RAID

A RAID system uses multiple disks to store data in a way that protects it from loss.

Consider a RAID system that has 5 disks. Each disk has a 1% chance of failing on a given day, but the system’s data will be protected as long as no more than one failure occurs each day.

What is the chance that 2 or more disks fail on the same day and the RAID system loses data?

### I'm a Terrible Advisor

Ellen can't decide if she should take chemistry or French next
semester. She estimates her probability of getting an A in each 
course as

```
P(A | French) = 1 / 2
P(A | Chemistry) = 2 / 3   
```

She decides to flip a coin to decide which class to take. What is the
probability that she takes chemistry and then gets an A?

What is the probability that she gets an A independent of which course she takes?

### Urns I

Consider an urn filled with 4 black balls and 16 red balls.

Draw from the urn according to the following rules:

- If you draw a red ball, put it back into the urn
- If you draw a black ball, take it out, set it aside, and then continue drawing

Write down an expression for the expected number of draws needed to remove all four black balls from the urn.

### Urns II



### Urns III: Pólya Urn

Suppose an urn contains 9 black balls and 6 red balls. On each trial,
I pick a ball at random from the urn, return it to the urn, and add
in **one more ball of the same color**.

Suppose I repeat this procedure two times. What are the **expected**
numbers of red and black balls in the urn?

Tip: draw a tree of possible outcomes.


### Yer a Wizard, Harry?

Harry Pottar has received a letter from Hogwarts and he wants to
reason about the probability that he's really a wizard.

Being a wizard is extremely rare: only .01% of the population can
defy the laws of physics and reshape reality to suit their whims.

Hogwarts is very good at delivering letters, but a bunch of owls
flapping about is no substitute for a proper postal service. The
probability of a true wizard correctly receiving a Hogwarts letter
is 99%, but the probability of a non-wizard incorrectly receiving
one is 1%.

Given that he received a Hogwarts letter, what is the probability
that Harry Pottar is really a wizard?

Start by writing down the following probabilities:

```
P(Wizard) = .0001
    
P(Not a Wizard) = 
    
P(Get a Letter | Wizard) = 
    
P(Get a Letter | Not a Wizard) =
```

Now use Bayes' Rule to calculate `P(Wizard | Get a Letter)`.
