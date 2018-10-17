import fetchSymptoms as fs
import fetchMedicalConditions as fmc


def fetch(text, gender, year_of_birth):
    text = text.lower()

    SymptomFound = False    # flag to check if symptom is found or not
    medicalConditionsDict = {}
    fs.fetch()
    for symptom in fs.symptomsName:
        if symptom in text:
            SymptomFound = True
            symptomMC = str([fs.symptoms[ele] for ele in fs.symptoms if ele == symptom][0])

            # The following code could have been used too

            # symptomsName = fs.symptomsDict['Name']
            # symptomsID = fs.symptomsDict['ID']
            # for symptomName, symptomID in zip(symptomsName, symptomsID):
            #     if symptomName == text:
            #         symptomMC = symptomID

            medicalConditionsDict = fmc.fetch(symptomMC, gender, year_of_birth)
    if not SymptomFound:
        print("No Symptom Found.")
        # When no data is found so something should be shown to the user.
        medicalConditionsDict = {"No Data": "No Data"}
    return medicalConditionsDict