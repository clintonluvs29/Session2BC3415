print('starting flask')

from flask import Flask, render_template, request

app = Flask(__name__)

#gunicorn runs wsgi standard (communicates with front and backend)
@app.route("/",methods=["GET","POST"]) #framework (landing page) #decorator
def index(): #1985 html style
    return(render_template("index.html"))

if __name__ == "__main__": #yes, run cloud
    app.run()

