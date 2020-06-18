import os
import requests
from requests.auth import HTTPDigestAuth  ## Module to handle digest authentication 
import pprint
import datetime


class mongoDB():
    def __init__(self):
        
        self.baseurl = "https://cloud.mongodb.com/api/atlas/v1.0/"
         ## URL to connect Python API to MongoDB Atlas 
        self.myDB       = "mongodb+srv://pi:N0tT0Kn0w@cluster0-wegmd.mongodb.net/test?retryWrites=true&w=majority"

    def auth():
        # This installs the code needed to respond to the server when it asks for the digest.
        response=requests.get(baseurl, auth=HTTPDigestAuth(os.environ["ATLAS_USER"], os.environ["ATLAS_USER_KEY"]))
        pprint.pprint(response.json())