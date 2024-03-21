import os
import secrets
from flask import Flask, render_template
from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= (
    os.environ.get('DATABASE_URL', 'postgresql:///fish_wallet'))
app.config['SECRET_KEY'] = secrets.token_hex(16)
connect_db(app)

#########################  Home Page and Error Pages #####################################
@app.route('/')
def home():
    return render_template('home.html')