from flask import Flask, render_template, request, redirect, url_for, send_file
from email.message import EmailMessage
import smtplib
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/open-pdf")
def open_pdf():
    return send_file("static/Anjana Nallanagula Resume.pdf", mimetype="application/pdf")

@app.route("/sendemail/", methods=["POST"])
def sendemail():
    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["subject"]
        email = request.form["_replyto"]
        message = request.form["message"]

        your_email = os.environ.get("GMAIL_USER")
        your_password = os.environ.get("GMAIL_PASSWORD")

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(your_email, your_password)

            msg = EmailMessage()
            msg.set_content(f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")
            msg["To"] = your_email
            msg["From"] = email
            msg["Subject"] = subject
            msg["Reply-To"] = email
            
            server.send_message(msg)
            server.quit()

            msg = "Thank you! Your email was sent successfully"
        except Exception as e:
            msg = f"Failed to send email: {e}"

        return render_template("index.html", message=msg)

if __name__ == "__main__":
    app.run(debug=True)