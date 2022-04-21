from flask import Flask, render_template, redirect, session
from app.config import Config
from app.shipping_form import ShippingForm
from app.model.models import db
from app.model.packages import Package
from flask_migrate import Migrate


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    packages = Package.query.all()
    return  render_template('package_status.html', packages=packages)
    # return render_template("index.html", display_item=my_list, title="Welcome!", views=views)


@app.route("/new_package", methods= ['GET', 'POST'])
def new_package():
    form = ShippingForm()
    print(form.expressCheck.data)
    print(form.data)
    if form.validate_on_submit():
        data = form.data
        new_package = Package(name=data["name_sender"],
                              recipient=data["name_recip"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect('/')

    return render_template('shipping_request.html', form=form)
