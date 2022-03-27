from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField

class RegistrationFormClass(FlaskForm):
    fname=StringField('First Name')
    lname = StringField('Last Name')
    address = StringField('Address')
    city = StringField('City')
    zip=StringField('Zip')
    state = StringField('State')
    age = StringField('Age')
    experience=StringField('Experience')
    income=StringField('Income')
    Married_choices = [('Married', 'Yes'), ('Single', 'No')]
    marriedyn = SelectField(u'Married', choices=Married_choices)
    profession_choices = [('Python', 'Yes'), ('IT', 'No')]
    profession = SelectField(u'Profession', choices=profession_choices)
    house_choices = [('Rented', 'Rented'), ('owned', 'owned')]
    houseownership = SelectField(u'House Ownership', choices=house_choices)
    car_choices = [(True, 'Yes'), (False, 'No')]
    carownership = SelectField(u'Car Ownership', choices=car_choices)
    currentjobyrs=StringField('Current Job Years')
    currenthouseyrs = StringField('Current Residence Years')
    amount = StringField('Amount')
    installment_rate = StringField('Installment Rate')
    telephone=StringField('telephone')
    submit = SubmitField('Register')

