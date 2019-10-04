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
    global reason
    print(url_for("success"))
    if ("username" in request.args) & ("password" in request.args):
        usernam = request.args["username"]
        passwor = request.args["password"]
        if (passwor == "1234") & (usernam == "Peglegs"):
            return redirect(url_for("success"))
        elif (usernam != "Peglegs") & (passwor != "1234"):
            reason = " Your username and password were both incorrect"
            return redirect(url_for("try_again"))
        elif (usernam != "Peglegs"):
            reason = " Your username was incorrect"
            return redirect(url_for("try_again"))
        else:
            reason = " Your password was incorrect"
            return redirect(url_for("try_again"))
    return render_template(
    'login.html'
        )
    

@app.route("/welcome")
def success():
    return render_template(
        "loggedIn.html"
        )

@app.route("/whoops")
def try_again():
    global reason
    if ("username" in request.args) & ("password" in request.args):
            usernam = request.args["username"]
            passwor = request.args["password"]
            if (passwor == "1234") & (usernam == "Peglegs"):
                return redirect(url_for("success"))
            elif (usernam != "Peglegs") & (passwor != "1234"):
                reason = " Your username and password were both incorrect"
                return redirect(url_for("try_again"))
            elif (usernam != "Peglegs"):
                reason = " Your username was incorrect"
                return redirect(url_for("try_again"))
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
