from flask import request,jsonify, Flask, make_response, url_for, render_template
import nest
import json


app = Flask(__name__)

## Authetication to /
# curl http://alex:admin@127.0.0.1:5000/

## POST to /data
# curl -vX POST -d @input.json http://alex:admin@127.0.0.1:5000/upload --header "Content-Type: application/json"

## GET request /raport?currency=USD
# curl  -X GET http://alex:admin@127.0.0.1:5000/raport?currency=USD
# curl -i -H "Accept: application/json" -H "Content-Type: application/json" "http://alex:admin@127.0.0.1:5000/upload?one=currency&two=country&three=city"

@app.route("/", methods = ["GET"])
def main():
    """ index """
    if request.authorization and request.authorization.username == "alex" and request.authorization.password == "admin":
        #return "<h3> You are logged in POST your json to http://localhost:5000/upload </h3>"
        return render_template('index.html')
    else:
        return make_response("Could not verify!", 401, {"WWW-Authenticate":'Basic realm="Login Required"'})


def open_file(name):
    try:
        with open(name) as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return None    

@app.route("/upload",methods=["POST","GET"])
def data():
    """ endpoint to upload/retrieve data"""

    # check if request is POST
    if request.method == "POST":
        r = request.json
        # ignore content-type r = request.get_json(force=True)
    
        #write json to disk
        with open('user_data.json', 'w') as f:
            json.dump(r,f)

        return jsonify(r)

    # check if request is GET
    elif request.method == "GET":
        f = open_file("user_data.json")
        if f:
            query_params = len(request.args)
            if (query_params>=1) and (query_params<=3) :
                
                q_params = [ v for k,v in request.args.items()]
                return jsonify(nest.create_output(f,*q_params))
            else:
                return "Please user between 1 or 3 query parameters"

        # user_json not present on disk
        else:
            return "Please first make  a POST request with json at http://localhost:5000/data "      
    
    else:
        return "Use POST /data or GET /data?param=value&param2=value"

if __name__ == "__main__":

    app.run(debug=True)
