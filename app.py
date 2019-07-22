from flask import Flask, render_template, request, jsonify
from redditFIles.reddit import getRed
import pickle
import pymongo
# import pandas as pd
import numpy as np


app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        link = request.form['name']
        result = getRed(link)
        model = pickle.load(open("../Data/modelTCBU-c2.sav",'rb'))
        result = model.predict([result])[0]
        return render_template('index.html',result=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    uri = 'mongodb://<dbuser>:<dbpassword>@ds253567.mlab.com:53567/heroku_kr16tlsv'
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    app.run(debug = True)