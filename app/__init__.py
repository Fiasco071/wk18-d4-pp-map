from crypt import methods
from flask import Flask, render_template
from app.config import Config
from app.shipping_form import ShippingForm

app = Flask(__name__)

app.config.from_object(Config)


@app.route("/")
def index():
    return "<h1>Package Tracker</h1>"
    # return render_template("index.html", display_item=my_list, title="Welcome!", views=views)
    

@app.route("/new_package", methods= ['GET', 'POST'])
def new_package():
    form = ShippingForm()
    print(form.expressCheck.data)
    return render_template('shipping_request.html', form=form)