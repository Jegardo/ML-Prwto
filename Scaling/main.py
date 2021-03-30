import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']
# The standardization method uses this formula:
# z = (x - u) / s
# Where z is the new value, x is the original value,
# u is the mean and s is the standard deviation.

regr = linear_model.LinearRegression()
scaledX = scale.fit_transform(X)
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1300]])

predictedCO2 = regr.predict([scaled[0]])

print(predictedCO2)
