from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html', name="Iresh", lists=[1,2,3,4])

if __name__ == "__main__":
    app.run(debug = True)