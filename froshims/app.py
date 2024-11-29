from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods= ["POST"])
def register():
    pname = request.form["pname"]

    return render_template("end.html", pname = pname)
