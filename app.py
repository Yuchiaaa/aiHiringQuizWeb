from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '14806762'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aihiring')
def aihiring():
    return render_template("aihiring.html")

@app.route('/dilemmas')
def dilemas():
    return render_template("dilemmas.html")

@app.route('/solutions')
def solutions():
    return render_template("solutions.html")

@app.route('/cases')
def cases():
    return render_template("cases.html")

@app.route('/sources')
def sources():
    return render_template("sources.html")

@app.route('/about')
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.run(debug=True, port=5006)
