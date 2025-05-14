from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TickerForm(FlaskForm):
    ticker = StringField('Enter Stock Ticker', validators=[DataRequired()])
    submit = SubmitField('Get Info')
