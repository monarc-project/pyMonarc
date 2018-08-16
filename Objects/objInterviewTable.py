

import json


class InterviewTable:

    def __init__(self, anrNumber, interviewList):
        self.anrNumber = anrNumber
        self.interviewList = []
        if len(interviewList)>0:
            for interview in interviewList:
                self.interviewList.append(Interview(self.anrNumber,interview['content'], interview['date'], interview['service']))

    def toJson(self):
        jsonList = [i.getInterview() for i in self.interviewList]
        
        return json.dumps(jsonList, sort_keys=True, indent=4)

    def __repr__(self):
        return self.toJson()

    def __str__(self):
        return self.toJson()


class Interview:

    def __init__(self, anrNumber=None, content=None, date=None, service=None):
        self.anr = anrNumber
        self.content = content
        self.date = date
        self.service = service


    def getInterview(self):
        jsonInterview = {}
        jsonInterview['anr'] = self.anr
        jsonInterview['date'] = self.date
        jsonInterview['service'] = self.service
        jsonInterview['content'] = self.content

        return jsonInterview

    def toJson(self,formatted=True):
        if formatted:
            return json.dumps(self.getInterview(), sort_keys=True, indent=4)
        else:
            return json.dumps(self.getInterview())

    def __repr__(self):
        return self.toJson()

    def __str__(self):
        return self.toJson()