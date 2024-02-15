import datetime
import uuid
import random
import pytz
from flask import Flask, request, Response

tz = pytz.timezone("Europe/London")

app = Flask(__name__)


@app.route("/err/<CODE>",
    methods=['GET'])
def returncode(CODE):
    c = int(CODE)
    if c > 100 and c < 599:
        resp = Response(status=c)
        return resp
    else:
        resp = Response(status=404)
        return resp


@app.route("/help",
    methods=['GET'])
def help():
    return "Visit /err/xxx where xxx is your favourite http response code :)"


@app.route("/health",
    methods=['GET'])
def health():
    return "ok"


@app.route("/",
    methods=["GET"])
def root():
    request_data = request.url
    return {
        "greeting": ["Hello", "World"],
        "date": datetime.date.today(),
        "you_visited": str(request_data)}


@app.route("/uuid",
    methods=["GET"])
def provide_uuid():
    unique_id = uuid.uuid4()
    return unique_id.__str__()


@app.route("/flaky/<CODE>/<FAILRATE>")
def flaky_fail(CODE,FAILRATE):
    try:
        c = int(CODE)
        r = int(FAILRATE)
    except:
        return ("code and failure rate must both be integers")

    if not (c > 100 and c < 599):
        return "Please supply a valid <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Status\">status code</a>"
    elif not (r > 0 and r < 100):
        return "Please supply a failure rate of at least 1 and no more than 100"
    
    rand = random.randint(1,100)
    if rand > 1 and rand <= r:
        return Response(status=c)
    else:
        return "Success"


if __name__ == "__main__":
    app.run(host='0.0.0.0',
        debug=False,
        port=80)
