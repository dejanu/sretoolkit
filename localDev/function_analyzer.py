import dis

## Static analysis module

class Codelizer():

    @staticmethod
    def count_calls(f):
        """ decorator that create calls function attribute """
        def wrapper(*args,**kwargs):
            wrapper.calls +=1
            return f(*args,**kwargs)
        wrapper.calls = 0
        return wrapper

    @staticmethod
    def get_bytecode(f):
        """ f- fuction return - bytecode of function object """
        if callable(f):
            return f.__code__.co_code
        else:
            raise Exception("f should be a function")

    @staticmethod
    def get_code_metadata(f):
        """ f - function, generator, coroutine, method, source code string, code object
            return - string """
        return " Byte code instructions {0} and {1}".format(dis.dis(f), dis.code_info(f))
    
    @staticmethod
    def generate_analysis( fpath ):
        """take file path and generate raport"""
        import subprocess, flake8
        #import sys
        f = open('raport.txt','w')
        proc = subprocess.Popen(["python", "-m", "flake8", fpath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in proc.stdout:
            #sys.stdout.write(line)
            #python3 convert from byte to str
            f.write(line.decode())
        f.close() 
        
        
        



if __name__ == "__main__":

    def f(): pass

    print(Codelizer.get_code_metadata(f))
