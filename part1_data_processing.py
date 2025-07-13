
"""
Part 1: Data Processing Script
Author: Andrey Balandin
Description:
    This script loads offline conversion data from a CSV,
    filters and formats it according to Google Ads API requirements,
    and outputs a clean CSV file ready for API upload.
"""

import pandas as pd
from datetime import datetime

# Load the dataset
df = pd.read_csv('data/conversions.csv')  # Assumes file is in ./data/ folder

# Step 1: Rename 'google_click_id (gclid)' to 'gclid' for easier reference
df.rename(columns={'google_click_id (gclid)': 'gclid'}, inplace=True)

# Step 2: Convert timestamps to Google Ads API format: 'YYYY-MM-DD HH:MM:SS+00:00'
# Assuming UTC time zone for simplicity
df['conversion_time'] = pd.to_datetime(df['timestamp'], errors='coerce').dt.strftime('%Y-%m-%d %H:%M:%S+00:00')

# Step 3: Filter only valid conversions:
# - conversion_value must be greater than 0
# - gclid must not be null
filtered_df = df[
    (df['conversion_value'] > 0) &
    (df['gclid'].notnull())
].copy()

# Step 4: Optional enrichment - bucket high vs. low-value conversions
# Let's say anything over 100 is considered high value
filtered_df['value_bucket'] = filtered_df['conversion_value'].apply(lambda x: 'High' if x > 100 else 'Low')

# Step 5: Keep only relevant columns for upload
final_df = filtered_df[[
    'gclid',
    'conversion_time',
    'conversion_value',
    'utm_campaign',
    'value_bucket'
]]

# Step 6: Save cleaned data to CSV (output directory)
final_df.to_csv('output/cleaned_conversions.csv', index=False)

print(f"Processed {len(df)} records. {len(final_df)} valid conversions saved to output/cleaned_conversions.csv")
