

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
        #list of all impact values (R,O,L,F,P,...)
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



class Asset():

    def __init__(self):
        self.anr = {}
        self.code = ""
        self.createdAt = {
            'date':'',
            'timezone':'',
            'timezone_type':'',
        }
        self.updatedAt = {
            'date':'',
            'timezone':'',
            'timezone_type':'',
        }
        self.creator = ""
        self.id = ""
        self.mode = ""
        self.status = ""
        self.type = ""
        self.updater = ""

        if MonarcConnector.CHOSEN_LANG == 'null':
            self.description = ""
            self.label = ""
        else:
            self.description1 = ""
            self.description2 = ""
            self.description3 = ""
            self.description4 = ""
            self.label1 = ""
            self.label2 = ""
            self.label3 = ""
            self.label4 = ""

    
    def getAsset(self):
        asset = {}
        asset['anr'] = self.anr
        asset['code'] = self.code
        asset['createdAt'] = self.createdAt
        asset['creator'] = self.creator
        asset['id'] = self.id
        asset['mode'] = self.mode
        asset['status'] = self.status
        asset['type'] = self.type
        asset['updatedAt'] = self.updatedAt
        asset['updated'] = self.updater

        if MonarcConnector.CHOSEN_LANG == 'null':
            self.description = ""
            self.label = ""
        else:
            self.description1 = ""
            self.description2 = ""
            self.description3 = ""
            self.description4 = ""
            self.label1 = ""
            self.label2 = ""
            self.label3 = ""
            self.label4 = ""




class GlobalAsset(Asset):
    
    
    def __init__(self):
        super().__init__()
        self.instances = []


class AssetInstance:

    def __init__(self):
        self.id = ""
        
        if MonarcConnector.CHOSEN_LANG == 'null':
            self.name = ""
        else:
            self.name1 = ""
            self.name2 = ""
            self.name3 = ""
            self.name4 = ""