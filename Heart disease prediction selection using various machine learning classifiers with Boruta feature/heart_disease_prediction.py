# -*- coding: utf-8 -*-
"""Heart Disease Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ejdOIPPQTnqpuEfLwFE84g_po9CIj_mz

## **Heart Disease Prediction**

## Importing the libraries
"""

import pandas as pd
import seaborn as sb
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
import xgboost as xgb
from boruta import BorutaPy
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.metrics import precision_score, recall_score, f1_score, cohen_kappa_score

"""## Importing the dataset"""

dataset = pd.read_csv('Dataset/heart.csv')
dataset.head()

dataset.isnull().sum()

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(x)
print(y)

"""## WITHOUT FEATURE SELECTION

### Random Forest
"""

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train the random forest classifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rfc.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy-Random forest classifier: %0.4f" %(accuracy))

"""#### Performance metrics"""

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion Matrix"""

# The true and predicted labels are stored in y_true and y_pred respectively
cm = confusion_matrix(y_test, y_pred)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for Random Forest")

# Show the plot
plt.show()

"""#### ROC curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='Random Forest (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

"""### Decision Tree"""

# Initialize an empty list to store the model's performance scores
scores_dt = []

# Train/test the model once without cross-validation
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train the decision tree classifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# Evaluate the model's performance on the test set
y_pred = dt.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy-Decision tree: %0.4f" %(accuracy))

"""#### Performance metrics"""

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion Matrix"""

# The true and predicted labels are stored in y_true and y_pred respectively
cm = confusion_matrix(y_test, y_pred)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for Decision Tree")

# Show the plot
plt.show()

"""#### ROC curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='Decision Tree (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for Decision Tree')
plt.show()

"""### Logistic Regression"""

# Initialize an empty list to store the model's performance scores
scores_lr = []

# # Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train the logistic regression model
lr = LogisticRegression(max_iter=5000, random_state=42)
lr.fit(X_train, y_train)

# Evaluate the model's performance on the test set
y_pred = lr.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy-Logistic regression classifier: %0.4f" %(accuracy))

"""#### Performance metrics"""

from sklearn.metrics import precision_score, recall_score, f1_score, cohen_kappa_score

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion matrix"""

cm = confusion_matrix(y_test, y_pred)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for Logistic Regression")

# Show the plot
plt.show()

"""#### ROC Curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='Random Forest (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for Logistic Regression')
plt.show()

"""### KNN"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# # Split the data into training and testing sets
 X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train the k-NN classifier with k=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict on the test set
y_pred = knn.predict(X_test)

# Compute accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Accuracy for k-NN: %0.4f" % accuracy)

"""#### Performance metrics"""

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion matrix"""

# The true and predicted labels are stored in y_true and y_pred respectively
cm = confusion_matrix(y_test, y_pred)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for K - NN")

# Show the plot
plt.show()

"""#### ROC curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='K - NN (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for k - NN')
plt.show()

"""### SVM"""

svm_b = SVC(kernel='linear', random_state=42, probability=True)

svm_b.fit(X_train, y_train)

y_pred = svm_b.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy of Logistic Regression with Boruta Feature selection: %0.4f" % accuracy)

"""#### Performance metrics"""

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion matrix"""

# The true and predicted labels are stored in y_true and y_pred respectively
cm = confusion_matrix(y_test, y_pred)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for SVM")

# Show the plot
plt.show()

"""#### ROC curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='K - NN (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for SVM')
plt.show()

"""### Naive Bayesian"""

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
nb= GaussianNB()
nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy of Naive - bayesian with Boruta Feature selection: %0.4f" % accuracy)

"""#### Performance metrics"""

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion matrix"""

# The true and predicted labels are stored in y_true and y_pred respectively
cm = confusion_matrix(y_test, y_pred)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for NB")

# Show the plot
plt.show()

"""#### ROC curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='K - NN (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for NB')
plt.show()

"""### Voting Ensemble"""

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier

# Initialize the models
rf = RandomForestClassifier(n_estimators=50)
dt = DecisionTreeClassifier(random_state=42)
ada = AdaBoostClassifier(estimator=dt, n_estimators=100)

# Fit the models to the entire dataset
rf.fit(x, y)
dt.fit(x, y)
ada.fit(x, y)

# Combine the models into a voting classifier
ensemble = VotingClassifier(estimators=[('rf', rf), ('ada', ada)], voting='hard')

# Fit the ensemble model to the entire dataset
ensemble.fit(x, y)

# Make predictions on the entire dataset
y_pred = ensemble.predict(x)

# Calculate the accuracy score
score = accuracy_score(y, y_pred)

# Print the result
print("AdaBoost Ensemble accuracy: %0.4f" % score)

"""### XGBoost"""

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=42)

# Define the XGBoost classifier
clf = xgb.XGBClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

"""### AdaBoosting"""

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Define the AdaBoost classifier
clf = AdaBoostClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

"""## Boruta feature selection"""

pip install boruta

# Define the random forest classifier
rf = RandomForestClassifier(n_estimators=100, n_jobs=-1)

# Define the Boruta feature selection method
boruta = BorutaPy(rf, n_estimators='auto', verbose=2)

# Perform feature selection
boruta.fit(x, y)

# Get the selected features
selected_features = dataset.columns[:-1][boruta.support_].tolist()[:6]
print("Selected features:", selected_features)

# Use selected features with your classifier
x_selected = dataset[selected_features]

# # Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(x_selected, y, test_size=0.2, random_state=42)

"""### Random forest"""

X_train, X_test, y_train, y_test = train_test_split(x_selected, y, test_size=0.2, random_state=42)

# Create and train the random forest classifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rfc.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy-Random forest classifier: %0.4f" %(accuracy))

"""#### Performance metrics"""

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion matrix"""

cm = confusion_matrix(y_pred,y_test)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for Random Forest")
plt.show()

"""#### ROC curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='Random Forest (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

"""### Decision tree"""

# Initialize an empty list to store the model's performance scores
scores_dt = []

# Train/test the model once without cross-validation
X_train, X_test, y_train, y_test = train_test_split(x_selected, y, test_size=0.2, random_state=42)

# Train the decision tree classifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# Evaluate the model's performance on the test set
y_pred = dt.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy-Random forest classifier: %0.4f" %(accuracy))

"""#### Performance metrics"""

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion matrix"""

cm = confusion_matrix(y_pred,y_test)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for Decision Tree")
plt.show()

"""#### ROC curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='Random Forest (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

# Initialize an empty list to store the model's performance scores
scores_lr = []

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x_selected, y, test_size=0.25, random_state=42)

# Train the logistic regression model
lr = LogisticRegression(max_iter=5000, random_state=42)
lr.fit(X_train, y_train)

# Evaluate the model's performance on the test set
y_pred = lr.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy-Logisitic regression: %0.4f" %(accuracy))

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

cm = confusion_matrix(y_pred,y_test)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for Logistic regression")
plt.show()

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='Random Forest (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

"""### KNN"""

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x_selected, y, test_size=0.2, random_state=42)

# Train the k-NN classifier with k=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict on the test set
y_pred = knn.predict(X_test)

# Compute accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Accuracy for k-NN: %0.4f" % accuracy)

"""#### Performance metrics"""

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion matrix"""

cm = confusion_matrix(y_pred,y_test)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for Logistic regression")
plt.show()

"""#### ROC curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='Random Forest (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

"""### SVM"""

svm_b = SVC(kernel='linear', random_state=42, probability=True)

svm_b.fit(X_train, y_train)

y_pred = svm_b.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy of Logistic Regression with Boruta Feature selection: %0.4f" % accuracy)

"""#### Performance metrics"""

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion matrix"""

cm = confusion_matrix(y_pred,y_test)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for SVM")
plt.show()

"""#### ROC curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='Random Forest (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

"""### Logistic Regression"""

# Initialize an empty list to store the model's performance scores
scores_lr = []

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x_selected, y, test_size=0.25, random_state=42)

# Train the logistic regression model
lr = LogisticRegression(max_iter=5000, random_state=42)
lr.fit(X_train, y_train)

# Evaluate the model's performance on the test set
y_pred = lr.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy-Logisitic regression: %0.4f" %(accuracy))

"""#### Performance metrics"""

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion matrix"""

cm = confusion_matrix(y_pred,y_test)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for Logistic regression")
plt.show()

"""#### ROC curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='Random Forest (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

"""###Naive Bayesian"""

nb= GaussianNB()
nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy of Naive - bayesian with Boruta Feature selection: %0.4f" % accuracy)

"""#### Performance metrics"""

# Calculate precision
precision = precision_score(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

# Calculate Cohen's kappa
kappa = cohen_kappa_score(y_test, y_pred)

print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

"""#### Confusion matrix"""

cm = confusion_matrix(y_pred,y_test)

# Heatmap of the confusion matrix using Seaborn
sb.heatmap(cm, annot=True, cmap="Blues", fmt = 'd')

# Add axis labels and a title
plt.xlabel("Predicted labels")
plt.ylabel("True labels")
plt.title("Confusion Matrix for NB")
plt.show()

"""#### ROC curve"""

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

# plot ROC curve
plt.plot(fpr, tpr, label='Random Forest (AUC = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], linestyle='--')  # plot random curve
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

"""### Voting Ensemble"""

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier

# Initialize the models
rf = RandomForestClassifier(n_estimators=50)
dt = DecisionTreeClassifier(random_state=42)
ada = AdaBoostClassifier(estimator=dt, n_estimators=100)

# Fit the models to the entire dataset
rf.fit(x, y)
dt.fit(x, y)
ada.fit(x, y)

# Combine the models into a voting classifier
ensemble = VotingClassifier(estimators=[('rf', rf), ('ada', ada)], voting='hard')

# Fit the ensemble model to the entire dataset
ensemble.fit(x, y)

# Make predictions on the entire dataset
y_pred = ensemble.predict(x)

# Calculate the accuracy score
score = accuracy_score(y, y_pred)

# Print the result
print("AdaBoost Ensemble accuracy: %0.4f" % score)

"""### XGBoost"""

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=42)

# Define the XGBoost classifier
clf = xgb.XGBClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

"""### AdaBoosting"""

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Define the AdaBoost classifier
clf = AdaBoostClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))