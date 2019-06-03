##Switch case =  functions are first class objects

def summ(a,b):
    """sum of two numbers"""
    return a+b

list_functions = [summ]
##function as first class obj
print(list_functions[0](2,3))


####swift swicth case
##let someString:String = "ceva"
##
##switch someString{
##    case "altceva":
##        print("case ul cu ceva")
##    case "orice":
##        print("case ul cu orice")
##    default:
##        print("this is default case")
    

def le_dict(key,x,y):
    return {
        'add':lambda x,y:x+y,
        'sub':lambda x,y:x-y,
        }.get(key,lambda:None)(x,y)

def switchdemo(argument):
    switcher ={1:'one',2:'two',3:'three'}
    print switcher.get(argument,'Non existing value in dict')




##switcher[Dict_key]("Func_argument")

def SwitchCaseee(key,f_arg):
    def one(a):
        print(a)
    def two(a):
        print(a)
    def three(a):
        print(a)
    switcher = {1:one,2:two,3:three}
    ##emulate the dict.get(argument,"Key not available in dict")
    try:
        return switcher[key](f_arg)
    except KeyError:
        print ("The key is not in the dict")
    

    
