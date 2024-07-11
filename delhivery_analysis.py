import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Load the dataset
file_path = r'C:\Users\devua\OneDrive\Desktop\MADHAV\delhivery_data.csv'  # Update this path to your CSV file
delhivery_data = pd.read_csv(file_path)


# Copy and drop NA values
dd = delhivery_data.copy()
df = dd.dropna()

# Define segment columns and create segment_key
segment_cols = ['segment_actual_time', 'segment_osrm_distance', 'segment_osrm_time']
df['segment_key'] = df['trip_uuid'] + '+' + df['source_center'] + '+' + df['destination_center']

# Calculate cumulative sum for segment columns
for col in segment_cols:
    df[col + '_sum'] = df.groupby('segment_key')[col].cumsum()

# Create a dictionary for aggregation
segment_dict = {
    'trip_uuid': 'first',
    'data': 'first',
    'route_type': 'first',
    'trip_creation_time': 'first',
    'source_name': 'first',
    'destination_name': 'last',
    'od_start_time': 'first',
    'od_end_time': 'last',
    'start_scan_to_end_scan': 'first',
    'actual_distance_to_destination': 'last',
    'actual_time': 'last',
    'osrm_time': 'last',
    'osrm_distance': 'last',
    'segment_actual_time': 'sum',
    'segment_osrm_time': 'sum',
    'segment_osrm_distance': 'sum',
    'segment_actual_time_sum': 'last',
    'segment_osrm_time_sum': 'last',
    'segment_osrm_distance_sum': 'last',
}

# Group by segment_key and aggregate
segment_agg_data = df.groupby('segment_key').agg(segment_dict).reset_index()
segment_agg_data = segment_agg_data.sort_values(by=['segment_key', 'od_end_time'])
de = segment_agg_data.copy()

# Extract information from destination_name
def extract_info(name):
    pattern = r'^(?P<city>[^\s_]+)_?(?P<place>[^\(\)]*)\s?\((?P<state>[A-Za-z\s&]+)\)$'
    match = re.match(pattern, name)
    if match:
        city = match.group('city').strip()
        place = match.group('place').strip() if match.group('place') else city
        state = match.group('state').strip()
        return city, place, state
    else:
        return None, None, None

de[['destination_city', 'destination_place', 'destination_state']] = de['destination_name'].apply(lambda x: pd.Series(extract_info(x)))

# Create value counts for corridor
if 'corridor' in de.columns:
    corridor_counts = de['corridor'].value_counts().to_frame().reset_index()
    corridor_counts.columns = ['Corridor', 'Count']
    
    # Plot the value counts for corridor
    plt.figure(figsize=(15, 10))
    a = sns.barplot(y='Corridor', x='Count', data=corridor_counts, palette='viridis', width=0.2)
    a.bar_label(a.containers[0], label_type='edge')
    plt.xticks([])
    plt.ylabel('Corridor')
    plt.xlabel('Count')
    plt.title('Value Counts of Corridor', fontsize=12, fontfamily='serif', fontweight='bold', backgroundcolor='k', color='w')
    plt.tight_layout()
    sns.despine(bottom=True, left=True)
    plt.show()
else:
    print("The column 'corridor' does not exist in the dataset.")
