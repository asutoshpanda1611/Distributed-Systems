from flask import Flask,request,render_template
import requests

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calc",methods=["POST"])
def calc():
    a=int(request.form["a"])
    b=int(request.form["b"])
    op=request.form["op"]

    r=requests.post(
        f"http://127.0.0.1:5000/{op}",
        json={"a":a,"b":b}
    ).json()

    return render_template("index.html",r=r)

app.run(port=3000)