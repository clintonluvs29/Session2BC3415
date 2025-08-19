print('starting flask')

from flask import Flask, render_template, request

app = Flask(__name__)

#gunicorn runs wsgi standard (communicates with front and backend)
@app.route("/",methods=["GET","POST"]) #framework (landing page) #decorator
def index(): #1985 html style
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"]) #3 places
def main(): 
    #database

    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs(): 
    q = float(request.form.get("q"))
    return(render_template("dbs.html", r=(-50.6*q)+90.2))

if __name__ == "__main__": #yes, run cloud
    app.run()

