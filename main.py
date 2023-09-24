from flask import Flask, render_template, request, redirect, jsonify, url_for, session
# from ML_model import *
from model import *
import os
import numpy as np
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

# model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def home():
  name = ""
  if 'email' in session:
    name = session['name']
  return render_template('dashboard.html', name=name)


@app.route("/login", methods=["GET", "POST"])
def login():
  status = "Pass"
  if request.method == "POST":
    username = request.form['email']
    password = request.form['password']
    alert = Login_firebase(username, password)
    print(alert)
    if alert == "Failed":
      status = "Failed"
      return render_template('login.html', status=status)
    else:
      session['email'] = username
      session['name'] = alert
    return redirect(url_for('home'))

  return render_template('login.html', status=status)
  # if request.method == 'POST':
  #     email = request.form["email"]
  #     faq =  User.query.filter_by(email = email).first()
  #     print(faq.email)
  #     return redirect(url_for('home'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
  session.pop('email')
  return redirect(url_for('home'))


@app.route("/signup", methods=["GET", "POST"])
def signup():
  if request.method == 'GET':
    return render_template('signup.html')
  if request.method == 'POST':
    email = request.form["email"]
    password = request.form["password"]
    name = request.form["name"]
    phno = request.form["phno"]
    season = request.form["season"]
    location = request.form["location"]

    data = {
      "email": email,
      "name": name,
      "Registered_on": datetime.datetime.now(),
      "phno": phno,
      "season": season,
      "location": location
    }

    print(name, email, password, phno, season, location)
    alert = Register_firebase(data, password)
    return redirect(url_for('login'))


@app.route("/profile", methods=['GET'])
def profile():
  data = ""
  if 'email' in session:
    email = session['email']
  data = get_user_data(email)
  return render_template('profile.html', data=data)


# @app.route('/index')
# def index():
#     return render_template('index.html')


@app.route('/SoilTypeAnalysis', methods=['POST'])
def predict():
  int_features = [int(x) for x in request.form.values()]
  final_features = [np.array(int_features)]
  prediction = model.predict(final_features)

  output = prediction

  return render_template(
    'SoilTypeAnalysis.html',
    prediction_text='Suggested crop for given soil health condition is: "{}".'.
    format(output[0]))


# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)


@app.route("/crop_estimation")
def crop_estimation():
  print("hello")
  return render_template('./Features/cost_estimation2.html')


@app.route("/crop_comparison")
def crop_comparison():
  return render_template('./Features/crop_comparison.html')


@app.route("/faq", methods=["GET", "POST"])
def faq():
  if request.method == 'GET':
    faq = get_faq()
    return render_template('faq.html', faq=faq)


@app.route("/crop_information", methods=["GET"])
def crop_information():
  return render_template('./Features/crop_information.html')


@app.route("/forms", methods=["GET", "POST"])
def forms():
  if request.method == 'GET':
    return render_template('Forms.html')
  if request.method == 'POST':
    print(request.form['fname'])

    return "THIS IS POST REQUEST"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
