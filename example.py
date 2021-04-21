# Bug: cannot log into another account
# temporary fix: delete userData.json
# JSON confusing give me a break T^T

import client as client #Import the client module~

Client = client.client() #initialize client

Client.login(username="USERNAME", password="PASSWORD") #Log into account, replace "USERNAME" and "PASSWORD" with your own details.

# example for printing material titles:
for i in Client.get_materials_list():
    print(i["course_title"])
    
# try "print((Client.get_materials_list())" to get entire response data, play as you wish!