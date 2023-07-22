from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalRangeField, BooleanField, SelectField
from wtforms.validators import DataRequired, URL,  number_range, length


class CafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired(), length(max=100)], )
    rating = SelectField("Cafe Rating", choices=[1, 2, 3, 4, 5])
    location = StringField("Location URL", validators=[DataRequired(), URL()])
    wifi_strength = SelectField("Wifi Strength", choices=[1, 2, 3, 4, 5])
    outlets = BooleanField("Has outlets")
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    submit = SubmitField("Create Cafe")


