import requests
import json
from colorist import Color
from colorist import Effect

def setUserAndToken(USER, TOKEN):
    global token
    token = TOKEN
    global user
    user = USER

def loveToggle(id, toggle):
    url = "https://projects.penguinmod.com/api/v1/projects/interactions/loveToggle"

    data = f'{{"projectId":"{id}","username":"{user}","token":"{token}","toggle":{toggle}}}'
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=data)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")

def voteToggle(id, toggle):
    url = "https://projects.penguinmod.com/api/v1/projects/interactions/voteToggle"

    data = f'{{"projectId":"{id}","username":"{user}","token":"{token}","toggle":{toggle}}}'
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=data)

    
    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")

def follow(target, toggle):
    url = "https://projects.penguinmod.com/api/v1/users/follow"

    data = f'{{"username":"{user}","token":"{token}","target":"{target}","toggle":{toggle}}}'
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=data)

    
    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")

def featured():
    url = f"https://projects.penguinmod.com/api/v1/projects/searchprojects?page=0&query=&type=featured&username={user}&token={token}&reverse=false"

    response = requests.get(url)
    
    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")

    global featuredp
    featuredp = response.text

def getPfp(target):
    url = f"https://projects.penguinmod.com/api/v1/users/getpfp?username={target}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
    
    file = open(f"{target}.png",'wb')
    file.write(response.content)
    file.close()

def getThumb(ID):
    url = f"https://projects.penguinmod.com/api/v1/projects/getproject?projectID={ID}&requestType=thumbnail"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
    
    file = open(f"{ID}.png",'wb')
    file.write(response.content)
    file.close()

def getAmountMessage():
    url = f"https://projects.penguinmod.com/api/v1/users/getunreadmessagecount?username={user}&token={token}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        
    global Message_Amount
    Message_Amount = json.loads(response.content.decode())["count"]

# setUserAndToken("USERNAME", "TOKEN")
# loveToggle("PROJECT-ID", "TOGGLE")
# voteToggle("PROJECT-ID", "TOGGLE")
# follow("TARGET", "TOGGLE")
# featured()
# featuredp lists all featured projects
# getPfp("TARGET")
# getThumb("PROJECT-ID")
# getAmountMessage() Note: you can only see your own!
# Message_Amount