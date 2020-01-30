#Biraj Chowdhury
#SoftDev1 pd 9
#K24
#2019--09--19
from urllib.request import urlopen
from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route("/")
def hello_world():
    url = urlopen(
        "https://api.nasa.gov/planetary/apod?api_key=Bd94PpfIjF98GbLOiD89AvlZwM2AE7f85s0kCXYv"
        )
    response = url.read()
    data = json.loads(response)
    return render_template('index.html',text=data['explanation'],pic = data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
