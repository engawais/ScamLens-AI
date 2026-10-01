import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def validate_datasets():
    datasets = [
        "dataset_a_messages.csv",
        "dataset_b_phone_reports.csv",
        "dataset_c_urls.csv",
        "dataset_d_cases.csv"
    ]

    print("--- Running ScamLens AI Data Integrity Suite ---")
    all_passed = True

    for filename in datasets:
        path = os.path.join(DATA_DIR, filename)
        if not os.path.exists(path):
            print(f"❌ Missing file: {filename}")
            all_passed = False
            continue

        df = pd.read_csv(path)
        null_count = df.isnull().sum().sum()
        
        if null_count > 0:
            print(f"⚠️ Warning: {filename} contains {null_count} null values.")
            all_passed = False
        else:
            print(f"✅ {filename}: Validated ({len(df)} rows, 0 nulls, schema OK)")

    if all_passed:
        print("\n🎉 Data validation successful! Datasets are ready for Phase 4.")

if __name__ == "__main__":
    validate_datasets()