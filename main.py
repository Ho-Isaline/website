import os
import glob
from flask import Flask, render_template
server = Flask("whatever")

@server.route("/")
def index():
    yuck = glob.glob("bookshelf/*")
    yuck = [suck.split("/")[-1] for suck in yuck[::-1]]
    return render_template("index.html", yucky = yuck)
@server.route("/bookshelf/<x>")
def bookshelf(x):
    firstname = glob.glob("bookshelf/" + x + "/*.txt")
    l = []
    for interview in firstname:
        name = os.path.split(interview)[-1].replace(".txt", "")
        i = open(interview)
        book = i.read()
        i.close()
        l.append((name, book))
    return render_template("bookshelf.html", j = l)
server.run(debug = True,
            host = "0.0.0.0",
            port = "3000")
