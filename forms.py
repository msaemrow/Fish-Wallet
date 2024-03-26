from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, FloatField
from wtforms.validators import InputRequired, Email, Length, NumberRange, Optional
from wtforms.widgets import RangeInput

##########  USER FORMS #######################
class AddUserForm(FlaskForm):
    """Form to create a new user"""
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    password2 = PasswordField('Confirm Password', validators=[Length(min=6)])

class UpdateUserForm(FlaskForm):
    """Form to update and existing user. Need to re-enter password to update user information"""
    username = StringField('Update Username', validators=[InputRequired()])
    email = StringField('Update Email', validators=[InputRequired(), Email()])
    password = PasswordField('Enter password to update information', validators=[Length(min=6)])

class SignInForm(FlaskForm):
    """Form for an existing user to sign in"""
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


########## FISH CATCH FORMS #######################
class FishCatch(FlaskForm):
    """Form to add or update a fish catch"""
    species = SelectField('Fish Species', validators=[InputRequired()])
    lake = SelectField('Lake', validators=[InputRequired()])
    length = FloatField('Fish Length (inches)', widget=RangeInput(step=0.25), validators=[NumberRange(min=0.0, max=60.0), Optional()] )
    weight = FloatField('Fish Weight (lbs)', widget=RangeInput(step=0.25), validators=[NumberRange(min=0.0, max=60.0), Optional()] )
    fish_image = StringField('Fish Image URL', validators=[Optional()])

########## LAKE FORMS #######################
class LakeForm(FlaskForm):
    """Form to add or update an existing lake. Only users with admin permission can update a lake"""
    name = StringField('Lake Name', validators=[InputRequired()])
    state = SelectField('Select State', validators=[InputRequired()])
    closest_town = StringField('Enter Closest Town (for weather data)', validators=[InputRequired()])

########## FISH SPECIES FORMS #######################
class AddFishSpeciesForm(FlaskForm):
    """Form to add a new fish speices. Only users with admin permission can add or update a fish species"""
    species = StringField('Fish Species Name', validators=[InputRequired()])

class UpdateFishSpeciesForm(FlaskForm):
    """Form to update an existing fish speices. Only users with admin permission can add or update a fish species"""
    old_species_name = StringField('Fish Species Name', validators=[InputRequired()])
    new_species_name = StringField('Fish Species Name', validators=[InputRequired(), Length(min=3)])

########## MASTER ANGLER FORMS #######################
class MasterAnglerForm(FlaskForm):
    """Form to add or update an existing master angler requirement. Only users with admin permission can add or update a master angler requirement"""

    species = SelectField('Fish Species', validators=[InputRequired()])
    min_length = FloatField('Minimum length to be considered master angler', validators=[InputRequired()])