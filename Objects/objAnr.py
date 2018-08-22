
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

        self.objects = {}

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