from django.urls import path
from . views import index,Formslist, FormsDetailView,userlistview,UsersDetailView

urlpatterns = [
    path('',index, name = "index"),
    path('formslist', Formslist, name = "formslist"),
    path('formslist/<int:pk>', FormsDetailView, name = "formsdetailview"),
    path('users',userlistview),
    path('users/<int:pk>',UsersDetailView)
]