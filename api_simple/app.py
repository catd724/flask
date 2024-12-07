from flask import Flask, jsonify,request,render_template,redirect
import requests


API_KEY = "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
headers = {"Authorization": API_KEY}
payload = {
     "inputs":None
}
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	

app = Flask(__name__)

test = {"name":"Kashif", "degree":"BSCS"}
@app.route("/")
def chatbot():

    return render_template("chatbot.html",response=None)

@app.route("/question" , methods=["POST","GET"])
def new_user():
    if request.method == "POST":
        question = request.form.get("question")
        payload["inputs"] = question
        response = query(payload=payload)
        answer = response[0]["generated_text"]
        

    return render_template("chatbot.html", response=answer)



if __name__ == "__main__":
    app.run(debug=True)