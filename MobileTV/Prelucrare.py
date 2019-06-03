import ConfigParser


##cinstit e o mizerie de parsare, dar isi face treaba 
def create_config(config_name):
    """ create a new configuration from vimtv.cfg """
    with open('vimtv.cfg','r') as v:
        f = open (str(config_name),'w')
        lines = v.readlines()
        #read until line 255 "NO CONFIGURATION BELOW THIS LINE"
        for i in range(0,256):
            x = lines[i].replace("#-","")
            z = x.replace("-","")
            f.write(z.lstrip())
        f.close()
            

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
            

if __name__ == "__main__":

    create_config("cristi.cfg")
    
    ##create parser object
    parser = ConfigParser.RawConfigParser()
    parser.read("cristi.cfg")

    ## list all [sections]   
    for i in parser.sections():
        print (i)

    ##call section_atr for a certain section
    section_atr('LOW PROFILE')

    ##call sec_val for 
    sect_val(section_atr('LOW PROFILE'))
