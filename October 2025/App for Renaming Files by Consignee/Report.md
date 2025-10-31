# Consignee-Based PDF Renaming Tool  

## Summary  
A Python-based Windows desktop application that uploads a ZIP of PDFs, extracts each file’s “Consignee (Ship to)” name, renames the files accordingly by removing unwanted text such as “Buyer's Order No.” or “Dated,” and exports them as a new ZIP file.  

---

## Tech Stack  

**Language:** Python 3  
**GUI:** Tkinter  
**Libraries:** pdfplumber, zipfile, tempfile, shutil, re, os, uuid, pathlib  

---

## Features  

- Upload a ZIP file containing multiple PDFs  
- Extract all PDF files and display them in a file list panel  
- Automatically detect “Consignee (Ship to)” or “Ship to” fields  
- Clean extracted names by removing unnecessary text  
- Rename files based on consignee names and handle duplicates with serial numbers  
- Export all renamed PDFs as a new ZIP file  

---

## Workflow  

1. Upload a ZIP file containing PDFs  
2. Extract all PDFs to a temporary directory  
3. Select the files and click “Rename”  
4. The application reads each consignee name and renames the files accordingly  
5. Download or save the final renamed ZIP file  

---

## Use Case  

This tool is designed for logistics, shipping, and documentation teams to automate the process of renaming shipment or invoice PDFs based on consignee names. It helps maintain organized file structures, reduces manual effort, and ensures consistent naming conventions across multiple documents.  
