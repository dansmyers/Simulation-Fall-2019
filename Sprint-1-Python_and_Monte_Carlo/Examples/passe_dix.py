# Estimate the odds of winning the passe-dix gambling game.

from random import random

def simulate():

    """ Simulate one game of passe-dix
    
        Generate three die rolls and test if sum > 10
    
        returns: True if the player wins
                 False otherwise
    """
    
    # Use randint to generate integers in an INCLUSIVE range
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    
    if die1 + die2 + die3 > 10:
        return True
    else:
        return False
        
def main():
    
    """ Run several simulated passe-dix games and report the fraction of successess """

    successes = 0
    num_trials = 1000
    
    for trial in range(num_trials):
        if simulate():
            successes += 1
            
    # Use float() to cast to a non-integer value
    print(successes / float(num_trials))
    
if __name__ == '__main__':
    main()
