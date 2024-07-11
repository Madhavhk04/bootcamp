# Import necessary libraries for visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Plot histogram for a numerical column
plt.figure(figsize=(10, 6))
sns.histplot(dd['actual_distance_to_destination'], bins=50, kde=True)
plt.xlabel('Actual Distance to Destination')
plt.ylabel('Frequency')
plt.title('Distribution of Actual Distance to Destination')
plt.show()

# Plot box plot for a numerical column
plt.figure(figsize=(10, 6))
sns.boxplot(x=dd['actual_distance_to_destination'])
plt.xlabel('Actual Distance to Destination')
plt.title('Box Plot of Actual Distance to Destination')
plt.show()

# Plot scatter plot for two numerical columns
plt.figure(figsize=(10, 6))
sns.scatterplot(x=dd['actual_distance_to_destination'], y=dd['actual_time'])
plt.xlabel('Actual Distance to Destination')
plt.ylabel('Actual Time')
plt.title('Scatter Plot of Actual Distance vs. Actual Time')
plt.show()

# Visual check of nulls with a heatmap
plt.figure(figsize=(25, 8))
plt.style.use('dark_background')
sns.heatmap(dd.isnull().T, cmap='Greys')
plt.title('Visual Check of Nulls', fontsize=20, color='r')
plt.show()
