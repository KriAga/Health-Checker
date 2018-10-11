import urllib.request
import ast


def fetch():
    urlSymptoms = 'https://sandbox-healthservice.priaid.ch/symptoms?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImtyaWFnYTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIzOTUxIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMjAwIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6Ijk5OTk5OTk5OSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IlByZW1pdW0iLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xhbmd1YWdlIjoiZW4tZ2IiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL2V4cGlyYXRpb24iOiIyMDk5LTEyLTMxIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwc3RhcnQiOiIyMDE4LTEwLTA3IiwiaXNzIjoiaHR0cHM6Ly9zYW5kYm94LWF1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE1MzkyODYyNDQsIm5iZiI6MTUzOTI3OTA0NH0.XixIBplEp6JeK_VjZjR8GFNur6PnD7jjHkoYVhI2fY4&format=json&language=en-gb'
    resultsSymptoms = urllib.request.urlopen(urlSymptoms).read()
    symptomsJson = ast.literal_eval(resultsSymptoms.decode("utf-8"))

    symptomsDict = {'Name': [], 'ID': []}
    IDs = []
    symptomsName = []

    for symptom in symptomsJson:
        symptomsName.append(symptom['Name'].lower())
        IDs.append(symptom['ID'])

    symptomsDict['Name'] = symptomsName
    symptomsDict['ID'] = IDs

    symptomsName = sorted(symptomsName, key=len)
    symptomTxt = open("Symptoms.txt", "w")

    # print(len(symptomsName))

    for symptom in symptomsName:
        symptomTxt.write(symptom + "\n")

    symptomTxt.close()

    # print(symptomsDict)


fetch()
