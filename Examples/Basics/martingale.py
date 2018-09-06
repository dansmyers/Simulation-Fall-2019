# Simulating the Martingale

# Key question: what is the distribution of outcomes produced by the
# martingale betting strategy?

# The martingale is used for games that have even-money bets with
# odds close to 50%. "Even-money" means that the player wins the
# amount of the bet. For example, if you bet $1 on black in roulette
# and win, you would keep the dollar you bet and win one additional
# dollar, for a net gain of $1.

# Strategy: 
#     - Bet $1 on the first round.
#     - If you win, you get $1. Continue to bet $1 in the next round.
#     - If you lose, double your bet to $2 on the second round. If
#       you win the second round, you'll have recovered the amount you
#       lost in the first round, plus one extra dollar. 
#     - If you lose the second round, double the bet again to $4 for
#       the third round. If you win the third round, you'll have
#       recovered all previous losses ($1 + $2) plus one extra dollar.
#
# Continue to repeat the process of doubling your bet after each loss
# until you reach a point where the bet exceeds your bankroll. In
# that case, bet as much as you can, and either win or go bankrupt.
#
# Always reset your bet to $1 after any win.
#
# Assumptions:
#     - The game is coin-flipping with a fair coin.
#     - You start with $100 and play for either 100 rounds or until
#       going bankrupt.
#     - Winnings are added back into your bankroll so they can be used
#       for bets in future rounds.

import matplotlib    # install with supo apt-get install python-matplotlib
matplotlib.use('Agg')  # Have to do this if you're running on a remote VM
from matplotlib import pyplot as plt
from random import random

def simulate(win_prob, max_rounds, bankroll):

    """ Simulate one complete game using the martingale betting
        strategy.
       
        inputs:
            win_prob: probability of winning
            max_rounds: number of rounds to play
            bankroll: starting amount of money
           
        output:
            amount of money remaining in the bankroll after
            max_rounds, or 0 if the player goes bankrupt early
    """
    
    bet = 1  # Initial bet
    
    for round in range(max_rounds):
        if random() > win_prob:
            bankroll -= bet
            bet = min(2 * bet, bankroll)  # Double or bet it all
        else:
            bankroll += bet
            bet = 1
            
        if bankroll == 0:
            break
            
    return bankroll
    
    
def main():
    
    """ Simulate the martingale betting strategy.
    
        inputs: none
        outputs: none (plots results as a histogram)
    """ 
    
    # Parameters
    simulation_iterations = 1000000  # Num. simulated trials to run
    win_prob = .50  # Prob. of winning each game round
    max_rounds = 100  # Max number of rounds for one sim
    start_bankroll = 100  # Player's starting cash

    # Store results in a list
    results = []
    
    # Iterate, performing a number of simulated trials
    # Record the results of each trial
    for iteration in range(simulation_iterations):
        results.append(simulate(win_prob, max_rounds, start_bankroll))
        
    # Visualize results
    plt.figure()  # Make a new figure
    plt.hist(results, 50)  # Histogram
    plt.savefig('martingale_hist.pdf', bbox_inches='tight')
    
    # plt.show() displays figure on a regular computer
    
    
# Standard way of accessing a main method in Python
#
# __name__ is an internal variable that keeps track of how the script
# runs. If it's '__main__', the script is running as the main script
# and the main method runs.
#
# This is commonly used when writing modules that might be imported
# by another script. The main() method can include testing code for
# the module's functions, but only runs if the module is directly
# invoked at the command line, and won't run if it's imported by
# another script.
if __name__ == '__main__':
    main()
    
       
       
