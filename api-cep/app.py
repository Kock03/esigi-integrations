import os
from flask import Flask
from flask_restful import Resource, Api
from requests import put, get, post, delete
from flask import request
import requests
from requests.api import request
from flask_cors import CORS, cross_origin

app = Flask('app')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/street/<zipCode>')
@cross_origin()
def getStreet(zipCode):

    request = requests.get(
        'https://viacep.com.br/ws/' + str(zipCode) + '/json')

    return request.json()

if __name__ == "__main__":

  app.run(port=8000) 
