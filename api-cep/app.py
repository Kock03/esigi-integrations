import os
from flask import Flask
from flask_restful import Resource, Api
from requests import put, get, post, delete
from flask import request
import requests
from requests.api import request

app = Flask(__name__)

@app.route('/street/<zipCode>')
def getStreet(zipCode):

    request = requests.get('https://viacep.com.br/ws/' + str(zipCode) + '/json')

    return request.json()
        
 
