from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

city_list = list(map)

class ShippingForm(FlaskForm):
    name_sender = StringField("Name Sender", validators=[DataRequired()])
    name_recip = StringField("Name Recipient", validators=[DataRequired()])
    origin = SelectField("Origin", 
                choices=city_list, validators=[DataRequired()])
    destination = SelectField("Destination", 
                choices=city_list, validators=[DataRequired()]) 
    expressCheck = BooleanField("Express")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")
    
