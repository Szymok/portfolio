from flask import Flask, render_template, redirect, request
from datetime import datetime

app = Flask(__name__, static_folder='./static')

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/single', methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run(debug = 'True')