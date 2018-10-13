import urllib.request
import ast

symptomsDict = {'Name': [], 'ID': []}
IDs = []
symptomsName = []
symptoms = {}
authKey = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImtyaWFnYTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxMjUwIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMTA4IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6IjEwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IkJhc2ljIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAxOC0xMC0wNyIsImlzcyI6Imh0dHBzOi8vYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTUzOTM5OTExMywibmJmIjoxNTM5MzkxOTEzfQ.q_I7hc7cQcaay4sfv9LCLyG52hirvcOBFU03OZCEPk0"


def fetch():
    urlSymptoms = 'https://healthservice.priaid.ch/symptoms?token=' + authKey + '&format=json&language=en-gb'
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
