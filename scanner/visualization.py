# scanner/visualization.py
import matplotlib.pyplot as plt
import os

def plot_disk_usage(extension_sizes):
    """Generates a bar chart for file type distribution."""
    os.makedirs("reports", exist_ok=True)
    
    extensions = list(extension_sizes.keys())
    sizes = [size / (1024 * 1024) for size in extension_sizes.values()]  # Convert bytes to MB
    
    plt.figure(figsize=(10, 6))
    plt.bar(extensions, sizes)
    plt.xlabel("File Types")
    plt.ylabel("Size (MB)")
    plt.title("Disk Usage by File Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("reports/disk_usage_chart.png")
    plt.show()
    
    print("📊 Disk usage chart saved in the 'reports' folder.")
