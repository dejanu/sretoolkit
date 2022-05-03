from bottle import request,response
from bottle import post,get,put,delete
import json,re

##routing is done by decorators, det, post,put,delete register handles for these actions


##@get('/') == @route(method='GET', '/') == @bottle.default_app().route(method='GET', '/')

##in memory data structure
_names = set()

@post('/names')
def creation_handler():
    """Handles name creation"""
    try:
        data = request.json()
        if data is None:
            raise ValueError
        else:
            name = data['name']
        #check for existence
        if name in _names:
            raise KeyError
    except ValueError:
        ##return 400 BadRequest
        response.status = 400
        return
    
    except KeyError:
        ##if name already exist, return 409 conflict
        response.status =409
        return
    _names.add(name)

    # return 200 Success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'name': name})
    
@get('/names')
def listing_handler():
    """Handle name listing"""
    pass

@put('/names/<name>')
def delete_hander(name):
    """Handles name deletions"""
    pass


