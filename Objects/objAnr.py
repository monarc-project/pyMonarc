
from Objects.objConnector import MonarcConnector

class Anr:
    
    def __init__(self):

        self.id = ""

        self.cacheModelIsScalesUpdatable = ""
        self.cacheModelShowRolfBrut = ""
        self.contextAnaRisk = ""
        self.contextGestRisk = ""
        self.createdAt = {
            'date':'',
            'timezone':'',
            'timezone_type':'',
        }
        self.UpdatedAt = {
            'date':'',
            'timezone':'',
            'timezone_type':'',
        }
        self.creator = ""

        self.evalLivrableDone = ""
        self.evalPlanRisks = ""
        self.evalRisks = ""

        self.initAnrContext = ""
        self.initDefContext = ""
        self.initEvalContext = ""
        self.initLivrableDone = ""
        self.initRiskContext = ""

        self.language = ""
        self.manageRisks = ""
        self.model = ""
        self.modelImpacts = ""
        self.modelLivrableDone = ""
        self.modelSummary = ""

        #assets called objects
        self.assets = {}

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

        self.seuil1 = ""
        self.seuil2 = ""
        self.seuilRolf1 = ""
        self.seuilTraitement = ""
        self.showRolfBrut = ""
        self.synthAct = ""
        self.synthThreat = ""
        self.updater = ""

    def getAnr(self):
        anr = {}
        anr['id'] = self.id

        anr['cacheModelIsScalesUpdatable'] = self.cacheModelIsScalesUpdatable
        anr['cacheModelShowRolfBrut'] = self.cacheModelShowRolfBrut
        anr['contextAnaRisk'] = self.contextAnaRisk
        anr['contextGestRisk'] = self.contextGestRisk
        anr['createdAt'] = self.createdAt
        anr['UpdatedAt'] = self.UpdatedAt
        anr['creator'] = self.creator

        anr['evalLivrableDone'] = self.evalLivrableDone
        anr['evalPlanRisks'] = self.evalPlanRisks
        anr['evalRisks'] = self.evalRisks

        anr['initAnrContext'] = self.initAnrContext
        anr['initDefContext'] = self.initDefContext
        anr['initEvalContext'] = self.initEvalContext
        anr['initLivrableDone'] = self.initLivrableDone
        anr['initRiskContext'] = self.initRiskContext

        anr['language'] = self.language
        anr['manageRisks'] = self.manageRisks
        anr['model'] = self.model
        anr['modelImpacts'] = self.modelImpacts
        anr['modelLivrableDone'] = self.modelLivrableDone
        anr['modelSummary'] = self.modelSummary

        #assets called objects
        anr['assets'] = self.assets

        if MonarcConnector.CHOSEN_LANG == 'null':
            anr['description'] = self.description
            anr['label'] = self.label
        else:
            anr['description1'] = self.description1
            anr['description2'] = self.description2
            anr['description3'] = self.description3
            anr['description4'] = self.description4
            anr['label1'] = self.label1
            anr['label2'] = self.label2
            anr['label3'] = self.label3
            anr['label4'] = self.label4

        anr['seuil1'] = self.seuil1
        anr['seuil2'] = self.seuil2
        anr['seuilRolf1'] = self.seuilRolf1
        anr['seuilTraitement'] = self.seuilTraitement
        anr['showRolfBrut'] = self.showRolfBrut
        anr['synthAct'] = self.synthAct
        anr['synthThreat'] = self.synthThreat
        anr['updater'] = self.updater
