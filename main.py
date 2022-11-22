from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<pThis is Flask from Vercel Serverless python</p>"