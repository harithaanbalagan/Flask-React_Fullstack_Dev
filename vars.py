from crypt import methods
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('hello.html',list_of_names=['hi','haritha'])

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/<int:name>")
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(debug=True)