import json


from Objects.objConnector import MonarcConnector


class EvaluationTable:

    def __init__(self,monarcConnector):
        self.monarcConnector = monarcConnector


class EvaluationTableColumn:

    def __init__(self,monarcConnector):
        self.monarcConnector = monarcConnector


class EvaluationTableIR(EvaluationTable):

    def __init__(self,monarcConnector,anrNumber):
        self.monarcConnector = monarcConnector
        self.scales = Scales(monarcConnector)
        self.anrNumber = anrNumber

    def getEvaluationTable(self):
        theScales = json.loads(self.scales.loadScales(self.anrNumber))
        scaleNames = json.loads(self.scales.loadScalesNames(self.anrNumber))
        scaleNamesExtracted = {}
        for sn in scaleNames["types"]:
            if sn['label1'] == None:
                continue
            scaleNamesExtracted[sn['id']] = sn['label'+str(MonarcConnector.LANGUAGE[MonarcConnector.CHOSEN_LANG])]


        evalTable = {
            "headers": scaleNamesExtracted,

        }

        for s in theScales['scales']:

            theDetails = json.loads(self.scales.loadScalesDescription(self.anrNumber,s['id']))

            for c in theDetails['comments']:
                if c['scaleImpactType'] != None:
                    entry = {"val":c['val'], "description":c['comment'+str(MonarcConnector.LANGUAGE[MonarcConnector.CHOSEN_LANG])]}
                    if c['scaleImpactType']['id'] not in evalTable:
                        evalTable[c['scaleImpactType']['id']] = []
                    evalTable[c['scaleImpactType']['id']].append(entry)
                    
                    #print (" +", scaleNamesExtracted[c['scaleImpactType']['id']], c['val'], c['comment1'])
                    pass
        return evalTable


class EvaluationTableOR(EvaluationTable):

    def __init__(self,monarcConnector):
        self.monarcConnector = monarcConnector


class AcceptanceTable():

    def __init__(self, irmin, irmax, ormin = 0, ormax = 0):
        self.irAcceptanceMin = irmin
        self.irAcceptanceMax = irmax
        self.opAcceptanceMin = ormin
        self.opAcceptanceMax = ormax
        

class Scales:

    baseurl = "api/client-anr/"

    def __init__(self,monarcConnector):
        self.monarcConnector = monarcConnector

    def loadScales(self,anrNumber):
        url = self.baseurl+str(anrNumber)+"/scales"
        return self.monarcConnector.getInformation(url)
    
    def loadScalesDescription(self,anrNumber,scaleID):
        url = self.baseurl+str(anrNumber)+"/scales/"+str(scaleID)+"/comments"
        return self.monarcConnector.getInformation(url)

    def loadScalesNames(self, anrNumber):
        url = self.baseurl+str(anrNumber)+"/scales-types"
        return self.monarcConnector.getInformation(url)

    def remoteUpdate(self,monarcConnection):
        pass

    def remoteAdd(self, monarcConnection):
        pass

    def remoteDelete(self, monarcConnection):
        pass


    
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