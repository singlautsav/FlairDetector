from flask import Flask, render_template, request, jsonify
from Supporter.reddit import getRed
import pickle
from pymongo import MongoClient
import urllib.parse
import pandas as pd
import numpy as np
import json



user = urllib.parse.quote_plus('utsavsingla')
password = urllib.parse.quote_plus('Python@123')
connection_params = {
'user': user,
'password': password,
'host': 'ds253567.mlab.com',
'port': 53567,
'namespace': 'heroku_kr16tlsv',}

connection = MongoClient(
'mongodb://{user}:{password}@{host}:'
'{port}/{namespace}'.format(**connection_params)
)
db = connection.heroku_kr16tlsv
    # print(db.collection_names())
graph = db.graphs
app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        link = request.form['name']
        result = getRed(link)
        model = pickle.load(open("modelTCBU-c2.sav",'rb'))
        result = model.predict([result])[0]
        return render_template('index.html',result=result)
    else:
        return render_template('index.html')


@app.route('/graphs')
def getGraph():
    df = pd.DataFrame(list(graph.find()))
    del df['_id']
    features = df.columns[1:].values.tolist()
    field = request.args.get('field')
    if field =='mean':
        vals = list(df[features[2]])
        vals2 = list(df[features[3]])
        # print(vals)
        return render_template('index1.html',v1='Average # Comments',v2='Average # of Upvotes',values = vals,values2=vals2,maxVal = 1500)
    elif field=='max':
        vals = list(df[features[0]])
        vals2 = list(df[features[1]])
        return render_template('index1.html',v1='Max # Comments',v2='Max # of Upvotes',values = vals,values2=vals2, maxVal=20000)





if __name__ == '__main__':
    
    app.run(debug = True)