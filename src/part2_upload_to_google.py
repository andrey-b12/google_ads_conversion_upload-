
"""
Part 2: Simulated Upload to Google Ads API
Author: Andrey Balandin
Description:
    This script simulates uploading cleaned offline conversion data
    to Google Ads' ConversionUploadService. It mimics real-world API
    payload structure and returns mock responses for testing purposes.
"""

import pandas as pd
import random
import time
import os

# Load the cleaned data
INPUT_PATH = 'output/cleaned_conversions.csv'
OUTPUT_LOG = 'output/upload_log.csv'

if not os.path.exists(INPUT_PATH):
    raise FileNotFoundError(f"Input file not found at {INPUT_PATH}")

df = pd.read_csv(INPUT_PATH)

# Function to simulate Google Ads API upload
def mock_upload_to_google_ads(row):
    # Simulate API response with 90% success rate
    if random.random() < 0.9:
        return {
            "status": "SUCCESS",
            "conversion_action_id": "1234567890",
            "gclid": row['gclid'],
            "conversion_time": row['conversion_time'],
            "conversion_value": row['conversion_value']
        }
    else:
        return {
            "status": "FAILURE",
            "error_message": "Simulated API failure",
            "gclid": row['gclid']
        }

# Store results
upload_results = []

for _, row in df.iterrows():
    response = mock_upload_to_google_ads(row)
    upload_results.append(response)
    # Simulate slight delay
    time.sleep(0.2)

# Convert results to DataFrame
results_df = pd.DataFrame(upload_results)

# Write log to CSV
results_df.to_csv(OUTPUT_LOG, index=False)

# Summary
total = len(results_df)
successes = len(results_df[results_df['status'] == 'SUCCESS'])
failures = total - successes

print(f"Upload Summary:")
print(f"Total Records: {total}")
print(f"Successes: {successes}")
print(f"Failures: {failures}")
print(f"Detailed log written to: {OUTPUT_LOG}")
