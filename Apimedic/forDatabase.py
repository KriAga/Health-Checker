import mysql.connector
import scraper


def databaseHandler():
    mydb = mysql.connector.connect(
        host="192.168.99.100",
        user="root",
        passwd="password"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES LIKE 'treatment';")
    if mycursor.arraysize == 0:
        mycursor.execute("CREATE DATABASE treatment")
        mycursor.execute("CREATE TABLE data (disease VARCHAR(255), treatment VARCHAR(255), description VARCHAR(255))")
    else:
        print("database exists")


databaseHandler()

mydb = mysql.connector.connect(
    host="192.168.99.100",
    user="root",
    passwd="password",
    database="treatment"
)
mycursor = mydb.cursor()


def insertData(disease, data):
    for eachType in data:
        query = "INSERT INTO data (disease, treatment, description) VALUES ('{}', '{}','{}')".format(disease, eachType,
                                                                                                     data[eachType])
        print(query)
        mycursor.execute(query)
    mydb.commit()


def showData(disease):
    mycursor.execute("SELECT * FROM data where disease = '{}'".format(disease))
    myresult = mycursor.fetchall()
    json = {}
    if len(myresult) == 0:
        tempData = scraper.scrapeGoogle(disease)
        insertData(disease, tempData)
        showData(disease)
    else:
        for eachRow in myresult:
            json[eachRow[1]] = eachRow[2]
        print(json)


disease = "dengue"
showData(disease.upper())
