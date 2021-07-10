from flask import Flask, render_template, url_for
from posts import posts # blog post data
from dotenv import dotenv_values

app = Flask(__name__) 

app.config['SECRET_KEY'] = dotenv_values('.env.SECRET_KEY')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title="About")
