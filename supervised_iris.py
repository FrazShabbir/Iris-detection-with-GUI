#from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier 

plt.style.use("ggplot")
iris = pd.read_csv("iris.csv")
df= pd.DataFrame(iris)
#print(df)
y = df['species'].values
X = df.drop('species', axis=1).values

# Create a k-NN classifier with 6 neighbors: knn
knn = knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X,y)

# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new=[]
X_new=[new]
for i in range(0,4):
    value = input(str(i+1) +" Value ")
    new.append(value)

new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))






# Import necessary modules
#from sklearn import datasets
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.model_selection import train_test_split

#digits = datasets.load_digits()

# Create feature and target arrays
# = digits.data
#y = digits.target

# Split into training and test set
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)

# Create a k-NN classifier with 7 neighbors: knn
#knn = KNeighborsClassifier(n_neighbors=7)

# Fit the classifier to the training data
#knn.fit(X_train, y_train)

# Print the accuracy
#print(knn.score(X_test, y_test))
