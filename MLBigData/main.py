import numpy
import matplotlib.pyplot as plt

randPin = numpy.random.uniform(0.0, 5.0, 100000)
# Create an array containing 100000 random floats between 0 and 5:

plt.hist(randPin, 100)
plt.show()
# We use the array from the example above to draw a histogram with 5 bars.
# The first bar represents how many values in the array are between 0 and 1.
# The second bar represents how many values are between 1 and 2
# Etc.

normPin = numpy.random.normal(5.0, 1.0, 100000)
# Create an array where the values are concentrated around a given value
# this kind of data distribution is known as the normal data distribution
# or the Gaussian data distribution
# A normal distribution graph is also known as the bell curve

plt.hist(normPin, 100)
plt.show()
