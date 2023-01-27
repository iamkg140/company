from django.contrib import admin
from .models import *

# Register your models here.


# SuperUser - username and password -> Company

class CompanyAdmin(admin.ModelAdmin):
    list_display =  ('name', 'email','address','contact')


admin.site.register(IndustryType)
admin.site.register(Company, CompanyAdmin)
