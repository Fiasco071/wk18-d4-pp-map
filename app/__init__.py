from flask import Flask, render_template
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)


@app.route("/")
def index():
    return "<h1>Package Tracker!</h1>"
    # return render_template("index.html", display_item=my_list, title="Welcome!", views=views)