from django.db import models



class listingRaw(models.Model):
    listing_name = models.CharField(max_length=30,default="")
    listing_contact = models.CharField(max_length=20,default="")
    listing_email = models.CharField(max_length=30,default="")
    listing_eir = models.CharField(max_length=30,default="")
    listing_latitude = models.CharField(max_length=20,default="")
    listing_longitude = models.CharField(max_length=20,default="")
    listing_available_from = models.DateField(auto_now=False)
    listing_available_to = models.DateField(auto_now=False)
    listing_address = models.CharField(max_length=50,default="")
    listing_rent = models.IntegerField(default=0)
    listing_deposite = models.IntegerField(default=0)
    listing_is_bill_included = models.BooleanField(null = True , default= False)
    listing_no_of_bedrooms = models.IntegerField(default=0)
    listing_no_of_bathrooms = models.IntegerField(default=0)
    listing_ensuite_no = models.IntegerField(default=0)
    listing_single_bed = models.BooleanField(null = True , default= False)
    listing_twin_share = models.BooleanField(null = True , default= False)
    listing_single_room = models.BooleanField(null = True , default= False)
    listing_male_preferred = models.BooleanField(null = True , default= False)
    listing_female_preferred = models.BooleanField(null = True , default= False)
    listing_couple_preferred = models.BooleanField(null = True , default= False)
    listing_student_preferred = models.BooleanField(null = True , default= False)
    listing_working_preferred = models.BooleanField(null = True , default= False)
    listing_tv_available = models.BooleanField(null = True , default= False)
    listing_wifi_available = models.BooleanField(null = True , default= False)
    listing_washing_available = models.BooleanField(null = True , default= False)
    listing_table_available = models.BooleanField(null = True , default= False)
    listing_wardrobe_available = models.BooleanField(null = True , default= False)
    listing_additional_text = models.CharField(max_length=300, default="")




