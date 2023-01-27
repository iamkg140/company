from django.urls import path, include
from django.conf.urls import url
from . import views

#Django admin header customiztaion

urlpatterns = [
    # path('',views.home, name="home"),
    path('allcompany',views.allcompany, name="allcompany"),
    path('industry',views.industry, name="industry"),
    path('company',views.company, name="company")
]