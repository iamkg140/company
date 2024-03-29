from django.db import models

# Create your models here.

class IndustryType(models.Model):
    name = models.CharField(max_length = 50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
       verbose_name_plural = "1. IndustryType" 

class Company(models.Model):
    name = models.CharField(max_length = 50, blank=True )
    owner_name = models.CharField(max_length = 50, blank=True)
    address = models.CharField(max_length = 50, blank=True)
    email = models.EmailField(max_length = 50, blank=True)
    contact = models.CharField(max_length=50, blank=True)
    industry = models.ForeignKey(IndustryType,on_delete=models.CASCADE, blank=True, null=True)
  
    def __str__(self):
        return self.name

    class Meta:
       verbose_name_plural = "2. Company" 



