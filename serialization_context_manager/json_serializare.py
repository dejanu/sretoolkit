import json

## reading and writing to/from unicode strings DUMPS/LOADS
## reading and writing to/from files  DUMP/LOAD  
## JSON into a file/socket or whatever, then you should go for dump()
## string (for printing, parsing or whatever) then use dumps()
## The functions with an s take string parameters. The others take file streams.



persons_dict =  [{"name":"lex","age":24},
                 {"name":"aria","age":23},
                 {"name":"vict","age":45},
                 {"name":"noser","age":51},]



def json_serial(python_object =  None):
    """ Serialization(dump) python object - json file """
    if python_object:
        with open('persons.json','w') as f:
            json.dump(python_object, f)

        # a bytes-like object is required, not 'str'
##        with open('persons.json','wb') as f:
##            json.dump(python_object, f)
    else:
        print("No object is given as parameter")
            



##Method_1 - serialize obj as a JSON formatted  STRING : DUMPS(obj) takes 1 positional argument
dict_info  = json.dumps(persons_dict)


## Write JSON formatted STRING TO file
f = open('Persons.json','w')
f.write(dict_info)
f.close()
    
##Desearialize json
f = open("Persons.json","r")
o = json.loads(f.read())
f.close()

print("Object serialised with DUMPS{} \n and read with LOADS{}".format(dict_info, o))


#--------------------------------------------------------------------------

##Method_2 - Serialize obj as a JSON formatted stream to fp: DUMP(obj, fp)
with open('Persons2.json','w') as MyFile:
    json.dump(persons_dict,MyFile)


##Deserialization - take the json file put it into an object (dict/list)

with open('Persons1.json','r') as f:
    dict_object = json.load(f)  

    


if __name__ == "__main__":

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

