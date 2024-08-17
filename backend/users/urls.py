from django.urls import path, include
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    PasswordResetRequestView,
    PasswordResetView,
    GoogleLoginView
)
from .users_views import UserView

urlpatterns = [
    # Your custom URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('google-login/', GoogleLoginView.as_view(), name='google-login'),

    # Include social_django URLs for handling OAuth2 callbacks
    path('auth/', include('social_django.urls', namespace='social')),
]
