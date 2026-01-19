# Dockerfile
# Temel imaj
FROM apache/airflow:2.7.1-python3.10

# Çalışma dizinini Airflow'un varsayılan dizini yapıyoruz
WORKDIR /opt/airflow

# Kütüphaneleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kendi yazdığın scriptleri imajın içine paketliyoruz
# Böylece imaj nereye giderse kodların da içinde gider
COPY scripts/ /opt/airflow/scripts/

# Gerekli klasörlerin (data/raw ve processed) oluşmasını garantiye alıyoruz
RUN mkdir -p /opt/airflow/data/raw /opt/airflow/data/processed