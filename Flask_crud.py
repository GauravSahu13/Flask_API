from flask import Flask, request, jsonify
import mysql.connector as conn

# connecting to mysql
mydb = conn.connect(host = '127.0.0.1',port = '3307', user = "root" , passwd = 'root123')
cursor = mydb.cursor()

cursor.execute("create database if not exists taskdbflask")
cursor.execute("create table if not exists taskdbflask.tasktableflask (name varchar(50), mailID varchar(30) , Mnumb int)")

app = Flask(__name__)

@app.route('/insert',methods = ['GET','POST'])
def insert():
    if(request.method == 'POST'):
        name = request.json['name']
        mailID = request.json['mailID']
        Mnumb = request.json['Mnumb']
        cursor.execute("insert into taskdbflask.tasktableflask  values(%s , %s , %s)", (name,mailID,Mnumb))
        mydb.commit()
        return jsonify(str('succesfully inserted'))

@app.route('/update',methods = ['POST'])
def update():
    if(request.method == 'POST'):
        get_name = request.json['get_name']
        cursor.execute("Update taskdbflask.tasktableflask set Mobile_number = Mobile_number + 10 where name = %s", (get_name,))
        mydb.commit()
        return jsonify(str('succesfully update'))

@app.route('/delete',methods = ['GET','POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name']
        cursor.execute("delete from taskdbflask.tasktableflask where name = %s", (name_del,))
        mydb.commit()
        return jsonify(str('succesfully deleted'))


@app.route('/fetch',methods = ['GET','POST'])
def fetch():
    cursor.execute("select * from taskdbflask.tasktableflask")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))


if __name__=='__main__'  :
    app.run()
