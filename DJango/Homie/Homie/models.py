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
    listing_male_preferred = models.BooleanField(null = True, default= False)
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
    listing_id = models.CharField(max_length=50, default="")


class loginDetails(models.Model):
    agent_id = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    agent_name = models.CharField(max_length=30,default="")
    agent_contact = models.CharField(max_length=20,default="")
    agent_email = models.CharField(max_length=30,default="")


class listing(models.Model):
    listing_id = models.CharField(max_length=50, default="")
    property_id = models.CharField(max_length=50, default="")
    eir_code = models.CharField(max_length=30,default="")
    rent = models.IntegerField(default=0)
    address = models.CharField(max_length=50,default="")
    no_of_bedroom = models.IntegerField(default=0)


class mappings(models.Model):
    eir_code = models.CharField(max_length=30,default="")
    latitude = models.CharField(max_length=20,default="")
    longitude = models.CharField(max_length=20,default="")
    responseJSON = models.CharField(max_length=1000, default="")
    isAvailable = models.BooleanField(null = True , default= False)

class propertyDetails(models.Model):
    property_id = models.CharField(max_length=50, default="")
    property_cost_id = models.CharField(max_length=50, default="")
    property_availability_id = models.CharField(max_length=50, default="")
    property_rooms_id = models.CharField(max_length=50, default="")
    property_preference_id = models.CharField(max_length=50, default="")
    property_amenities_id = models.CharField(max_length=50, default="")
    property_info_id = models.CharField(max_length=50, default="")


class propertyCostingDetails(models.Model):
    property_cost_id = models.CharField(max_length=50, default="")
    rent = models.IntegerField(default=0)
    deposite = models.IntegerField(default=0)
    billsIncluded = models.BooleanField(null = True , default= False)

class propertyAvailabilityDetails(models.Model):
    property_availability_id = models.CharField(max_length=50, default="")
    availableFrom = models.DateField(auto_now=False)
    availableTill = models.DateField(auto_now=False)

class propertyRoom(models.Model):
    #uniquely generated
    property_rooms_id = models.CharField(max_length=50, default="")
    bedroom_id = models.CharField(max_length=50, default="")
    no_of_bathrooms = models.IntegerField(default=0)
    ensuite_no = models.IntegerField(default=0)

class propertyBedroomInfo(models.Model):
    bedroom_id = models.CharField(max_length=50, default="")
    no_of_bedrooms = models.IntegerField(default=0)
    single_bed = models.BooleanField(null = True , default= False)
    double_bed = models.BooleanField(null = True , default= False)
    twin_share = models.BooleanField(null = True , default= False)

class preferenceInfo(models.Model):
    property_preference_id = models.CharField(max_length=50, default="")
    male_pref = models.BooleanField(null = True , default= False)
    female_pref = models.BooleanField(null = True , default= False)
    couple_pref = models.BooleanField(null = True , default= False)
    student_pref = models.BooleanField(null = True , default= False)
    working_pref = models.BooleanField(null = True , default= False)

class aminitiesInfo(models.Model):
    property_amenities_id = models.CharField(max_length=50, default="")
    tv_available = models.BooleanField(null = True , default= False)
    table_available = models.BooleanField(null = True , default= False)
    wardrobe_available = models.BooleanField(null = True , default= False)
    washing_available = models.BooleanField(null = True , default= False)

class extraInfo(models.Model):
    property_info_id = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=50,default="")
    additional_info = models.CharField(max_length=300, default="")

    







