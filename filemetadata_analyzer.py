import os
import subprocess
import threading
from colorama import init, Fore
from tabulate import tabulate
from datetime import datetime

init(autoreset=True)

# Constants
EXIFTOOL_PATH = os.path.join("tools", "exiftool-13.21_64", "exiftool.exe")
VERSION = "v1.0"
AUTHOR = "Created by Mr. Sami"
REPORTS_FOLDER = "reports"

# 🔥 ASCII Banner
BANNER = f"""
{Fore.CYAN}
███████╗███╗   ███╗██╗   ██╗███████╗ █████╗ ███╗   ███╗██╗
██╔════╝████╗ ████║██║   ██║██╔════╝██╔══██╗████╗ ████║██║
███████╗██╔████╔██║██║   ██║███████╗███████║██╔████╔██║██║
╚════██║██║╚██╔╝██║██║   ██║╚════██║██╔══██║██║╚██╔╝██║██║
███████║██║ ╚═╝ ██║╚██████╔╝███████║██║  ██║██║ ╚═╝ ██║██║
╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  
    {Fore.YELLOW}Metadata Extraction Tool {VERSION} - {AUTHOR}
{Fore.RESET}
"""

def print_banner():
    print(BANNER)

def get_files():
    files_folder_path = input(Fore.GREEN + "📂 Enter Folder Path for Metadata Extraction: ")
    
    if not os.path.exists(files_folder_path):
        print(Fore.RED + "❌ Error: Folder not found. Please enter a valid path.")
        return []

    print(Fore.YELLOW + "🔍 Scanning Files...")
    return [os.path.join(files_folder_path, j) for j in os.listdir(files_folder_path)]

def generate_html_report(file_name, metadata):
    # Create reports folder if it doesn't exist
    os.makedirs(REPORTS_FOLDER, exist_ok=True)

    # HTML Template with Hacker Style
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Metadata Report - {file_name}</title>
        <style>
            body {{
                background-color: #0d0d0d;
                color: #00ff00;
                font-family: 'Courier New', Courier, monospace;
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                color: #00ff00;
                text-align: center;
            }}
            pre {{
                background-color: #1a1a1a;
                padding: 15px;
                border-radius: 5px;
                border: 1px solid #00ff00;
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
            .footer {{
                text-align: center;
                margin-top: 20px;
                font-size: 0.8em;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <h1>📄 Metadata Report for {file_name}</h1>
        <pre>{metadata}</pre>
        <div class="footer">
            Generated by {AUTHOR} | {VERSION} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        </div>
    </body>
    </html>
    """

    # Save HTML report
    report_file = os.path.join(REPORTS_FOLDER, f"{file_name}_report.html")
    with open(report_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    return report_file

def extract_metadata(file_path, results):
    file_name = os.path.basename(file_path)
    print(Fore.CYAN + f"🔧 Extracting metadata for: {file_name}")

    try:
        # Run ExifTool and capture output
        result = subprocess.run([EXIFTOOL_PATH, file_path], capture_output=True, text=True)
        metadata = result.stdout

        # Generate HTML report
        report_file = generate_html_report(file_name, metadata)
        results.append((file_name, "✔ Extracted", report_file))  # Store result for table
    except Exception as e:
        results.append((file_name, "❌ Failed", str(e)))

def extract_all_metadata():
    files = get_files()
    if not files:
        return

    results = []
    threads = []

    print(Fore.BLUE + "🚀 Extracting metadata (multi-threaded)...")

    for file in files:
        if os.path.isfile(file):
            thread = threading.Thread(target=extract_metadata, args=(file, results))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    print(Fore.GREEN + "\n✅ Metadata Extraction Completed!\n")
    
    # 📋 Display results in table format
    print(tabulate(results, headers=["File Name", "Status", "Report File"], tablefmt="fancy_grid"))

def extract_one_file():
    file_path = input(Fore.GREEN + "📄 Enter File Path: ")

    if not os.path.isfile(file_path):
        print(Fore.RED + "❌ Error: Invalid file. Please enter a correct file path.")
        return

    results = []
    extract_metadata(file_path, results)
    print(Fore.CYAN + f"\n✔ Metadata extracted for: {file_path}")
    print(Fore.CYAN + f"📄 Report saved at: {results[0][2]}\n")

def main():
    print_banner()
    while True:
        print(Fore.YELLOW + "1️⃣ Extract Metadata from All Files in a Folder")
        print(Fore.YELLOW + "2️⃣ Extract Metadata from a Single File")
        print(Fore.YELLOW + "3️⃣ Exit\n")

        choice = input(Fore.GREEN + "🎯 Select an option (1-3): ")
        
        if choice == "1":
            extract_all_metadata()
        elif choice == "2":
            extract_one_file()
        elif choice == "3":
            print(Fore.MAGENTA + "👋 Exiting... Have a great day!")
            break
        else:
            print(Fore.RED + "❌ Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()