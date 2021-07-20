from flask import Flask, render_template, session, redirect, url_for, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/user/input", methods = ["POST"])
def user_input():
    amount = request.form.get("amount")
    category = request.form.get("category")
    difficulty = request.form.get("difficulty")
    type = request.form.get("type")

    return jsonify(0)


if __name__ == '__main__':
    app.run(debug=True)