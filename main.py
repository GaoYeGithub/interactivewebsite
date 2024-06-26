from flask import Flask, redirect, session, request

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
  userid = request.headers['X-Replit-User-Name']
  page = ""
  f = open("index.html", "r")
  page = f.read()
  return page

app.run(host='0.0.0.0', port=81)