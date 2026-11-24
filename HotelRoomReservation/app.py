from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Welcome to the Hotel Room Reservation app!"
print("Hotel Room Reservation app is running")
