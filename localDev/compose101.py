# https://docs.docker.com/compose/compose-file/#service-configuration-reference

###############################
## Docker Compose Dumb parser #
###############################

import yaml
import sys

# cxx = client
# ixx = internal
# xxx = engine



compose_keywords = {
        "extends":"enables sharing of common configuration among different files or even different projects",
        "image":"image is pulled from a registry",
        "build":"image is build under context",
        "container_name":"name of container",
        "context":"either a path to directory containg a Dockefile or a url to a git repo",
        "args":"envrionment variables accesible only during build process",
        "environment":"envrionment variables, values are resolved on the machine on which Compose is running on",
        "version":"compose version",
        "links":"link to containers in another service",
                    }

        
               
def iterdict(d):
    """recursive function for dictionary iteration"""
    for k,v in d.items():
        #verify if value is a dictionary:
        if isinstance(v,dict):
            iterdict(v)
        else:
            #print("Key is {0} and value {1}".format(k,v))
            print("* {0} : {1}".format(k,v))


def scan_compose(composefile):
    """describe services from a docker-compose file"""
    
    #deserialize file object into a python object
    with open(composefile,'r') as stream:
        try:
            compose_object = yaml.load(stream)
            #print(compose_object)
            return compose_object
        except yaml.YAMLError as exc:
            print(exc)    
    return compose_object

def service_description(compose_object=None, verbose = False):
    """receive compose object as dict object"""
    
    if compose_object:
        #count no if services
        print("No of services: {0}".format(len(compose_object['services'])))
        #service counter
        c = 0
        # describe each service (dict)
        for i in compose_object['services']:
            if verbose:
                print("Service: {0}\n Definition: {1}\n".format(i, compose_object['services'][i]))
                iterdict(compose_object['services'][i])
                print("-----------------")

            else:
                c+=1
                try:
                    #verify if it has links
                    print(" {2})Service: {1}\n Dependencies: {0}\n".format(compose_object['services'][i]['links'],i,c))
                    print("-------------------------")
                except:
                    print("{1})Service: {0}\n Dependencies:None \n".format(i,c))
                    print("-------------------------")
            

            


if __name__ == "__main__":
    
    #x = scan_compose(sys.argv[1])
    service_description(scan_compose('docker-compose.yml'), verbose = False)

    
    
   

    
