import pandas as pd
###################################### FIRST LOAD AND EXPLORE THE DATASET ###################################### 
################################################################################################################## 

# Load the Iris dataset from sklearn
from sklearn.datasets import load_iris
import numpy as np

# Load the data into a pandas DataFrame
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display the first few rows of the dataset
print(df.head())

# Check data types and missing values
print("\nData types and missing values:")
print(df.info())

# Handle missing values (if any)
df = df.dropna()  # Alternatively, you can use df.fillna() to fill missing values

# Display the cleaned data
print("\nCleaned dataset:")
print(df.head())

#################################################### END ######################################################### 
################################################################################################################## 

###################################### NEXT DO A BASIC DATA ANALYSIS ############################################# 
################################################################################################################## 

# Basic statistics for numerical columns
print("\nBasic statistics:")
print(df.describe())

# Group by 'species' and compute mean for each group
grouped_by_species = df.groupby('species').mean()
print("\nGrouped data by species (mean):")
print(grouped_by_species)


#################################################### END ######################################################### 
##################################################################################################################

###################################### LAST DO DATA VISUALIZATION ################################################ 
################################################################################################################## 

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of the plot
sns.set(style="whitegrid")

# 1. Line Chart - Simulate time-series data (you can replace with actual time data)
plt.figure(figsize=(8, 6))
plt.plot(df['sepal length (cm)'], label="Sepal Length")
plt.title("Trend of Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart - Average sepal length per species
plt.figure(figsize=(8, 6))
df.groupby('species')['sepal length (cm)'].mean().plot(kind='bar', color='skyblue')
plt.title("Average Sepal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Sepal Length (cm)")
plt.xticks(rotation=45)
plt.show()

# 3. Histogram - Distribution of sepal length
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal length (cm)'], kde=True, color='green')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - Relationship between sepal length and petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', data=df, hue='species', palette='Set1')
plt.title("Relationship Between Sepal Length and Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()


#################################################### END ######################################################### 
##################################################################################################################
