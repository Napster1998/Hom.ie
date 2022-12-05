from django.http import HttpResponse
from django.shortcuts import render



"Listing Page Triggered"

def goToListingPage(request):
    return render(request,'listingPage.html')