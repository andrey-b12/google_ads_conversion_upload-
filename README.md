
# Google Ads Offline Conversion Uploader

This project is part of a technical assessment for a Marketing Engineer role at Beamer/Userflow. It demonstrates how to process offline conversion data and prepare it for upload to the Google Ads API.

---

## 📁 Project Structure

```
google_ads_conversion_upload/
│
├── data/
│   └── conversions.csv               # Raw input conversion data
│
├── output/
│   └── cleaned_conversions.csv       # Filtered, formatted conversions
│
├── src/
│   └── part1_data_processing.py      # ✅ Part 1: Data processing logic
│
├── README.md                         # Project overview & usage
└── requirements.txt                  # Dependencies (e.g. pandas)
```

---

## ✅ Part 1: Data Cleaning & Enrichment

### What It Does
- Loads raw offline conversion data
- Formats timestamps for Google Ads API (`YYYY-MM-DD HH:MM:SS+00:00`)
- Filters valid conversions:
  - `conversion_value > 0`
  - Non-null `gclid`
- Adds value bucket labels (`High` or `Low`)
- Outputs cleaned data to `output/cleaned_conversions.csv`

### How to Run

```bash
# Navigate to the repo root
cd google_ads_conversion_upload

# Run the data processing script
python src/part1_data_processing.py
```

Output will be saved to `output/cleaned_conversions.csv`.

---

## 🧠 Why It Matters

Google Ads offline conversion tracking relies on clean, structured, high-confidence data. This script ensures only valid and high-signal conversion events are submitted for attribution and optimization.

---

## 🔜 Next Step: Google Ads API Integration

The next part of the project will demonstrate how to upload this cleaned dataset to Google Ads via the `ConversionUploadService`.

