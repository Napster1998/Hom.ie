
import requests
from datetime import datetime
from .models import mappings

#Used to add space to EIR code if user doesn't

def spaceEir(eir):
    for i in enumerate(eir):
            if " " not in eir:
                eir = eir[:-4] + " " + eir[-4:]
                return(eir)
    else:
        return(eir)

#Used to call Google Maps API and check if location exists or not and also return response json if it does while returning lat and lng

def validateEir(eir):
    API_KEY = "AIzaSyCtly0rm-GQOUsWupPChTkT7shYVtNl0wk"
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+eir+'&key='+API_KEY)
    ApiResponse = response.json()
    try:
        lat = ApiResponse['results'][0]["geometry"]["location"]["lat"]
        lng = ApiResponse['results'][0]["geometry"]["location"]["lng"]
        return(str(lat),str(lng))
    except:
        return False

def responseReturn(eir):

    API_KEY = "AIzaSyCtly0rm-GQOUsWupPChTkT7shYVtNl0wk"
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+eir+'&key='+API_KEY)
    ApiResponse = response.json()
    return(str(ApiResponse))



#Used to format dates on filter of Home Page in 
def convertDateToFormat(fromWhen):
    datetime.strptime(fromWhen if fromWhen != "" else datetime.today().strftime('%Y-%m-%d'),'%Y-%m-%d').date()
    return(fromWhen)


#Setting the Till date

def tilldate():
    temp = datetime(2100, 12, 31).strftime('%Y-%m-%d')
    return temp

def fromdate():
    temp = datetime(2022, 9, 10).strftime('%Y-%m-%d')
    return temp

def tillWhenSetter(tillWhen):
    if tillWhen != "":
        dateTillWhen = datetime.strptime(tillWhen, '%Y-%m-%d').date()
    else:
        dateTillWhen = datetime.strptime(tilldate(), '%Y-%m-%d').date()
    return(dateTillWhen)

def fromWhenSetter(fromWhen):
    if fromWhen != "":
        dateFromWhen = datetime.strptime(fromWhen, '%Y-%m-%d').date()
    else:
        dateFromWhen = datetime.strptime(fromdate(), '%Y-%m-%d').date()
    return(dateFromWhen)


