from flask import Flask, render_template, request
import fetchSymptoms as fs
import json

app = Flask(__name__)


@app.route('/')
def home():
    return "Hey there!"


@app.route("/hello")
def hello_world():
    return "hello world"


@app.route('/hello/<name>')
def hello_name(name, surname):
    return 'Hello %s!' % name


@app.route('/api/foo/', methods=['GET'])
def foo():
    bar = request.args.to_dict()
    # print(bar)
    symptomDict = fs.fetch()
    symptomStr = json.dumps(symptomDict)
    return render_template("rough.html", symptomsData=json.loads(symptomStr))


@app.route('/api/one/')
def one():
    symptomDict = fs.fetch()
    symptomStr = json.dumps(symptomDict)
    return render_template("rough.html", symptomsData=json.loads(symptomStr))


if __name__ == '__main__':
    app.run(debug=True)
