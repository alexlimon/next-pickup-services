from . import delivery, pickup, food_lookup, store_lookup
from app import app
import os

@app.route("/")
def index():
    return "Welcome to the food finding services!"
