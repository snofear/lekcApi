from flask import Flask, render_template
import requests

app = Flask(__name__)

f = open("API_KEY.txt", "r")
API_KEY = f.read()

URL = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}"

@app.route("/", methods=["GET"])
def index():
    result = requests.get(URL)
    return render_template("index.html", data=result)

if __name__ == "__main__":
    app.run()