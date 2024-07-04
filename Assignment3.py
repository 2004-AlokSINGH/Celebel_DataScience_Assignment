import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# Display the first few rows of the dataset
print(iris.head())

# Basic statistics
print(iris.describe())

# Pairplot to show relationships between variables
sns.pairplot(iris, hue="species")
plt.show()

# Boxplot to show the distribution of values
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris)
plt.show()

# Heatmap to show correlations
plt.figure(figsize=(10, 6))
sns.heatmap(iris.corr(), annot=True, cmap='coolwarm')
plt.show()

# Histograms for each feature
iris.hist(edgecolor='black', linewidth=1.2, figsize=(12, 8))
plt.suptitle("Histograms of Iris Dataset Features")
plt.show()

# KDE plots for each feature
plt.figure(figsize=(12, 8))
for column in iris.columns[:-1]:
    sns.kdeplot(iris[column], shade=True, label=column)
plt.title("KDE Plots of Iris Dataset Features")
plt.legend()
plt.show()

# Bar plot to show the average measurements per species
plt.figure(figsize=(10, 6))
iris.groupby('species').mean().plot(kind='bar')
plt.title("Average Measurements per Species")
plt.ylabel("Measurement (cm)")
plt.xticks(rotation=0)
plt.show()

# Violin plots to show the distribution of measurements per species
plt.figure(figsize=(12, 8))
for column in iris.columns[:-1]:
    plt.figure()
    sns.violinplot(x='species', y=column, data=iris)
    plt.title(f"Violin Plot of {column} by Species")
    plt.show()

# PairGrid for more detailed relationships
g = sns.PairGrid(iris, hue="species")
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot, cmap="Blues_d")
g.map_diag(sns.histplot, kde=True)
g.add_legend()
plt.show()
