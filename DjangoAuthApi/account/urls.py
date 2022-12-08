from django.urls import path,include
from account.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),
    name='register'),
    path('login/', UserLoginView.as_view(),
    name='login'),
    path('profile/', UserProfileView.as_view(),
    name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(),
    name='changepassword'),
    path('resetpassword/', SendPasswordResetEmailView.as_view(),
    name='resetpassword'),
]