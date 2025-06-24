from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, ValidationError

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    image = StringField('Image')
    submit = SubmitField('Submit')

    def validate_name(self, field):
        if "დაუშვებელი" in field.data:
            raise ValidationError("სახელში აკრძალულია სიტყვა 'დაუშვებელი'.")

    def validate_price(self, field):
        if field.data <= 0:
            raise ValidationError("ფასი უნდა იყოს 0-ზე მეტი.")
