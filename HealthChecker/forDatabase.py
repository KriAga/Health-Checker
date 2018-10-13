import mysql.connector
import scrapeWeb

treatmentData = {}


def databaseHandler():
    myDB = mysql.connector.connect(
        host="192.168.99.100",
        user="root",
        passwd="password"
    )
    myCursor = myDB.cursor()
    myCursor.execute("SHOW DATABASES")

    createDatabase = True
    for each in myCursor:
        if each[0] == 'treatment':
            createDatabase = False

    if createDatabase:
        print("Creating Database ... ")
        myCursor.execute("CREATE DATABASE treatment")
        # myCursor.execute("CREATE TABLE data (disease VARCHAR(255), treatment VARCHAR(255), description VARCHAR(255))")
    else:
        print("Database already exists ...")


databaseHandler()

myDB = mysql.connector.connect(
    host="192.168.99.100",
    user="root",
    passwd="password",
    database="treatment"
)
myCursor = myDB.cursor()
myCursor.execute(
    "CREATE TABLE IF NOT EXISTS data (disease VARCHAR(255), treatment VARCHAR(255), description VARCHAR(255))")


def insertData(disease, data):
    for eachType in data:
        query = "INSERT INTO data (disease, treatment, description) VALUES ('{}', '{}','{}')".format(disease, eachType,
                                                                                                     data[eachType])
        myCursor.execute(query)
    myDB.commit()


def showData(disease):
    myCursor.execute("SELECT * FROM data where disease = '{}'".format(disease))
    myResult = myCursor.fetchall()

    if len(myResult) == 0:
        tempData = scrapeWeb.scrapeGoogle(disease)
        insertData(disease, tempData)
        showData(disease)
    else:
        for eachRow in myResult:
            treatmentData[eachRow[1]] = eachRow[2]


def findTreatment(disease):
    showData(disease.upper())
    return treatmentData


