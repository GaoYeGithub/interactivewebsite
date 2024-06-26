from flask import Flask, redirect, session, request
import schedule, time, random, os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__, static_url_path='/static')
password = os.environ['mailPassword']
username = os.environ['mailUsername']

@app.route('/')
def index():
  userid = request.headers['X-Replit-User-Name']
  page = ""
  f = open("index.html", "r")
  page = f.read()
  f.close()
  f = open("template/footer.html", "r")
  footer = f.read()
  f.close()
  page = page.replace("{footer}", footer)
  return page

@app.route('/send',  methods=["GET", "POST"])
def send():
  form = request.form
  thing = request.form["subject"]
  content = request.form["message"]
  server = "smtp.gmail.com"
  port = 587
  s = smtplib.SMTP(host=server, port=port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg["To"] = username
  msg["From"] = username
  msg["Subject"] = content
  msg.attach(MIMEText(thing, 'html'))
  s.sendmail(username, username, msg.as_string()) # Sending the email
  s.quit()

  return redirect("/")  # Returning a string as the response

app.run(host='0.0.0.0', port=81)