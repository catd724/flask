from flask import Flask,url_for,render_template,request
from markupsafe import escape
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def mainpage():
    return render_template('index.html')




@app.route("/name", methods=["POST","GET"])
def namepage():

    pname = request.form.get("pname","[No name entered!]")
    page = request.form.get("page","[No age entered!]")
    pemail = request.form.get("pemail","[No email entered!!]")

    return render_template("name.html",pname=pname,page=page,pemail=pemail)


# @app.route("/post/<int:post_id>")
# def post(post_id):
#     return f"you are reading post with post_id {escape(post_id)}"

# @app.route("/about/")
# def about():
#     return "<h1>about</h1>"

# with app.test_request_context():
#     print(url_for("namepage",pname =  "kashif"))
#     print(url_for("post",post_id = '1234'))
