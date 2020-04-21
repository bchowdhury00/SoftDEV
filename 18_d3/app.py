# Calvin Chu, Biraj Chowdhury - Team McChargers
# SoftDev2 pd9
# K18: Come Up For Air
# 2020-04-20

from flask import Flask, render_template
import csv

app = Flask(__name__)

def parseCSV(file):
    arr = []
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        count = 0
        categories = []
        for row in spamreader:
            if (count == 0):
                for i in row:
                    categories.append(i)
            else:
                dict = {}
                for i in range (len(categories)):
                    dict[categories[i]] = row[i]
                arr.append(dict)
            count += 1
    return arr

@app.route("/")
def root():
    # print(parseCSV("static/drinks.csv"))
    categories = []
    result = parseCSV("static/drinks.csv")
    for key in result[0]:
        categories.append(key)
    return render_template('index.html', data = result, cat = categories)

if __name__ == "__main__":
    app.debug = True
    app.run()
