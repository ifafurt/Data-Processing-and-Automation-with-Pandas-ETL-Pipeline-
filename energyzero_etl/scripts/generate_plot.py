import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

def create_report():
    # Find the latest processed file
    files = glob.glob("/opt/airflow/data/processed/*.parquet")
    if not files: 
        print("Error: Processed file not found!")
        return
    
    # Select the most recent file
    latest_file = max(files, key=os.path.getctime)
    df = pd.read_parquet(latest_file)
    
    # Ensure data types are correct for plotting
    df['time'] = df['time'].astype(str)
    df['date'] = df['date'].astype(str)
    
    # Create the figure
    plt.figure(figsize=(14, 8))
    
    unique_dates = sorted(df['date'].unique())
    
    for date in unique_dates:
        day_data = df[df['date'] == date].sort_values('time')
        
        # Plot the daily trend lines
        line, = plt.plot(day_data['time'], day_data['price_with_vat'], 
                         label=date, alpha=0.5, linewidth=2)
        
        # IDENTIFY CHEAPEST HOUR
        cheapest_idx = day_data['price_with_vat'].idxmin()
        cheapest_time = day_data.loc[cheapest_idx, 'time']
        cheapest_price = day_data.loc[cheapest_idx, 'price_with_vat']
        
        # Highlight the cheapest point with a distinct marker
        plt.plot(cheapest_time, cheapest_price, 
                 marker='o',          # Circular marker
                 markersize=10,       
                 color=line.get_color(), 
                 markeredgecolor='white', 
                 markeredgewidth=1.5,
                 label='_nolegend_')

    # Chart Styling (English Labels)
    plt.title("Weekly Energy Price Analysis: Daily Lowest Price Points", fontsize=16, fontweight='bold')
    plt.xlabel("Hour of the Day (00:00 - 23:00)", fontsize=12)
    plt.ylabel("Price (€/MWh - Incl. VAT)", fontsize=12)
    
    # Optimize X-axis ticks (Show every 2nd hour for clarity)
    all_times = sorted(df['time'].unique())
    plt.xticks(all_times[::2], rotation=45)
    
    # Legend settings
    plt.legend(title="Reference Dates", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.2)
    plt.tight_layout()
    
    # Save the output
    output_path = '/opt/airflow/data/processed/energy_chart_multiline.png'
    plt.savefig(output_path, dpi=300)
    print(f"✅ Report generated successfully: {output_path}")

if __name__ == "__main__":
    create_report()