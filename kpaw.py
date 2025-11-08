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
        
    global message_amount
    message_amount = json.loads(response.content.decode())["count"]

def registerView(ID): # This is experimental! May not work!
    url = "https://projects.penguinmod.com/api/v1/projects/interactions/registerView"

    data = f'{{"username":"koffeejava","token":"16e6c1430dcd17089b5328a5afcce010164fd978651371aa8f791466bf94e528","projectID":"0876643039"}}'
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=data)

    
    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")

def getProjectMeta(ID):
    url = f"https://projects.penguinmod.com/api/v1/projects/getproject?projectID={ID}&requestType=metadata"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        
    global project_meta
    project_meta = json.loads(response.content.decode())
def getUserMeta(target):
    url = f"https://projects.penguinmod.com/api/v1/users/profile?target={target}&username={user}&token={token}"

    response = requests.get(url)

    if not response.status_code == 200:
        print(f"{Color.RED}Something went wrong!")
        print(f"Status code: {response.status_code}")
        print(f"Response from url: {Effect.BOLD}{Effect.UNDERLINE}{json.loads(response.content.decode())["error"]}{Effect.OFF}")
        
    global user_meta
    user_meta = json.loads(response.content.decode())