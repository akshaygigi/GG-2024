from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login',methods=['GET','POST'])
def login():
    uname = request.form['uname']
    password = request.form['pass']

    if uname=="admin" and password=="hammer":
        return render_template("welcome.html")
    else:
        return "password error"

if __name__=="__main__":
    app.run(debug=True)
