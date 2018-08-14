
import json

class UserRoles:

    url = "api/users-roles"

    def __init__(self,monarcConnector):
        self.monarcConnector = monarcConnector


    def getUserRoles(self):
        # get user roles
        
        return self.monarcConnector.getInformation(self.url)



class RiskAnalysisList:

    url = "api/client-anr"

    def __init__(self,monarcConnector):
        self.monarcConnector = monarcConnector

    def getFullAnrList(self):
        # get the ANR list for the registered user
        
        return json.loads(self.monarcConnector.getInformation(self.url))['anrs']