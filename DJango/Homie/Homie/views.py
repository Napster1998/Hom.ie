from contextlib import _RedirectStream
from django.http import HttpResponse
from django.shortcuts import *
from django.http import HttpResponseRedirect
from .models import listingRaw
from .validators import spaceEir, tilldate, validateEir, convertDateToFormat, tillWhenSetter, fromWhenSetter
from datetime import datetime
from django.db.models import Q


#Listing Page Triggered

def goToListingPage(request):

    if request.method=="POST":

        fName = request.POST.get('firstName')
        contact = request.POST.get('contact')
        emailId = request.POST.get('email')
        eir = request.POST.get('EIR')
        availableFrom = request.POST.get('availableFromDate')
        availableTo = request.POST.get('availableTillDate')
        address = request.POST.get('fullAddress')
        rent = request.POST.get('expectedRent')
        deposite = request.POST.get('expectedDeposite')
        includingBill = request.POST.get('billcheck')
        noOfBedrooms = request.POST.get('numberOfBedrooms')
        noOfBathrooms = request.POST.get('numberofBathrooms')
        ensuiteNumber = request.POST.get('ensuiteNumber')
        singleBed = request.POST.get('singleBed')
        twinShare = request.POST.get('twinShare')
        singleRoom = request.POST.get('singleRoom')
        malePref = request.POST.get('malePref')
        femalePref = request.POST.get('femalePref')
        couplePref = request.POST.get('couplePref')
        studentPref = request.POST.get('studentPref')
        workingPref = request.POST.get('workingPref')
        tvAvailable = request.POST.get('tvAvailable')
        wifiAvailable = request.POST.get('wifiAvailable')
        washingAvailable = request.POST.get('washingAvailable')
        tableAvailable = request.POST.get('tableAvailable')
        wardrobeAvailable = request.POST.get('wardrobeAvailable')
        additionalTextOnListing = request.POST.get('additionalInfo')

        spacedeir = spaceEir(eir)
        validated_eir = validateEir(eir)
        if validated_eir is not False:
            latitude,longitute = validated_eir
        else:
            print("GoogleAPI returned false")
            return render(request,'listingPage.html')

        dateFormatAvailableFrom = datetime.strptime(availableFrom,'%Y-%m-%d').date()
        dateFormatAvailableTo = datetime.strptime(availableTo,'%Y-%m-%d').date()
        print(dateFormatAvailableFrom)
        print(dateFormatAvailableTo)


        rawlist = listingRaw(
            listing_name = fName, 
            listing_contact = contact, 
            listing_email = emailId, 
            listing_eir = spacedeir,
            listing_latitude = latitude,
            listing_longitude = longitute,
            listing_available_from = dateFormatAvailableFrom, 
            listing_available_to = dateFormatAvailableTo,
            listing_address = address, 
            listing_rent = rent, 
            listing_deposite = deposite,
            listing_is_bill_included = includingBill, 
            listing_no_of_bedrooms = noOfBedrooms, 
            listing_no_of_bathrooms = noOfBathrooms,
            listing_ensuite_no = ensuiteNumber,
            listing_single_bed = singleBed, 
            listing_twin_share = twinShare, 
            listing_single_room = singleRoom, 
            listing_male_preferred = malePref, 
            listing_female_preferred = femalePref, 
            listing_couple_preferred = couplePref, 
            listing_student_preferred = studentPref,
            listing_working_preferred = workingPref, 
            listing_tv_available = tvAvailable, 
            listing_wifi_available = wifiAvailable, 
            listing_washing_available = washingAvailable,
            listing_table_available = tableAvailable,
            listing_wardrobe_available = wardrobeAvailable,
            listing_additional_text = additionalTextOnListing
            )

        rawlist.save()

        return redirect('/homePage',{'listings':None})

    return render(request,'listingPage.html')

def goToLandingPage(request):
    return render(request,'landingPage.html')

def goToHomePage(request):

    if request.method == "POST":

        #Basic Filters
        mapSearch = request.POST.get('mapSearch')
        dateFromWhen = fromWhenSetter(fromWhen=request.POST.get('fromWhen'))
        dateTillWhen = tillWhenSetter(tillWhen=request.POST.get('tillWhen'))

        #Filter for Preferences 
        maleClicked = True if request.POST.get('malePref') else False
        femaleClicked = True if request.POST.get('femalePref') else False
        coupleClicked = True if request.POST.get('couplePref') else False
        studentClicked = True if request.POST.get('studentPref') else False
        workingProfessionalClicked = True if request.POST.get('workingPref') else False
        
        #Query Builder and Return Result
        query_set = listingRaw.objects.filter(listing_eir__contains=mapSearch,listing_available_from__gte=dateFromWhen,
        listing_available_to__lte=dateTillWhen).filter(Q(listing_male_preferred=maleClicked) | Q(listing_male_preferred=True))
        resultList = []
        for listing in query_set.values():
            lat,lng = listing["listing_latitude"],listing["listing_longitude"]
            noOfBeds = listing["listing_no_of_bedrooms"]
            eir = listing["listing_eir"]
            contact = listing["listing_contact"]
            resultList.append({'lat':lat,'lng':lng,'noOfBeds':noOfBeds,'eir':eir,'contact':contact})
        return render(request,'homePage.html',{'listings':resultList})

    return render(request,'homePage.html')
