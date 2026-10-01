import os
import re
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def clean_text(text: str) -> str:
    """Normalizes text by removing URLs, phone numbers, and extra spaces."""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "[URL]", text)
    text = re.sub(r"\+?\d[\d\s-]{8,}\d", "[PHONE]", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def process_messages_dataset():
    input_path = os.path.join(DATA_DIR, "dataset_a_messages.csv")
    output_path = os.path.join(DATA_DIR, "dataset_a_messages_processed.csv")

    df = pd.read_csv(input_path)
    
    # Feature Engineering
    df["clean_message"] = df["message"].apply(clean_text)
    df["char_count"] = df["message"].str.len()
    df["word_count"] = df["message"].apply(lambda x: len(str(x).split()))
    df["has_urgency_words"] = df["clean_message"].apply(
        lambda x: 1 if any(w in x for w in ["urgent", "suspended", "immediately", "lost", "pay"]) else 0
    )

    df.to_csv(output_path, index=False)
    print(f"✓ Processed Dataset A saved to: {output_path} ({len(df)} records)")

if __name__ == "__main__":
    process_messages_dataset()