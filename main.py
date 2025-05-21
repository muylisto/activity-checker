import requests
import datetime

URLS = {
    "Ceramics": "https://example.com/ceramics",  # Replace with real URLs
    "Guitar": "https://example.com/guitar"
}

def check_classes():
    print("🔍 Checking CivicRec at", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    for category, url in URLS.items():
        try:
            res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            if res.status_code == 200:
                if "classTitle" in res.text:
                    print(f"✅ {category} - Classes found!")
                else:
                    print(f"✔️ {category} - No classes listed.")
            else:
                print(f"❌ {category} - HTTP {res.status_code}")
        except Exception as e:
            print(f"❌ {category} - Error: {e}")

if __name__ == "__main__":
    check_classes()
