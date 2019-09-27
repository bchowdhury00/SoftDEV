#Biraj Chowdhury and Taejoon Kim Team Excelcius
#SoftDev1 pd 9
#K12 <Echo Echo EchoRise The Tide/Html forms/Using the request methods and html forms>
#2019 09 26

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/auth")
def render():
    render_template("foo.html")
    print(app)
    print("//////////////}}}}}}}}}}}}}}}}}}}}}}}}")
    print(request.args)
    print("################################################")
    if "yourname" in request.args:
        yourname = request.args["yourname"]
    else:
        yourname = "User"
    return render_template("foo.html",name=yourname)
    

if __name__ == "__main__":
    app.debug = True
    app.run()
