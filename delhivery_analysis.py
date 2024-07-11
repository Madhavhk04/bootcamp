import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from scipy.stats import norm, zscore, boxcox, probplot
from scipy.stats import ttest_ind, ttest_rel, mannwhitneyu, wilcoxon
from scipy.stats import shapiro, levene, kstest, anderson
import statsmodels.api as sm
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
import warnings

warnings.filterwarnings('ignore')

# Load the dataset
file_path = r'C:\Users\devua\OneDrive\Desktop\MADHAV\delhivery_data.csv'  # Update this path to your CSV file
delhivery_data = pd.read_csv(file_path)

# Display all columns
pd.set_option('display.max_columns', 50)

# Make a deep copy of the data for backup
dd = delhivery_data.copy()

# Display the first few rows of the dataset
print(dd.head())

# Display the shape of the dataset
print(dd.shape)

# Display column names
print(dd.columns)

# Display basic information about the dataset
print(dd.info())

# Display summary statistics for numerical columns
print(dd.describe().T)

# Display summary statistics for object (categorical) columns
print(dd.describe(include='object').T)

# Check for duplicated rows
print(dd[dd.duplicated()])

# Check for columns with missing values
print(dd.isna().any())

# Display the count of missing values in each column
print(dd.isnull().sum())

# Function to calculate missing data
def missing_data(df):
    total_missing_df = df.isnull().sum().sort_values(ascending=False)
    percent_missing_df = (df.isnull().sum() / df.isna().count() * 100).sort_values(ascending=False)
    missing_data_df = pd.concat([total_missing_df, percent_missing_df], axis=1, keys=['Total', 'Percent'])
    return missing_data_df

missing_pct = missing_data(dd)
print(missing_pct[missing_pct['Total'] > 0])

# Visualize missing data
plt.figure(figsize=(25, 8))
plt.style.use('dark_background')
sns.heatmap(dd.isnull().T, cmap='Greys')
plt.title('Visual Check of Nulls', fontsize=20, color='r')
plt.show()

# Drop unknown fields
unknown_fields = ['is_cutoff', 'cutoff_factor', 'cutoff_timestamp', 'factor', 'segment_factor']
dd = dd.drop(columns=unknown_fields)
print(dd.sample())

# Check unique values in each column
for col in dd.columns:
    print(f'\nTotal Unique Values in {col} column are :- {dd[col].nunique()}')
    print(f'Unique Values in {col} column are :-\n {dd[col].unique()}')
    print('\n' + '-'*120)

# Convert to 'category' for columns with only 2 unique values
dd['data'] = dd['data'].astype('category')
dd['route_type'] = dd['route_type'].astype('category')

# Convert time columns to datetime format
datetime_cols = ['trip_creation_time', 'od_start_time', 'od_end_time']
for col in datetime_cols:
    dd[col] = pd.to_datetime(dd[col])

# Display the updated information about the dataset
print(dd.info())

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

# Number of deliveries by a relevant column (replace 'state' with the correct column name)
# Example: if 'destination_state' is the correct column name
plt.figure(figsize=(14, 7))
sns.countplot(data=dd, x='destination_state', order=dd['destination_state'].value_counts().index)
plt.xlabel('Destination State')
plt.ylabel('Number of Deliveries')
plt.title('Number of Deliveries by Destination State')
plt.xticks(rotation=90)
plt.show()

# Value counts of corridor
plt.figure(figsize=(14, 7))
sns.countplot(data=dd, x='corridor', order=dd['corridor'].value_counts().index)
plt.xlabel('Corridor')
plt.ylabel('Count')
plt.title('Value Counts of Corridor')
plt.xticks(rotation=90)
plt.show()

# Value counts of state, city, corridor combined
dd['state_city_corridor'] = dd['destination_state'] + ', ' + dd['destination_city'] + ', ' + dd['corridor']
plt.figure(figsize=(14, 7))
sns.countplot(data=dd, y='state_city_corridor', order=dd['state_city_corridor'].value_counts().index)
plt.xlabel('Count')
plt.ylabel('State, City, Corridor')
plt.title('Value Counts of State, City, Corridor')
plt.show()

