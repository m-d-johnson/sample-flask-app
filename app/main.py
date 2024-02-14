import datetime
import uuid

import pytz
from flask import Flask, request, Response

unique_id = uuid.uuid4()
tz = pytz.timezone("Europe/London")

app = Flask(__name__)

@app.route("/err/<CODE>", methods=['GET'])
def returncode(CODE):
    c = int(CODE)
    if c > 100 and c < 599:
        resp = Response(status=c)
        return resp
    else:
        resp = Response(status=404)
        return resp

@app.route("/help", methods=['GET'])
def help():
    return "visit /err/xxx where xxx is your favourite http response code :)"

@app.route("/", methods=["GET"])
def root():
    request_data = request.url
    return {
        "greeting": ["Hello", "World"],
        "date": datetime.date.today(),
        "you_visited": str(request_data)
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
