from django.urls import path,include
from . views import  RegisterView, LoginView, LogoutView, PasswordResetView, PasswordResetRequestView
from . users_views import UserView


urlpatterns = [
    # path('',index),
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('user',UserView.as_view()),
    path('logout',LogoutView.as_view()),
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
]
