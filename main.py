from flask import Flask,url_for
from markupsafe import escape

app = Flask(__name__)
@app.route("/")
def mainpage():
    return f'''<h1> Home </h1>
    <a href = "{url_for('home',name = 'kashif')}">kashif</a> '''




@app.route("/<name>")
def home(name):

    return f"<p>Hello, World! {escape(name)}</p>"


@app.route("/post/<int:post_id>")
def post(post_id):
    return f"you are reading post with post_id {escape(post_id)}"

@app.route("/about/")
def about():
    return "<h1>about</h1>"

with app.test_request_context():
    print(url_for("home",name =  "kashif"))
    print(url_for("post",post_id = '1234'))
