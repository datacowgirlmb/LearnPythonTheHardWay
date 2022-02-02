from flask import Flask
from flask import render_template
from flask import request
import os
from datetime import datetime, date

app = Flask(__name__, template_folder="templates/")

@app.route('/', methods=['POST','GET'])

def index():
    customername='(None)'

    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        # dob2 = datetime.datetime.strptime(dob, "%B %d, %Y")
        customer_name = first_name + ' ' + last_name
        return render_template("index.html", customer_name=customer_name, dob=dob)
    else:
        return render_template("customer_form.html")

if __name__ == "__main__":
    app.run(threaded=True)
