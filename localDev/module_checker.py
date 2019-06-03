import subprocess
import os

## https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t
def verify_module(modulename=None):
    """ python3 implementation returns None if module is not installed"""
    if modulename:
        modules_dict = dict()
        proc = subprocess.run("pip freeze", shell=True, encoding="utf-8", stdout = subprocess.PIPE)
        #get modules as a list
        installed_modules = proc.stdout.splitlines()
        for m in installed_modules:
            m_tuple = m.partition("==")
            modules_dict[m_tuple[0]] = m_tuple[-1]
        #get module version if module is installed locally 
        module_version = modules_dict.get(modulename.lower())
        if module_version:
            #maybe return pip show
            print ('Module {0} with version {1}'.format(modulename.lower(),module_version))
            return True
        else:
            return False
    else:
        print("please provide argument")

def install_module(modulename=None,flag=None):
    """install module and send output to stdout"""
    if flag == False:
        cmd = "pip install {0}".format(modulename)
        returned_value = os.system(cmd)
        print("Exit code: {0}".format(returned_value))
    else:
        print("Module already installed")

if __name__ == "__main__":
    modulename = "flask"
    f = verify_module(modulename)
    install_module(modulename,f)
