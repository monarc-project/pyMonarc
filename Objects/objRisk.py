




class Risk:

    baseurl = "api/client-anr/"

    def __init__(self,monarcConnector,anrNumber):
        self.monarcConnector = monarcConnector
        self.anrNumber = anrNumber



class OperationalRisk(Risk):

    finalurl = "/risksop?limit=-1"

    def __init__(self,monarcConnector,anrNumber):
        super().__init__(monarcConnector,anrNumber)
    
    def loadAllOpRisks(self):
        url = self.baseurl+str(self.anrNumber)+self.finalurl
        return self.monarcConnector.getInformation(url)

class InformationRisk(Risk):

    finalurl = "/risks?limit=-1"

    def __init__(self,monarcConnector,anrNumber):
        super().__init__(monarcConnector,anrNumber)
    
    def loadAllInfoRisks(self):
        url = self.baseurl+str(self.anrNumber)+self.finalurl
        return self.monarcConnector.getInformation(url)
