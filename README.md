
# Google Ads Offline Conversion Uploader

This project was developed as part of a technical assessment for a Marketing Engineer role at Beamer/Userflow.

It demonstrates:
- Cleaning and enriching offline conversion data
- Structuring payloads for the Google Ads API
- Simulating an upload process with logging and error handling

---

## Project Structure

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
│   ├── part1_data_processing.py      # Part 1: Data processing logic
│   └── part2_upload_to_google.py     # Part 2: API upload simulation
│
├── README.md                         # Project overview & instructions
└── requirements.txt                  # Python dependencies
```

---

## Part 1: Clean and Enrich Offline Conversion Data

### Features
- Loads raw data from CSV
- Formats timestamps for Google Ads API (`YYYY-MM-DD HH:MM:SS+00:00`)
- Filters:
  - `conversion_value > 0`
  - Non-null `gclid`
- Adds `value_bucket` field (`High` vs. `Low`)
- Outputs results to `output/cleaned_conversions.csv`

### Run It

```bash
python src/part1_data_processing.py
```

---

## Part 2: Simulated Google Ads Upload

### Features
- Loads cleaned data from Part 1
- Mocks a Google Ads API upload call
- Randomly returns success/failure responses
- Logs results to `output/upload_log.csv`
- Prints summary of total uploads, successes, and failures

### Run It

```bash
python src/part2_upload_to_google.py
```

---

## Design Principles

- Modular scripts with clear separation of concerns
- Simulated API logic mirrors Google Ads `ConversionUploadService`
- Output logs for traceability and review
- Prepped for real credential integration if needed

---

## Next Steps (for real-world use)

To integrate this into a live Google Ads API system:
- Replace the mock upload with actual API calls using the `google-ads` client library
- Securely manage `developer_token`, `client_id`, and `refresh_token`
- Add conversion action resource naming

---

