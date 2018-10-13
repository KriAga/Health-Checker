import ast
import urllib.request
import tokenGen as token
authKey = token.getToken()


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
