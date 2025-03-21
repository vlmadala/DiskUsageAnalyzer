# scanner/duplicate_finder.py
import os
import hashlib
import csv
import pandas as pd

def find_duplicate_files(directory):
    """Finds duplicate files based on hash comparison."""
    file_hashes = {}
    duplicates = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                
                if file_hash in file_hashes:
                    duplicates.append((file_hashes[file_hash], file_path, file_hash))
                else:
                    file_hashes[file_hash] = file_path
            except Exception as e:
                print(f"⚠️ Error processing {file_path}: {e}")
    
    return duplicates

def save_duplicate_report(duplicate_files):
    """Saves duplicate files report as CSV and Excel."""
    os.makedirs("reports", exist_ok=True)
    
    # Save CSV Report
    with open("reports/duplicate_files_report.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Duplicate File 1", "Duplicate File 2", "File Hash"])
        writer.writerows(duplicate_files)
    
    # Save Excel Report
    df_duplicates = pd.DataFrame(duplicate_files, columns=["Duplicate File 1", "Duplicate File 2", "File Hash"])
    with pd.ExcelWriter("reports/duplicate_files_report.xlsx") as writer:
        df_duplicates.to_excel(writer, sheet_name="Duplicate Files", index=False)
    
    print("📂 Duplicate files report saved in the 'reports' folder as CSV and Excel.")
