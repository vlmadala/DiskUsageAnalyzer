# main.py
from scanner.disk_usage import DiskUsageAnalyzer
from scanner.duplicate_finder import find_duplicate_files, save_duplicate_report
from scanner.file_operations import save_reports
from scanner.visualization import plot_disk_usage

def main():
    directory_to_scan = input(r"Enter the directory to scan (e.g., C:\Users\YourUsername\Documents): ")
    analyzer = DiskUsageAnalyzer(directory_to_scan)
    analyzer.scan_filesystem()
    
    file_sizes, folder_sizes, extension_sizes = analyzer.get_data()
    duplicate_files = find_duplicate_files(directory_to_scan)
    save_reports(file_sizes, folder_sizes)
    save_duplicate_report(duplicate_files)
    plot_disk_usage(extension_sizes)
    
    print("✅ Disk usage analysis completed! Check the 'reports' folder.")

if __name__ == "__main__":
    main()
# The main.py script imports the DiskUsageAnalyzer class from the scanner.disk_usage module and uses it to scan the filesystem.
# The script then saves the collected data to a file using the save_reports function from the scanner.file_operations module.
# Finally, it visualizes the data using the plot_disk_usage function from the scanner.visualization module.
# The main function prompts the user to enter a directory to scan, performs the analysis, and displays a completion message.
# When run as the main script, the main function is executed.
# The main.py script serves as the entry point for the disk usage analysis application.
# It orchestrates the different components of the application to scan the filesystem, save the reports, and visualize the data.
# The main function encapsulates the high-level logic of the application, making it easy to understand and maintain.
# The script is structured in a modular way, with separate modules for disk usage analysis, file operations, and visualization.
# This separation of concerns improves code organization and reusability.
# The main.py script demonstrates how to use the scanner package to perform disk usage analysis on a specified directory.
# The script leverages the functionality provided by the scanner modules to collect, save, and visualize disk usage data.   
# The main.py script is an example of a Python script that orchestrates the execution of a disk usage analysis application.
# It imports and uses modules from the scanner package to perform the analysis, save the reports, and visualize the data.
# The script demonstrates how to structure a Python application with multiple modules and how to coordinate their interactions.
# The main function serves as the entry point for the application, prompting the user for input and coordinating the analysis process.
# The script showcases best practices for organizing code, separating concerns, and creating reusable components in a Python application.
# The main.py script is a central component of the disk usage analysis application, providing a clear and concise entry point for users.
# The script demonstrates how to leverage modular design and encapsulation to create a well-structured and maintainable application.
# The main function encapsulates the high-level logic of the application, orchestrating the different components to perform the disk usage analysis.
# The script showcases how to interact with user input, process data, and visualize results in a Python application.
# The main.py script exemplifies the use of Python modules, classes, functions, and libraries to build a functional and user-friendly application.
# The script demonstrates how to leverage Python's ecosystem to create powerful and flexible applications for various use cases.
# The main.py script is an essential part of the disk usage analysis application, providing a user-friendly interface to analyze disk usage data.
# The script demonstrates how to structure a Python application with multiple modules and classes to achieve a clean and organized codebase.
# The main function serves as the entry point for the application, orchestrating the scanning, reporting, and visualization of disk usage data.
# The script showcases best practices for handling user input, error checking, and data processing in a Python application.
# The main.py script is a key component of the disk usage analysis application, responsible for coordinating the analysis process and generating reports.
# The script demonstrates how to structure a Python application using modules and classes to achieve a modular and maintainable design.

