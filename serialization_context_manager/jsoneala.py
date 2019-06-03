import json

##{
##    "name":"alex",
##    "surname":"dej",
##    "phone":"1231432"
##
##}

book = {}

#add elem
book['tom'] = {
    "name":"super",
    "surname":"tare",
    "phone":"313"
}

book['marinica'] = {
    "name":"dany",
    "surname":"mocanu",
    "phone":"1423"
}

#json dumps  the object into a string
s=json.dumps(book)

with open('book.json','wb') as f:
    f.write(s)

f=open('book.json','rb')
citit=f.read()
f.close()

json_out=json.loads(citit)

print(type(json_out))
def serializeBody(request_obj,file_name="default.json"):
    """Serialize a dict object to s JSON formatted str"""
    # DUMPS = serialize a dict object to a JSON formatted str
    repos_obj = json.dumps(request_obj.json())
    with open(file_name,'wb') as f:
        f.write(repos_obj)

def deserializeJson(file_name="default.json"):
    """ open file and deserialize the json object into a dict """
    json_file = open(file_name,'rb')
    info = json.load(json_file)
    json_file.close()
    return info
