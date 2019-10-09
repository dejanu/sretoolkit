#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import json
import sys
from itertools import groupby
from operator import itemgetter
from collections import Counter
import argparse


def parse_json():
    """Read json file from stdin and return list of dict """

    if sys.stdin.isatty():
        sys.exit("Please provide json input file from stdin")
    else: 
        return json.load(sys.stdin)  

def parameters():
    """Return the list of arguments passed to the script """

    parser = argparse.ArgumentParser(description=" Process a json array from stdin and return a nested dictionary of dictionaries of arrays ")
    parser.add_argument('keys', nargs='*', type=str, help="Keys used to construct the json")
    args = parser.parse_args()
    if len(args.keys)>3 or len(args.keys)<1:
        sys.exit("Please pass: \nMin 1 arg  and Max 3 args")
    else:
        print("You have passed the follwoing arguments to the script: {} ".format(args.keys))
        return args.keys


def create_output(data = None, *args):
    """ data: list of dict
        args: list of args passed to the script
        result: dict """

    nesting_level = len(args)
    # take keys ['country', 'city', 'currency', 'amount'] from the first dict in input.json assuming that all dict are the same
    first_dict_values = list(data[0].keys())
    

    # check for typo in script args
    if all(map(lambda x: x in first_dict_values,args)):
        if nesting_level == 3:
            if isinstance(data,list):
                result = {}
                args_diff_list = [item for item in first_dict_values if not item in args]
                try:             
                    for key, values in groupby(sorted(data, key=itemgetter(args[0])), key=itemgetter(args[0])):
                        result[key] = {
                            v[args[1]]: {v[args[2]]: [{args_diff_list[0]: v[args_diff_list[0]]}]} for v in values
                                }      
                    return result
                except KeyError:
                    raise KeyError(f"Please verify passed args {args}")
            else:
                raise TypeError("Please pass a list of dict objects aka array of json")

        elif nesting_level == 2:
                result = {}
                args_diff_list = [item for item in first_dict_values if not item in args]
                for key, values in groupby(sorted(data, key=itemgetter(args[0])), key=itemgetter(args[0])):
                    result[key] = {
                        v[args[1]]: [{v[args_diff_list[0]]: 
                                        {args_diff_list[1]:   
                                                        v[args_diff_list[1]]
                                        }
                                    }] for v in values
                                    }    
                return result

        elif nesting_level == 1:
            result = {}
            args_diff_list = [item for item in first_dict_values if not item in args]
            for key, values in groupby(sorted(data, key=itemgetter(args[0])), key=itemgetter(args[0])):
                result[key] = [{
                    v[args_diff_list[0]]: {v[args_diff_list[1]]: 
                                    {args_diff_list[2]:   
                                                    v[args_diff_list[2]]
                                    }
                                } for v in values  
                                }]  
            return result  
    # passed args are not in ["currency", "country" ,"city", "amount"]        
    else:
        sys.exit("Please check the name of args passed to the scripts")

def nice_print(r):
    """ Serialize dict to json formatted str"""
    print(json.dumps(r, indent=4))


if __name__ == "__main__":

    args_list = parameters()
    r = create_output(parse_json(),*args_list)
    nice_print(r)



  
    
   


    

