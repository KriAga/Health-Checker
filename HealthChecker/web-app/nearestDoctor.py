import urllib.request
import json
import config
# lat = "39.0289"
# long = "-116.5950"


def nearestDoctors(lat, long):
    # getting maximum 33(random number) doctors in the ascending order of their distance from the user
    url = "https://api.betterdoctor.com/2016-03-01/practices?location=" + lat + "%2C" + long + "%2C100&user_location=" + lat + "%2C" + long + "&sort=distance-asc&skip=0&limit=33&user_key=" + config.BetterDoctoruserKey
    resultString = urllib.request.urlopen(url).read().decode("utf-8")
    resultJson = json.loads(resultString)
    index = 1
    doctorProfiles = {}
    # getting the main data from the result
    for doctors in resultJson['data']:
        try:    # if any of the keys don't occur we skip that doctor
            doctorProfile = {}  # this dictionary stores the data of each doctor to be displayed at the front end.
            # getting info about each doctor
            for doctor in doctors['doctors']:
                # storing the name
                try:
                    doctorProfile["Name"] = doctor['profile']['first_name'] + " " + doctor['profile'][
                        'middle_name'] + " " + \
                                            doctor['profile'][
                                                'last_name']
                except KeyError:    # if middle name doesn't exist
                    doctorProfile["Name"] = doctor['profile']['first_name'] + " " + doctor['profile']['last_name']

                # the doctors specialisations to be stored as a list
                doctorSpecialities = []
                for specialties in doctor['specialties']:
                    doctorSpecialities.append(specialties['actor'])

                doctorProfile["specialities"] = doctorSpecialities
                # storing the address with comma-separated string
                doctorProfile["address"] = doctors['visit_address']['street'] + ", " + doctors['visit_address'][
                    'city'] + ", " + doctors['visit_address']['state_long'] + ", " + doctors['visit_address']['zip']
            doctorProfiles[index] = doctorProfile
            index = index + 1
        except KeyError:
            continue    # just in case some key doesn't exist
    return doctorProfiles