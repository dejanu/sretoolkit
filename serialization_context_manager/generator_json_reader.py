
# read meetup.json file as INPUT and write line for each function call in rsvp.csv file 

# meetup.json head
"""
{"venue":{"venue_name":"Datong High School","lon":0,"lat":0,"venue_id":23779799},"visibility":"public","response":"no","guests":0,"member":{"member_id":120119272,"photo":"http:\/\/photos3.meetupstatic.com\/photos\/member\/b\/2\/b\/c\/thumb_262125756.jpeg","member_name":"Allen Wang"},"rsvp_id":1658733801,"mtime":1489925470960,"event":{"event_name":"Play Intermediate Volleyball","event_id":"jkpwmlywgbmb","time":1491613200000,"event_url":"https:\/\/www.meetup.com\/Taipei-Sports-and-Social-Club\/events\/236786445\/"},"group":{"group_topics":[{"urlkey":"fitness","topic_name":"Fitness"},{"urlkey":"mountain-biking","topic_name":"Mountain Biking"},{"urlkey":"sports","topic_name":"Sports and Recreation"},{"urlkey":"outdoors","topic_name":"Outdoors"},{"urlkey":"fun-times","topic_name":"Fun Times"},{"urlkey":"winter-and-summer-sports","topic_name":"Winter and Summer Sports"},{"urlkey":"adventure","topic_name":"Adventure"},{"urlkey":"water-sports","topic_name":"Water Sports"},{"urlkey":"sports-and-socials","topic_name":"Sports and Socials"},{"urlkey":"hiking","topic_name":"Hiking"},{"urlkey":"excercise","topic_name":"Exercise"},{"urlkey":"recreational-sports","topic_name":"Recreational Sports"}],"group_city":"Taipei","group_country":"tw","group_id":16585312,"group_name":"Taipei Sports and Social Club","group_lon":121.45,"group_urlname":"Taipei-Sports-and-Social-Club","group_lat":25.02}}
{

"""

import csv
import ast
import json

def json_read_gen(file_name):
    """"
    Read one line of data from the provided json file (a single RSVP)
    Filter the relevant fields you want to use to calculate trending topics
    Append this line to a csv file (same for each run)

    """
    with open(file_name) as fh:
        for line in fh:
            # convert to dict and use mtime as key
            with open("rsvp.csv", "a") as out_file:
                # writer = csv.writer(out_file, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)
                writer = csv.writer(out_file, delimiter=',')
                writer.writerow([ ast.literal_eval(line).get("mtime"), 
                                 list(map( lambda d: d.get("urlkey"), ast.literal_eval(line)["group"]["group_topics"])) 
                ])
            yield json.loads(line)


if __name__ == "__main__":

	# create generator object
	producer  = json_read_gen("meetup.json")

	# write 3 lines
	next(producer)
	next(producer)
	next(producer)
	
