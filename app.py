import os
import secrets
from flask import Flask, render_template, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError
from models import db, connect_db, User, Lake, FishCatch, FishSpecies, MasterAnglerReq
from forms import SignInForm, AddUserForm, UpdateUserForm, FishCatch, LakeForm, AddFishSpeciesForm, UpdateFishSpeciesForm, MasterAnglerForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= (
    os.environ.get('DATABASE_URL', 'postgresql:///fish_wallet'))
app.config['SECRET_KEY'] = secrets.token_hex(16)
connect_db(app)

#########################  Home Page and Error Pages #####################################
@app.route('/')
def home():
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_error.html'), 404

#########################  User Routes #####################################
@app.route('/signup', methods=["GET", "POST"])
def signup():
    """
    If form is not valid, show add user form
    If form is valid, create user in DB and redirect to the user home page
    If the username is already taken, flash message to user and re-load form
    """
    form = AddUserForm()

    if form.validate_on_submit():
        try:
            User.signup(username=form.username.data,
                        password=form.password.data,
                        email=form.email.data)
            db.session.commit()

        except IntegrityError:
            flash("Username taken. Select a different username", 'danger')
            return render_template('user/signup.html', form=form)
        
        return redirect(url_for('home'))
    else:
        return render_template('user/signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    """
    If form is valid, verify username and password are correct
    If form in not valid, display existing user login form
    """
    form = SignInForm()
    return render_template('user/login.html', form=form)

@app.route('/logout')
def logout():
    return redirect(url_for('home'))

#########################  Fish Catch Routes #####################################
#########################  Fish Species Routes #####################################
#########################  Lake Routes #####################################
#########################  Master Angler Routes #####################################

