import smtplib
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()


# Configure App
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    email = request.form.get("email")
    if not name or not dorm or not email:
        return render_template("failure.html")
    message = "You are registered!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
    server.sendmail(os.getenv("EMAIL"), email, message)
    server.quit()
    return render_template("success.html")
