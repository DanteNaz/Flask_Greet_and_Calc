# Put your app in here.

from flask import Flask, request

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




@app.route("/add")
def add():

    a = request.args["a"]
    b = request.args["b"]

    return str(int(a) + int(b))



@app.route("/sub")
def sub():
    
    a = request.args["a"]
    b = request.args["b"]

    return str(int(a) - int(b))


@app.route("/mult")
def mult():

    a = request.args["a"]
    b = request.args["b"]

    return str(int(a) * int(b))




@app.route("/div")
def div():

    a = request.args["a"]
    b = request.args["b"]

    return str(int(a) / int(b))
