from flask import Flask, render_template, request
from database import *
from textblob import TextBlob

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

# TODO: Add all of the routes you want below this line!


@app.route("/")
def index():
	return render_template("index.html")



@app.route("/precomment", methods=['GET', 'POST'])
def precomment():
  if request.method == 'GET':
    return render_template('precomment.html')
  else:
    textmsg = request.form['comment']
    add_post(textmsg)
    a = query_all_posts()
    blob1 = TextBlob(textmsg).sentiment.polarity
    if blob1>0:
      polarity="positive"
    else:
      polarity="negative"
    return render_template('comment.html', posts=a ,blob=polarity)
def sentement(txt):
  return TextBlob(txt).polarity

@app.route("/comment")
def comment():
	return render_template("comment.html")

@app.route("/mariam")
def mariam():
	return render_template("mariam.html")

@app.route("/post")
def post():
	return render_template("post.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login.html")
	else:
		email = request.form['email']
		print(email)
		print(check_email(email))
		if check_email(email) != None:
			response = requests.get(
			    "https://api.thecatapi.com/v1/images/search?api_key=5ca4c802-7ef7-4f56-a413-07a5e46eb8b4"
			).json()
			cat_pic = response[0]['url']
			# print(cat_pic)
			return render_template("precomment.html", cat_url=cat_pic)
		else:
			return render_template("login.html")


@app.route("/conversations", methods=['GET', 'POST'])
def conversations():

	if request.method == 'GET':
		return render_template("conversations.html")
	else:
		comment = request.form['comment']

		add_comment(comment)
		return render_template("comment.html")


@app.route("/about_us")
def about_us():
	return render_template("about_us.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template("signup.html")
	else:
		email = request.form['email']

		password = request.form['password']

		add_user(email, password)
		return render_template('login.html')


# cat = parsed_content["photos"][0]["img_src"]

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=504, debug=True)
