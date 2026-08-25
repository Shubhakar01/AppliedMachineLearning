# Purchase based on Features(Age and Salary)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn import tree
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/MSIS/AIML/Shubhakar/AML/data/Social_Network_Ads.csv')
dataset = data
x = dataset.iloc[:, 2:4].values
y = dataset.iloc[:, 4].values

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=0
)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier = DecisionTreeClassifier(criterion= 'entropy',random_state=0)
# classifier = DecisionTreeClassifier(criterion= 'gini',random_state=0)
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)
# print("Prediction\n",y_pred)
# print("Actual\n",y_test)

cm = confusion_matrix(y_test,y_pred)
# print("Confusion Matrix\n",cm)

accuracy =  ((cm[0][0]+cm[1][1])/(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1]))
# print("Accuracy\n",accuracy)

prediction = metrics.accuracy_score(y_test,y_pred)
# print("Accuracy:",prediction*100,"%")

print(classification_report(y_test,y_pred))

new_individual = np.array([[29,80000]])
new_individual_scaled = sc.transform(new_individual)

prediction = classifier.predict(new_individual_scaled)

if prediction[0] == 1:
    print("The individual is predicted to purchase")
else:
    print("Individual is predicted not to purchase")

plt.figure(figsize=(12, 8))
tree.plot_tree(classifier)
plt.show()
