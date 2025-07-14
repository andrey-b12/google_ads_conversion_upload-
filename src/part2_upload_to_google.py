
"""
Part 2 (Enhanced): Simulated Upload to Google Ads API with Bonus Goals
Author: Andrey Balandin
Description:
    This script simulates uploading offline conversion data to Google Ads.
    It includes:
    - Checking for and simulating creation of a conversion action
    - Retrying failed uploads using exponential backoff
    - Logging the results of all uploads
"""

import pandas as pd  # For working with CSV data
import random        # For simulating upload success/failure
import time          # For adding delays in retry logic
import os            # For checking file paths

# Define input and output file paths
INPUT_PATH = 'output/cleaned_conversions.csv'
OUTPUT_LOG = 'output/upload_log.csv'

# STEP 1: Load Cleaned Conversion Data
# -------------------------------------
# Check if the cleaned conversions file exists
if not os.path.exists(INPUT_PATH):
    raise FileNotFoundError(f"Input file not found at {INPUT_PATH}")

# Read the cleaned conversion data into a pandas DataFrame
df = pd.read_csv(INPUT_PATH)

# STEP 2: Simulate Conversion Action Creation
# -------------------------------------------
# Create a set to simulate stored conversion actions
conversion_actions = set()

def create_conversion_action_if_missing(action_name):
    """
    Check if the conversion action exists.
    If not, simulate creating it and add to our local set.
    """
    if action_name not in conversion_actions:
        print(f"Conversion action '{action_name}' not found. Creating it...")
        conversion_actions.add(action_name)
    else:
        print(f"Conversion action '{action_name}' already exists.")

# Call the simulated function to ensure the conversion action is available
create_conversion_action_if_missing("offline_purchase")

# STEP 3: Simulate Google Ads API Upload with Retry Logic
# -------------------------------------------------------
def mock_upload_with_retry(row, retries=3, backoff=1.0):
    """
    Simulates an upload to Google Ads API with retry logic.
    Tries up to 'retries' times with exponential backoff if failed.
    Returns either a success or failure response.
    """
    attempt = 0
    while attempt < retries:
        attempt += 1

        # Simulate a 90% success rate
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
            # Print failed attempt and wait before retrying
            print(f"Attempt {attempt} failed for gclid {row['gclid']}")
            time.sleep(backoff)
            backoff *= 2  # Exponential backoff: 1s -> 2s -> 4s

    # If all attempts fail, return a failure response
    return {
        "status": "FAILURE",
        "error_message": "Simulated persistent failure after retries",
        "gclid": row['gclid'],
        "attempts": attempt
    }

# STEP 4: Run Simulated Upload for Each Conversion Record
# --------------------------------------------------------
# This list will store the upload results for each row
upload_results = []

# Loop through each conversion record
for _, row in df.iterrows():
    # Simulate upload and append result
    result = mock_upload_with_retry(row)
    upload_results.append(result)

# STEP 5: Save Upload Results to a CSV Log File
# ----------------------------------------------
# Convert the results list to a DataFrame
results_df = pd.DataFrame(upload_results)

# Save the upload log to the specified file
results_df.to_csv(OUTPUT_LOG, index=False)

# STEP 6: Print a Summary Report to the Console
# ----------------------------------------------
total = len(results_df)
successes = len(results_df[results_df['status'] == 'SUCCESS'])
failures = total - successes

# Print summary information
print(f"Upload Summary:")
print(f"Total Records: {total}")
print(f"Successes: {successes}")
print(f"Failures: {failures}")
print(f"Detailed log written to: {OUTPUT_LOG}")
