from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/random")
def random_num():
    import random
    resp={
        "random_number":random.randint(1,100)
    }
    return resp