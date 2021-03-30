import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")

# To make a decision tree, all data has to be numerical.
# Pandas has a map() method that takes a dictionary
# with information on how to convert the values

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# Then we have to separate the feature columns from the
# target column.
# The feature columns are the columns that we try to predict from,
# and the target column is the column with the values we try to predict.

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

# Now we can create the actual decision tree, fit it with our details,
# and save a .png file on the computer:

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.jpg')

img = pltimg.imread('mydecisiontree.jpg')
imgplot = plt.imshow(img)
plt.show()


print(df)
print(X)
print(y)
