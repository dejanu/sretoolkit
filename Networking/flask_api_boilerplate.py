from flask import request,jsonify, Flask


app = Flask(__name__)

## Authetication to /
# curl http://alex:admin@127.0.0.1:5000/

## POST to /data
# curl -vX POST -d @input.json http://alex:admin@127.0.0.1:5000/upload --header "Content-Type: application/json"

@app.route("/", methods = ["GET"])
def main():
    """ index """
    if request.authorization and request.authorization.username == "alex" and request.authorization.password == "admin":
        return "<h3> You are logged in go to http://localhost:5000/upload to <b>upload</b> data</h3>"
    else:
        return make_response("Could not verify!", 401, {"WWW-Authenticate":'Basic realm="Login Required"'})

@app.route("/upload",methods=["POST"])
def data():
    """ get the json from body of POST request"""
    r = request.json
    print(r)
    return jsonify(r)


if __name__ == "__main__":

    app.run(debug=True)

