from flask import Flask, render_template, request
import requests
import smtplib
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
SMTP_ADDRESS = os.getenv('SMTP_ADDRESS')

recipient_email = os.getenv('RECIPIENT_EMAIL')

posts = requests.get("https://api.npoint.io/b67ad1c30240153dba9c").json()

# --------------------------- SET UP FLASK -------------------------#

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    submit_status = False
    if request.method == 'POST':
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])

        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        time = datetime.now()

        with smtplib.SMTP(SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=recipient_email,
                msg=(
                    f"Subject:New form submitted by {name}!\n\n"
                    f"Date Submitted: {time}\n"
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n"
                    f"Message: {message}"
                )
            )
        submit_status = True
        return render_template("contact.html", submit_status=submit_status)
    return render_template("contact.html", submit_status=submit_status)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
