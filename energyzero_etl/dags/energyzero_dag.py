# energyzero_dag.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='energyzero_etl_pipeline',
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    # 1. ADIM: API'den veriyi çek (Extract)
    extract = BashOperator(
        task_id='extract_energyzero_json',
        bash_command='python /opt/airflow/scripts/extract_energyzero.py'
    )

    # 2. ADIM: Veriyi temizle, KDV ekle ve Postgres'e bas (Transform & Load)
    transform = BashOperator(
        task_id='transform_json_to_parquet',
        bash_command='python /opt/airflow/scripts/transform_pandas.py'
    )

    # 3. ADIM: Analiz yap ve Grafik oluştur (Analysis/Reporting)
    # Bu adım senin "En ucuz saat ne zaman?" soruna cevap veren raporu üretecek
    analyze = BashOperator(
        task_id='generate_energy_analysis',
        bash_command='python /opt/airflow/scripts/generate_plot.py' # Veya analiz kodun hangisindeyse
    )

    # ZİNCİRLEME (Pipeline)
    extract >> transform >> analyze