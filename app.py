from flask import Flask
from flask import request, render_template, redirect

app = Flask(__name__)

@app.route('/me', methods = ['GET', 'POST'])
def hello_o():
    if request.method == 'GET':

        return render_template("o-mnie.html")
    elif request.method == 'POST':
        f = open("formatka", "a")
        f.write(request.form["firstname"])
        f.close()
        return render_template("thanks.html", kto=request.form["firstname"])

    return

@app.route('/contakt', methods=['GET', 'POST'])
def hello_k():
    if request.method == 'GET':
        return render_template("kontakt.html")
    elif request.method == 'POST':
        f = open("formatka", "a")
        f.write(request.form["wiadomosc"]+"\n")
        f.close()
        return render_template("o-mnie.html", kto=request.form["wiadomosc"])