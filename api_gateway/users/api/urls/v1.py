from ..views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'api_users_v1'

urlpatterns = [
     path('signup/', SignUp.as_view(), name='signup'),
     path('jwt-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('login/', LogInView.as_view(), name='user-login'),
     path('logout/', LogoutView.as_view(), name="logout"),
     path('verify-email/', VerifyOtpView.as_view(), name='verify-otp'),
     path('fetch-users/', FetchUsersView.as_view(), name='fetch-users'),
     path('forgot-password/', ForgotPasswordApiView.as_view(),
          name='forget-password'),
     path('reset-password/', ResetPasswordApiView.as_view(),
         name='reset-password'),
     path('google-login/', CustomGoogleLoginView.as_view(), name='google-login'),


]
