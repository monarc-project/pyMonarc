# TODO: download a complete ANR (maybe multiple files needed?)
# TODO: test for Internet connection to the server
# TODO: update when language stuff is done

import requests
import json

from Objects.objConnector import MonarcConnector
from Objects.objUserInformation import RiskAnalysisList
from Objects.objRisk import InformationRisk
from Objects.objEvaluationTable import EvaluationTableIR
from Objects.objInterviewTable import InterviewTable, Interview

CHOSEN_LANG = 'en'
LANGUAGE = { 
    'null': "",
    'fr': "1",
    'en': "2",
    'de': "3",
    'nl': "4",
}


if __name__ == "__main__":
    monarcConn = MonarcConnector()
    anrListObj = RiskAnalysisList(monarcConn)

    anrList = anrListObj.getFullAnrList()

    baseurl = "api/client-anr/"

    analysis = anrList[-1]

    url = baseurl+str(analysis['id'])+"/interviews"

    ### ADD INTERVIEW   
    newInterview = Interview(analysis['id'], "The James Bond Test 1", "Today and Yesterday", "Michael, James, Marion and Peter")
    newInterview.remoteAdd(monarcConn)

    #interview2change = interviews.getInterviews()[-1]
    #interview2change.content = "Mario was the reason! NO!!!"
    #interview2change.remoteDelete(monarcConn)
    

    interviewList = json.loads(monarcConn.getInformation(url))['interviews']
    interviews = InterviewTable(analysis['id'],interviewList)
    print(interviews.toJson())


    for analysis in anrList:
        #print (analysis['id'], analysis['label1'], analysis['description1'], "created by", analysis['creator'])

        #infoRiskObj = InformationRisk(monarcConn,analysis['id'])

        #allRisks = json.loads(infoRiskObj.loadAllInfoRisks())

        i=0
        
        #theTableObj = EvaluationTableIR(monarcConn, analysis['id'])
        #theTable = theTableObj.getEvaluationTable()

        # print (json.dumps(theTable,indent=4))
        '''
        for h in theTable['headers']:
            print()
            print (theTable['headers'][h])
            if h != "headers":
                for l in theTable[h]:
                    print ("   ",l['val'],l['description'])
                
        '''

        
        url = baseurl+str(analysis['id'])+"/assets?limit=-1"
        #print(json.dumps(json.loads(monarcConn.getInformation(url))['assets'][0],indent=4))

        url = baseurl+str(analysis['id'])+"/threats?limit=-1"
        #print(json.dumps(json.loads(monarcConn.getInformation(url))['threats'][0],indent=4))

        url = baseurl+str(analysis['id'])+"/vulnerabilities?limit=-1"
        #print(json.dumps(json.loads(monarcConn.getInformation(url))['vulnerabilities'][0],indent=4))

        url = baseurl+str(analysis['id'])+"/measures?limit=-1"
        #print(json.dumps(json.loads(monarcConn.getInformation(url))['measures'][0],indent=4))

        url = baseurl+str(analysis['id'])+"/amvs?limit=-1"
        #print(json.dumps(json.loads(monarcConn.getInformation(url))['amvs'][0],indent=4))

        url = baseurl+str(analysis['id'])+"/rolf-tags?limit=-1"
        #print(json.dumps(json.loads(monarcConn.getInformation(url))['tags'][0],indent=4))

        url = baseurl+str(analysis['id'])+"/rolf-risks?limit=-1"
        #print(json.dumps(json.loads(monarcConn.getInformation(url))['risks'][0],indent=4))

        




        '''
        for risk in allRisks['risks']:
            i+=1
            #print (risk['id'], json.dumps(risk, indent=4))
            comment = risk['comment']
            if comment != None:
                comment = comment.replace("\n","/")
            else:
                comment = ""
            print (str(i)+".", risk['asset'], risk['threatCode'], risk['vulnCode'], comment)
        '''
        
        '''
        theScales = json.loads(monarcConn.loadScales(analysis['id']))
        #print(json.dumps(theScales,indent=4))
        

        scaleNames = json.loads(monarcConn.loadScalesNames(analysis['id']))
        #print (json.dumps(scaleNames, indent=4))
        scaleNamesExtracted = {}
        for sn in scaleNames["types"]:
            scaleNamesExtracted[sn['id']] = sn['label1']

        #print (json.dumps(final, indent=4))
        #print (json.dumps(theScales, indent=4))
        for s in theScales['scales']:
            #print (s['type'], s['min'],"to",s['max'])
            #print (json.dumps(s,indent=4))
            theDetails = json.loads(monarcConn.loadScalesDescription(analysis['id'],s['id']))
            #print (json.dumps(theDetails,indent=4))
            #index = 1
            
            #print (json.dumps(theDetails['comments'],indent=4))

            for c in theDetails['comments']:
                if c['scaleImpactType'] != None:
                    print (" +", scaleNamesExtracted[c['scaleImpactType']['id']], c['val'], c['comment1'])
                #print (json.dumps(c,indent=4))
                #print("  +", c['val'], c['comment1'])
                #index = index % len(final)+1
                #print()
                # print (json.dumps(c))
                pass
        '''



        '''
        if analysis['id'] == 481:
            xx = json.dumps(analysis, indent=4)
            print (xx)
        '''