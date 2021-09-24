from flask_wtf import FlaskForm
from wtforms import StringField


class commentForm(FlaskForm):
    content = StringField('content')
