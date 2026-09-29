import csv
import random
import os
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

random.seed(42)

scam_templates = [
    ("Congratulations! You won Rs. {amount}. Pay Rs. {fee} processing fee to claim instantly.", "Prize", 1),
    ("Dear customer, your bank account is suspended. Click link to verify details immediately.", "Banking", 1),
    ("Earn Rs. {amount} daily by watching YouTube videos! Contact WhatsApp {phone}.", "Fake Job", 1),
    ("Guaranteed {rate}% weekly return on crypto investment. Deposit now to secure your spot.", "Investment", 1),
    ("Urgent: Your parcel is held at customs. Pay Rs. {fee} clearance fee to deliver.", "Payment", 1),
    ("Hi Mom, I lost my phone. Send Rs. {amount} to this account urgently, need help.", "Impersonation", 1),
]

legit_templates = [
    ("Your OTP for transaction is {otp}. Do not share it with anyone.", "Banking", 0),
    ("Your package from Daraz has been dispatched. Track at official app.", "Legitimate", 0),
    ("Hi, please review the document attached for tomorrow's meeting.", "Legitimate", 0),
    ("Reminder: Doctor appointment scheduled for tomorrow at 4 PM.", "Legitimate", 0),
    ("Your monthly electricity bill is Rs. {amount}. Due date is 15th.", "Legitimate", 0),
]

def generate_dataset_a(count=1000):
    filepath = os.path.join(DATA_DIR, "dataset_a_messages.csv")
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["msg_id", "message", "category", "label", "source"])
        for i in range(1, count + 1):
            is_scam = random.choice([0, 1])
            tmpl, cat, label = random.choice(scam_templates if is_scam else legit_templates)
            msg = tmpl.format(
                amount=random.randint(10000, 500000),
                fee=random.randint(500, 5000),
                rate=random.randint(15, 100),
                otp=random.randint(100000, 999999),
                phone=f"+92300{random.randint(1000000, 9999999)}"
            )
            writer.writerow([f"MSG_{i:04d}", msg, cat, label, random.choice(["WhatsApp", "SMS", "User Report"])])
    print(f"✓ Created Dataset A: {filepath}")

def generate_dataset_b(count=300):
    filepath = os.path.join(DATA_DIR, "dataset_b_phone_reports.csv")
    categories = ["Investment", "Fake Job", "Prize", "Banking", "Payment", "Impersonation"]
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["report_id", "phone_number", "category", "report_count", "source_type", "status", "last_reported"])
        for i in range(1, count + 1):
            phone = f"+923{random.randint(0,4)}{random.randint(1000000, 9999999)}"
            cat = random.choice(categories)
            reports = random.randint(1, 45)
            status = "confirmed" if reports > 10 else "reported"
            date = (datetime.now() - timedelta(days=random.randint(0, 180))).strftime("%Y-%m-%d")
            writer.writerow([f"REP_{i:04d}", phone, cat, reports, random.choice(["Community", "Threat Intel", "User Report"]), status, date])
    print(f"✓ Created Dataset B: {filepath}")

def generate_dataset_c(count=1000):
    filepath = os.path.join(DATA_DIR, "dataset_c_urls.csv")
    legit_domains = ["google.com", "github.com", "bankofpunjab.com.pk", "daraz.pk", "wikipedia.org", "easypaisa.com.pk"]
    suspicious_words = ["login-verify", "secure-update", "claim-reward", "account-check", "free-crypto"]
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["url_id", "url", "domain", "url_length", "subdomains_count", "has_https", "suspicious_keyword", "label"])
        for i in range(1, count + 1):
            is_scam = random.choice([0, 1])
            if is_scam:
                dom = f"secure-{random.choice(suspicious_words)}.xyz"
                url = f"http://{dom}/account/login/{random.randint(100,999)}"
                has_https, kw = 0, 1
            else:
                dom = random.choice(legit_domains)
                url = f"https://{dom}/page/{random.randint(1,50)}"
                has_https, kw = 1, 0
            writer.writerow([f"URL_{i:04d}", url, dom, len(url), dom.count("."), has_https, kw, is_scam])
    print(f"✓ Created Dataset C: {filepath}")

def generate_dataset_d(count=200):
    filepath = os.path.join(DATA_DIR, "dataset_d_cases.csv")
    categories = ["Investment", "Fake Job", "Prize", "Banking", "Payment"]
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["case_id", "message", "phone_number", "url", "category", "risk_level", "created_at"])
        for i in range(1, count + 1):
            cat = random.choice(categories)
            phone = f"+92300{random.randint(1000000, 9999999)}"
            url = f"http://verify-claim-{i}.xyz/login"
            msg = f"Claim your {cat} award immediately. Contact {phone} or visit {url}."
            date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
            writer.writerow([f"CASE_{i:04d}", msg, phone, url, cat, random.choice(["MEDIUM", "HIGH", "CRITICAL"]), date])
    print(f"✓ Created Dataset D: {filepath}")

if __name__ == "__main__":
    generate_dataset_a()
    generate_dataset_b()
    generate_dataset_c()
    generate_dataset_d()
    print("\n🎉 All 4 ScamLens datasets generated successfully in ml/data/")