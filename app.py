from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

@app.route("/")
def home():
    greeting = get_greeting()
    return render_template("index.html", greeting=greeting)

@app.route("/letter")
def letter():
    with open("letter.txt", "r", encoding="utf-8") as f:
        content = f.read()
    return render_template("letter.html", letter=content)

if __name__ == "__main__":
    app.run(debug=True)
