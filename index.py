from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def getVal():
    name = request.form['Emp']
    return render_template('pass.html', nm=name)


if __name__ == "__main__":
    app.run(debug=True)
