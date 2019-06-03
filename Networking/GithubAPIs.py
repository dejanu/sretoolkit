# Github API

#API list
# https://api.github.com/users/dejanu
# https://api.github.com/users/dejanu/repos
# https://api.github.com/repos/dejanu/linux

from getpass import getpass
import requests
from requests.exceptions import HTTPError
from requests.auth import HTTPDigestAuth
import json
import os


from textblob import TextBlob
import nltk

import matplotlib.pyplot as plt

# FIX: lease use the NLTK Downloader to obtain the resource
nltk.download('punkt')

def basic_request (url='https://api.github.com'):
    try:
        response =  requests.get('https://api.github.com')
    #response.status_code == 200:
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
        #return message body content as  bytes
        return response.content
    
def get_polarity( commit = None):
    """ commit : str
        return polarity from tuple (polarity, subjectivity) of the commit sentence"""
    blob = TextBlob(commit)
        #attempt spelling correction
        #blob = blob.correct()

        # Polarity classification = classifying sentece as positive, negative or neutral opinion
        #  The polarity score is a float within the range [-1.0, 1.0]. The subjectivity is a float within the range [0.0, 1.0]
    return blob.sentiment.polarity


def plot_graf( x = None, y = None):
    """ x,y: lists
        plot commits polarity evolution"""
    if x and y:
        plt.xlabel("Commits")
        plt.ylabel("Polarity")
        plt.title("Polarity evolution")
        plt.plot(x,y)
        plt.show()
    
if __name__ == "__main__":

    #r = requests.get('https://api.github.com/user', verify=False,auth=('dejanu', getpass()))
    
    #r = requests.get("https://api.github.com/repos/dejanu/linux/commits",params={'per_page': '100'}, verify=False,auth=('dejanu', getpass()))
    u = os.environ["u"]
    p = os.environ["pas"]
    r = requests.get("https://api.github.com/repos/dejanu/linux/commits",params={'per_page': '100'}, verify=False,auth=HTTPDigestAuth(u,p))
    if r.status_code == 200:
        # get the content as  a list
        parsed = json.loads(r.content)
        commits_list = [i["commit"]["message"] for i in parsed]

    polarity_list = [get_polarity(i) for i in commits_list]
    t = list(range(len(commits_list)))
    plot_graf(t, polarity_list)
    
