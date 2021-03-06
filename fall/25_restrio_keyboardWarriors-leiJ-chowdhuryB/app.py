from os import urandom
from flask import Flask, render_template

from urllib.request import urlopen
from json import loads, dumps

app = Flask(__name__)

app.secret_key = urandom(32)

@app.route("/")
def root():
    return "redirect to /citibike, /ricknmorty, or /collegescorecard"

@app.route("/citibike")
def citibike():
    req = urlopen(
        "http://api.citybik.es/v2/networks/bikemi"
    )
    res = req.read()
    data = loads(res)
    return render_template(
        "citibike.html",
        company=data["network"]["company"][0],
        location=data["network"]["location"]["city"]
    )


@app.route("/ricknmorty")
def ricknmorty():
    req = urlopen(
        "https://rickandmortyapi.com/api/character"
    )
    res = req.read()
    data = loads(res)['results']
    return render_template(
        "ricknmorty.html",
        characters = data
        )


@app.route("/collegescorecard")
def collegescorecard():
    try:
        req = urlopen(
            "https://api.data.gov/ed/collegescorecard/v1/schools?school.name=harvard%20university&api_key=HCoVQQL84LJnQJHkcLlb3p1ZTJn1hVp4AOAnKP1P"
        )
        res = req.read()
        data = loads(res)
        return render_template(
            "collegescorecard.html",
            school=data["results"][0]["school"]["name"],
            avgsat=data["results"][0]["2017"]["admissions"]["sat_scores"]["average"]["overall"],
            medact=data["results"][0]["2017"]["admissions"]["act_scores"]["midpoint"]["cumulative"],
            admitrate=data["results"][0]["2017"]["admissions"]["admission_rate"]["overall"]
        )
    except:
        print("REPLACE YOUR_API_KEY WITH AN ACTUAL API KEY")
        return render_template(
            "collegescorecard.html",
            school="REPLACE YOUR_API_KEY WITH AN ACTUAL API KEY"
        )


if __name__ == "__main__":
    app.run(debug=True)
