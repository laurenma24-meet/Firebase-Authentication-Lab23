from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyD2BQXXECRmnPLSmJ2T39q14isfE4WlN-U",
  "authDomain": "example-9d1d1.firebaseapp.com",
  "projectId": "example-9d1d1",
  "storageBucket": "example-9d1d1.appspot.com",
  "messagingSenderId": "304177667159",
  "appId": "1:304177667159:web:f1ba6294bfb288b37d5712",
  "measurementId": "G-M32WMDY4PH",
  "databaseURL":""
}

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

firebase= pyrebase.initialize_app(config)
auth= firebase.auth()

app= Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error=""
    if request.method== 'POST':
        email= request.form['email']
        password=request.form['password']
        try:
            login_session['user']=auth.create_user_with_email_and_password(email,password)
            return redirect(url_for('home'))
        except:
            error="Authentication failed"
    return render_template("signup.html")

print(signup())


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)