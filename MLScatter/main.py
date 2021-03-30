import matplotlib.pyplot as plt
import numpy
from scipy import stats

# Graphs and Linear Regression

age = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0 , 1000)

plt.scatter(age, speed)
plt.show()

plt.scatter(x, y)
plt.show()

# The Matplotlib module has a method for drawing scatter plots,
# it needs two arrays of the same length, one for the values of
# the x-axis, and one for the values of the y-axis

slope, intercept, r, p, std_err = stats.linregress(age, speed)

# a method that returns some important key values
# of Linear Regression

# It is important to know how the relationship between
# the values of the x-axis and the values of the y-axis is,
# if there are no relationship the linear regression can not
# be used to predict anything.
# This relationship - the coefficient of correlation - is called r.
# The r value ranges from -1 to 1, where 0 means no relationship,
# and 1 (and -1) means 100% related

def myfunc(x):
    return slope * x + intercept

# A function that uses the slope and intercept values to return a new value.
# This new value represents where on the y-axis the corresponding x value will be placed

mymodel = list(map(myfunc, age))

# Run each value of the x array through the function.
# This will result in a new array with new values for the y-axis

nspeed = myfunc(10)

print(nspeed)
print(r)
plt.scatter(age, speed)
plt.plot(age, mymodel)
plt.show()
