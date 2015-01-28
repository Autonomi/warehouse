#!/usr/bin/env python3

import os, json, bson, re
from bottle import Bottle, request

application = Bottle()
app = application

@app.route('/')
def index():
    return  '''
                <p><a href="/parks">All Parks</a></p>
                <p><a href="/parks/park">Query by Park ID</a></p>
                <p><a href="/parks/name">Query by Park Name</a></p>
                <p><a href="/parks/near">Query by Coordinates</a></p>
                <p><a href="/parks/name/near">Query by Park Name & Coordinates</a></p>
            '''

@app.route('/hello')
@app.route('/hello/<name>')
def greet(name='Stranger'):
    return 'Hello %s, how are you?' % name
