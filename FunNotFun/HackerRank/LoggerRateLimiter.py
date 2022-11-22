

# Design a logger system that receives a stream of msgs along with their timestamp
# each unique message should only be printed at most every 10 seconds
# i.e a message printed at timestamp t ill prevent other identical messga from being printed until t+10

# all msgs will come in chronologogical order



class Logger:
    def __init__(self):
        # hash map msg:timestamp
        self.message_dict={}

    def shouldPrintMessage(self, timestamp, msg):
        
        """ 
        returns True if msg should be printed in the given timestamp
        otherwise false
        """

        if msg not in self.message_dict