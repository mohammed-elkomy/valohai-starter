# -*- coding: utf-8 -*-
import sys

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
queries = []


@app.route("/", methods=['GET'])  # go to localhost:PORT/
def main():
    return request.args['hub.challenge']


@app.route("/c", methods=['GET'])  # go to localhost:PORT/c
def check():
    return jsonify("The server is okay don't worry")


@app.route("/", methods=['POST'])  # go to localhost:PORT/ you cant POST from browser
def post():
    try:
        # print(json.dumps(request.get_json(), indent=4, sort_keys=True))
        content = request.get_json()
        # print("content", content)

        jsondata = {
            # go to facebook messenger api webhook and add the server tunnelled url
            # 'access_token': "GET ACCESS TOKEN FROM MESSENGER API"
            'access_token': "EAAaZCJ5hSWOMBADSRE4GIyellRNTBTq90r3bnZCmBuCfNQtESE4hL11aZCpmEoi1yuZBht82UFx9G4O67ZCSqHWpOlqdLnUOEJeRiSQqZAh7OXF8ib8PxWRLTg9FbIv5dksQAG4wbaH5he7rkBF1PCMYoWCxGr80ZCk4vW1w24qQwZDZD"

            , "recipient": {"id": content["entry"][0]["messaging"][0]['sender']['id']}
            , "message": {"text": "يسطى متقوليش " + content["entry"][0]["messaging"][0]['message']['text']}
        }
        requests.post('https://graph.facebook.com/v2.6/me/messages', json=jsondata)

    except Exception as e:
        print(e, file=sys.stderr)

    # content[]
    return "s"


if __name__ == "__main__":
    app.run()

# the server will work on port 5000
# go to this http://127.0.0.1:5000/c
# use node and install local tunnel https://github.com/localtunnel/localtunnel
# run the command lt --port 8000
# try this too https://www.noip.com/


