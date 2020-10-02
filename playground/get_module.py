

import os
import imp

print("Location of module is {}".format(os.__file__))
print(imp.find_module("json"))
