import urllib.request
import json

lat = "39.0289"
long = "-116.5950"
userKey = "0fedaeaf5df36f560a93305c66e20373"
url = "https://api.betterdoctor.com/2016-03-01/practices?location=" + lat + "%2C" + long + "%2C100&user_location=" + lat + "%2C" + long + "&sort=distance-asc&skip=0&limit=1000&user_key=" + userKey

resultString = urllib.request.urlopen(url).read().decode("utf-8")

resultJson = json.loads(resultString)
# print(type(resultJson['data']))

for doctors in resultJson['data']:
    # print(doctors)
    # print(doctors['name'])
    for doctor in doctors['doctors']:
        # print(doctor)
        try:
            print(doctor['profile']['first_name'] + " " + doctor['profile']['middle_name'] + " " + doctor['profile'][
                'last_name'])
        except:
            print(doctor['profile']['first_name'] + " " + doctor['profile']['last_name'])
        for specialties in doctor['specialties']:
            print(specialties['actor'])
        print("\n")
    print(doctors['visit_address']['street'] + " " + doctors['visit_address']['city'] + " " + doctors['visit_address'][
        'state_long'] + " " + doctors['visit_address']['zip'])
    print("\n")