from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# TODO: Add your models below this line!

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key = True)
  email = Column(String)
  password = Column(String)

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key = True)
  post_text = Column(String)

class Comment(Base):
  __tablename__ = 'comments'
  id = Column(Integer, primary_key = True)
  comment = Column(String)
