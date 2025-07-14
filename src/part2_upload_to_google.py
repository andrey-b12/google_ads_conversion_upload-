
"""
Part 2 (Enhanced): Simulated Upload to Google Ads API with Bonus Goals
Author: Andrey Balandin
Description:
    This script simulates uploading offline conversion data to Google Ads,
    including bonus functionality to:
    - Create the conversion action if it doesn't exist (simulated)
    - Add retry logic for failed uploads
"""

import pandas as pd
import random
import time
import os

# Load cleaned data
INPUT_PATH = 'output/cleaned_conversions.csv'
OUTPUT_LOG = 'output/upload_log.csv'

if not os.path.exists(INPUT_PATH):
    raise FileNotFoundError(f"Input file not found at {INPUT_PATH}")

df = pd.read_csv(INPUT_PATH)

# Simulated conversion action database (mock)
conversion_actions = set()

def create_conversion_action_if_missing(action_name):
    """Simulate checking and creating a conversion action."""
    if action_name not in conversion_actions:
        print(f"Conversion action '{action_name}' not found. Creating it...")
        conversion_actions.add(action_name)
    else:
        print(f"Conversion action '{action_name}' already exists.")

# Simulated API upload with retry logic
def mock_upload_with_retry(row, retries=3, backoff=1.0):
    attempt = 0
    while attempt < retries:
        attempt += 1
        if random.random() < 0.9:
            return {
                "status": "SUCCESS",
                "conversion_action_id": "1234567890",
                "gclid": row['gclid'],
                "conversion_time": row['conversion_time'],
                "conversion_value": row['conversion_value'],
                "attempts": attempt
            }
        else:
            print(f"Attempt {attempt} failed for gclid {row['gclid']}")
            time.sleep(backoff)
            backoff *= 2  # exponential backoff

    return {
        "status": "FAILURE",
        "error_message": "Simulated persistent failure after retries",
        "gclid": row['gclid'],
        "attempts": attempt
    }

# Simulate checking or creating conversion action
create_conversion_action_if_missing("offline_purchase")

# Process each row
upload_results = []
for _, row in df.iterrows():
    result = mock_upload_with_retry(row)
    upload_results.append(result)

# Save upload results
results_df = pd.DataFrame(upload_results)
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
