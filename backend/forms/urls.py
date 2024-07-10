from django.urls import path
from . views import index,FormsList

urlpatterns = [
    path('',index, name = "index"),
    path('formslist', FormsList, name = "formslist")
]
