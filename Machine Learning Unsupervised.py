#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans

# Access the dataset through the pandas read function.
data = pd.read_excel('#ENTER PATHFILE HERE')

#Print the original shape of the data.
print('Original Data Rows:',data.shape[0])
print()

#Create a variable for categorical columns and an empty distinct value dictionary.
categorical_columns = ['fuel', 'seller_type', 'transmission','owner']
    
value_counts_dict = {}

# Calculate value counts for each column and their unique values.
for column in categorical_columns:
    value_counts_dict[column] = data[column].value_counts()

# Print value counts for each column.
for column, counts in value_counts_dict.items():
    print(f"Value counts for {column}:")
    print(counts)
    print()

# Drop all of the rows with smaller amount of categorical values.
data.drop(data[data['fuel'] == 'CNG'].index, inplace=True)
data.drop(data[data['fuel'] == 'LPG'].index, inplace=True)
data.drop(data[data['owner'] == 'Fourth & Above Owner'].index, inplace=True)
data.drop(data[data['owner'] == 'Test Drive Car'].index, inplace=True)

# Drop columns with values I do not want.
data.drop('name', axis=1, inplace=True)

# Drop all missing values.
data.dropna(inplace=True)

# Print the shape of the clean data.
print('Cleaned Data:',data.shape[0])


# Encode categorical columns.
label_encoders = {}
categorical_columns = ['fuel', 'seller_type', 'transmission', 'owner']
for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Normalize the Data.
scaler = StandardScaler()

data[['year_T','selling_price_T','km_driven_T','fuel_T','seller_type_T','transmission_T','owner_T','mileage(km/ltr/kg)_T','engine_T','max_power_T','seats_T']] = scaler.fit_transform(data[['year','selling_price','km_driven','fuel','seller_type','transmission','owner','mileage(km/ltr/kg)','engine','max_power','seats']])

scaled_features = ['year_T', 'selling_price_T', 'km_driven_T', 'fuel_T', 'seller_type_T', 'transmission_T', 'owner_T', 'mileage(km/ltr/kg)_T', 'engine_T', 'max_power_T', 'seats_T']

# Further normalizing the data getting rid of any outliers.
for feature in scaled_features:
    data[feature] = np.clip(data[feature], -3, 3)

# Create a function for making the elbow graph.
def optimise_k_means(data, max_k):
    means=[]
    inertias=[]
    
    # Using max k input get values for the elbow graph
    for k in range(1, max_k):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(data)
        
        means.append(k)
        inertias.append(kmeans.inertia_)
    
    # Plot the Elbow Graph
    fig = plt.subplots(figsize=(10,5))
    plt.plot(means,inertias, 'o-')
    plt.xlabel('Number of Clusters')
    plt.xlabel('Interia')
    plt.title('Elbow Method Showing Ideal K')
    plt.grid(True)
    plt.show()
    
def plot_kmeans_clusters(data, features, n_clusters):
    # Apply K-means clustering to your dataset using specified features and clusters number.
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data[features])
    data['cluster'] = kmeans.labels_
    
    # Plot the clustering model.
    plt.figure(figsize=(8, 6))
    plt.scatter(data[features[0]], data[features[1]], c=data['cluster'], cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='*', label='Centroids')
    plt.xlabel(features[0])
    plt.ylabel(features[1])
    plt.title(f'K-Means Clustering with {n_clusters} clusters')
    plt.legend()
    plt.show()

# Usage:

# Use optimise_k_means to determine optimal number of clusters to show the visualization of the elbow graph
optimise_k_means(data[['selling_price_T', 'km_driven_T']], 10)

# Use plot_kmeans_clusters with desired number of clusters to show the visualization of the clustering
plot_kmeans_clusters(data, ['selling_price_T', 'km_driven_T'], n_clusters=3)


# In[ ]:




