from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# TODO: Add your database functions below this line!

posts = {}

def add_user(email, password):
	user_object = User(
	  email = email,
    password = password) 
	session.add(user_object)
	session.commit()

def query_all_posts():
   posts = session.query(
      Post).all()
   return posts



def check_email(emailExistence):
  email = session.query(User).filter_by(email=emailExistence).first()
  return email
# add_user("yoav4321@gmail.com", "yoav4321")
# add_user("joman1357@gmail.com", "joman1357")
# add_user("saba2468@gamil.com", "saba2468")
# add_user("rashadrabah21@gmail.com", "rashadrabah21")


def add_post(post_text):
  post_object = Post(
    post_text = post_text)
  session.add(post_object)
  session.commit()

# add_post("hiii", "hello everyone how u doin")
# add_post("sad post", "this is sad post :( ")


def add_comment(comment):
  comment_object = Comment(
  comment = comment)
  session.add(comment_object)
  session.commit()
  
# add_comment( "Don’t Let Yesterday Take Up Too Much Of Today. – Will Rogers", "")
# add_comment("I would say that this is very emotional", "")