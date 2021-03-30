import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

# Independent values in a variable called X:
X = df[['Weight', 'Volume']]
# Dependent values in a variable called y:
y = df['CO2']

# The method called fit() takes the independent and dependent
# values as parameters and fills the regression object with
# data that describes the relationship:

regr = linear_model.LinearRegression()
regr.fit(X, y)

# Predict the CO2 emission of a car where the weight is 2300kg,
# and the volume is 1300cm3:

predictedCO2 = regr.predict([[2300,1300]])

print(predictedCO2)

# The coefficient is a factor that describes the relationship
# with an unknown variable
# In this case, we can ask for the coefficient value of weight against
# CO2, and for volume against CO2.
# The answers we get tells us what would happen if we increase,
# or decrease, one of the independent values.

print(regr.coef_)