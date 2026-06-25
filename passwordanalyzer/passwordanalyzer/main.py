from flask import Flask, render_template, request
from analyzer import analyze_password, estimate_crack_time, format_time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        password = request.form["password"]

        score, feedback = analyze_password(password)
        crack_time_seconds = estimate_crack_time(password)

        if score >= 5:
            strength = "strong"
        elif score >= 3:
            strength = "medium"
        else:
            strength = "weak"

        result = {
            "score": score,
            "feedback": feedback,
            "crack_time": format_time(crack_time_seconds),
            "strength": strength
        }

    return render_template("index.html", result=result)

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))