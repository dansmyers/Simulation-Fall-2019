#--- Estimating pi using Monte Carlo simulation
#
# The method is described at this link:
#
# https://academo.org/demos/estimating-pi-monte-carlo/

from random import random
        
def main():
    
    """ Monte Carlo approach to estimating pi
    
        inputs: none
        outputs: prints the estimate of pi
    """ 
    
    # Parameters
    num_points = 100000000
    num_in_circle = 0
    
    for point in range(num_points):
        x = random()
        y = random()
        
        # Distance from origin
        distance = (x ** 2 + y ** 2) ** .5
        
        # If the point is within the circle's radius, count it as
        # a hit
        if distance < 1:
            num_in_circle += 1
            
    fraction = float(num_in_circle) / float(num_points)
    
    # pi is approximately fraction * 4
    print 'pi ~ %f' % (fraction * 4)
    
    
# Run main() if this program is running from the terminal
if __name__ == '__main__':
    main()
