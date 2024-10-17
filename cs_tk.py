import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# Establish the database connection
def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="krishna",
        database="medical"
    )

# Menu for Medicine section
def menu1():
    def insert_medicine():
        try:
            conn = db_connection()
            cur = conn.cursor()
            med_id = int(med_id_entry.get())
            med_name = med_name_entry.get()
            category = category_entry.get()
            dose = dose_entry.get()
            manufacturer = manufacturer_entry.get()
            exp_dt = exp_dt_entry.get()
            price = float(price_entry.get())
            stock = int(stock_entry.get())
            prescrip = int(prescrip_entry.get())

            query = "INSERT INTO medicines VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(query, (med_id, med_name, category, dose, manufacturer, exp_dt, price, stock, prescrip))
            conn.commit()
            messagebox.showinfo("Success", "Medicine details inserted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cur.close()
            conn.close()

    def delete_medicine():
        try:
            conn = db_connection()
            cur = conn.cursor()
            dat = datetime.now().date()
            query = "DELETE FROM medicines WHERE ExpiryDate <= %s"
            cur.execute(query, (dat,))
            conn.commit()
            messagebox.showinfo("Success", "Expired medicines deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cur.close()
            conn.close()

    def update_medicine():
        try:
            conn = db_connection()
            cur = conn.cursor()
            chan = update_column_entry.get()
            med_id = int(med_id_update_entry.get())
            new_value = new_value_entry.get()

            query = f"UPDATE medicines SET {chan} = %s WHERE MedicineID = %s"
            cur.execute(query, (new_value, med_id))
            conn.commit()
            messagebox.showinfo("Success", "Medicine details updated successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cur.close()
            conn.close()

    def search_medicine():
        try:
            conn = db_connection()
            cur = conn.cursor()
            med_name = search_name_entry.get()
            query = "SELECT * FROM medicines WHERE MedicineName = %s"
            cur.execute(query, (med_name,))
            result = cur.fetchall()
            if result:
                messagebox.showinfo("Result", str(result))
            else:
                messagebox.showinfo("Result", "No data found")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cur.close()
            conn.close()

    # Create medicine section frame
    medicine_frame = tk.Frame(root)
    medicine_frame.pack(pady=10)

    tk.Label(medicine_frame, text="Medicine ID").grid(row=0, column=0)
    tk.Label(medicine_frame, text="Medicine Name").grid(row=1, column=0)
    tk.Label(medicine_frame, text="Category").grid(row=2, column=0)
    tk.Label(medicine_frame, text="Dosage (mg)").grid(row=3, column=0)
    tk.Label(medicine_frame, text="Manufacturer").grid(row=4, column=0)
    tk.Label(medicine_frame, text="Expiry Date").grid(row=5, column=0)
    tk.Label(medicine_frame, text="Price").grid(row=6, column=0)
    tk.Label(medicine_frame, text="Stock Quantity").grid(row=7, column=0)
    tk.Label(medicine_frame, text="Prescription Required (1/0)").grid(row=8, column=0)

    med_id_entry = tk.Entry(medicine_frame)
    med_name_entry = tk.Entry(medicine_frame)
    category_entry = tk.Entry(medicine_frame)
    dose_entry = tk.Entry(medicine_frame)
    manufacturer_entry = tk.Entry(medicine_frame)
    exp_dt_entry = tk.Entry(medicine_frame)
    price_entry = tk.Entry(medicine_frame)
    stock_entry = tk.Entry(medicine_frame)
    prescrip_entry = tk.Entry(medicine_frame)

    med_id_entry.grid(row=0, column=1)
    med_name_entry.grid(row=1, column=1)
    category_entry.grid(row=2, column=1)
    dose_entry.grid(row=3, column=1)
    manufacturer_entry.grid(row=4, column=1)
    exp_dt_entry.grid(row=5, column=1)
    price_entry.grid(row=6, column=1)
    stock_entry.grid(row=7, column=1)
    prescrip_entry.grid(row=8, column=1)

    tk.Button(medicine_frame, text="Insert", command=insert_medicine).grid(row=9, column=0)
    tk.Button(medicine_frame, text="Delete Expired", command=delete_medicine).grid(row=9, column=1)

    # Update section
    tk.Label(medicine_frame, text="Update Column").grid(row=10, column=0)
    update_column_entry = tk.Entry(medicine_frame)
    update_column_entry.grid(row=10, column=1)

    tk.Label(medicine_frame, text="Medicine ID").grid(row=11, column=0)
    med_id_update_entry = tk.Entry(medicine_frame)
    med_id_update_entry.grid(row=11, column=1)

    tk.Label(medicine_frame, text="New Value").grid(row=12, column=0)
    new_value_entry = tk.Entry(medicine_frame)
    new_value_entry.grid(row=12, column=1)

    tk.Button(medicine_frame, text="Update", command=update_medicine).grid(row=13, column=0)

    # Search section
    tk.Label(medicine_frame, text="Search Medicine").grid(row=14, column=0)
    search_name_entry = tk.Entry(medicine_frame)
    search_name_entry.grid(row=14, column=1)

    tk.Button(medicine_frame, text="Search", command=search_medicine).grid(row=15, column=0)

# Menu for Customer section
def menu2():
    def insert_customer():
        try:
            conn = db_connection()
            cur = conn.cursor()
            cust_id = int(cust_id_entry.get())
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            address = address_entry.get()
            dob = dob_entry.get()
            med_id = int(med_id_customer_entry.get())

            query = "INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(query, (cust_id, first_name, last_name, email, phone, address, dob, med_id))
            conn.commit()
            messagebox.showinfo("Success", "Customer details inserted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cur.close()
            conn.close()

    def delete_customer():
        try:
            conn = db_connection()
            cur = conn.cursor()
            cust_id = int(cust_id_delete_entry.get())
            query = "DELETE FROM customers WHERE CustomerID = %s"
            cur.execute(query, (cust_id,))
            conn.commit()
            messagebox.showinfo("Success", "Customer details deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cur.close()
            conn.close()

    def update_customer():
        try:
            conn = db_connection()
            cur = conn.cursor()
            chan = update_column_customer_entry.get()
            cust_id = int(cust_id_update_entry.get())
            new_value = new_value_customer_entry.get()

            query = f"UPDATE customers SET {chan} = %s WHERE CustomerID = %s"
            cur.execute(query, (new_value, cust_id))
            conn.commit()
            messagebox.showinfo("Success", "Customer details updated successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cur.close()
            conn.close()

    def search_customer():
        try:
            conn = db_connection()
            cur = conn.cursor()
            cust_name = search_customer_name_entry.get()
            query = "SELECT * FROM customers WHERE FirstName = %s"
            cur.execute(query, (cust_name,))
            result = cur.fetchall()
            if result:
                messagebox.showinfo("Result", str(result))
            else:
                messagebox.showinfo("Result", "No data found")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cur.close()
            conn.close()

    # Create customer section frame
    customer_frame = tk.Frame(root)
    customer_frame.pack(pady=10)

    tk.Label(customer_frame, text="Customer ID").grid(row=0, column=0)
    tk.Label(customer_frame, text="First Name").grid(row=1, column=0)
    tk.Label(customer_frame, text="Last Name").grid(row=2, column=0)
    tk.Label(customer_frame, text="Email").grid(row=3, column=0)
    tk.Label(customer_frame, text="Phone").grid(row=4, column=0)
    tk.Label(customer_frame, text="Address").grid(row=5, column=0)
    tk.Label(customer_frame, text="Date of Birth").grid(row=6, column=0)
    tk.Label(customer_frame, text="Medicine ID").grid(row=7, column=0)

    cust_id_entry = tk.Entry(customer_frame)
    first_name_entry = tk.Entry(customer_frame)
    last_name_entry = tk.Entry(customer_frame)
    email_entry = tk.Entry(customer_frame)
    phone_entry = tk.Entry(customer_frame)
    address_entry = tk.Entry(customer_frame)
    dob_entry = tk.Entry(customer_frame)
    med_id_customer_entry = tk.Entry(customer_frame)

    cust_id_entry.grid(row=0, column=1)
    first_name_entry.grid(row=1, column=1)
    last_name_entry.grid(row=2, column=1)
    email_entry.grid(row=3, column=1)
    phone_entry.grid(row=4, column=1)
    address_entry.grid(row=5, column=1)
    dob_entry.grid(row=6, column=1)
    med_id_customer_entry.grid(row=7, column=1)

    tk.Button(customer_frame, text="Insert", command=insert_customer).grid(row=8, column=0)
    
    # Delete customer
    tk.Label(customer_frame, text="Delete Customer ID").grid(row=9, column=0)
    cust_id_delete_entry = tk.Entry(customer_frame)
    cust_id_delete_entry.grid(row=9, column=1)
    tk.Button(customer_frame, text="Delete", command=delete_customer).grid(row=9, column=2)

    # Update customer
    tk.Label(customer_frame, text="Update Column").grid(row=10, column=0)
    update_column_customer_entry = tk.Entry(customer_frame)
    update_column_customer_entry.grid(row=10, column=1)

    tk.Label(customer_frame, text="Customer ID").grid(row=11, column=0)
    cust_id_update_entry = tk.Entry(customer_frame)
    cust_id_update_entry.grid(row=11, column=1)

    tk.Label(customer_frame, text="New Value").grid(row=12, column=0)
    new_value_customer_entry = tk.Entry(customer_frame)
    new_value_customer_entry.grid(row=12, column=1)

    tk.Button(customer_frame, text="Update", command=update_customer).grid(row=13, column=0)

    # Search customer
    tk.Label(customer_frame, text="Search Customer").grid(row=14, column=0)
    search_customer_name_entry = tk.Entry(customer_frame)
    search_customer_name_entry.grid(row=14, column=1)

    tk.Button(customer_frame, text="Search", command=search_customer).grid(row=15, column=0)

# Menu for Bill section
def menu3():
    def generate_bill():
        try:
            conn = db_connection()
            cur = conn.cursor()
            customer_id = int(customer_id_entry.get())
            quantity = int(quantity_entry.get())
            query = """
                SELECT FirstName, LastName, Address, PhoneNumber, dateofbirth
                FROM Customers 
                WHERE CustomerID = %s
            """
            cur.execute(query, (customer_id,))
            customer = cur.fetchone()

            query = """
                SELECT m.MedicineName, m.Price, (m.Price * %s) AS TotalCost, c.Purchase_Date 
                FROM Cost c
                JOIN Medicines m ON c.MedicineID = m.MedicineID
                WHERE c.CustomerID = %s
            """
            cur.execute(query, (quantity, customer_id))
            medicines = cur.fetchall()

            if not customer or not medicines:
                messagebox.showerror("Error", f"No records found for CustomerID: {customer_id}")
                return

            bill_text = f"{'='*30} BILL {'='*30}\n"
            bill_text += f"Customer: {customer[0]} {customer[1]}\n"
            bill_text += f"Address: {customer[2]}\n"
            bill_text += f"Phone: {customer[3]}\n"
            bill_text += f"Date_of_birth: {customer[4]}\n"
            bill_text += f"{'-'*70}\n"
            bill_text += f"{'Medicine':<25}{'Unit Price':<15}{'Purchase Date'}\n"
            bill_text += f"{'-'*70}\n"
            total_amount = 0
            for med in medicines:
                medicine_name, unit_price, total_cost, purchase_date = med
                total_amount += total_cost
                bill_text += f"{medicine_name:<25}{unit_price:<15}{purchase_date}\n"
            bill_text += f"{'-'*70}\n"
            bill_text += f"{'Total Amount':<25}{'':<15}{total_amount:<15}\n"
            bill_text += f"{'='*70}\n"

            messagebox.showinfo("Bill", bill_text)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cur.close()
            conn.close()

    # Create bill section frame
    bill_frame = tk.Frame(root)
    bill_frame.pack(pady=10)

    tk.Label(bill_frame, text="Customer ID").grid(row=0, column=0)
    customer_id_entry = tk.Entry(bill_frame)
    customer_id_entry.grid(row=0, column=1)

    tk.Label(bill_frame, text="Quantity").grid(row=1, column=0)
    quantity_entry = tk.Entry(bill_frame)
    quantity_entry.grid(row=1, column=1)

    tk.Button(bill_frame, text="Generate Bill", command=generate_bill).grid(row=2, column=0)

# Menu for Refund section
def menu4():
    def refund_amount():
        try:
            conn = db_connection()
            cur = conn.cursor()
            med_name = med_name_refund_entry.get()
            first_name = first_name_refund_entry.get()
            quantity = int(quantity_refund_entry.get())

            query = """
            SELECT price * %s AS `amount to be refunded`, firstname, lastname 
            FROM medicines
            JOIN cost ON cost.medicineid = medicines.medicineid 
            WHERE medicinename = %s AND firstname = %s
            """
            cur.execute(query, (quantity, med_name, first_name))
            res = cur.fetchall()

            if res:
                messagebox.showinfo("Refund Amount", f"The amount to be refunded is: {res[0][0]}\nCustomer name is {res[0][1]} {res[0][2]}")
            else:
                messagebox.showinfo("Refund Amount", "No result matches")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cur.close()
            conn.close()

    # Create refund section frame
    refund_frame = tk.Frame(root)
    refund_frame.pack(pady=10)

    tk.Label(refund_frame, text="Medicine Name").grid(row=0, column=0)
    med_name_refund_entry = tk.Entry(refund_frame)
    med_name_refund_entry.grid(row=0, column=1)

    tk.Label(refund_frame, text="Customer First Name").grid(row=1, column=0)
    first_name_refund_entry = tk.Entry(refund_frame)
    first_name_refund_entry.grid(row=1, column=1)

    tk.Label(refund_frame, text="Quantity").grid(row=2, column=0)
    quantity_refund_entry = tk.Entry(refund_frame)
    quantity_refund_entry.grid(row=2, column=1)

    tk.Button(refund_frame, text="Calculate Refund", command=refund_amount).grid(row=3, column=0)

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Tharun Medical Store")

# Create main menu buttons
tk.Button(root, text="Medicine Section", command=menu1).pack(pady=10)
tk.Button(root, text="Customer Section", command=menu2).pack(pady=10)
tk.Button(root, text="Bill Section", command=menu3).pack(pady=10)
tk.Button(root, text="Refund Section", command=menu4).pack(pady=10)

# Start the main loop
root.mainloop()
