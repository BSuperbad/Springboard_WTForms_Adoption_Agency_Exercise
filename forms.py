from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""
    name = StringField("Pet name", validators=[
                       InputRequired(message="Name cannot be blank")])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],  validators=[
        InputRequired(message="Species cannot be blank")])
    photo_url = StringField("Photo URL", validators=[
                            Optional(), URL(require_tld=True)])
    age = FloatField("Age", validators=[
        Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available for Adoption?",
                             validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""
    photo_url = TextAreaField("Edit Photo URL", validators=[
        Optional(), URL(require_tld=True)])
    notes = TextAreaField("Add Notes", validators=[Optional()])
    available = BooleanField("Still available for Adoption?",
                             validators=[Optional()])
