# Generated by Django 4.1.3 on 2022-12-27 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homie', '0016_aminitiesinfo_extrainfo_preferenceinfo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybedroominfo',
            name='bedroom_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
