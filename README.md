
# Google Ads Offline Conversion Uploader

This project was developed as part of a technical assessment for a Marketing Engineer role at Beamer/Userflow.

It demonstrates:
- Data cleaning and enrichment for offline conversions
- Payload construction for Google Ads API
- Simulated upload logic with error handling, retry strategy, and audit logging
- Clear and prescriptive code documentation for readability and handoff

---

## 📁 Project Structure

```
google_ads_conversion_upload/
│
├── data/
│   └── conversions.csv               # Raw input conversion data
│
├── output/
│   ├── cleaned_conversions.csv       # Filtered, formatted conversions (Part 1)
│   └── upload_log.csv                # Simulated upload results (Part 2)
│
├── src/
│   ├── part1_data_processing.py      # Part 1: Cleans & enriches conversion data
│   └── part2_upload_to_google.py     # Part 2: Simulated upload with bonus features
│
├── README.md                         # Project overview & run instructions
└── requirements.txt                  # Python dependencies (if needed)
```

---

## Part 1: Data Cleaning and Enrichment

### Key Features
- Removes records with missing `gclid` or zero `conversion_value`
- Formats timestamps to Google Ads API specification (`YYYY-MM-DD HH:MM:SS+00:00`)
- Adds a `value_bucket` column to group conversions into `High` or `Low` value tiers
- Saves cleaned output to `output/cleaned_conversions.csv`

### Run Part 1

```bash
python src/part1_data_processing.py
```

---

## Part 2: Simulated Upload with Retry & Conversion Action Logic

### Key Features
- Simulates `ConversionUploadService` using realistic payload structure
- Randomly returns `SUCCESS` or `FAILURE` with retry logic (exponential backoff)
- Automatically checks and “creates” a simulated conversion action if not found
- Logs each upload’s outcome, including number of attempts and error messages
- Saves log to `output/upload_log.csv` and prints a summary

### Run Part 2

```bash
python src/part2_upload_to_google.py
```

---

## Bonus Logic Implemented

- Automatically create conversion actions if they don't exist (simulated logic)
- Add retry logic for intermittent failures or rate limits using exponential backoff

---

## Design Considerations

- Modular, self-contained scripts
- Highly readable and prescriptive in-code comments
- Output logs enable traceability and debugging
- Designed for test-mode simulation but easily extendable to live API integration

---

## Future Expansion for Production

If this were a live implementation:
- Replace `mock_upload_with_retry` with `google-ads` API client
- Use `OAuth2` + Developer Token + Customer ID for authentication
- Implement batching and partial failure handling per API specs
- Use real `conversion_action` resource names tied to your Google Ads account

