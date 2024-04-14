#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Import the required libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load data from csv file
data = pd.read_csv('/Users/mason/Desktop/Datasets/Portfolio/Project #3/Customer-Satisfaction.csv')

# Data cleaning and preprocessing

# Get the number of rows before dropping
num_rows_before = data.shape[0]

# Data cleaning: Drop rows with missing values
data.dropna(inplace=True)

# Get the number of rows after dropping
num_rows_after = data.shape[0]

# Calculate the number of rows dropped
num_rows_dropped = num_rows_before - num_rows_after

# Print the chane in data
print("Number of rows originally:", num_rows_before)
print("Number of rows dropped:", num_rows_dropped)
print("Number of rows remaining:", num_rows_after)

# Identify the unnamed ID column (usually the first column, index 0)
unnamed_id_column = data.columns[0]  # Assuming the ID column is the first column

# Drop the unnamed and named ID column from the DataFrame
data.drop(columns=[unnamed_id_column], inplace=True)

data.drop(columns=['id'], inplace=True)  # Drop unnecessary column 'id'

# Encode categorical columns
label_encoders = {}
categorical_columns = ['Gender', 'Customer Type', 'Type of Travel', 'Class']
for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le


# Split data into features (X) and target variable (y)
X = data.drop(columns=['satisfaction'])
y = data['satisfaction']

# Normalize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Generate classification report
report = classification_report(y_test, y_pred, output_dict=True)
df_report = pd.DataFrame(report).transpose()

# Plotting First Chart
plt.figure(figsize=(10, 5))
sns.heatmap(df_report.iloc[:-1, :-1], annot=True, cmap="YlGnBu", fmt=".2f")
plt.title('Classification Report')
plt.show()

# Get feature importances
feature_importances = clf.feature_importances_

# Sort feature importances in descending order
sorted_indices = np.argsort(feature_importances)[::-1]

# Plot feature importances
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances[sorted_indices], y=X.columns[sorted_indices], palette='viridis')
plt.xlabel('Feature Importance')
plt.ylabel('Features')
plt.title('Feature Importance')
plt.show()


# In[ ]:




