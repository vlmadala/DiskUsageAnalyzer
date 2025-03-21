Disk Usage Analyzer

Overview

The Disk Usage Analyzer is a Python-based tool that scans a directory and provides insights into file and folder sizes. It generates reports and visualizes disk usage to help users identify large or unused files.

Features

Scans a specified directory for file and folder sizes.

Generates CSV reports for disk usage analysis.

Identifies the largest folders.

Visualizes file type distribution using a bar chart.

Project Structure

Installation & Setup

1. Clone the Repository

2. Install Dependencies

3. Run the Program

Enter the directory to scan when prompted.

Output

Reports Generated

reports/disk_usage_report.csv → Contains file paths, sizes, and creation times.

reports/largest_folders_report.csv → Lists the top 10 largest folders.

reports/disk_usage_chart.png → Visual representation of file type distribution.

Future Enhancements

Cleanup Feature: Automatically suggest or delete large unused files.

Scheduling: Set up automatic periodic scans.

Exclude System Files: Prevent scanning unnecessary system folders.

Contributing

Feel free to fork the repository and submit pull requests for improvements.

License

This project is licensed under the MIT License.

