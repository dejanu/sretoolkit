import json

##json.dump = serialize obj to a JSON formatted string
##json.dumps = serialize obj as a JSON formatted stream to fp

persons_dict =  [{"name":"lex","age":24},
                 {"name":"aria","age":23},
                 {"name":"vict","age":45},
                 {"name":"noser","age":51},]



##Serialization(dump) python object - json file


##Method_1 - put the python object into json file DUMPS(obj)
dict_info  = json.dumps(persons_dict)
f = open('Persons1.json','wb')
f.write(dict_info)
f.close()
    

##Method_2 - put the python object into json file DUMP(obj, fp)- Serialize obj as a JSON formatted stream to fp
with open('Persons2.json','wb') as MyFile:
    json.dump(persons_dict,MyFile)

#JSON into a file/socket or whatever, then you should go for dump()
# string (for printing, parsing or whatever) then use dumps()
#The functions with an s take string parameters. The others take file streams.

##Deserialization - take the json file put it into an object (dict/list)

with open('Persons1.json','rb') as f:
    dict_object = json.load(f)
    
print(type(dict_object))


x = json.loads('{"name":"lex","age":24}')
