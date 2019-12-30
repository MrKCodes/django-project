from django.db import models

# Create your models here.
class CICD(models.Model):
    tech = models.CharField(max_length=20)
    deploy_date = models.DateField(auto_now=False)
    environment = models.CharField(max_length=30)
    machine_name = models.CharField(max_length=30)
    classifier = models.BigIntegerField(primary_key=True)
    smoke_test = models.BooleanField(default=False)
    smoke_test_status =models.BooleanField(default=False)