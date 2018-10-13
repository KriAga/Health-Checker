import ast
import urllib.request

authKey = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImtyaWFnYTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxMjUwIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMTA4IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6IjEwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IkJhc2ljIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAxOC0xMC0wNyIsImlzcyI6Imh0dHBzOi8vYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTUzOTM5OTA4OCwibmJmIjoxNTM5MzkxODg4fQ.00EGvwuAzqopQ00wbBltQXshlF96sLQTFLith1i0rSM"


def fetch(symptomMC, gender, year_of_birth):
    urlMedicalCondition = "https://healthservice.priaid.ch/diagnosis?symptoms=[" + symptomMC + "]&gender=" + gender + "&year_of_birth=" + year_of_birth + "&token=" + authKey + "&format=json&language=en-gb"
    resultsMC = urllib.request.urlopen(urlMedicalCondition).read()
    medicalConditionsList = ast.literal_eval(resultsMC.decode("utf-8"))
    medicalConditionsDict = {}
    index = 1
    for issue in medicalConditionsList:
        medicalConditionsDict[index] = issue['Issue']['Name']
        index = index + 1
    return medicalConditionsDict
