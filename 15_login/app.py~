#Henry Liu and Biraj Chowdhury
#SoftDev1 pd9
#K15: Do I Know You?
#2019-10-02

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
#imports
app = Flask(__name__)

@app.route("/")
def dis_loginpage():
    print(url_for("success"))
    if ("username" in request.args) & ("password" in request.args):
        usernam = request.args["username"]
        passwor = request.args["password"]
        if (passwor == "1234") & (usernam == "Peglegs"):
            return redirect(url_for("success"))
        else:
            return redirect(url_for("try_again_please"))
    return render_template(
    'form.html'
    )

##link the starting page to the template, then connect it
#to the form

@app.route("/welcome")
def success():
    return "Welcome"
    #when you get redireccted to auth, show them the submited
    #the submited has python on it to show the username

@app.route("/whoops")
def try_again_please():
    if ("username" in request.args) & ("password" in request.args):
        usernam = request.args["username"]
        passwor = request.args["password"]
        if (passwor == "1234") & (usernam == "Peglegs"):
            return redirect(url_for("success"))
    return render_template(
    'loginError.html'
    )



if __name__ == "__main__":
  app.debug = True
  #run the main code
  app.run()
