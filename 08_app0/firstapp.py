#Biraj Chowdhury
#SoftDev1 pd 9
#K08 -- <LemmeFlaskYouSump'n/Flask App/first flask app>
#2019--09--19

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "no hablo queso!"

@app.route("/this")
def what_even():
    print("isyou")
    return "doing even"

@app.route("/cream")
def how_even():
    print("absolutelynothing")
    return "what is it good for"

if __name__ == "__main__":
    app.debug = True
    app.run()
