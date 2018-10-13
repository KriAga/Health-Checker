import mysql.connector
import scrapeWeb


def databaseHandler():
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="admin"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")

    createDatabase = True
    for each in mycursor:
        if (each[0] == 'treatment'):
            createDatabase = False

    if createDatabase:
        print("Creating Database ... ")
        mycursor.execute("CREATE DATABASE treatment")
        # mycursor.execute("CREATE TABLE data (disease VARCHAR(255), treatment VARCHAR(255), description VARCHAR(255))")
    else:
        print("Database already exists ...")


databaseHandler()

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database="treatment"
)
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS data (disease VARCHAR(255), treatment VARCHAR(255), description VARCHAR(255))")


def insertData(disease, data):
    for eachType in data:
        query = "INSERT INTO data (disease, treatment, description) VALUES ('{}', '{}','{}')".format(disease, eachType,
                                                                                                     data[eachType])
        mycursor.execute(query)
    mydb.commit()


def showData(disease):
    treatmentData = {}
    mycursor.execute("SELECT * FROM data where disease = '{}'".format(disease))
    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        disease, tempData = scrapeWeb.scrapeGoogle(disease)
        insertData(disease, tempData)
        treatmentData = showData(disease)
    else:
        for eachRow in myresult:
            treatmentData[eachRow[1]] = eachRow[2]
    return treatmentData


def fetch(disease):
    treatmentData = showData(disease.upper())
    return (treatmentData)
