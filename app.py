from flask import Flask, render_template, request
from redditFIles.reddit import getRed
import pickle

# import pandas as pd
import numpy as np

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    name = "Utsav"
    return render_template('index.html',name = name)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
        link = request.form['name']
        print(link)
        print(type(link))
        result = getRed(link)
        model = pickle.load(open("modelTCBU-c2.sav",'rb'))
        result = model.predict([result])[0]
        print(result)
        return result

if __name__ == '__main__':
    app.run(debug = True)