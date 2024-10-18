import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as con

# Function to connect to the database
def db_connection():
    return con.connect(
        host="localhost",
        user="root",
        password="krishna",
        database="medical"
    )

# Color scheme
COLORS = {
    "bg": "#F0F4F8",
    "button": "#4A90E2",
    "button_text": "#FFFFFF",
    "frame": "#E1E8ED",
    "text": "#2C3E50"
}

# Styles
def configure_styles():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', background=COLORS['button'], foreground=COLORS['button_text'], font=('Arial', 10, 'bold'), padding=5)
    style.configure('TLabel', background=COLORS['frame'], foreground=COLORS['text'], font=('Arial', 10))
    style.configure('TEntry', fieldbackground='#FFFFFF', font=('Arial', 10))

# Menu 1: Medicine Section
def menu1():
    clear_main_frame()
    medicine_frame = ttk.Frame(main_frame, style='TFrame')
    medicine_frame.pack(pady=20, padx=20, fill='both', expand=True)

    ttk.Label(medicine_frame, text="Medicine Section", font=('Arial', 16, 'bold'), background=COLORS['frame']).pack(pady=10)

    fields = ["Medicine ID", "Medicine Name", "Category", "Dosage (mg)", "Manufacturer", "Expiry Date", "Price", "Stock Quantity", "Prescription Required"]
    entries = []

    for i, field in enumerate(fields):
        row_frame = ttk.Frame(medicine_frame, style='TFrame')
        row_frame.pack(fill='x', padx=5, pady=5)
        ttk.Label(row_frame, text=field, width=20).pack(side='left')
        entry = ttk.Entry(row_frame)
        entry.pack(side='left', expand=True, fill='x')
        entries.append(entry)

    ttk.Button(medicine_frame, text="Insert Medicine", command=lambda: insert_medicine(entries)).pack(pady=10)

def insert_medicine(entries):
    # Implementation remains the same
    pass

# Menu 2: Customer Section
def menu2():
    clear_main_frame()
    customer_frame = ttk.Frame(main_frame, style='TFrame')
    customer_frame.pack(pady=20, padx=20, fill='both', expand=True)

    ttk.Label(customer_frame, text="Customer Section", font=('Arial', 16, 'bold'), background=COLORS['frame']).pack(pady=10)

    fields = ["Customer ID", "First Name", "Last Name", "Email", "Phone Number", "Address", "Date of Birth", "Medicine ID", "Purchase Date"]
    entries = []

    for i, field in enumerate(fields):
        row_frame = ttk.Frame(customer_frame, style='TFrame')
        row_frame.pack(fill='x', padx=5, pady=5)
        ttk.Label(row_frame, text=field, width=20).pack(side='left')
        entry = ttk.Entry(row_frame)
        entry.pack(side='left', expand=True, fill='x')
        entries.append(entry)

    ttk.Button(customer_frame, text="Insert Customer", command=lambda: insert_customer(entries)).pack(pady=10)

def insert_customer(entries):
    # Implementation remains the same
    pass

# Menu 3: Bill Section
def menu3():
    clear_main_frame()
    bill_frame = ttk.Frame(main_frame, style='TFrame')
    bill_frame.pack(pady=20, padx=20, fill='both', expand=True)

    ttk.Label(bill_frame, text="Bill Section", font=('Arial', 16, 'bold'), background=COLORS['frame']).pack(pady=10)

    fields = ["Customer ID", "Quantity"]
    entries = []

    for i, field in enumerate(fields):
        row_frame = ttk.Frame(bill_frame, style='TFrame')
        row_frame.pack(fill='x', padx=5, pady=5)
        ttk.Label(row_frame, text=field, width=20).pack(side='left')
        entry = ttk.Entry(row_frame)
        entry.pack(side='left', expand=True, fill='x')
        entries.append(entry)

    ttk.Button(bill_frame, text="Generate Bill", command=lambda: generate_bill(*entries)).pack(pady=10)

def generate_bill(customer_id_entry, quantity_entry):
    # Implementation remains the same
    pass

def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Main Window
root = tk.Tk()
root.title("Medical Store Management System")
root.geometry("800x600")
root.configure(bg=COLORS['bg'])

configure_styles()

# Create main frame
main_frame = ttk.Frame(root, style='TFrame')
main_frame.pack(pady=20, padx=20, fill='both', expand=True)

# Create buttons instead of menu
button_frame = ttk.Frame(root, style='TFrame')
button_frame.pack(fill='x', padx=20, pady=10)

ttk.Button(button_frame, text="Medicine Section", command=menu1).pack(side='left', padx=5)
ttk.Button(button_frame, text="Customer Section", command=menu2).pack(side='left', padx=5)
ttk.Button(button_frame, text="Bill Section", command=menu3).pack(side='left', padx=5)

# Start with the Medicine Section open
menu1()

# Start the Tkinter main loop
root.mainloop()