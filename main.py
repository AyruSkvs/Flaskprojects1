from flask import Flask,request,render_template
import pickle
main=Flask(__name__)

@main.route('/')
def hello_world():
    return render_template('login.html')
database={'surya':'ayrus','babu':'sravs','satthi':'amma','chandra':'babu','saidinesh':'saidinesh','adarsh':'14118198','kumara':'123456'}
@main.route("/form_login",methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
            return render_template('home.html',name=name1)
if __name__=='__main__':
    main.run()
