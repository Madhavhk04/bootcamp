#The dataset contains 144,867 entries and 24 columns. Here are the key observations:


import pandas as pd

# Correct file path
file_path = r'C:\\Users\\devua\\OneDrive\\Desktop\\MADHAV\\delhivery_data.csv'
data = pd.read_csv(file_path)

# Display the first few rows and the summary of the dataset
data_info = data.info()
data_head = data.head()
data_describe = data.describe()

print(data_info)
print(data_head)
print(data_describe)

# Handle null values
# Fill missing 'source_name' and 'destination_name' with a placeholder
data['source_name'].fillna('Unknown', inplace=True)
data['destination_name'].fillna('Unknown', inplace=True)

# Verify if null values are handled
null_values_after_handling = data.isnull().sum()

null_values_after_handling

import matplotlib.pyplot as plt
import seaborn as sns

# List of numerical columns
numerical_columns = [
    'start_scan_to_end_scan', 'actual_distance_to_destination', 'actual_time',
    'osrm_time', 'osrm_distance', 'factor', 'segment_actual_time', 'segment_osrm_time',
    'segment_osrm_distance', 'segment_factor'
]

# Function to plot box plots for numerical columns
def plot_boxplots(data, columns):
    plt.figure(figsize=(15, 20))
    for i, column in enumerate(columns, 1):
        plt.subplot(len(columns), 1, i)
        sns.boxplot(x=data[column])
        plt.title(f'Box plot of {column}')
    plt.tight_layout()
    plt.show()

# Plot box plots for numerical columns
plot_boxplots(data, numerical_columns)
