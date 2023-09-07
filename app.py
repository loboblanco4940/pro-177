from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs":5,
        "category":"Deportes",
        "word":"Ajedrez"
    },
    {
        "inputs":6,
        "category": "Nombres de pises Europeos",
        "word":"Francia"
    },
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status":"success",
        "word": random.chice(templates)
    })