import os
import re
import math
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def calculate_entropy(text: str) -> float:
    """Calculates Shannon Entropy to detect randomized/suspicious domain strings."""
    if not text:
        return 0.0
    prob = [float(text.count(c)) / len(text) for c in set(text)]
    return round(-sum([p * math.log(p, 2) for p in prob]), 4)

def process_url_dataset():
    input_path = os.path.join(DATA_DIR, "dataset_c_urls.csv")
    output_path = os.path.join(DATA_DIR, "dataset_c_urls_processed.csv")

    df = pd.read_csv(input_path)

    # Feature engineering
    df["entropy"] = df["url"].apply(calculate_entropy)
    df["digits_count"] = df["url"].apply(lambda x: sum(c.isdigit() for c in str(x)))
    df["special_char_count"] = df["url"].apply(lambda x: sum(not c.isalnum() for c in str(x)))
    df["is_ip_address"] = df["domain"].apply(
        lambda d: 1 if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", str(d)) else 0
    )

    df.to_csv(output_path, index=False)
    print(f"✓ Processed Dataset C saved to: {output_path} ({len(df)} records)")

if __name__ == "__main__":
    process_url_dataset()