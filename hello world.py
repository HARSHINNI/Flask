from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>hello world</h1>'
@app.route('/about/<username>')
def about_page(username):
    return f'<h1>about page of the {username}</h1>'