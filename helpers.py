import os.path
import json

class Headers:
    def __init__(self, data = None, type = None, auth = None):
        headers = {
            "Accept-Language": "en-US",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "okhttp/3.14.4",
            "app-type": "classera",
            "Accept-Encoding": "gzip"
        }
        self.headers = headers

        headersAuth = {
            "Accept-Language": "en-US",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "okhttp/3.14.4",
            "app-type": "classera",
            "authtoken" : auth,
            "Accept-Encoding": "gzip"
        }
        self.headersAuth = headersAuth

class Device:
    def __init__(self):
        self.userAgent = "okhttp/3.14.4"
        self.token = "a3d8c21b54c8ad8e4cc0d7d066b476c2ce9da709"

class Auth:
    def __init__(self, auth = None): #TODO get this thing to actually update the file
        if os.path.exists("userData.json") == True:
            f = open('userData.json',)
            data = json.load(f)
            self.key = data['AUTH_KEY']
        
        else:
            data = {"AUTH_KEY": auth}
            f = open("userData.json", "x")
            with open('userData.json', 'w') as outfile:
                json.dump(data, outfile)
            self.key = auth


        

