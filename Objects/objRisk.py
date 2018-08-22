

from Objects.objConnector import MonarcConnector


class Risk:

    baseurl = "api/client-anr/"

    def __init__(self,monarcConnector,anrNumber):
        self.monarcConnector = monarcConnector
        self.anrNumber = anrNumber
    
    def remoteUpdate(self,monarcConnection):
        pass

    def remoteDelete(self,monarcConnection):
        pass
        
    def remoteAdd(self, monarcConnection):
        pass



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



class ImpactTable():

    def __init__(self):
        # list of all impact values (R,O,L,F,P,...)
        self.table = {}
        # for impact in scales possibilities do
        # append all ;)



class Impact():


    def __init__(self):
        self.c = ""
        self.a = ""
        self.i = ""
        self.id = ""
        self.isHidden = ""
        self.locallyTouched = ""
        self.impactType = ""
        self.impactTypeID = ""
        if MonarcConnector.CHOSEN_LANG == 'null':
            self.impactTypeDescription = ""
        else:
            self.impactTypeDescription1 = ""
            self.impactTypeDescription2 = ""
            self.impactTypeDescription3 = ""
            self.impactTypeDescription4 = ""

    
    def getImpact(self):
        impact = {}
        impact['c_risk'] = self.c
        impact['d_risk'] = self.a
        impact['i_risk'] = self.i
        impact['id'] = self.id
        impact['scaleImpactType'] = self.impactType
        impact['scaleImpactTypeId'] = self.impactTypeID
        impact['isHidden'] = self.isHidden
        impact['locallyTouched'] = self.locallyTouched
        if MonarcConnector.CHOSEN_LANG == 'null':
            impact['scaleImpactTypeDescription'] = self.impactTypeDescription
        else:
            impact['scaleImpactTypeDescription1'] = self.impactTypeDescription1
            impact['scaleImpactTypeDescription2'] = self.impactTypeDescription2
            impact['scaleImpactTypeDescription3'] = self.impactTypeDescription3
            impact['scaleImpactTypeDescription4'] = self.impactTypeDescription4

        return impact



