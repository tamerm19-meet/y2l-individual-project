from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :

class prod(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    product = Column(String)
    info = Column(String)


    def __repr__(self):
        return ("product: {}, info:{}".format(self.product, self.info))



class Post(Base):
	__tablename__ = "posts"
	id = Column(Integer, primary_key = True)
	category = Column(String)
	description = Column(String)