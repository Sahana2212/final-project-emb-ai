import requests, render_template
from flask import Flask

app = Flask("Emotion Detector")

@app.route("/")


