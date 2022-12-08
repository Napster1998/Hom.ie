
import requests

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
    a = response.json()
    try:
        lat = a['results'][0]["geometry"]["location"]["lat"]
        lng = a['results'][0]["geometry"]["location"]["lng"]
        return(str(lat),str(lng))
    except:
        return False



