import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

config = {
  "apiKey": "AIzaSyDgR-7Dd46Es9lNv7LX1NyDuy5QYjFUTfw",
    "authDomain": "farmers-advisor.firebaseapp.com",
    "projectId": "farmers-advisor",
    "storageBucket": "farmers-advisor.appspot.com",
    "messagingSenderId": "79280119667",
    "appId": "1:79280119667:web:88edbe05bcd0f5c67e2f06",
    "databaseURL": '',
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

cred = credentials.Certificate('farmers-advisor-firebase-adminsdk.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
