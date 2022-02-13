from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class BrandNameForm(FlaskForm):
    brand_name = StringField('Brand Name')
    submit = SubmitField("Send")