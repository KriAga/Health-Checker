import urllib.request
import ast
import tokenGen as token
import config

symptomsDict = {'Name': [], 'ID': []}  # To store the name and id together. This would be passed on to the frontend
IDs = []
symptomsName = []   # This list will be sorted for better results in API 5
symptoms = {}   # Another dictionary that will store the data as name:id

authKey = token.getToken()


def fetch():
    urlSymptoms = config.priaid_healthservice_url + '/symptoms?token=' + authKey + '&format=json&language=en-gb'
    resultsSymptoms = urllib.request.urlopen(urlSymptoms).read()
    symptomsJson = ast.literal_eval(resultsSymptoms.decode("utf-8"))    # converting the byte string to string type

    for symptom in symptomsJson:
        Name = symptom['Name'].lower()  # converting to lower case to avoid Case-mismatch
        ID = symptom['ID']
        global symptomsName
        symptomsName.append(Name)
        IDs.append(ID)
        symptoms[Name] = ID

    # storing all the names in lower case in a list and then referring it to symptomsDict['Name'] and same with id
    symptomsDict['Name'] = symptomsName
    symptomsDict['ID'] = IDs

    # sorting in the reverse order
    symptomsName = sorted(symptomsName, key=len, reverse=True)
    symptomTxt = open("Symptoms.txt", "w")
    # storing the data in a text file
    for symptom in symptomsName:
        symptomTxt.write(symptom + "\n")

    symptomTxt.close()
    return symptoms
