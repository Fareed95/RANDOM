from django.urls import path, include
from . views import index,Formslist, Userslist
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('formslist',Formslist,basename='forms')
router.register('users',Userslist,basename='users')




urlpatterns = [
    path('',index, name = "index"),
    path('',include(router.urls))
]