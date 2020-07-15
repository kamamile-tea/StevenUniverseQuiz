from flask import Flask
from flask import render_template
from flask import request

# -- Initialization section --
app = Flask(__name__)

user = ""

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ["GET", "POST"])
def results():
    score = 0
    
    if request.method == "GET":
        print(request.form)
    elif request.method == "POST":
        print(request.form['q1'])
        for i in request.form:
            score += int(request.form[i])
        if score >=0 and score < 5:
            user = "Pearl"
        elif score >=5 and score < 7:
            user = "Amythest"
        elif score >=7 and score <=9:
            user = "Garnet"
        else:
            user = "ERROR"
    return render_template('results.html', props = user)
