import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import shutil
import re
from pathlib import Path
from collections import defaultdict
import threading
import base64
from io import BytesIO

try:
    import pdfplumber
    from pypdf import PdfReader, PdfWriter
except ImportError:
    pdfplumber = None
    PdfReader = None
    PdfWriter = None

try:
    from PIL import Image, ImageTk
except ImportError:
    Image = None
    ImageTk = None

try:
    import pandas as pd
except ImportError:
    pd = None

try:
    import openpyxl
except ImportError:
    openpyxl = None


class ModernPDFRenamer:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF & Excel Batch Processor - SLCM GROUP")
        self.root.geometry("1200x800")
        self.root.minsize(1100, 750)
        
        self.folder_path = tk.StringVar()
        self.file_path = tk.StringVar()
        self.pdf_files = []
        self.processing = False
        self.current_mode = "pdf_rename"
        
        self.colors = {
            'primary': '#2c3e50',
            'secondary': '#3498db',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'bg': '#ecf0f1',
            'card': '#ffffff',
            'sidebar': '#34495e',
            'sidebar_active': '#2c3e50'
        }
        
        self.set_app_icon()
        
        self.setup_ui()
        self.check_dependencies()
        
    def set_app_icon(self):
        icon_data = """
        iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
        AAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAKkSURB
        VFiFxZdNaBNBFMd/s5vdZJPdJJtNk6ZN06RaW7WKFkVQPHjw4MWbBy9ePXjy5sFLQRBBEAQRBEEQ
        xIMgCIIgiAcRBEEQRLAqrVqr1VrT2jbZr93NzLyZt022GmvBg//lzc68+c2b92YmAs45/udH+N8A
        9QAVABUAlf4HUAFQAVABUP9fAEopQghBCCEIIQQhBCGEIIQQhBCCEEIQQghCCAEAIIQghBD0v68A
        Sinied4c57xN0/RAURT1+/2+4zguAMCyLMuyLMuyLMuyLMuyLMuyLMuyLGtubm52dna2
        oqKiwsLCQrFYLBaLxWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsljocDofL5dLr9Xo9
        Ho/H4/F4PB6Px+PxeDwej8fj8Xg8Ho/H4/F4PB6Px+NxOp1Op9Pp5JxzzvmSJVy2bLnT6XQ6nU4A
        gBBCSinnnHPOOeecc8455/8M4Pf7fYZhGIZhGIZhGIZhGIZhGIZhGIZhGIZhGIZhGIZhGIZhGIZh
        GIZhGIZhGIZhGIZhGIZhGIZhGIZhGIZhmKZpmmVZlmVZlmVZlmVZlmVZlmVZlmVZlmVZlmVZlmVZ
        lmVZlmVZlmVZlmVZlmVZlmVZlmVZlmVZAACEEEII4ZxzzjnnnHPOOef/DKCUUs75kiVLlixZ
        smTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLAPg9APw7AAAAAAAAAAAAAP//
        """
        
        try:
            if Image and ImageTk:
                icon_bytes = base64.b64decode(icon_data.replace('\n', '').replace(' ', ''))
                icon_image = Image.open(BytesIO(icon_bytes))
                icon_photo = ImageTk.PhotoImage(icon_image)
                self.root.iconphoto(True, icon_photo)
        except Exception:
            pass
        
    def setup_ui(self):
        self.root.configure(bg=self.colors['bg'])
        
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True)
        
        self.create_sidebar(main_container)
        
        self.content_frame = tk.Frame(main_container, bg=self.colors['bg'])
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.show_pdf_rename_mode()
        
    def create_sidebar(self, parent):
        sidebar = tk.Frame(parent, bg=self.colors['sidebar'], width=250)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)
        
        title_frame = tk.Frame(sidebar, bg=self.colors['primary'], height=100)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        tk.Label(
            title_frame,
            text="SLCM\nProcessor",
            font=("Segoe UI", 16, "bold"),
            fg="white",
            bg=self.colors['primary'],
            justify=tk.CENTER
        ).pack(expand=True)
        
        tk.Label(
            sidebar,
            text="CATEGORIES",
            font=("Segoe UI", 9, "bold"),
            fg="#95a5a6",
            bg=self.colors['sidebar']
        ).pack(anchor=tk.W, padx=20, pady=(30, 10))
        
        self.sidebar_buttons = {}
        
        categories = [
            ("pdf_rename", "PDF Rename\n(1 Page File)", self.show_pdf_rename_mode),
            ("pdf_split", "PDF Split & Rename\n(Multi Page File)", self.show_pdf_split_mode),
            ("excel_split", "Excel Split & Rename", self.show_excel_split_mode)
        ]
        
        for mode, text, command in categories:
            btn = tk.Button(
                sidebar,
                text=text,
                command=command,
                font=("Segoe UI", 10, "bold"),
                bg=self.colors['sidebar'],
                fg="white",
                relief=tk.FLAT,
                cursor="hand2",
                anchor=tk.W,
                padx=20,
                pady=15,
                bd=0,
                activebackground=self.colors['sidebar_active'],
                activeforeground="white"
            )
            btn.pack(fill=tk.X, padx=5, pady=2)
            self.sidebar_buttons[mode] = btn
        
        self.highlight_sidebar_button("pdf_rename")
        
        footer = tk.Frame(sidebar, bg=self.colors['primary'])
        footer.pack(side=tk.BOTTOM, fill=tk.X)
        
        tk.Label(
            footer,
            text="© 2025 SLCM GROUP\nIT TEAM",
            font=("Segoe UI", 8),
            fg="#95a5a6",
            bg=self.colors['primary'],
            justify=tk.CENTER
        ).pack(pady=15)
        
    def highlight_sidebar_button(self, mode):
        for btn_mode, btn in self.sidebar_buttons.items():
            if btn_mode == mode:
                btn.config(bg=self.colors['sidebar_active'])
            else:
                btn.config(bg=self.colors['sidebar'])
    
    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_pdf_rename_mode(self):
        self.current_mode = "pdf_rename"
        self.highlight_sidebar_button("pdf_rename")
        self.clear_content_frame()
        
        self.create_header(self.content_frame, "PDF Rename (1 Page File)", 
                          "Automatically rename single-page PDFs based on Consignee information")
        
        self.create_folder_section(self.content_frame)
        
        content = tk.Frame(self.content_frame, bg=self.colors['bg'])
        content.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.create_file_list_section(content)
        
        self.create_controls_section(content)
        
    def show_pdf_split_mode(self):
        self.current_mode = "pdf_split"
        self.highlight_sidebar_button("pdf_split")
        self.clear_content_frame()
        
        self.create_header(self.content_frame, "PDF Split & Rename (Multi Page File)", 
                          "Split multi-page PDFs and rename each page based on Consignee information")
        
        self.create_file_selection_section(self.content_frame)
        
        content = tk.Frame(self.content_frame, bg=self.colors['bg'])
        content.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.create_simple_controls_section(content)
        
    def show_excel_split_mode(self):
        self.current_mode = "excel_split"
        self.highlight_sidebar_button("excel_split")
        self.clear_content_frame()
        
        self.create_header(self.content_frame, "Excel Split & Rename", 
                          "Split Excel files by Party Name and Comm Grouping")
        
        self.create_excel_file_selection_section(self.content_frame)
        
        content = tk.Frame(self.content_frame, bg=self.colors['bg'])
        content.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.create_simple_controls_section(content)
    
    def create_header(self, parent, title, subtitle):
        header = tk.Frame(parent, bg=self.colors['primary'], height=100)
        header.pack(fill=tk.X, pady=(0, 20))
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text=title,
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg=self.colors['primary']
        ).pack(pady=(20, 5))
        
        tk.Label(
            header,
            text=subtitle,
            font=("Segoe UI", 9),
            fg="#ecf0f1",
            bg=self.colors['primary']
        ).pack()
    
    def create_folder_section(self, parent):
        folder_frame = tk.LabelFrame(
            parent,
            text=" Select Folder ",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors['card'],
            fg=self.colors['primary'],
            padx=15,
            pady=15
        )
        folder_frame.pack(fill=tk.X, pady=(0, 15))
        
        path_frame = tk.Frame(folder_frame, bg=self.colors['card'])
        path_frame.pack(fill=tk.X)
        
        self.path_entry = tk.Entry(
            path_frame,
            textvariable=self.folder_path,
            font=("Segoe UI", 10),
            relief=tk.FLAT,
            bg="#f8f9fa",
            fg=self.colors['primary']
        )
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))
        
        self.browse_btn = tk.Button(
            path_frame,
            text="Browse Folder",
            command=self.browse_folder,
            font=("Segoe UI", 10, "bold"),
            bg=self.colors['secondary'],
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.browse_btn.pack(side=tk.LEFT)
        
        self.scan_btn = tk.Button(
            path_frame,
            text="Scan PDFs",
            command=self.scan_folder,
            font=("Segoe UI", 10, "bold"),
            bg=self.colors['success'],
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=8,
            state=tk.DISABLED
        )
        self.scan_btn.pack(side=tk.LEFT, padx=(5, 0))
    
    def create_file_selection_section(self, parent):
        file_frame = tk.LabelFrame(
            parent,
            text=" Select PDF File ",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors['card'],
            fg=self.colors['primary'],
            padx=15,
            pady=15
        )
        file_frame.pack(fill=tk.X, pady=(0, 15))
        
        path_frame = tk.Frame(file_frame, bg=self.colors['card'])
        path_frame.pack(fill=tk.X)
        
        self.file_entry = tk.Entry(
            path_frame,
            textvariable=self.file_path,
            font=("Segoe UI", 10),
            relief=tk.FLAT,
            bg="#f8f9fa",
            fg=self.colors['primary']
        )
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))
        
        self.browse_file_btn = tk.Button(
            path_frame,
            text="Browse PDF File",
            command=self.browse_pdf_file,
            font=("Segoe UI", 10, "bold"),
            bg=self.colors['secondary'],
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.browse_file_btn.pack(side=tk.LEFT)
    
    def create_excel_file_selection_section(self, parent):
        file_frame = tk.LabelFrame(
            parent,
            text=" Select Excel File ",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors['card'],
            fg=self.colors['primary'],
            padx=15,
            pady=15
        )
        file_frame.pack(fill=tk.X, pady=(0, 15))
        
        path_frame = tk.Frame(file_frame, bg=self.colors['card'])
        path_frame.pack(fill=tk.X)
        
        self.excel_file_entry = tk.Entry(
            path_frame,
            textvariable=self.file_path,
            font=("Segoe UI", 10),
            relief=tk.FLAT,
            bg="#f8f9fa",
            fg=self.colors['primary']
        )
        self.excel_file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))
        
        self.browse_excel_btn = tk.Button(
            path_frame,
            text="Browse Excel File",
            command=self.browse_excel_file,
            font=("Segoe UI", 10, "bold"),
            bg=self.colors['secondary'],
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.browse_excel_btn.pack(side=tk.LEFT)
    
    def create_file_list_section(self, parent):
        list_frame = tk.LabelFrame(
            parent,
            text=" PDF Files ",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors['card'],
            fg=self.colors['primary'],
            padx=10,
            pady=10
        )
        list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        tree_frame = tk.Frame(list_frame, bg=self.colors['card'])
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        
        self.file_tree = ttk.Treeview(
            tree_frame,
            columns=("checkbox", "name", "status"),
            show="tree headings",
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set,
            selectmode="none"
        )
        
        vsb.config(command=self.file_tree.yview)
        hsb.config(command=self.file_tree.xview)
        
        self.file_tree.heading("#0", text="No.")
        self.file_tree.heading("checkbox", text="[ ]", command=self.toggle_all_checkboxes)
        self.file_tree.heading("name", text="File Name")
        self.file_tree.heading("status", text="Status")
        
        self.file_tree.column("#0", width=50, stretch=False)
        self.file_tree.column("checkbox", width=40, stretch=False, anchor="center")
        self.file_tree.column("name", width=280)
        self.file_tree.column("status", width=100)
        
        self.file_tree.bind('<Button-1>', self.on_tree_click)
        
        self.file_tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        selection_frame = tk.Frame(list_frame, bg=self.colors['card'])
        selection_frame.pack(fill=tk.X, pady=(10, 5))
        
        self.select_all_btn = tk.Button(
            selection_frame,
            text="Select All",
            command=self.select_all,
            font=("Segoe UI", 9),
            bg="#27ae60",
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            pady=6,
            padx=10
        )
        self.select_all_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 4))
        
        self.deselect_all_btn = tk.Button(
            selection_frame,
            text="Deselect All",
            command=self.deselect_all,
            font=("Segoe UI", 9),
            bg="#e74c3c",
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            pady=6,
            padx=10
        )
        self.deselect_all_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(2, 2))
        
        self.invert_btn = tk.Button(
            selection_frame,
            text="Invert",
            command=self.invert_selection,
            font=("Segoe UI", 9),
            bg="#9b59b6",
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            pady=6,
            padx=10
        )
        self.invert_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(4, 0))
        
        self.count_label = tk.Label(
            list_frame,
            text="No PDFs loaded",
            font=("Segoe UI", 9),
            bg=self.colors['card'],
            fg=self.colors['primary']
        )
        self.count_label.pack(pady=(5, 0))
        
        self.checkbox_states = {}
    
    def create_controls_section(self, parent):
        control_frame = tk.Frame(parent, bg=self.colors['bg'])
        control_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        btn_frame = tk.LabelFrame(
            control_frame,
            text=" Actions ",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors['card'],
            fg=self.colors['primary'],
            padx=15,
            pady=15
        )
        btn_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.rename_btn = tk.Button(
            btn_frame,
            text="Rename Selected PDFs",
            command=self.start_rename_process,
            font=("Segoe UI", 11, "bold"),
            bg=self.colors['success'],
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            pady=12,
            state=tk.DISABLED
        )
        self.rename_btn.pack(fill=tk.X, pady=(0, 10))
        
        self.open_folder_btn = tk.Button(
            btn_frame,
            text="Open Output Folder",
            command=self.open_output_folder,
            font=("Segoe UI", 10),
            bg=self.colors['secondary'],
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            pady=10
        )
        self.open_folder_btn.pack(fill=tk.X, pady=(0, 10))
        
        self.refresh_btn = tk.Button(
            btn_frame,
            text="Refresh",
            command=self.scan_folder,
            font=("Segoe UI", 9),
            bg="#95a5a6",
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            pady=8
        )
        self.refresh_btn.pack(fill=tk.X)
        
        self.progress = ttk.Progressbar(btn_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=(15, 0))
        
        self.create_log_section(control_frame)
    
    def create_simple_controls_section(self, parent):
        control_frame = tk.Frame(parent, bg=self.colors['bg'])
        control_frame.pack(fill=tk.BOTH, expand=True)
        
        btn_frame = tk.LabelFrame(
            control_frame,
            text=" Actions ",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors['card'],
            fg=self.colors['primary'],
            padx=15,
            pady=15
        )
        btn_frame.pack(fill=tk.X, pady=(0, 10))
        
        if self.current_mode == "pdf_split":
            process_text = "Split & Rename PDF"
            process_cmd = self.start_pdf_split_process
        else:
            process_text = "Split & Rename Excel"
            process_cmd = self.start_excel_split_process
        
        self.process_btn = tk.Button(
            btn_frame,
            text=process_text,
            command=process_cmd,
            font=("Segoe UI", 11, "bold"),
            bg=self.colors['success'],
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            pady=12
        )
        self.process_btn.pack(fill=tk.X, pady=(0, 10))
        
        self.open_output_btn = tk.Button(
            btn_frame,
            text="Open Output Folder",
            command=self.open_output_folder_simple,
            font=("Segoe UI", 10),
            bg=self.colors['secondary'],
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            pady=10
        )
        self.open_output_btn.pack(fill=tk.X)
        
        self.progress = ttk.Progressbar(btn_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=(15, 0))
        
        self.create_log_section(control_frame)
    
    def create_log_section(self, parent):
        log_frame = tk.LabelFrame(
            parent,
            text=" Activity Log ",
            font=("Segoe UI", 11, "bold"),
            bg=self.colors['card'],
            fg=self.colors['primary'],
            padx=10,
            pady=10
        )
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        log_scroll = tk.Scrollbar(log_frame)
        log_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.log_text = tk.Text(
            log_frame,
            wrap=tk.WORD,
            font=("Consolas", 9),
            bg="#f8f9fa",
            fg=self.colors['primary'],
            relief=tk.FLAT,
            yscrollcommand=log_scroll.set
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        log_scroll.config(command=self.log_text.yview)
        
        self.log_text.tag_config("info", foreground="#3498db")
        self.log_text.tag_config("success", foreground="#27ae60")
        self.log_text.tag_config("warning", foreground="#f39c12")
        self.log_text.tag_config("error", foreground="#e74c3c")
    
    def log(self, message, level="info"):
        self.log_text.insert(tk.END, message + "\n", level)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def check_dependencies(self):
        missing = []
        if pdfplumber is None:
            missing.append("pdfplumber")
        if PdfReader is None:
            missing.append("pypdf")
        if pd is None:
            missing.append("pandas")
        if openpyxl is None:
            missing.append("openpyxl")
        
        if missing:
            self.log(f"Missing dependencies: {', '.join(missing)}", "warning")
            self.log("Install with: pip install pdfplumber pypdf pandas openpyxl", "info")
    
    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select Folder Containing PDFs")
        if folder:
            self.folder_path.set(folder)
            self.scan_btn.config(state=tk.NORMAL)
            self.log(f"Folder selected: {folder}", "info")
            self.scan_folder()
    
    def browse_pdf_file(self):
        file = filedialog.askopenfilename(
            title="Select Multi-Page PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if file:
            self.file_path.set(file)
            self.log(f"File selected: {os.path.basename(file)}", "info")
    
    def browse_excel_file(self):
        file = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if file:
            self.file_path.set(file)
            self.log(f"File selected: {os.path.basename(file)}", "info")
    
    def scan_folder(self):
        folder = self.folder_path.get()
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid folder")
            return
        
        self.file_tree.delete(*self.file_tree.get_children())
        self.pdf_files = []
        self.checkbox_states = {}
        
        self.log("Scanning for PDF files...", "info")
        
        for file in os.listdir(folder):
            if file.lower().endswith('.pdf'):
                file_path = os.path.join(folder, file)
                self.pdf_files.append(file_path)
                idx = len(self.pdf_files)
                
                item_id = self.file_tree.insert("", tk.END, values=("[ ]", file, "Ready"), text=str(idx))
                self.checkbox_states[item_id] = False
        
        if self.pdf_files:
            count = len(self.pdf_files)
            self.count_label.config(text=f"Found {count} PDF file(s) | 0 selected")
            self.log(f"Found {count} PDF file(s)", "success")
            self.rename_btn.config(state=tk.NORMAL)
        else:
            self.count_label.config(text="No PDF files found")
            self.log("No PDF files found in folder", "error")
            messagebox.showwarning("No PDFs", "No PDF files found in the selected folder")
    
    def on_tree_click(self, event):
        region = self.file_tree.identify_region(event.x, event.y)
        column = self.file_tree.identify_column(event.x)
        
        if region == "cell" and column == "#1":
            item = self.file_tree.identify_row(event.y)
            if item:
                self.toggle_checkbox(item)
    
    def toggle_checkbox(self, item):
        current_state = self.checkbox_states.get(item, False)
        new_state = not current_state
        self.checkbox_states[item] = new_state
        
        values = list(self.file_tree.item(item)['values'])
        values[0] = "[X]" if new_state else "[ ]"
        self.file_tree.item(item, values=values)
        
        self.update_selection_count()
    
    def toggle_all_checkboxes(self):
        any_checked = any(self.checkbox_states.values())
        
        if any_checked:
            self.deselect_all()
        else:
            self.select_all()
    
    def select_all(self):
        for item in self.file_tree.get_children():
            self.checkbox_states[item] = True
            values = list(self.file_tree.item(item)['values'])
            values[0] = "[X]"
            self.file_tree.item(item, values=values)
        
        self.update_selection_count()
    
    def deselect_all(self):
        for item in self.file_tree.get_children():
            self.checkbox_states[item] = False
            values = list(self.file_tree.item(item)['values'])
            values[0] = "[ ]"
            self.file_tree.item(item, values=values)
        
        self.update_selection_count()
    
    def invert_selection(self):
        for item in self.file_tree.get_children():
            current_state = self.checkbox_states.get(item, False)
            new_state = not current_state
            self.checkbox_states[item] = new_state
            
            values = list(self.file_tree.item(item)['values'])
            values[0] = "[X]" if new_state else "[ ]"
            self.file_tree.item(item, values=values)
        
        self.update_selection_count()
    
    def update_selection_count(self):
        total = len(self.pdf_files)
        selected = sum(1 for checked in self.checkbox_states.values() if checked)
        self.count_label.config(text=f"Found {total} PDF file(s) | {selected} selected")
    
    def get_selected_items(self):
        return [item for item, checked in self.checkbox_states.items() if checked]
    
    def extract_consignee_name(self, pdf_path):
        if pdfplumber is None:
            return None
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = ""
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
            
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if re.search(r"Consignee\s*\(Ship\s*to\)", line, re.IGNORECASE):
                    for j in range(i + 1, min(i + 5, len(lines))):
                        candidate = lines[j].strip()
                        if candidate:
                            name = self.clean_consignee_name(candidate)
                            if name:
                                return name
            return None
            
        except Exception as e:
            self.log(f"Error reading PDF: {str(e)}", "error")
            return None
    
    def clean_consignee_name(self, text):
        patterns = [
            r"Buyer'?s?\s*Order\s*No\.?",
            r"Dated",
            r"GSTIN",
            r"State\s*Name",
            r"Invoice\s*No\.?",
            r"Address",
            r"Buyer"
        ]
        
        for pattern in patterns:
            text = re.split(pattern, text, flags=re.IGNORECASE)[0].strip()
        
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text if text else None
    
    def start_rename_process(self):
        if self.processing:
            return
        
        selected = self.get_selected_items()
        if not selected:
            messagebox.showwarning("No Selection", "Please select at least one PDF file")
            return
        
        self.processing = True
        self.rename_btn.config(state=tk.DISABLED)
        self.scan_btn.config(state=tk.DISABLED)
        self.progress.start(10)
        
        thread = threading.Thread(target=self.rename_single_page_pdf, args=(selected,))
        thread.daemon = True
        thread.start()
    
    def rename_single_page_pdf(self, selected_items):
        folder = self.folder_path.get()
        output_folder = os.path.join(folder, "output")
        
        try:
            os.makedirs(output_folder, exist_ok=True)
            self.log(f"Output folder: {output_folder}", "info")
        except Exception as e:
            self.log(f"Failed to create output folder: {str(e)}", "error")
            self.finish_processing()
            return
        
        name_counts = defaultdict(int)
        success_count = 0
        
        self.log("\n" + "="*50, "info")
        self.log("Starting rename process...", "info")
        self.log("="*50 + "\n", "info")
        
        for item in selected_items:
            values = self.file_tree.item(item)['values']
            original_name = values[1]
            
            pdf_path = None
            for path in self.pdf_files:
                if os.path.basename(path) == original_name:
                    pdf_path = path
                    break
            
            if not pdf_path:
                continue
            
            self.log(f"Processing: {original_name}", "info")
            self.file_tree.item(item, values=(values[0], original_name, "Processing..."))
            
            consignee_name = self.extract_consignee_name(pdf_path)
            
            if not consignee_name:
                self.log(f"  Could not find consignee name", "warning")
                self.file_tree.item(item, values=(values[0], original_name, "Failed"))
                continue
            
            name_counts[consignee_name] += 1
            count = name_counts[consignee_name]
            
            if count > 1:
                new_name = f"{consignee_name} - {count}.pdf"
            else:
                new_name = f"{consignee_name}.pdf"
            
            new_path = os.path.join(output_folder, new_name)
            
            try:
                shutil.copy2(pdf_path, new_path)
                self.log(f"  Renamed to: {new_name}", "success")
                self.file_tree.item(item, values=(values[0], original_name, "Done"))
                success_count += 1
            except Exception as e:
                self.log(f"  Error: {str(e)}", "error")
                self.file_tree.item(item, values=(values[0], original_name, "Error"))
        
        self.log("\n" + "="*50, "info")
        self.log(f"Complete! Successfully renamed {success_count} file(s)", "success")
        self.log("="*50 + "\n", "info")
        
        self.finish_processing()
        
        messagebox.showinfo(
            "Complete",
            f"Successfully renamed {success_count} PDF file(s)!\n\nOutput: {output_folder}"
        )
    
    def start_pdf_split_process(self):
        file_path = self.file_path.get()
        if not file_path or not os.path.exists(file_path):
            messagebox.showerror("Error", "Please select a valid PDF file")
            return
        
        if PdfReader is None or PdfWriter is None:
            messagebox.showerror("Error", "pypdf library is required. Install with: pip install pypdf")
            return
        
        self.processing = True
        self.process_btn.config(state=tk.DISABLED)
        self.progress.start(10)
        
        thread = threading.Thread(target=self.split_and_rename_multi_page_pdf, args=(file_path,))
        thread.daemon = True
        thread.start()
    
    def split_and_rename_multi_page_pdf(self, pdf_path):
        output_folder = os.path.join(os.path.dirname(pdf_path), "output")
        
        try:
            os.makedirs(output_folder, exist_ok=True)
            self.log(f"Output folder: {output_folder}", "info")
        except Exception as e:
            self.log(f"Failed to create output folder: {str(e)}", "error")
            self.finish_processing()
            return
        
        self.log("\n" + "="*50, "info")
        self.log("Starting PDF split & rename process...", "info")
        self.log(f"Source: {os.path.basename(pdf_path)}", "info")
        self.log("="*50 + "\n", "info")
        
        try:
            reader = PdfReader(pdf_path)
            total_pages = len(reader.pages)
            self.log(f"Total pages: {total_pages}", "info")
            
            name_counts = defaultdict(int)
            success_count = 0
            
            for page_num in range(total_pages):
                self.log(f"\nProcessing page {page_num + 1}/{total_pages}...", "info")
                
                writer = PdfWriter()
                writer.add_page(reader.pages[page_num])
                
                temp_path = os.path.join(output_folder, f"temp_page_{page_num + 1}.pdf")
                with open(temp_path, 'wb') as temp_file:
                    writer.write(temp_file)
                
                consignee_name = self.extract_consignee_name(temp_path)
                
                if consignee_name:
                    name_counts[consignee_name] += 1
                    count = name_counts[consignee_name]
                    
                    if count > 1:
                        new_name = f"{consignee_name} - {count}.pdf"
                    else:
                        new_name = f"{consignee_name}.pdf"
                    
                    final_path = os.path.join(output_folder, new_name)
                    
                    try:
                        os.rename(temp_path, final_path)
                        self.log(f"  Saved as: {new_name}", "success")
                        success_count += 1
                    except Exception as e:
                        self.log(f"  Error renaming: {str(e)}", "error")
                        try:
                            os.remove(temp_path)
                        except:
                            pass
                else:
                    fallback_name = f"Page_{page_num + 1}.pdf"
                    fallback_path = os.path.join(output_folder, fallback_name)
                    try:
                        os.rename(temp_path, fallback_path)
                        self.log(f"  No consignee found, saved as: {fallback_name}", "warning")
                    except Exception as e:
                        self.log(f"  Error: {str(e)}", "error")
                        try:
                            os.remove(temp_path)
                        except:
                            pass
            
            self.log("\n" + "="*50, "info")
            self.log(f"Complete! Successfully processed {success_count}/{total_pages} page(s)", "success")
            self.log("="*50 + "\n", "info")
            
            self.finish_processing()
            
            messagebox.showinfo(
                "Complete",
                f"Split and renamed {success_count} out of {total_pages} pages!\n\nOutput: {output_folder}"
            )
            
        except Exception as e:
            self.log(f"Error processing PDF: {str(e)}", "error")
            self.finish_processing()
            messagebox.showerror("Error", f"Failed to process PDF:\n\n{str(e)}")
    
    def start_excel_split_process(self):
        file_path = self.file_path.get()
        if not file_path or not os.path.exists(file_path):
            messagebox.showerror("Error", "Please select a valid Excel file")
            return
        
        if pd is None:
            messagebox.showerror("Error", "pandas library is required. Install with: pip install pandas openpyxl")
            return
        
        self.processing = True
        self.process_btn.config(state=tk.DISABLED)
        self.progress.start(10)
        
        thread = threading.Thread(target=self.split_excel_by_party_and_comm, args=(file_path,))
        thread.daemon = True
        thread.start()
    
    def split_excel_by_party_and_comm(self, excel_path):
        output_folder = os.path.join(os.path.dirname(excel_path), "output")
        
        try:
            os.makedirs(output_folder, exist_ok=True)
            self.log(f"Output folder: {output_folder}", "info")
        except Exception as e:
            self.log(f"Failed to create output folder: {str(e)}", "error")
            self.finish_processing()
            return
        
        self.log("\n" + "="*50, "info")
        self.log("Starting Excel split & rename process...", "info")
        self.log(f"Source: {os.path.basename(excel_path)}", "info")
        self.log("="*50 + "\n", "info")
        
        try:
            if excel_path.lower().endswith('.csv'):
                df = pd.read_csv(excel_path)
            else:
                df = pd.read_excel(excel_path)
            
            self.log(f"Total rows: {len(df)}", "info")
            self.log(f"Columns: {', '.join(df.columns.tolist())}", "info")
            
            party_col = None
            comm_col = None
            
            for col in df.columns:
                col_lower = col.lower().strip()
                if 'party' in col_lower and 'name' in col_lower:
                    party_col = col
                if 'comm' in col_lower and 'group' in col_lower:
                    comm_col = col
            
            if not party_col:
                self.log("Could not find 'Party Name' column", "error")
                self.finish_processing()
                messagebox.showerror("Error", "Could not find 'Party Name' column in the Excel file")
                return
            
            if not comm_col:
                self.log("Could not find 'Comm grouping' column", "error")
                self.finish_processing()
                messagebox.showerror("Error", "Could not find 'Comm grouping' column in the Excel file")
                return
            
            self.log(f"Using columns: '{party_col}' and '{comm_col}'", "success")
            
            grouped = df.groupby([party_col, comm_col])
            
            success_count = 0
            
            for (party, comm), group_df in grouped:
                party_clean = re.sub(r'[^a-zA-Z0-9\s]', '', str(party))
                party_clean = re.sub(r'\s+', ' ', party_clean).strip()
                
                comm_clean = re.sub(r'[^a-zA-Z0-9\s]', '', str(comm))
                comm_clean = re.sub(r'\s+', ' ', comm_clean).strip()
                
                filename = f"{party_clean}_{comm_clean}.xlsx"
                output_path = os.path.join(output_folder, filename)
                
                try:
                    group_df.to_excel(output_path, index=False, engine='openpyxl')
                    self.log(f"Created: {filename} ({len(group_df)} rows)", "success")
                    success_count += 1
                except Exception as e:
                    self.log(f"Error creating {filename}: {str(e)}", "error")
            
            self.log("\n" + "="*50, "info")
            self.log(f"Complete! Created {success_count} Excel file(s)", "success")
            self.log("="*50 + "\n", "info")
            
            self.finish_processing()
            
            messagebox.showinfo(
                "Complete",
                f"Successfully split into {success_count} Excel file(s)!\n\nOutput: {output_folder}"
            )
            
        except Exception as e:
            self.log(f"Error processing Excel: {str(e)}", "error")
            self.finish_processing()
            messagebox.showerror("Error", f"Failed to process Excel file:\n\n{str(e)}")
    
    def finish_processing(self):
        self.processing = False
        self.progress.stop()
        
        if self.current_mode == "pdf_rename":
            self.rename_btn.config(state=tk.NORMAL)
            self.scan_btn.config(state=tk.NORMAL)
        else:
            self.process_btn.config(state=tk.NORMAL)
    
    def open_output_folder(self):
        folder = self.folder_path.get()
        if folder:
            output_folder = os.path.join(folder, "output")
            if os.path.exists(output_folder):
                os.startfile(output_folder)
            else:
                messagebox.showinfo("Info", "Output folder doesn't exist yet!")
    
    def open_output_folder_simple(self):
        file = self.file_path.get()
        if file:
            output_folder = os.path.join(os.path.dirname(file), "output")
            if os.path.exists(output_folder):
                os.startfile(output_folder)
            else:
                messagebox.showinfo("Info", "Output folder doesn't exist yet!")


def main():
    root = tk.Tk()
    app = ModernPDFRenamer(root)
    root.mainloop()


if __name__ == "__main__":
    main()