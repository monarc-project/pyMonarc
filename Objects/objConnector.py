
import requests
import json

class MonarcConnector:


    CLIENT_BASE_URL = "api/client-anr/"

    CHOSEN_LANG = 'en'
    LANGUAGE = { 
        'null': "",
        'fr': "1",
        'en': "2",
        'de': "3",
        'nl': "4",
    }



    def __init__(self):
        self.loadLoginSettings()
        self.testLogin()

    def getInformation(self,url):
        head = {'token': self.user_token}
        information = requests.get((self.base_url+url), headers=head)
        return information.content.decode()

    def addInformation(self,url,jsonData):
        head = {'token': self.user_token,'Content-Type':'application/json;charset=utf-8'}
        response = requests.post(self.base_url+url, json=jsonData, headers=head)
        print (response.content)

    def updateInformation(self,url,jsonData):
        head = {'token': self.user_token,'Content-Type':'application/json;charset=utf-8'}
        response = requests.patch(self.base_url+url,json=jsonData, headers=head)
        print (response.content)

    def deleteInformation(self,url,jsonData):
        head = {'token': self.user_token,'Content-Type':'application/json;charset=utf-8'}
        response = requests.delete(self.base_url+url,json=jsonData, headers=head)
        print (response.content)

    def testLogin(self):
        try:
            # if file exists load the token
            with open("settingsFile.cfg","r") as tokenfile:
                fileContents = json.loads(tokenfile.read())
                self.user_token = fileContents['token']
                self.user_id = fileContents['uid']
                self.user_lang = fileContents['language']
                
        except FileNotFoundError as e:
            # if file does not exist then one has to login anyways!
            print (e.strerror)
            self.login()
        else:
            url = "api/users-roles"
            if self.getInformation(url) == "":
                # if the return is empty, the token is invalid so login again!
                self.login()

    def loadLoginSettings(self):
        # TODO: Test if file exists
        with open("loginInfo.cfg", 'r') as loginInfoFile:
            loginInfo = json.loads(loginInfoFile.read())
        
        self.loginData = {'login': loginInfo['username'], 
                    'password': loginInfo['password']}
        self.base_url = loginInfo['url']

    def login(self):
        # TODO: what happens if user/pwd combination is wrong
        
        respLogin = json.loads(requests.post(self.base_url+"auth",data=self.loginData).content.decode())
        self.user_token = respLogin['token']
        with open("settingsFile.cfg", 'w') as settingsFile:
            settingsFile.write(json.dumps(respLogin))
            settingsFile.flush()
