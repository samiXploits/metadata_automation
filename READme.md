# File Metadata Analyzer

## Overview
File Metadata Analyzer is a powerful tool for extracting metadata from files using ExifTool. It allows users to analyze files in bulk or individually, generating detailed reports in an easy-to-read HTML format.

## Features
- 🔍 Extract metadata from all files in a specified folder.
- 📂 Extract metadata from a single file.
- 📄 Generate HTML reports with a hacker-style theme.
- 🚀 Multi-threaded metadata extraction for faster processing.
- 🖥️ User-friendly command-line interface.

## Requirements
- Python 3.x
- `colorama` (for colored terminal output)
- `tabulate` (for displaying results in a tabular format)
- `ExifTool` (required for metadata extraction)

### Install Dependencies
Run the following command to install required Python modules:
```bash
pip install colorama tabulate
```

Ensure that ExifTool is available in the specified path:
```
tools/exiftool-13.21_64/exiftool.exe
```

## Usage
### Run the Script
To start the tool, use:
```bash
python filemetadata_analyzer.py
```

### Options
1️⃣ Extract metadata from all files in a folder.
2️⃣ Extract metadata from a single file.
3️⃣ Exit the program.

### Example
1. Extract metadata from a folder:
   - Enter the path to the folder when prompted.
   - The script scans and extracts metadata from all files in the folder.
   - An HTML report is generated for each file.

2. Extract metadata from a single file:
   - Enter the path to the file when prompted.
   - The metadata is extracted and an HTML report is created.

## Output
Reports are saved in the `reports/` folder with the format:
```
reports/{file_name}_report.html


Also Unzip the Tools.zip then it works
```

## Author
👤 Mr. Sami

## License
This project is licensed under the MIT License.

