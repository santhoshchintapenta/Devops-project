from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_feedback, get_all_feedback

app = Flask(__name__)

# Initialize database when app starts
init_db()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()

        if name and message:
            add_feedback(name, message)

        return redirect(url_for("feedback"))

    return render_template("index.html")


@app.route("/feedback")
def feedback():
    feedback_list = get_all_feedback()
    return render_template("feedback.html", feedbacks=feedback_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)