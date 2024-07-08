import pandas as pd

# Load the data
file_path = r"C:\Users\devua\OneDrive\Desktop\MADHAV\delhivery_data.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
df.head()

null_values = df.isnull().sum()
null_values

source_name_dist = df['source_name'].value_counts()
destination_name_dist = df['destination_name'].value_counts()

source_name_dist, destination_name_dist