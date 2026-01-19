#extract_energyzero.py
import requests
import json
from datetime import datetime, timedelta
import os

def fetch_energy_data():
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=7)
    
    url = f"https://api.energyzero.nl/v1/energyprices?fromDate={start_date.date()}T00:00:00.000Z&tillDate={end_date.date()}T23:59:59.999Z&interval=4&usageType=1&inclBtw=false"
    
    response = requests.get(url)
    data = response.json()

    # Ödevdeki dosya ismi formatı: data/raw/energy_20251020_120000.json
    # Not: Docker içinde çalıştığı için başına /opt/airflow/ ekliyoruz
    file_name = f"/opt/airflow/data/raw/energy_{end_date.strftime('%Y%m%d_%H%M%S')}.json"
    
    # Klasörün var olduğundan emin olalım
    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    with open(file_name, "w") as f:
        json.dump(data, f)
    print(f"Saved: {file_name}")

if __name__ == "__main__":
    fetch_energy_data()