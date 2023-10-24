""" A module for fetching data from the API and returning it in a usable format. """

from sys import exit as sys_exit
import json
import re
import requests

class API:
    """ A class for fetching data from the API and returning it in a usable format. """

    REQUESTS_TIMEOUT = 10

    @staticmethod
    def fetch():
        """ Fetches data from the API and returns it in a usable format. """

        try:
            api_requests_city = requests.get("http://api.gios.gov.pl/pjp-api/rest/station/findAll",
            timeout=API.REQUESTS_TIMEOUT)

            api_city = json.loads(api_requests_city.content)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            API.api_error()

        stations = []
        options = []

        for station_data in api_city:
            if (station_data["city"]["name"] == "Kraków" or
                station_data["city"]["commune"]["districtName"] == "krakowski"):

                try:
                    sensors = requests.get(
                        "http://api.gios.gov.pl/pjp-api/rest/station/sensors/"
                        + str(station_data['id']),
                        timeout=API.REQUESTS_TIMEOUT
                    )

                    indexes = requests.get(
                        "http://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/"
                        + str(+station_data['id']),
                        timeout=API.REQUESTS_TIMEOUT
                    )

                    sensors = json.loads(sensors.content)
                    indexes = json.loads(indexes.content)

                except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
                    API.api_error()

                cut_sensors = []

                for sensor in sensors:
                    sensor_name = sensor["param"]["paramFormula"]


                    sensor_value = sensor_name.lower()
                    sensor_value = re.sub(r"\.", "", sensor_value)
                    sensor_value = sensor_value+'IndexLevel'

                    if (sensor_value in indexes
                        and indexes[sensor_value] is not None
                        and 'indexLevelName' in indexes[sensor_value]
                    ):
                        sensor_value = indexes[sensor_value]['indexLevelName']
                    else:
                        continue

                    cut_sensors.append({
                        'name': sensor_name,
                        'value': sensor_value
                    })

                stations.append(
                {
                "stationName": station_data["stationName"],
                "id": station_data["id"],
                "sensors": cut_sensors,
                }
                )

                options.append(station_data["stationName"])

        return {
            "stations": stations,
            "options": options
        }

    @staticmethod
    def api_error():
        """ Displays an error message and exits the program. """

        print("There was an error while fetching data from API. Please try again later.")
        print("Check if the API is working properly:", end=" ")
        print("http://api.gios.gov.pl/pjp-api/rest/station/findAll")
        print("Also check if you have an internet connection.")
        print("If the problem persists, please contact the developer.")
        print("Exiting...")
        sys_exit()
