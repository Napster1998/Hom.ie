from contextlib import _RedirectStream
from django.http import HttpResponse
from django.shortcuts import *
from django.http import HttpResponseRedirect
from .models import listingRaw , loginDetails, listing, mappings, propertyDetails, propertyCostingDetails, propertyAvailabilityDetails, propertyRoom, propertyBedroomInfo, preferenceInfo, aminitiesInfo, extraInfo
from .validators import spaceEir, tilldate, validateEir, convertDateToFormat, tillWhenSetter, fromWhenSetter, responseReturn
from datetime import datetime
from django.db.models import Q
import uuid


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
        listing_id_generated = uuid.uuid4()
        agent_id_generated = uuid.uuid4()
        property_id_generated = uuid.uuid4()

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
            listing_additional_text = additionalTextOnListing,
            listing_id = listing_id_generated
            )

        rawAgent = loginDetails(
            agent_id = agent_id_generated,
            agent_name = fName,
            agent_contact = contact,
            agent_email = emailId
            )

        rawlisttable = listing(
            listing_id = listing_id_generated,
            property_id = property_id_generated,
            eir_code = spacedeir,
            rent = rent,
            address = address,
            no_of_bedroom = noOfBedrooms
            )

        mapper = mappings(
            eir_code = spacedeir,
            latitude = latitude,
            longitude = longitute,
            responseJSON = responseReturn(eir)
        )

        property_cost_id_generated = uuid.uuid4()
        property_availability_id_generated = uuid.uuid4()
        property_rooms_id_generated = uuid.uuid4()
        property_preference_id_generated = uuid.uuid4()
        property_amenities_id_generated = uuid.uuid4()
        property_info_id_generaated = uuid.uuid4()
        property_bedroom_id = uuid.uuid4()

        prop = propertyDetails(
            property_id = property_id_generated,
            property_cost_id = property_cost_id_generated,
            property_availability_id = property_availability_id_generated,
            property_rooms_id = property_rooms_id_generated,
            property_preference_id = property_preference_id_generated,
            property_amenities_id = property_amenities_id_generated,
            property_info_id = property_info_id_generaated
        )

        cost = propertyCostingDetails(
            property_cost_id = property_cost_id_generated,
            rent = rent,
            deposite = deposite,
            billsIncluded = includingBill
        )

        avail = propertyAvailabilityDetails(
            property_availability_id = property_availability_id_generated,
            availableFrom = dateFormatAvailableFrom,
            availableTill = dateFormatAvailableTo
        )

        roomDetail = propertyRoom(
            property_rooms_id = property_rooms_id_generated,
            bedroom_id = property_bedroom_id,
            no_of_bathrooms = noOfBathrooms,
            ensuite_no = ensuiteNumber
        )

        bedroomDetails = propertyBedroomInfo(
            bedroom_id = property_bedroom_id,
            no_of_bedrooms = noOfBedrooms,
            single_bed = singleBed,
            #Double Bed doesn't exist
            double_bed = singleRoom,
            twin_share = twinShare
        )

        preferences = preferenceInfo(
            property_preference_id = property_preference_id_generated,
            male_pref = malePref,
            female_pref = femalePref,
            couple_pref = couplePref,
            student_pref = studentPref,
            working_pref = workingPref
        )

        aminities = aminitiesInfo(
            property_amenities_id = property_amenities_id_generated,
            tv_available = tvAvailable,
            table_available = tableAvailable,
            wardrobe_available = wardrobeAvailable,
            washing_available = washingAvailable
        )

        extrainfo = extraInfo(
            property_info_id = property_info_id_generaated,
            address = address,
            additional_info = additionalTextOnListing
        )

        extrainfo.save()
        aminities.save()
        preferences.save()
        bedroomDetails.save()
        roomDetail.save()
        avail.save()
        cost.save()
        prop.save()
        mapper.save()
        rawlist.save()
        rawlisttable.save()
        rawAgent.save()

        return redirect('/homePage',{'listings':None})

    return render(request,'listingPage.html')

def goToHomePage(request):

    if request.method == "POST":

        #Basic Filters
        mapSearch = request.POST.get('mapSearch')
        dateFromWhen = fromWhenSetter(fromWhen=request.POST.get('fromWhen'))
        dateTillWhen = tillWhenSetter(tillWhen=request.POST.get('tillWhen'))

        #Filter for Preferences 
        # maleClicked = True if request.POST.get('malePref') else False
        # femaleClicked = True if request.POST.get('femalePref') else False
        # coupleClicked = True if request.POST.get('couplePref') else False
        # studentClicked = True if request.POST.get('studentPref') else False
        # workingProfessionalClicked = True if request.POST.get('workingPref') else False
        
        #Query Builder and Return Result
        query_set = listingRaw.objects.filter(listing_eir__contains=mapSearch,listing_available_from__gte=dateFromWhen,
        listing_available_to__lte=dateTillWhen)
        resultList = []
        for listing in query_set.values():
            lat,lng = listing["listing_latitude"],listing["listing_longitude"]
            noOfBeds = listing["listing_no_of_bedrooms"]
            eir = listing["listing_eir"]
            contact = listing["listing_contact"]
            rent = listing["listing_rent"]
            print(resultList)
            resultList.append({'lat':lat,'lng':lng,'noOfBeds':noOfBeds,'eir':eir,'contact':contact,'rent':rent})
        return render(request,'homePage.html',{'listings':resultList})

    return render(request,'homePage.html')



    