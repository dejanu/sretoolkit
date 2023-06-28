

# Design a logger system that receives a stream of msgs along with their timestamp
# each unique message should only be printed at most every 10 seconds
# i.e a message printed at timestamp will prevent other identical messgages from being printed until t+10

# all msgs will come in chronologogical order
# dict = {msg:timestamp} 
## for incomming msgs we check if the msg is in dict:
## if msg  NOT in dict we'll update the dict
## if msg is in dict we check 
## if the incomming timestamp >= timestamp_from_dict + 10 (return TRUE and update dict)
## else return FALSE and not update the dict 


class Logger:
    def __init__(self):
        # hash map msg:timestamp
        self.message_dict = {}

    def shouldPrintMessage(self, timestamp, msg):
        """ 
        returns True if msg should be printed in the given timestamp
        otherwise false
        """
        if msg not in message_dict:
            self.message_dict[msg] = timestamp

            return True
        # check if the diff between incoming msg timestamp and current timestamp from dict >=10
        if timestamp - self.message_dict[msg] >= 10:
            self.message_dict[msg] = timestamp
            return True
        else:
            return False



