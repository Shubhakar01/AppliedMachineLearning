import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

dataset = pd.read_csv('C:/Users/MSIS/AIML/Shubhakar/AML/data/diabetes.csv')

# 2. Select features (Columns 0 to 7: Pregnancies through Age)
x = dataset.iloc[:, 0:8].values

# 3. Select the target variable (Outcome column, index 8)
y = dataset.iloc[:, 8].values

# 4. Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=0
)

# 5. Feature Scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# 6. Train the Decision Tree Classifier
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
# classifier = DecisionTreeClassifier(criterion= 'gini',random_state=0)
classifier.fit(x_train, y_train)

# 7. Predictions and Evaluation
y_pred = classifier.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Manual accuracy calculation (works for binary classification)
accuracy = ((cm[0][0] + cm[1][1]) / (cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1]))
print("Accuracy (Manual Calculation):", accuracy)

prediction = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy (Metrics Score): {prediction * 100:.2f}%\n")

print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# 8. Predict for a new individual
# Format: [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
new_individual = np.array([[6, 148, 92, 35, 150, 33.6, 0.627, 50]])
new_individual_scaled = sc.transform(new_individual)

prediction_result = classifier.predict(new_individual_scaled)

if prediction_result[0] == 1:
    print("The individual is predicted to have diabetes (Outcome: 1)")
else:
    print("The individual is predicted not to have diabetes (Outcome: 0)")

# 9. Visualize the Decision Tree
plt.figure(figsize=(12, 8))
tree.plot_tree(classifier, 
               feature_names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                              'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'], 
               class_names=['No Diabetes', 'Diabetes'], 
               filled=True)
plt.show()