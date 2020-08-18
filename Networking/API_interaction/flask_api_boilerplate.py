from flask import request,jsonify, Flask, make_response


app = Flask(__name__)

## Authetication to /
# curl http://alex:admin@127.0.0.1:5000/

## POST to /data
# curl -vX POST -d @input.json http://alex:admin@127.0.0.1:5000/upload --header "Content-Type: application/json"

## GET request /raport?currency=USD
# curl  -X GET http://alex:admin@127.0.0.1:5000/raport?currency=USD
# curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://alex:admin@127.0.0.1:5000/raport?currency=USD

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
    #ignore content-type
    #r = request.get_json(force=True)
    print(r)
    return jsonify(r)

@app.route("/raport", methods=["GET"])
def get_data():
    """ get raport """
    # dict object request.args
    print(request.args)
    return request.args
    
    



if __name__ == "__main__":

    app.run(debug=True)

