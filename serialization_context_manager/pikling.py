## Pickling boilerplate



import pickle

def pck_ling( d = None):
    """ serialization of d: convert dict obj to byte stream
        and save it to disk"""
    
    if isinstance(d, dict):

        #create file on disk
        pickle_out = open("dict.tar","wb")
        
        
        #DUMP
        pickle.dump(d, pickle_out)
        pickle_out.close()

    elif isinstance(d, list):

        #using context manager    
        with open('lista.pickle','wb') as f:
            pickle.dump(example_list,f)
        
    else:
        print("d not dict")


def unpck_ling( file_pickle = None):
    """ Deserialization of file_pickle """

    if file_pickle:

        with open(file_pickle, 'rb') as f:
            #LOAD
            python_object = pickle.load(f)
        return python_object

if __name__ == "__main__":
    
    example_dict ={1:"word1",2:"word2",3:"word3"}

    example_list=["get","post","put","delete"]

    pck_ling(example_dict)
    pck_ling(example_list)
    
    print(unpck_ling( file_pickle = "lista.pickle"))
