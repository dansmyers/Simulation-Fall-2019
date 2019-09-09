# Plot example histogram using matplotlib

# Import matplotlib and configure it to save files in the web IDE
import matplotlib
matplotlib.use('Agg')  # <-- Required if you're using matplotilb in Mimir, see below
from matplotlib import pyplot as plt

# Example data
data = [10, 12, 15, 25, 4, 8, 11, 64, 100]

# Create a new figure
plt.figure()

# Histogram of the example data
plt.hist(data, 15)

# Title and axis labels
plt.title('Example Histogram')
plt.xlabel('Data value')
plt.ylabel('Count')

# Save the figure to a file
plt.savefig('example_histogram.pdf', bbox_inches='tight')
