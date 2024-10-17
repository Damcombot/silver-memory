def menu1():
    print('__________________________________MEDICAL-SECTION______________________________________')
    import mysql.connector as con
    con=con.connect(
        host="localhost",
        user="root",
        password="krishna",
        database="medical"
    )
    cur=con.cursor()
    print('select(1) to insert medicine details')
    print('select (2) to update a medicine details')
    print('select (3) to search a medicine')
    op=int(input('enter the choice:::::::::::::'))
    if  op==1:
        print('Insert medicine details')
        med_id = int(input('Enter medicine ID: '))
        med_name = input('Enter the name of the medicine: ')
        category = input('Enter the category: ')
        dose = input('Enter the dosage in mg: ')
        manufacturer = input('Enter the manufacturer: ')
        exp_dt = input('Enter the expiry date (YYYY-MM-DD): ')
        price = float(input('Enter the price of the medicine: '))
        stock = int(input('Enter the number of stock: '))
        prescrip = int(input('Enter 1 if prescription is required, else 0: '))
        st = "INSERT INTO medicines (medicineid, medicinename, category, dosage, manufacturer, expirydate, price, stockQuantity, prescriptionrequired) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(st, (med_id, med_name, category, dose, manufacturer, exp_dt, price, stock, prescrip))
        con.commit()
        print("Medicine details inserted successfully!")
    elif op==2:
        print('update medicine details')
        med_iid = int(input('Enter the ID of the medicine: '))
        chan = input('Enter the column name to update: ')
        ch = int(input('Enter {1} if the value is int/float, else {2} if the value is string: '))
        if ch == 1:
            val = float(input('Enter the new value: '))
        elif ch == 2:
            val = input('Enter the new value: ')
        s = f"UPDATE medicines SET {chan} = %s WHERE medicineid = %s"
        cur.execute(s, (val, med_iid))
        con.commit()
        print('Update done successfully')
    elif op==3:
        print('search  medicine details')
        med_nam=input('enter thee name of the medicine:')
        st2="select * from medicines where  MedicineName='"+med_nam+"'"
        cur.execute(st2)
        res=cur.fetchall()
        if len(res)>0:
            print(res)
        else:
            print('no data found')
        con.commit()
    else:
        print('<<<<<<<enter the correct option>>>>>>')
def menu2():
    print('_______________________________________CUSTOMER-SECTION_________________________________________')
    import mysql.connector as con
    con=con.connect(
        host="localhost",
        user="root",
        password="krishna",
        database="medical"
    )
    cur=con.cursor()
    print('select(1) to insert customer details')
    print('select (2) to delete customer details')
    print('select (3) to update a customer details')
    print('select (4) to search a customer')
    op=int(input('enter the choice:::::::::::::'))
    if  op==1:
        print('insert customer details')
        cust_id=int(input('enter the new id of the customer:'))
        first_name=input('enter the  first name of the customer:')
        last_name=input('enter the last name of the customer:')
        email=input('enter the email of the customer:')
        phone=input('enter the phone number of the customer:')
        address=input('enter the address of the customer:')
        dob=input('enter the date of birth of the customer:')
        med_id=int(input('enter the id of the medicine:'))
        pur_dat=input('enter purchase date:')
        s="insert into cost(customerid,firstname,lastname,email,phonenumber,address,dateofbirth,medicineid,purchase_date) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(s,(cust_id,first_name,last_name,email,phone,address,dob,med_id,pur_dat))
        con.commit()
        print("inserted sucessfully")
    if  op==2:
        print('Delete customer details')
        cust_id = int(input('Enter the ID of the customer: '))
        s = "DELETE FROM cost WHERE CustomerID = %s"
        cur.execute(s, (cust_id,))
        con.commit()
        print("Deleted successfully")
    if   op==3:
        print('update customer details')
        chan=input('what column  you want to change:')
        cust_iid=int(input('enter the  id of the customer:'))
        ch=int(input('enter {1} if the  value is int else {2} if the value is string:'))
        if ch==1:
            val=float(input('enter the new value:'))
            s=f"update COST set {chan}=%s where customerid=%s"
            cur.execute(s,(val,cust_iid))
            con.commit()
            print('update done sucessfully')
        if ch==2:
            val=input('enter the new value:')
            s=f"update COST set {chan}=%s where customerid=%s"
            cur.execute(s,(val,cust_iid))
            con.commit()
            print('update done sucessfully')
    if   op==4:
        print('search customer details')
        cust_nam=input('enter the first name of the customer:')
        st2="select * from COST where  FirstName='"+cust_nam+"'"
        cur.execute(st2)
        res=cur.fetchall()
        if len(res)>0:
            print(res)
        else:
            print('no data found')
        con.commit()
    else:
        print('<<<<<<<enter the correct option>>>>>>') 
def menu3():
    import mysql.connector as con
    from datetime import datetime
    con=con.connect(
        host="localhost",
        user="root",
        password="krishna",
        database="medical"
    )
    cur=con.cursor()
    def generate_bill(customer_id,quantity):
        cur.execute("""
            SELECT FirstName, LastName, Address, PhoneNumber ,dateofbirth
            FROM Customers 
            WHERE CustomerID = %s
        """, (customer_id,))
        customer = cur.fetchone()
        cur.execute("""
            SELECT 
                m.MedicineName, 
                m.Price,  
                (m.Price * %s) AS TotalCost, 
                c.Purchase_Date 
            FROM Cost c
            JOIN Medicines m ON c.MedicineID = m.MedicineID
            WHERE c.CustomerID = %s
        """, (quantity,customer_id))
        medicines = cur.fetchall()
        if not customer or not medicines:
            print(f"No records found for CustomerID: {customer_id}")
            return
        print(f"{'='*30} BILL {'='*30}")
        print(f"Customer: {customer[0]} {customer[1]}")
        print(f"Address: {customer[2]}")
        print(f"Phone: {customer[3]}")
        print(f"Date_of_birth:{customer[4]}" )
        print(f"{'-'*70}")
        print(f"{'Medicine':<25}{'Unit Price':<15}{'Purchase Date'}")
        print(f"{'-'*70}")
        total_amount = 0
        for med in medicines:
            medicine_name, unit_price, total_cost, purchase_date = med
            total_amount += total_cost
            print(f"{medicine_name:<25}{unit_price:<15}{purchase_date}")
        print(f"{'-'*70}")
        print(f"{'Total Amount':<25}{'':<15}{'':<15}{total_amount:<15}")
        print(f"{'='*70}\n")
    customer_id = int(input("Enter Customer ID: "))
    quantity=int(input('enter the no of quantity:'))
    generate_bill(customer_id,quantity)   
def menu4():
    import mysql.connector as con
    con=con.connect(
        host="localhost",
        user="root",
        password="krishna",
        database="medical"
    ) 
    cur=con.cursor()
    med_name=input('enter  the name of the medicine:')
    f_nam=input('enter the first nameof the customer:')
    quan=int(input('how many quantity:'))
    st = '''
    SELECT price * %s AS `amount to be refunded`, firstname, lastname 
    FROM medicines
    JOIN cost ON cost.medicineid = medicines.medicineid 
    WHERE medicinename = %s 
    AND firstname = %s
    '''
    cur.execute(st,(quan,med_name,f_nam))
    res=cur.fetchall()
    if res:
        print('the amount to be refunded is:',res[0][0])
        print(f'customer  name is {res[0][1]} {res[0][2]}')
    else:
        print('no result matches')
        con.commit()
x = True 
while x == True:
    print("") 
    print(" -------------------------THARUN-MEDICAL-STORE------------------------- ")
    print("select (1) Medicine section ") 
    print("select (2) customer section") 
    print("select (3) bill section")
    print("select (4) re fund") 
    print("select (5) exit") 
    print("-"*100) 
    option=int(input("\nenter from choices (1-5) ="))
    if option ==1:
        menu1() 
    elif option==2:
        menu2() 
    elif option == 3:
        menu3() 
    elif option == 4:
        menu4()  
    elif option== 5: 
        print("-"*50, "Thank you", "-"*50) 
        x= False 
    else:
        print('enter a correct option')
