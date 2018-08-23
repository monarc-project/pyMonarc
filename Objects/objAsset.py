

from Objects.objConnector import MonarcConnector



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
            asset['description'] = self.description = ""
            asset['label'] = self.label = ""
        else:
            asset['description1'] = self.description1 = ""
            asset['description2'] = self.description2 = ""
            asset['description3'] = self.description3 = ""
            asset['description4'] = self.description4 = ""
            asset['label1'] = self.label1 = ""
            asset['label2'] = self.label2 = ""
            asset['label3'] = self.label3 = ""
            asset['label4'] = self.label4 = ""

        return asset




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
    
    def getAssetInstance(self):
        assetInstance = {}
        assetInstance['íd'] = self.id

        if MonarcConnector.CHOSEN_LANG == 'null':
            assetInstance['name'] = self.name
        else:
            assetInstance['name1'] = self.name1
            assetInstance['name2'] = self.name2
            assetInstance['name3'] = self.name3
            assetInstance['name4'] = self.name4
        
        return assetInstance