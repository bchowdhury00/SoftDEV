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
reason = ""
@app.route("/")
def dis_loginpage():
    #global is a keyword that allows an user to modify a variable outside the current scope
    global reason
    print(url_for("success"))
    #Check to see if user entered username and password
    if ("username" in request.args) & ("password" in request.args):
        usernam = request.args["username"]
        passwor = request.args["password"]
        #If password and username are correct, say so
        if (passwor == "1234") & (usernam == "Peglegs"):
            return redirect(url_for("success"))
        #If password and username are incorrect,
        elif (usernam != "Peglegs") & (passwor != "1234"):
            reason = " Your username and password were both incorrect"
            return redirect(url_for("try_again"))
        #If username is incorrect, say so
        elif (usernam != "Peglegs"):
            reason = " Your username was incorrect"
            return redirect(url_for("try_again"))
        #If password is incorrect, say so
        else:
            reason = " Your password was incorrect"
            return redirect(url_for("try_again"))
    return render_template(
    'login.html'
        )

#Welcome page
@app.route("/welcome")
def success():
    return render_template(
        "loggedIn.html"
        )

#If password or username is incorrect
@app.route("/whoops")
def try_again():
    global reason
    if ("username" in request.args) & ("password" in request.args):
            usernam = request.args["username"]
            passwor = request.args["password"]
            #If password and username are correct, say so
            if (passwor == "1234") & (usernam == "Peglegs"):
                return redirect(url_for("success"))
            #If password and username are incorrect, say so
            elif (usernam != "Peglegs") & (passwor != "1234"):
                reason = " Your username and password were both incorrect"
                return redirect(url_for("try_again"))
            #If username is incorrect, say so
            elif (usernam != "Peglegs"):
                reason = " Your username was incorrect"
                return redirect(url_for("try_again"))
            #If password is incorrect, say so
            else:
                reason = " Your password was incorrect"
                return redirect(url_for("try_again"))
    return render_template(
        'loginError.html',reasonforError=reason
    )



if __name__ == "__main__":
  app.debug = True
  #run the main code
  app.run()
