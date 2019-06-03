#!/usr/bin/python

##def getVarFromFile(filename):
##    import imp
##    f = open(filename)
##    global data
##    data = imp.load_source('data', '', f)
##    f.close() 


import ConfigParser

parser = ConfigParser.RawConfigParser()
parser.read('ex.cfg')

##vezi sectiunile [sectiunie]
for i in parser.sections():
    print(i)


    


    
def section_atr(sect):
    """sect:name of a section as str
       atr_sect: list of atr for the sect section""" 
    if parser.has_section(str(sect)):
        print (parser.options(str(sect)))
        #vezi optiunile unei setiuni
        atr_sect = parser.options(str(sect))
    else:
        print ("Section not available in cfg file")
    return atr_sect
               
        
def sect_val(l):
    """ l : list of atribute of a section
        return: None
            """
    for i in parser.sections():
        for j in l:
            try:
                print("Section "+str(i)+" has "+str(j)+" value :"+parser.get(i,j,))
            except:
                pass


## sect_val(section_atr('TRANSCODING'))
