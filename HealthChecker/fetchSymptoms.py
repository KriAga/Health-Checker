import urllib.request
import ast
import tokenGen as token
import config
symptomsDict = {'Name': [], 'ID': []}
IDs = []
symptomsName = []
symptoms = {}
authKey = token.getToken()


def fetch():
    urlSymptoms = config.priaid_healthservice_url +'/symptoms?token=' + authKey + '&format=json&language=en-gb'
    # print(urlSymptoms)
    resultsSymptoms = urllib.request.urlopen(urlSymptoms).read()
    symptomsJson = ast.literal_eval(resultsSymptoms.decode("utf-8"))

    for symptom in symptomsJson:
        Name = symptom['Name'].lower()
        ID = symptom['ID']
        global symptomsName
        symptomsName.append(Name)
        IDs.append(ID)
        symptoms[Name] = ID

    symptomsDict['Name'] = symptomsName
    symptomsDict['ID'] = IDs

    symptomsName = sorted(symptomsName, key=len, reverse=True)
    symptomTxt = open("Symptoms.txt", "w")

    for symptom in symptomsName:
        symptomTxt.write(symptom + "\n")

    symptomTxt.close()
    return symptoms
