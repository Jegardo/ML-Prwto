import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Train/Test is a method to measure the accuracy of your model.
# It is called Train/Test because you split the the data set into
# two sets: a training set and a testing set.
# Train the model means create the model.
# Test the model means test the accuracy of the model.

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# Split Into Train/Test
# The training set should be a random selection of 80% of the
# original data.
# The testing set should be the remaining 20%.

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0, 6, 100)
r2 = r2_score(train_y, mymodel(train_x))

mymodeltest = numpy.poly1d(numpy.polyfit(test_x, test_y, 4))
r2test = r2_score(test_y, mymodeltest(test_x))

print(r2test)
print(r2)
print(mymodeltest(5))
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

plt.scatter(test_x, test_y)
plt.show()
