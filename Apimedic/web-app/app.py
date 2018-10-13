import json
from flask import Flask, render_template, request
import fetchMedicalConditions as fmc
import TextMedicalCondition as fileMC
import fetchSymptoms as fs
import nearestDoctor as nd

app = Flask(__name__)


@app.route('/api/one/')
def one():
    symptomDict = fs.fetch()
    symptomStr = json.dumps(symptomDict)
    symptomsData = json.loads(symptomStr)
    return render_template("fetchSymptoms.html", symptomsData=symptomsData)


@app.route('/api/two/')
def two():
    return render_template("fetchMedicalConditions.html")


@app.route('/api/two/result', methods=['POST'])
def apiTwoResult():
    data = request.get_json()
    medicalConditions = fmc.fetch(data["id"], data["gender"], data["year"])
    medicalConditionsDict = json.dumps(medicalConditions)
    return medicalConditionsDict


@app.route('/api/four/')
def four():
    return render_template("findMyDoctor.html")


@app.route('/api/four/result', methods=['POST'])
def apiFourResult():
    data = request.get_json()
    nearestDocs = nd.nearestDoctors(data["lat"], data["long"])
    nearestDocsDict = json.dumps(nearestDocs)
    return nearestDocsDict


@app.route('/api/five/')
def fifth():
    return render_template("fetchTextMedicalCondition.html")


@app.route('/api/five/result', methods=['POST'])
def apiFifthResult():
    data = request.get_json()
    medicalConditions = fileMC.fetch(data["sentence"], data["gender"], data["year"])
    medicalConditionsDict = json.dumps(medicalConditions)
    return medicalConditionsDict


if __name__ == '__main__':
    app.run(debug=True)
