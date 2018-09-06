#--- Estimating pi using Monte Carlo simulation

from random import random
        
def main():
    
    """ Monte Carlo approach to estimating pi
    
        inputs: none
        outputs: prints the estimate of pi
    """ 
    
    # Parameters
    num_points = 10000000000
    num_in_circle = 0
    
    for point in range(num_points):
        x = random()
        y = random()
        
        # Distance from origin
        distance = (x ** 2 + y ** 2) ** .5
        
        if distance < 1:
            num_in_circle += 1
            
    fraction = float(num_in_circle) / float(num_points)
    
    print 'pi ~ %f' % (fraction * 4)
    
    
# Run main() if this program is running from the terminal
if __name__ == '__main__':
    main()
