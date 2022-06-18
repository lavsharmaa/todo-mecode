from flask import Flask, render_template, request, abort, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/forgot_password')
def forgot_password():
    return render_template("forgot_password.html")

@app.route('/todo_list')
def todo_list():
    return render_template("todo_list.html")

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')