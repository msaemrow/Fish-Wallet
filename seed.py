from app import db
from models import FishCatch, User, MasterAnglerReq, Lake, FishSpecies

db.drop_all()
db.create_all()
