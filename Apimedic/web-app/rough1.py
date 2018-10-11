import os
from flask import Flask, render_template, request
from scraper import *

sshConfigDir=  ('~')+"/.ssh"

app = Flask(__name__)

APP_ROOT= os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target=sshConfigDir
    print (target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename=file.filename
        destination="/".join([target,filename])
        print(destination)
        file.save(destination)
    diskData=run_scraper()
    return render_template("complete.html", diskData=diskData)

@app.route("/run_script", methods=['POST'])
def run_script():
    print("Running Script")
    #run_scraper();
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(port=4555, debug=True)