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


<img width="395" height="296" alt="Screenshot 2026-01-19 202641" src="https://github.com/user-attachments/assets/583bb2c8-677d-4e82-8e12-febb24e768f7" />



