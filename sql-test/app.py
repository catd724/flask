from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:489096@localhost/test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    def __repr__(self) -> str:
        return f"<user: {self.name}>"
    

@app.route("/")
def show_user():
    data = User.query.all()

    return render_template("index.html", data=data)


@app.route("/add", methods = ["POST"])
def tadd():
    ename = request.form.get("name")
    eemail = request.form.get("email")
    new_user= User(name = ename, email = eemail)
    db.session.add(new_user)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)