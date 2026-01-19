🧠 Data Processing and Automation with Pandas (ETL & Pipeline)
🎯 Project Goal
The goal of this project is to help you learn how to use the Pandas library for data processing and to understand the basics of Docker and Apache Airflow.

You will use the EnergyZero API to get real energy price data for one week and build a full ETL (Extract – Transform – Load) pipeline.

📦 Project Steps
1️⃣ Extract – Get the Data
Use the EnergyZero API to get the last 7 days of energy price data.

Save the raw data as a JSON file on your computer.

2️⃣ Transform – Clean and Change the Data
Read the JSON file with Pandas and convert it into a DataFrame.

Split the column ReadingDate into two parts: Date and Time.

Add a new column called Price_with_VAT, which includes a 21% tax.

Check that column names, formats, and data types are correct.

3️⃣ Load – Save the Data
Save the transformed data in Parquet format in the folder data/processed/.

Parquet files are smaller and faster for data analysis.

🧰 Tools You Will Use
🐍 Python & Pandas – to process and transform data
🐳 Docker – to run the project in a simple and portable environment
🪶 Apache Airflow – to automate and schedule your ETL process
🔌 EnergyZero API – to get real-time energy price data

🎓 What You Will Learn
After finishing this project, you will be able to:

✅ Get data from a real API
✅ Process and clean data using Pandas
✅ Use Docker to containerize your project
✅ Create and schedule workflows with Apache Airflow

🔗 Useful Links
🌐 EnergyZero API
"https://api.energyzero.nl/v1/energyprices?fromDate={start_date}
T00:00:00.000Z&tillDate={end_date}
T23:59:59.999Z&interval=4&usageType=1&inclBtw=false"

<img width="4200" height="2400" alt="energy_chart_multiline" src="https://github.com/user-attachments/assets/2f7b1740-ceca-4440-b6a2-a7de4adb01ed" />

<img width="1251" height="752" alt="Screenshot 2026-01-19 201725" src="https://github.com/user-attachments/assets/f4a93972-9bb9-45f4-8e63-f3f31103f4ae" />

<img width="952" height="1023" alt="Screenshot 2026-01-19 195836" src="https://github.com/user-attachments/assets/bb0ea1a7-712b-4d64-8c4e-5d1a7bf312b5" />

<img width="935" height="1018" alt="Screenshot 2026-01-19 195845" src="https://github.com/user-attachments/assets/55fe0bc2-cce4-4666-87c9-6d8c88cf4883" />

<img width="1430" height="839" alt="Screenshot 2026-01-19 201702" src="https://github.com/user-attachments/assets/147275ac-753b-46d3-b34f-e40a5654402d" />







