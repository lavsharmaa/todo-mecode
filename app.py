from flask import Flask, render_template, request, abort, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def index():
    return 'Nothing'

if __name__ == '__main__':
    app.run(host='0.0.0.0')