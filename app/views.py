import pyrebase
import os

config = {
    "apiKey":  "AIzaSyBATHQcLEjqAc7_wIGTMD4Az38Abgt-FW4",
    "authDomain": "test-django-f19cb.firebaseapp.com",
    "projectId": "test-django-f19cb",
    "storageBucket": "test-django-f19cb.appspot.com",
    "messagingSenderId": "1099312618333",
    "appId":  "1:1099312618333:web:75443819cfa9919963a6b4",
    "measurementId":"G-TKKQPG041F",
    "databaseURL": ""
}


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
