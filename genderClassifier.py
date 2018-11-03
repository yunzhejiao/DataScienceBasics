from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Perceptron
import numpy as np

# Data set:
# X: height, weight, shoe size
# Y: gender
X = [[181,80,44],[160,60,38],[181,70,44],[181,70,40],
	[161,60,38],[167,70,45],[177,70,44],[155,70,36]]

Y = ['male', 'female', 'male', 'female',
	'female', 'male', 'male', 'female']

# Three classifiers
clf_tree = tree.DecisionTreeClassifier()
clf_knn = KNeighborsClassifier()
clf_linear = Perceptron()

# Train models
clf_tree = clf_tree.fit(X,Y)
clf_knn = clf_knn.fit(X,Y)
clf_linear = clf_linear.fit(X,Y)

# prediction
_X=[[184,84,44],[198,92,48],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
_Y=['male','male','male','female','female','female','male','male']

prediction_tree = clf_tree.predict(_X)
prediction_knn = clf_knn.predict(_X)
prediction_linear = clf_linear.predict(_X)

# accuracy scores
acc_tree = accuracy_score(_Y, prediction_tree)
acc_knn = accuracy_score(_Y, prediction_knn)
acc_linear = accuracy_score(_Y, prediction_linear)
print ('Accuracy for decision tree: {}'.format(acc_tree))
print ('Accuracy for KNN: {}'.format(acc_knn))
print ('Accuracy for perceptron: {}'.format(acc_linear))

# choose winner of best gender classifier!
index = np.argmax([acc_tree, acc_knn, acc_linear])
clfs = {0: 'decision tree', 1: 'KNN', 2: 'perceptron'}
print('Best gender classifier is {}'.format(clfs[index]))


