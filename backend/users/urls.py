from django.urls import path,include
from . views import index , RegisterView, LoginView,UserView, LogoutView

urlpatterns = [
    path('',index),
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('user',UserView.as_view()),
    path('logout',LogoutView.as_view()),
]
