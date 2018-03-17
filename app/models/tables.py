# from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Base



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30),unique=True, nullable=False)
    password = Column(String(30), nullable=False)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User: %s>' % self.username


# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)

# def insert_user(username, password):
#     new_user = User(username=username, password=password)
#     session = Session()
#     session.add(new_user)
#     session.commit()

# insert_user('marcos', '1234')
