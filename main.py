from flask import Flask, render_template, request
from analyzer import analyze_password, estimate_crack_time, format_time
from breach_checker import check_breach

app = Flask(__name__)

# Home route to handle password analysis and breach checking
@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        password = request.form["password"]

        score, feedback = analyze_password(password)
        crack_time_seconds = estimate_crack_time(password)
        score, feedback = analyze_password(password)
        crack_time_seconds = estimate_crack_time(password)
        breach_count = check_breach(password)

        if score >= 5:
            strength = "Strong"
        elif score >= 3:
            strength = "Medium"
        else:
            strength = "Weak"

        result = {
            "score": score,
            "feedback": feedback,
            "crack_time": format_time(crack_time_seconds),
            "strength": strength,
            "breach_count": breach_count
        }

    return render_template("index.html", result=result) # Render the index.html template with the result dictionary

import os
# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))