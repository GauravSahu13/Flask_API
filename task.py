from flask import Flask, request, jsonify
import mysql.connector as conn

# connecting to mysql
mydb = conn.connect(host = '127.0.0.1',port = '3307', user = "root" , passwd = 'root123')
cursor = mydb.cursor()

# creating database
#cursor.execute("create database gaurav")

# creating table
#cursor.execute("create table gaurav.ineuron1(employe_id int(10)  , emp_name varchar(80) , emp_mailid varchar(20),emp_salary int(6) , emp_attendence int(3))")
'''
# insert into table
cursor.execute("insert into gaurav.ineuron1(employe_id,emp_name,emp_mailid,emp_salary, emp_attendence) values (90, 'Quik', 'quik@gmail.com', 105000, 73)")
mydb.commit()
print("record inserted into table")

# fetching data
cursor.execute("select * from gaurav.ineuron1")
result = cursor.fetchall()
for i in result:
    empId = i[0]
    empName = i[1]
    empEmail = i[2]
    salary = i[3]
    attend= i[4]
    print(empId,empName,empEmail,salary,attend)

# Update data
cursor.execute("Update gaurav.ineuron1 set emp_name= 'Harsh' where employe_id = 19")
mydb.commit()


# Delete data
cursor.execute("Delete from gaurav.ineuron1 where employe_id = 19")
mydb.commit()
'''