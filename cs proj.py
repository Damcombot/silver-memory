import sys
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='manager',database='dental_management')
cur=conn.cursor()
if conn.is_connected:
    print(" SS MEDICAL STORE ")
    print("1. Login")
    print("2. Exit")
    print()
    option=int(input("Enter your choise : "))
if option==1:
    print()
    user=input('User Name : ')
    user=user.upper()
    c1.execute("select * from accounts where User_Name like '" + user + "'")
    datas=c1.fetchall()
for i in datas:
    value_1=i[0]
    value_2=i[1]
    if user==value_1:
        password=input('Password : ')
        password=password.upper()
    if password==value_2:
        print()
        print('Login succefull')
        print()
        print("1. Patients records")
        print("2. Salary records")
        print("3. Veiw Patient Detail")
        print("4. Delete patient detail")
        print()
        choise=int(input('Enter a option : '))
if choise==1:
print()
s_no=int(input('S.no : '))

name=input('Name : ')
name=name.upper()
age=int(input('Age : '))
doc=input('Doctor Consulted : ')
doc=doc.upper()
add=input('Address : ')
add=add.upper()
phone_no=int(input('Phone Number : '))
cur.execute("insert into patient_record values(" + str(s_no) +",'" + name + "'," +
str(age) + ",'" + doc + "','" + add + "'," + str(phone_no) + ")")
conn.commit()
print('Record added')
if choise==2:
print()
s_no=int(input('S_No : '))
emp_name=input('Employee_Name : ')
emp_name=emp_name.upper()
proffesion=input('Proffession : ')
proffesion=proffesion.upper()
salary=int(input('Salary Amount : '))
add=input('Address : ')
add=add.upper()
phone_no=input('Phone_Number : ')
cur.execute("insert into salary_record values(" + str(s_no) +",'" + emp_name + "','" +
proffesion + "'," + str(salary) + ",'" + add + "'," + str(phone_no) + ")")
conn.commit()
print('Record added')
if choise==3:
print()
name=input('Name of the patient : ')
name=name.upper()
cur.execute("select * from patient_record where patient_name like '" + str(name) +
"'")
data=cur.fetchall()
for row in data:
print()

print('Name : ',row[1])
print('Age : ',row[2])
print('Doctor consulted : ',row[3])
print('Address : ',row[4])
print('Phone Number : ',row[5])
if choise==4:
print()
name=input('Name of the patient : ')
name=name.upper()
cur.execute("delete from patient_record where Patient_Name like '" + name + "'")
print('Record Deleted Succefully')
else:
print('Invalid Password')
print('Tryagain')
elif option==2:
sys.exit()
conn.commit()
input()