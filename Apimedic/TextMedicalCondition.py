import fetchSymptoms as fs
import fetchMedicalConditions as fmc


def fetch(text, gender, year_of_birth):
    text = text.lower()

    flag = 0
    medicalConditionsDict = {}
    for symptom in fs.symptomsName:
        if symptom in text:
            flag = 1
            symptomMC = str([fs.symptoms[ele] for ele in fs.symptoms if ele == symptom][0])

            # symptomsName = fs.symptomsDict['Name']
            # symptomsID = fs.symptomsDict['ID']
            # for symptomName, symptomID in zip(symptomsName, symptomsID):
            #     if symptomName == text:
            #         symptomMC = symptomID

            medicalConditionsDict = fmc.fetch(symptomMC, gender, year_of_birth)
    if flag == 0:
        print("No Symptom Found.")
    return medicalConditionsDict