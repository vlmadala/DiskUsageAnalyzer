# scanner/disk_usage.py
import os
import time
from collections import Counter

class DiskUsageAnalyzer:
    def __init__(self, directory):
        self.directory = directory
        self.file_sizes = []
        self.folder_sizes = Counter()
        self.extension_sizes = Counter()
    
    def scan_filesystem(self):
        """Scans the directory and collects file and folder size data."""
        for root, _, files in os.walk(self.directory):
            folder_size = 0
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(file_path)
                    self.file_sizes.append((file_path, file_size, time.ctime(os.path.getctime(file_path))))
                    extension = os.path.splitext(file)[1]
                    self.extension_sizes[extension] += file_size
                    folder_size += file_size
                except Exception as e:
                    print(f"⚠️ Error accessing {file_path}: {e}")
            self.folder_sizes[root] = folder_size
    
    def get_data(self):
        """Returns collected file size, folder size, and extension data."""
        return self.file_sizes, self.folder_sizes, self.extension_sizes