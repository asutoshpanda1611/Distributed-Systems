from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route("/<op>",methods=["POST"])
def calc(op):
    a=request.json["a"]
    b=request.json["b"]

    if op=="add": r=a+b
    elif op=="sub": r=a-b
    elif op=="mul": r=a*b
    elif op=="div":
        if b==0:
            return jsonify({"result":"Cannot divide by 0"})
        r=a/b
    else: return jsonify({"error":"Invalid"})

    return jsonify({"result":r})

app.run(port=5000)
