import ast
import urllib.request
import tokenGen as token
import config

authKey = token.getToken()


def fetch(symptomMC, gender, year_of_birth):
    urlMedicalCondition = config.priaid_healthservice_url + "/diagnosis?symptoms=[" + symptomMC + "]&gender=" + gender + "&year_of_birth=" + year_of_birth + "&token=" + authKey + "&format=json&language=en-gb"
    resultsMC = urllib.request.urlopen(urlMedicalCondition).read()  # returns a byte string
    medicalConditionsList = ast.literal_eval(resultsMC.decode("utf-8"))  # converting the byte string to string and then parsing it into a list
    medicalConditionsDict = {}
    index = 1
    for issue in medicalConditionsList:
        medicalConditionsDict[index] = issue['Issue']['Name']
        index = index + 1
    return medicalConditionsDict
