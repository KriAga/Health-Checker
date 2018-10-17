import mysql.connector
import scrapeWeb
import config


def databaseHandler():
    mydb = mysql.connector.connect(
        host=config.host,
        user=config.dbuser,
        passwd=config.dbpassword
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")  # returns all the stored databases

    createDatabase = True
    for each in mycursor:
        if each[0] == 'treatment':
            createDatabase = False

    if createDatabase:
        print("Creating Database ... ")
        mycursor.execute("CREATE DATABASE treatment")
    else:
        print("Database already exists ...")


# calling the databaseHandler() to create a Database if it does not exists already
databaseHandler()

# Creating the table if it does not exists after we are sure that the Database exits
mydb = mysql.connector.connect(
    host=config.host,
    user=config.dbuser,
    passwd=config.dbpassword,
    database="treatment"
)
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS data (disease VARCHAR(255), treatment VARCHAR(255), description VARCHAR(255))")


#   insert data into the database
def insertData(disease, data):
    for eachType in data:
        query = "INSERT INTO data (disease, treatment, description) VALUES ('{}', '{}','{}')".format(disease, eachType,
                                                                                                     data[eachType])
        mycursor.execute(query)
    mydb.commit()


#   returns the corresponding treatment of the disease
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


#   main function
def fetch(disease):
    treatmentData = showData(disease.upper())
    return treatmentData
