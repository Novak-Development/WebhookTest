import json
import os
import datetime

from flask import *
app = Flask(__name__)

@app.route('/main', methods=['POST'])

def main():
    text = generate_text()
    resp= hello_world(text)
    resp = json.dumps(resp, indent=4)

    r = make_response(resp)
    r.headers['Content-Type'] = 'application/json'
    return r


def hello_world(text):
    return {
        "speech": text,
        "displayText": "some text",
        "source": "apiai-weather-webhook-sample"
    }
	
def generate_text():
    text = str(datetime.datetime.now())
    return text