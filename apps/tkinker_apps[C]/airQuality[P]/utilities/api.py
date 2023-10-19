""" A module for fetching data from the API and returning it in a usable format. """

import requests
import json
import re

class API:

    @staticmethod
    def fetch():
        """ Fetches data from the API and returns it in a usable format. """

        try:
            apiRequestsCity = requests.get("http://api.gios.gov.pl/pjp-api/rest/station/findAll")
            apiCity = json.loads(apiRequestsCity.content)
        except Exception:
            API.api_error()

        stations = []
        options = []

        for x in apiCity:
            if (x["city"]["name"] == "Kraków" or x["city"]["commune"]["districtName"] == "krakowski"):
                try:
                    sensors = requests.get("http://api.gios.gov.pl/pjp-api/rest/station/sensors/"+str(x['id']))
                    indexes = requests.get("http://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/"+str(+x['id']))
                    sensors = json.loads(sensors.content)
                    indexes = json.loads(indexes.content)
                except Exception:
                    API.api_error()
            
                cutSensors = []
                
                for sensor in sensors:
                    sensorName = sensor["param"]["paramFormula"]


                    sensorValue = sensorName.lower()
                    sensorValue = re.sub("\.", "", sensorValue)
                    sensorValue = sensorValue+'IndexLevel'

                    if (sensorValue in indexes):
                        sensorValue = indexes[sensorValue]['indexLevelName']
                    else:
                        continue

                    cutSensors.append({
                        'name': sensorName,
                        'value': sensorValue
                    })

                stations.append({
                "stationName": x["stationName"],
                "id": x["id"],
                "sensors": cutSensors,
                })

                options.append(x["stationName"])

        return {
            "stations": stations,
            "options": options
        }
    
    @staticmethod
    def api_error():
        """ Displays an error message and exits the program. """

        print("There was an error while fetching data from API. Please try again later.")
        print("Check if the API is working properly: http://api.gios.gov.pl/pjp-api/rest/station/findAll")
        print("Also check if you have an internet connection.")
        print("If the problem persists, please contact the developer.")
        print("Exiting...")
        exit()
