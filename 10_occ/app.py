#Biraj Chowdhury and Leia Park
#SoftDev Pd 9
#K10 -- Jinga Tuning/Templating with Jinga/Use Jinga to write HTML
#2019--09-22Biraj Chowdhury and Leia Park

from flask import Flask, render_template

import random
csv = open("occupations.csv", "r")
data = csv.read().strip('\n').split('\n')

occupations_dict = {}


def init_dict():
    for entry in data[1:len(data)-1]:
        if entry.count(',') > 1:
            occupation = entry.strip('"').split('"')
            occupations_dict[occupation[0]] = float(occupation[1].strip(','))
        else:
            occupation = entry.split(',')
            occupations_dict[occupation[0]] = float(occupation[1])


csv.close()
init_dict()

def random_occupation(dict):
    rand = random.random() * float(data[len(data)-1].split(',')[1])
    sum = 0.0
    for occupation in dict:
        sum += dict[occupation]
        if rand < sum:
            return occupation


app = Flask(__name__)

@app.route("/occupyflaskst")
def flaskismIsKillingTheMiddleClass():
    print("huh")
    return render_template('jobs.html',
                               randomOccupation=random_occupation(occupations_dict),
                               jobs = list(occupations_dict.keys()),
                               percents =list(occupations_dict.values()))
app.debug = True
app.run()

    
