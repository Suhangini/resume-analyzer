from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

# Simple skill keywords
skills = {
    "python": 10,
    "java": 10,
    "machine learning": 15,
    "data science": 15,
    "communication": 5,
    "teamwork": 5,
    "sql": 10,
    "html": 5,
    "css": 5
}

@app.route("/", methods=["GET", "POST"])
def index():
    score = 0
    found_skills = []

    if request.method == "POST":
        file = request.files["resume"]
        text = file.read().decode("utf-8", errors="ignore").lower()

        for skill, value in skills.items():
            if skill in text:
                score += value
                found_skills.append(skill)

        score = min(score, 100)

        return render_template("index.html",
                               score=score,
                               skills=found_skills)

    return render_template("index.html", score=None)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
