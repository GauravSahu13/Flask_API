from flask import Flask, request
import mysql.connector as conn
import jsonify

app = Flask(__name__)


@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get('mail_id')

    return "this is my first function for get {} {} {}".format(get_name, mobile_number, mail_id)
# passing a data through browser in unsecured mode ( i.e called as get)
# "127.0.0.1.5002/testfun?get_name=Gaurav sahu & mobile = 9822211" calling through url link



# getting database from browser
@app.route('/get_data')
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        con = conn.connect(host="localhost", user="root", password="root123", database=db)
        cur = con.cursor(dictionary=True)
        cur.execute(f'select * from {tn}')
        data = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5002)