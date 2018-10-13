import urllib.request
import json

# lat = "39.0289"
# long = "-116.5950"

# Using BetterDoctor API


def nearestDoctors(lat, long):
    userKey = "0fedaeaf5df36f560a93305c66e20373"
    url = "https://api.betterdoctor.com/2016-03-01/practices?location=" + lat + "%2C" + long + "%2C100&user_location=" + lat + "%2C" + long + "&sort=distance-asc&skip=0&limit=33&user_key=" + userKey

    resultString = urllib.request.urlopen(url).read().decode("utf-8")
    doctorsProfile = {}
    resultJson = json.loads(resultString)
    index = 1

    for doctors in resultJson['data']:
        try:
            doctorProfile = {}
            for doctor in doctors['doctors']:
                try:
                    doctorProfile["Name"] = doctor['profile']['first_name'] + " " + doctor['profile'][
                        'middle_name'] + " " + \
                                            doctor['profile'][
                                                'last_name']
                except KeyError:
                    doctorProfile["Name"] = doctor['profile']['first_name'] + " " + doctor['profile']['last_name']

                doctorSpecialities = []
                for specialties in doctor['specialties']:
                    doctorSpecialities.append(specialties['actor'])

                doctorProfile["specialities"] = doctorSpecialities
                doctorProfile["address"] = doctors['visit_address']['street'] + ", " + doctors['visit_address'][
                    'city'] + ", " + doctors['visit_address']['state_long'] + ", " + doctors['visit_address']['zip']

            doctorsProfile[index] = doctorProfile
            index = index + 1
        except KeyError:
            continue
    return doctorsProfile