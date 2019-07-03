import httplib2 # http library in python
import json # convert in memory python objects to serialized json objects

def getGeocodeLocation(inputString):
    google_api_key="AIzaSyDojugkn3ZOsQ54Md2f68sAgDrnfzgsRg8"
    locationString=inputString.replace("","+")
    url=('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString,google_api_key))
    h = httplib2.Http()
    response,content=h.request(url,'GET')
    result=json.loads(content)
    return result
