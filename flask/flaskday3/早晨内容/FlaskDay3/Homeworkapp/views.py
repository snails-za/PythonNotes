from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)


@app.route("/index/")
def index_view():
    return render_template("index.html")


@app.route("/sex/<choicesex>/")
def sex_view(choicesex):
    if choicesex == "man":
        pic_path = url_for('static',filename='images/boy.jpg')
    else:
        pic_path = url_for('static',filename='images/girl.jpg')
    return jsonify({"sex_path":pic_path})

print(app.url_map)