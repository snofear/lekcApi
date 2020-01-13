from flask import Flask, render_template
import requests
from random import randint
import os

app = Flask(__name__)

try:
    API_KEY = os.environ["API_KEY"]
except:
    API_KEY = open("API_KEY.txt").read().strip()


ime_mesta = ["Ljubljana", "London", "Paris", "Berlin"][randint(0,3)]

@app.route("/", methods=["GET"])
def index():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={ime_mesta}&appid={API_KEY}&units=metric"
    result = requests.get(URL).json()
    return render_template("index.html", data=result)

if __name__ == "__main__":
    app.run()