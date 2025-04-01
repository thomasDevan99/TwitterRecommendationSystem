import time
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"api/*":{"origins":"*"}})
app.config['CORS HEADERS'] = 'Content-Type'


@app.route('/api/search_query', methods = ['GET', 'POST', 'PATCH', 'DELETE'])
@cross_origin()
def search_query(): 
    if request.method == 'PATCH': 
        data = request.get_json('query')
        return {
            'type': 'PATCH', 
            'data': data
        }
    if request.method == 'POST':
        data = request.get_json('query')
        return {
            'type': 'POST', 
            'data': data
        }
    if request.method == 'GET': 
        data = request.get_json()
        return {
            'type': 'GET', 
            'data': data
        }


@app.route('/api/results', methods = ['GET', 'POST', 'PATCH', 'DELETE'])
@cross_origin()
def results(): 
    data = request.get_json()
    return {
        'data': data
    }

    




