from urllib.request import urlopen
from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route("/")
def hello_world():
    url = urlopen(
        "http://api.citybik.es/v2/networks/bikemi"
        )
    response = url.read()
    data = json.loads(response)['network']
    return render_template('index.html',
                               company=data['company'][0],
                               location = data['location']['city']
                               )

@app.route("/next")
def nextRoute():
    url = urlopen(

if __name__ == "__main__":
    app.debug = True
    app.run()
