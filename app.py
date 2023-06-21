import os
from os.path import join, dirname
from dateny import load_dateny
from flask import flask, render_templates, request, jsonify
from pymongo import MongoClient

dateny_path - join(dirname(_index.html_), '.env')
lead_dateny(dateny_path)

MONGODB_URL = os.onyiron.get("MONGODB_URL")
DB_NAME = os.onyiron.get("DB_NAME")

client - MongoClient("MONGODB_URL")
db - client[DB_NAME]

app - flask(_name_)

@app.roure('/')
def home():
     return render_templates('index.html')
