

import json
from Objects.objConnector import MonarcConnector




class InterviewTable:

    def __init__(self, anrNumber, interviewList):
        self.anrNumber = anrNumber
        self.interviewList = []
        if len(interviewList)>0:
            for interview in interviewList:
                self.interviewList.append(Interview(self.anrNumber,interview['content'], interview['date'], interview['service'], interview['id']))



    def toJson(self):
        jsonList = [i.getInterview() for i in self.interviewList]
        
        return json.dumps(jsonList, sort_keys=True, indent=4)

    def getInterviews(self):
        return self.interviewList

    def addInterview(self, interview):
        self.interviewList.append(interview)

    def __repr__(self):
        return self.toJson()

    def __str__(self):
        return self.toJson()





class Interview:

    url = "/interviews"

    def __init__(self, anrNumber=None, content=None, date=None, service=None, id=None):
        self.anr = anrNumber
        self.content = content
        self.date = date
        self.service = service
        self.id = id



    def getInterview(self):
        jsonInterview = {}
        jsonInterview['anr'] = self.anr
        jsonInterview['date'] = self.date
        jsonInterview['service'] = self.service
        jsonInterview['content'] = self.content

        if self.id != None:
            jsonInterview['id'] = self.id

        return jsonInterview

    def toJson(self,formatted=True):
        if formatted:
            return json.dumps(self.getInterview(), sort_keys=True, indent=4)
        else:
            return json.dumps(self.getInterview())

    def remoteUpdate(self,monarcConnection):
        if self.id == None:
            self.remoteAdd(monarcConnection)
        else:
            url = MonarcConnector.CLIENT_BASE_URL+str(self.anr)+Interview.url+"/"+str(self.id)
            print (url)
            monarcConnection.updateInformation(url,self.getInterview())

    def remoteDelete(self,monarcConnection):
        if self.id == None:
            print('cannot delete a non-existant Object!')
        else:
            url = MonarcConnector.CLIENT_BASE_URL+str(self.anr)+Interview.url+"/"+str(self.id)
            monarcConnection.deleteInformation(url,self.getInterview())

    def remoteAdd(self, monarcConnection):
        url = MonarcConnector.CLIENT_BASE_URL+str(self.anr)+Interview.url
        monarcConnection.addInformation(url,self.getInterview())



    def __repr__(self):
        return self.toJson()

    def __str__(self):
        return self.toJson()