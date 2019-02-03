from models import *
import requests,json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def function(parameter):
    pass

def add_product(user,password):
    new_prod= User(username = user, info= info) 
    session.add(new_prod)
    session.commit()
