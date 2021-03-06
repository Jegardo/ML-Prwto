import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# NumPy has a method that lets us make a polynomial model:
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Then specify how the line will display, we start at position 1,
# and end at position 22:
myline = numpy.linspace(1, 22, 100)


# Predict the speed of a car that passes the tollbooth at around 17 P.M:
speed = mymodel(17)

print(speed)

# -> R-Squared <-
# It is important to know how well the relationship between the
# values of the x- and y-axis is, if there are no relationship
# the polynomial regression can not be used to predict anything.
# The relationship is measured with a value called the r-squared.
# The r-squared value ranges from 0 to 1, where 0 means no relationship,
# and 1 means 100% related.
print(r2_score(y, mymodel(x)))
# Draw the original scatter plot:
plt.scatter(x, y)
# Draw the line of polynomial regression:
plt.plot(myline, mymodel(myline))
# Display the diagram:
plt.show()
