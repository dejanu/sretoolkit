#Serialization = convert python obj into byte stream and save it to a file
import pickle

example_dict ={1:"word1",2:"word2",3:"word3"}

#serialization of a dictionary
pickle_out = open("dict.tar","wb")
#dump (object,file)
pickle.dump(example_dict,pickle_out)
pickle_out.close()            

#deserialization
##pickle_in=open("dict.pickle","rb")
##new_dict=pickle.load(pickle_in)
###print (new_dict)

#--------------------------
example_list=["get","post","put","delete"]

with open('lista.pickle','wb') as f:
    pickle.dump(example_list,f)


with open('lista.pickle','rb') as f:
    pickle_out=pickle.load(f)
print(pickle_out)
