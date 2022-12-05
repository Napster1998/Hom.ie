from django.db import models


class listingInsertion(models.Model):
    listing_name = models.CharField(max_length=30)

