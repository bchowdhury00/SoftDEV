#Biraj Chowdhury and Leia Park
#SoftDev Pd 9
#K10 -- Jinga Tuning/Templating with Jinga/Use Jinga to write HTML
#2019--09-22Biraj Chowdhury and Leia Park
import randomOccupation
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/occupyflaskst")
def flaskismIsKillingTheMiddleClass():
    print("huh")
    return render_template('jobs.html',randomOccupation=randomOccupation.random_occupation(randomOccupation.occupations_dict),jobs = list(randomOccupation.occupations_dict.keys()),percents =list(randomOccupation.occupations_dict.values()))
app.debug = True
app.run()

    
