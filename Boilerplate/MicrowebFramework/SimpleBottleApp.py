##Bottle has no dependencies it is just one module
from bottle import run, route, template

import socket

##application object
##app = Bottle()
##run(app, host='localhost', port=8080)


## route = links an URL path to a callback function,
##and adds a new route to the default application.

## STATIC routes

@route('/')
def index():
    my_ip = str(socket.gethostbyname(socket.gethostname()))
    return '<h1> Your ip:'+my_ip+'</h1>'

@route('/about')
def about_page():
    return "<h2> About page </h2>"

## DYNAMIC routes (user wildcard and match more the one url)

##bind more than one route to a single callback
@route('/hello')
@route('/hello/<name>')
def greet(name="Stranger"):
    """default argument for route hello without get params"""
    return template('Hello {{name}}, what is up',name=name)




if __name__ == '__main__':
    run(host='localhost',port=8080,debug=True)
