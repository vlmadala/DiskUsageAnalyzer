# scanner/file_operations.py
import csv
import os
import pandas as pd

def save_reports(file_sizes, folder_sizes):
    """Saves disk usage reports as CSV and Excel files."""
    os.makedirs("reports", exist_ok=True)
    
    # Save CSV Reports
    with open("reports/disk_usage_report.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["File Path", "File Size (bytes)", "Creation Time"])
        writer.writerows(file_sizes)
    
    with open("reports/largest_folders_report.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Folder Path", "Total Size (bytes)"])
        for folder, size in folder_sizes.most_common(10):
            writer.writerow([folder, size])
    
    # Save Excel Reports
    df_files = pd.DataFrame(file_sizes, columns=["File Path", "File Size (bytes)", "Creation Time"])
    df_folders = pd.DataFrame(folder_sizes.most_common(10), columns=["Folder Path", "Total Size (bytes)"])
    
    with pd.ExcelWriter("reports/disk_usage_report.xlsx") as writer:
        df_files.to_excel(writer, sheet_name="Files", index=False)
        df_folders.to_excel(writer, sheet_name="Largest Folders", index=False)
    
    print("📂 Reports saved in the 'reports' folder as CSV and Excel files.")
