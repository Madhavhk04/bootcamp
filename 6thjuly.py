import pandas as pd

# Load the data from the CSV file
file_path = r'C:\Users\devua\OneDrive\Desktop\MADHAV/delhivery_data.csv'
data = pd.read_csv(file_path)

# Display basic information about the data
print(data.info())
print(data.describe(include='all'))
print(data.head())

# Identify missing values
missing_values = data.isnull().sum()
print(missing_values[missing_values > 0])

# Fill missing values with the most frequent value (mode)
data['source_name'].fillna(data['source_name'].mode()[0], inplace=True)
data['destination_name'].fillna(data['destination_name'].mode()[0], inplace=True)

# Verify that there are no missing values
missing_values_after_fill = data.isnull().sum().sum()
print(missing_values_after_fill)

def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

# Detect outliers for each numerical column
outliers = {column: detect_outliers(data, column) for column in data.select_dtypes(include=['float64', 'int64']).columns}

# Print the number of outliers for each column
for column, outlier_df in outliers.items():
    print(f'{column}: {len(outlier_df)} outliers')


def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Remove outliers for each numerical column
for column in data.select_dtypes(include=['float64', 'int64']).columns:
    data = remove_outliers(data, column)

# Verify the data after outlier removal
print(data.describe(include='all'))

import matplotlib.pyplot as plt

# Plot histogram for a numerical column
data['actual_distance_to_destination'].hist(bins=50)
plt.xlabel('Actual Distance to Destination')
plt.ylabel('Frequency')
plt.title('Distribution of Actual Distance to Destination')
plt.show()

# Plot box plot for a numerical column
data.boxplot(column='actual_distance_to_destination')
plt.xlabel('Actual Distance to Destination')
plt.title('Box Plot of Actual Distance to Destination')
plt.show()

# Plot scatter plot for two numerical columns
data.plot.scatter(x='actual_distance_to_destination', y='actual_time')
plt.xlabel('Actual Distance to Destination')
plt.ylabel('Actual Time')
plt.title('Scatter Plot of Actual Distance vs. Actual Time')
plt.show()
