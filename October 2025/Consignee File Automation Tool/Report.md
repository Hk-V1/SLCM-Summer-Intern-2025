# Consignee File Automation Tool

A desktop application built with Tkinter for automating PDF and Excel file processing tasks, including renaming, splitting, and organizing consignee-related files.

## Features
- **PDF Rename (1 Page File):**  
  Automatically extracts consignee names from single-page PDFs and renames files accordingly.

- **PDF Split & Rename (Multi Page File):**  
  Splits multi-page PDFs into individual pages and renames each file using extracted consignee details.

- **Excel Split & Rename:**  
  Splits Excel files by columns such as *Party Name* or *Comm Grouping* and saves organized output files.

- **Smart UI:**  
  Simple and modern interface with mode switching, live progress tracking, and color-coded activity logs.

- **Threaded Execution:**  
  Handles heavy operations in the background without freezing the interface.

## Tech Stack
- Python 3  
- Tkinter (GUI)  
- PyPDF2, pdfplumber  
- Pandas, OpenPyXL

## Installation
Install all dependencies before running the tool:
```bash
pip install PyPDF2 pdfplumber pandas openpyxl
```

## Usage
- Launch the application.
- Select the desired mode from the sidebar.
- Choose the input folder or file.
- Click Start Processing to begin.
- View progress and logs in real time.

## Notes
- Ensure input files are properly formatted.
- PDF files must contain readable text for name extraction.
- Output files are automatically renamed and saved in the selected directory.
