import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# 1. Load the dataset (Replace 'Iris.csv' with your actual file path)
dataset = pd.read_csv('C:/Users/MSIS/AIML/Shubhakar/AML/data/Iris.csv')

# 2. Select features (columns 1 to 4: SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
# Note: Python uses 0-based indexing, so columns 1, 2, 3, 4 are accessed via [:, 1:5]
x = dataset.iloc[:, 1:5].values

# 3. Select the target variable (Species column, index 5)
y = dataset.iloc[:, 5].values

# 4. Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=0
)

# 5. Feature Scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# 6. Train the Decision Tree Classifier
# classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier = DecisionTreeClassifier(criterion= 'gini',random_state=0)
classifier.fit(x_train, y_train)

# 7. Predictions and Evaluation
y_pred = classifier.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

prediction_accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {prediction_accuracy * 100:.2f}%")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# 8. Predict for a new individual flower
# Format: [SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]
new_individual = np.array([[5.1, 3.5, 1.4, 0.2]])
new_individual_scaled = sc.transform(new_individual)

flower_prediction = classifier.predict(new_individual_scaled)
print(f"Predicted Species for new individual: {flower_prediction[0]}")

# 9. Visualize the Decision Tree
plt.figure(figsize=(12, 8))
tree.plot_tree(classifier, feature_names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'], 
            filled=True)
plt.show()