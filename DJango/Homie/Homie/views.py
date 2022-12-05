from contextlib import _RedirectStream
from django.http import HttpResponse
from django.shortcuts import *
from django.http import HttpResponseRedirect


"Listing Page Triggered"

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

        print(fName,contact,emailId,eir,availableFrom,availableTo,address,rent,deposite,includingBill,noOfBedrooms,noOfBathrooms,ensuiteNumber,
        singleBed,twinShare,singleRoom,malePref,femalePref,couplePref,studentPref,workingPref,tvAvailable,wifiAvailable,washingAvailable,
        tableAvailable,wardrobeAvailable,additionalTextOnListing)

        return redirect('/landingPage')

    return render(request,'listingPage.html')

def goToLandingPage(request):
    return render(request,'landingPage.html')