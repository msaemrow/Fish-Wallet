from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app"""

    db.app = app
    db.init_app(app)
    app.app_context().push()

class User(db.Model):
    """Users in the platform"""

    __tablename__='users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.Text,
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )

    fish_catches = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    is_admin = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    @classmethod
    def signup(cls, username, email, password):
        
        user = User(username=username,
                    email=email,
                    password=password,
                    fish_catches=0,
                    is_admin=False)
        db.session.add(user)
        return user
    
class Lake(db.Model):
    """Model for a lake that a fish is caught from"""
    
    __tablename__ = 'lakes'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.Text,
        nullable=False
    )

    state = db.Column(
        db.String(2),
        nullable=False
    )

    closest_town = db.Column(
        db.Text
    )

class FishSpecies(db.Model):
    """Model for fish that are caught"""

    __tablename__ = 'fish_species'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name= db.Column(
        db.Text,
        nullable=False,
        unique=True
    ) 

class FishCatch(db.Model):
    """Model that shows details for a single fish catch and connects it to a user"""

    __tablename__ = 'fish_catches'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    species_id = db.Column(
        db.Integer,
        db.ForeignKey('fish_species.id')
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    lake_id = db.Column(
        db.Integer,
        db.ForeignKey('lakes.id')
    )

    length = db.Column(
        db.Float
    )

    weight = db.Column(
        db.Float
    )
    
    catch_timestamp = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now
    )

    barometric = db.Column(
        db.Float
    )

    temperature = db.Column(
        db.Integer
    )

    weather_conditions = db.Column(
        db.Text
    )

    wind_direction = db.Column(
        db.String(2)
    )

    fish_image = db.Column(
        db.Text,
        default='/static/images/stock-fish.jpg'
    )

    is_master_angler = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
    )

    species= db.relationship('FishSpecies', backref=db.backref('species_fish_catches'))
    user = db.relationship('User', backref=db.backref('uesr_fish_catches'))
    lake = db.relationship('Lake', backref=db.backref('lake_fish_catches'))

class MasterAnglerReq(db.Model):
    """Model to display master angler length requirements for each species"""

    __tablename__ = 'master_angler_reqs'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    species_id = db.Column(
        db.Integer,
        db.ForeignKey('fish_species.id')
    )

    min_length = db.Column(
        db.Float,
        nullable = False
    )

    master_angler_species= db.relationship('FishSpecies', backref=db.backref('master_angler_reqs'))


