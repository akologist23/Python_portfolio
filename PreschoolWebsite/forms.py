from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email
from flask_ckeditor import CKEditorField

class ContactForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[Email()])
    message = CKEditorField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit Message")