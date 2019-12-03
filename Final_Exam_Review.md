# Final Exam Review

## Directions

The following questions are the material for the final exam. I will choose approximately twelve of them as the content for the exam.

The questions on the exam will appear exactly as they do in this document. There will be no questions that are not in this review.

No notes, books, or other aids are allowed during the exam. I will give you a formula sheet with the following:

- Bayes' Rule
- M/G/1 queue length equation
- Little's Law and the Utilization Law
- PMFs of the binomial and geometric distributions
- PDF and CDF of the exponential distribution

## Discrete Probability Distributions

### Binomial vs. Geometric
Describe a situation that would be best modeled with a binomial distribution and a situation that would be best modeled with a geometric
distribution.

### Jolly Roving Tar
Daniel Myers has received an acceptance letter from Rollins College and he wants to reason about the probability that he will become
Tommy the Tar.
	
Becoming Tommy the Tar is extremely rare: only .0001% of the United States population has been Tommy the Tar. 

While Rollins College is very quick to send out acceptance letters, the United States 
Postal Service is not a very reliable way of sending out letters in this modern age. The 
probability of a true Tommy the Tar replacement receiving an acceptance letter is 2%, 
but the probability of a random United States citizen receiving the acceptance letter is 
37%.

Given that he received a Rollins College acceptance letter, what is the probability that Daniel Myers will be the new Tommy the Tar?

Hint:

P(Letter) = .37

### Urns of War

In an ancient land, the Emperor would select a random ball out of a magical urn: every time the Emperor picked out a ball, 2 random balls disappear and 3 new ones appear.

The Urn contains 10 Red balls and 13 black balls when he begins.

Suppose the Emperor uses the urn to decide whether to enter a battle, attacking if the SECOND ball he picks is a red ball and retreating 
if the SECOND ball is black.

What is the probability that the Emperor attacks?

Hint:

The changes to the urn happen in the following order:

1. Draw one ball.
2. Randomly remove two more balls.
3. Randomly add three balls

### He Sees You When You're Sleeping

For the generic day of festive gift-giving, you would really like to get a **BlackWidow Wired Gaming Mechanical Green Switch Keyboard with RGB Back Lighting**.

The probability of you getting this keyboard (what with the frenzy of gamers scrambling to buy it) is 83%. The probability of being nice given that you get the keyboard is 96%. The probability that you are nice even if you don't get the keyboard is 13%. 

What is the probability of getting the keyboard given that you are nice?

### Defects

We built a robot that can detect defective items produced in our factory. 

- If an item is defective, it is spotted with 98% probability by the robot. 
- When an item is not defective, the robot has a 1% chance of making a false positive. 

We draw an item at random from a production lot in which 0.1% of items are defective.  If the robot tells us that the drawn item is 
defective, what is the probability that the robot is right? 

In probabilistic terms, what we know about this problem can be formalized as follows:

P(Robot says defective | defective) = 0.98
P(Robot says defective | not defective) = 0.01
P(defective) = 0.001

What is P(defective | Robot says defective)?

### Frog

Harmoine is still trying to collect all of her Chocolate Frog cards. She only needs two more out of the set of thirty: Hermes 
Trismegistus and David Blaine.

Suppose Hermoine buys 10 Chocolate Frogs and opens them all at the same time. What's the probability that she gets exactly one
of the cards she hasn't seen before?

### Survival of the Brightest

A generic bulb with an expected exponentially-distributed lifetime of 200 hours. What is the probability of the bulb
surviving between 40 hours and 60 hours?

### I Can't Remember

Suppose that a bulb with an expected exponentially-distributed lifetime has already been burning for 100 hours. What's the probability
the bulb survives for more than 300 hours?

### Elves

To keep Santa’s workshop efficient, toy-making is divided between multiple elves. Assume that this has been done in a way so that each toy is made by only one elf, and the load on the elves is balanced.

Santa wants 10,000 Rubik’s cubes made in a day. There are three available kinds of elves willing to do that job:
- A newbie elf, who will work for $70 and can make 100 cubes in a day
- A senior elf, who will work for $235 (specifically) and can make 500 cubes in a day
- A special hybrid elf-human, who will work for $300 and can make 1000 cubes in a day

For each of the three options, how many elves would Santa need to hire to make 10,000 cubes in a day? If Santa only wants to hire one kind of elf, what is the most cost-effective elf that meets the workshop’s requirements?


### Erlang Variates

The Erlang-*k* distribution is created by adding *k* independent and identically distributed exponential random variables.

Write a Python method that can generate Erlang-*k* random variables. The inputs are *k* and *µ*, the rate parameter of the underlying exponential distribution.


### LCPRNG

Find a set of parameters for a linear-congruential random number generator that achieves a full period of 8.

Tip:

*Full period of 8* means that the generator must cycle through all of the values 0-7, in some order, before repeating.

### PageRank

Explain, in your own words, how the original PageRank algorithm ranks web pages.


### Even Empresses Have to Wait in Line

We have a store that sells magical urn for emperors and empresses who like war. There are two queues in the store.

One is for emperors and it has an average service time of 5 seconds. The second queue is for empresses and it has an average service time of 10 seconds. Service times are exponentially distributed.

The total arrival rate to the store is 3 customers per minute. If 60% of the clients are empresses, what is the average residence time
of an arbitrary empress?


### Derive

Use the tagged customer method to derive the expected residence time in an M/D/1 queue.

### LCFSPR

Recall the last-come-first-serve-preemptive-resume strategy: a newly arriving customer gets to enter service immediately, preempting any
customer that's currently in service.

Customers are served in last-come-first-serve order, and a preempted customer always resumes its service at the place it left off.

Derive the expected residence time in the LCFSPR queue with Poisson arrivals.

### M/E<sub>*k*</sub>/1

The Erlang-*k* distribution has squared coefficient of variation 1 / *k*.

What is the residence time in an M/E<sub>*5*</sub>/1 queue average service time 10 seconds and 80% utilization?

### Cruise Elroy

In the grimdark Pac-Man universe, ghosts are bound to servitude in a maze filled with tiny balls and bouncing fruits.

Every ghost arriving to the Netherworld must first be judged by Plinky, the fuschia ghost. Ghosts then go to one of the two Pac-mazes.

Ghosts arrive to be judged at a rate of two per day. The following paramters apply:

- Netherworld: s = .60 sec, Cs^2 = 1.0
- Pac-World 1: s = .30 sec, Cs^2 = .45
- Pac-World 2: s = .25 sec, Cs^2 = 1.2

Haunting each world is random:
-fraction of light ghosts haunting Pac-World 1 = .25
-fraction of dark ghosts haunting Pac-World 2 = .75
