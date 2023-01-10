
from flask import Flask

app = Flask(__name__)



@app.route('/')
def home_page():  
    html = """ 
    <html>
        <body>
        </body>
    </html>
    """
    return html


@app.route("/welcome")
def say_welcome():
    return "Welcome!"


@app.route("/welcome/home")
def say_welcome_home():
    return "Welcome Home!"


@app.route("/welcome/back")
def say_welcome_back():
    return "Welcome Back!"