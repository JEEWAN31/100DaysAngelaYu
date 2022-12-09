# Application Programming Interface
# Coinbase, Etherium
# Beautiful Soap
# Program and External System for all the deatils from the external Details
# Yahoo Weather Forecast and other values
# API Calling and a Post and pull requests in this detailing

# API endpoint: The last HTTPs for all the data
# Get Requests and Post request in Python
# JSON File and other Program in the Python how to handle the JSON data

import requests as re
import datetime

my_Lat = 19.119677
my_Long = 72.905083

parameters = {
    "lat": my_Lat,
    "long": my_Long,
    "formatted": 0,
}

response = re.get(url='https://api.sunrise-sunset.org/json', params=parameters)

if response.status_code != 200:
    raise Exception("That resource doesn't exist")
response.raise_for_status()

print(response)

# What are response code : 404 or something 5XX Something is wrong with the server, 3XX we don;t have the access to
# the website


Sunrise = response.json()["results"]["sunrise"]
Sunset = response.json()["results"]["sunset"]
#
Rise = (Sunrise, Sunset)
print(Rise)

# API Parameters: get different output depending upon the parameters
# latitude and longitude (Both need to be floating number)
# Optional also have some values which can be default or something else

response = re.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
print()
sunrise = data["results"]["sunrise"]
sunset = data['results']["sunset"]
print(sunrise.split("T")[0].split(":")[0])
print(sunrise)

time_now = datetime.datetime.now()
print(time_now)

response.raise_for_status()
