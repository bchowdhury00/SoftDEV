from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "no hablo queso!"

@app.route("/cream")
def how_zebra():
    print("_mane_")
    return "cheese cake is the best type of cake"

@app.route("/next")
def not_even():
    print("true")
    return "everything you just said is a lie"

if __name__ == "__main__":
    app.debug = True
    app.run()
