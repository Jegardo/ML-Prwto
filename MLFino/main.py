import numpy
from scipy import stats
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

speed2 = [99, 86, 87, 88, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.mean(speed)
# NumPy mean() method to find the average speed

med = numpy.median(speed)
# NumPy median() method to find the middle value

med2 = numpy.median(speed2)
# NumPy median() method to find the middle value
# If there are two numbers in the middle, divide the sum of those numbers by two

y = stats.mode(speed)
# SciPy mode() method to find the number that appears the most

x1 = numpy.std(speed)
x2 = numpy.std(speed2)
# NumPy std() method to find the standard deviation
# Standard deviation is a number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.

v1 = numpy.var(speed)
v2 = numpy.var(speed2)
# NumPy var() method to find the variance
# Variance is another number that indicates how spread out the values are
# In fact, if you take the square root of the variance, you get the standard deviation!
# To calculate the variance you have to do as follows:
# 1. Find the mean
# 2. For each value: find the difference from the mean
# 3. For each difference: find the square value
# 4. The variance is the average number of these squared differences

p1 = numpy.percentile(speed, 75)
p2 = numpy.percentile(speed2, 75)
# NumPy percentile() method to find the percentiles:
# Percentiles are used in statistics to give you a number that describes
# the value that a given percent of the values are lower than

print('mean:', x)
print('median:', med)
print('median2:', med2)
print('mode:', y)
print('std:', x1)
print('std:', x2)
print('var:', v1)
print('var:', v2)
print('var(std^2):', x1*x1)
print('percentile:', p1)
print('percentile:', p2)

