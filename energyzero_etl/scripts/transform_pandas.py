import pandas as pd
import glob
import os
from sqlalchemy import create_engine

def transform_latest_json():
    # Dosyaları bul
    raw_files = glob.glob("/opt/airflow/data/raw/*.json")
    if not raw_files:
        print("Dosya bulunamadı!")
        return
        
    latest_file = sorted(raw_files)[-1]
    raw_data = pd.read_json(latest_file)
    
    # API yapısını kontrol et ve temizle
    if "Prices" in raw_data.columns:
        df = pd.json_normalize(raw_data["Prices"])
    else:
        df = raw_data

    # Kolonları küçük harfe çevir
    df.columns = [c.lower() for c in df.columns]

    if 'readingdate' in df.columns:
        df["readingdate"] = pd.to_datetime(df["readingdate"])
        # SQL ve Parquet hatası almamak için stringe çeviriyoruz
        df["date"] = df["readingdate"].dt.date.astype(str)
        df["time"] = df["readingdate"].dt.time.astype(str)
        df["price_with_vat"] = df["price"] * 1.21
    else:
        raise KeyError(f"Veride 'readingdate' bulunamadı! Mevcutlar: {df.columns}")

    # 1. Parquet Kaydet
    output_path = "/opt/airflow/data/processed/energy_transformed.parquet"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_parquet(output_path, index=False)

    # 2. PostgreSQL Yükle
    try:
        engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')
        df.to_sql('energy_data', engine, if_exists='append', index=False)
        print("Postgres'e yazıldı!")
    except Exception as e:
        print(f"Postgres Hatası: {e}")

    # 3. Analiz Logu
    cheapest = df.loc[df['price_with_vat'].idxmin()]
    print(f"\n💡 EN UCUZ SAAT: {cheapest['time']} (Fiyat: {cheapest['price_with_vat']:.4f})")

if __name__ == "__main__":
    transform_latest_json()