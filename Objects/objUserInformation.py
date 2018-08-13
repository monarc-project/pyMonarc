
import json

class UserRoles:

    def __init__(self,monarcConnector):
        self.monarcConnector = monarcConnector


    def getUserRoles(self):
        # get user roles
        url = "api/users-roles"
        return self.monarcConnector.getInformation(url)



class RiskAnalysisList:

    url = "api/client-anr"

    def __init__(self,monarcConnector):
        self.monarcConnector = monarcConnector

    def getFullAnrList(self):
        # get the ANR list for the registered user
        
        return json.loads(self.monarcConnector.getInformation(self.url))['anrs']