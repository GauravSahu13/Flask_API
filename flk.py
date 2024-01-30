'''
API ---> platform independent (set of rules / set of protocals to reach out to different system)
connection btw two independent platform[language] ---> https protocal
'''

from flask import Flask, request, jsonify

app = Flask(__name__)


'''
jsonify --> return everything in json format
GET/ POST --> send a data 
Get --> random search data science (passing through url)
Post --> (passing login details through a body)  eg. email login
'''
@app.route('/abc',methods = ['GET','POST'])
def test():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify((str(result)))

if __name__=='__main__'  :
    app.run()