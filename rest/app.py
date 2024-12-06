from flask import Flask,request,redirect,render_template,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "hello"

even_json = {
    "Number":None,
    "Type":None
}

@app.route("/even/<int:num>")
def find(num):
    even_json["Number"] = num
    if num%2==0:
        even_json["Type"] = "even"
        return jsonify(even_json)
    even_json["Type"] = "odd"
    return jsonify(even_json)

if __name__ == "__main__":
    app.run(debug=True)