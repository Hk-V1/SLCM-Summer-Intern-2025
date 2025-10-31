# Project Summaries

---

## 1. Consignee-Based PDF Renaming Tool

### Summary  
A Python-based desktop utility that uploads a ZIP of PDFs, extracts each file’s “Consignee (Ship to)” name, cleans it by removing unwanted text like “Buyer’s Order No.” or “Dated,” and renames the PDFs automatically. The processed files are then exported as a new ZIP.

### Workflow  
1. Upload a ZIP file containing PDFs  
2. Extract all files to a temporary directory  
3. Automatically detect consignee names from each PDF  
4. Clean and rename files, handling duplicates with serial numbers  
5. Export the renamed PDFs as a new ZIP file  

### Tech Stack  
- Language: Python 3  
- GUI: Tkinter  
- Libraries: pdfplumber, zipfile, tempfile, shutil, re, os, uuid, pathlib  

### Use Case  
Ideal for logistics, shipping, and documentation teams to automate the renaming of shipment or invoice PDFs based on consignee names — improving organization, accuracy, and efficiency.

---

## 2. Consignee File Automation Tool

### Summary  
A desktop application built with Tkinter that automates PDF and Excel file processing — including renaming, splitting, and organizing consignee-related files. It features a clean user interface, mode switching, real-time progress tracking, and background task execution.

### Features  
- **PDF Rename (1 Page File):** Automatically extracts consignee names from single-page PDFs and renames files accordingly.  
- **PDF Split & Rename (Multi Page File):** Splits multi-page PDFs into individual pages and renames each using extracted consignee details.  
- **Excel Split & Rename:** Splits Excel files by columns such as *Party Name* or *Comm Grouping* and organizes outputs.  
- **Smart UI:** Simple and modern interface with mode switching, live progress tracking, and color-coded logs.  
- **Threaded Execution:** Handles heavy operations in the background without freezing the interface.  

### Tech Stack  
- Language: Python 3  
- GUI: Tkinter  
- Libraries: PyPDF2, pdfplumber, pandas, openpyxl  

### Usage  
1. Launch the application  
2. Select the desired mode from the sidebar  
3. Choose the input folder or file  
4. Click “Start Processing” to begin  
5. View progress and logs in real time  

---

## 3. Job Scheduler Dashboard

### Summary  
A full-stack system for creating, managing, and monitoring background jobs in real time. Built with Django, Celery, Redis, and Next.js, it provides live analytics, job history, and secure multi-user access.

### Features  
- Job Management: Create, edit, delete, and schedule background jobs  
- Real-Time Monitoring: Live job updates via WebSockets  
- Analytics: Success and failure statistics with execution logs  
- Authentication: Secure multi-user access  
- Responsive UI: Modern dashboard with interactive charts and live progress  

### Workflow  
1. User schedules a job through the dashboard  
2. The Django REST API adds the job to the Celery queue  
3. Redis manages communication between Celery workers  
4. Job progress updates are sent through Channels and WebSockets  
5. The frontend dashboard displays live updates and analytics  

### Tech Stack  
- Backend: Django, Django REST Framework, Celery, Redis, Channels, PostgreSQL  
- Frontend: Next.js, Tailwind CSS, Axios, WebSockets  
- Deployment: Render (API) · Vercel (Dashboard)  

### Links  
- Backend (API): [https://job-schedulers-dashboard.onrender.com](https://job-schedulers-dashboard.onrender.com)  
- Frontend (UI): [https://job-schedulers-dashboard.vercel.app/login](https://job-schedulers-dashboard.vercel.app/login)  

---

## 4. Wheat Disease Recognition & Treatment Advisor

### Summary  
An AI-powered web app for detecting wheat leaf diseases and recommending treatments using deep learning. The system analyzes uploaded leaf images, classifies diseases, and provides treatment suggestions to assist farmers and agricultural experts.

### Features  
- Detects six wheat diseases with confidence scores  
- Provides expert treatment recommendations  
- Includes a responsive interface with history tracking  
- Supports real-time image uploads and preprocessing  

### Disease and Treatment Table  

| Disease | Treatment |
|----------|------------|
| Healthy | Monitor regularly |
| Wheat Rust | Triazole or strobilurin fungicides |
| Leaf Blight | Mancozeb 75 WP, reduce irrigation |
| Powdery Mildew | Sulfur dust or Hexaconazole |
| Septoria Leaf Spot | Propiconazole, improve drainage |
| Fusarium Head Blight | Tebuconazole, seed quality control |

### Tech Stack  
- Language: Python 3.13+  
- Frameworks: Streamlit, PyTorch/TensorFlow  
- Libraries: Pillow, NumPy  
- Model Format: .pth / .h5  

### Future Scope  
- Real-time camera input  
- Batch processing for multiple images  
- PDF report generation  
- Multi-language support  
- Mobile app (TensorFlow Lite)  
- API integration with FastAPI
  
