from django.db import models
from . import views


class listingRaw(models.Model):
    listing_name = models.CharField(max_length=30)
    listing_contact = models.IntegerField()
    listing_is_bill_included = models.BooleanField(null = True , default= False)
    