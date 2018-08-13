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