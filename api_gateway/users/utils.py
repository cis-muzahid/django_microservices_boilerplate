import random
from api_gateway.settings.dev import EMAIL_HOST_USER
import requests
from rest_framework.exceptions import ValidationError
from api_gateway.settings import base
import requests
from typing import Dict, Any
from api_gateway.settings import base
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# from datetime import datetime
# from django_otp import devices_for_user
# from django_otp.plugins.otp_totp.models import TOTPDevice

# def send_and_return_otp(email):
#     """Generate and send a One-Time Password (OTP) to the provided email address.

#     Parameters:
#     - email (str): The email address to which the OTP will be sent.

#     Returns:
#     - otp (str): The generated OTP."""

#     otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
#     subject = 'Your OTP for verification'
#     message = f'Your OTP is: {otp}'
#     from_email = EMAIL_HOST_USER + "lklj"
#     recipient_list = [email]
#     send_mail(subject, message, from_email, recipient_list)
#     return otp


# def generate_otp(user):
#     otp = random.randint(100000, 999999)
#     print(otp)
#     user.otp = otp
#     user.otp_timestamp = datetime.now()
#     user.save()
#     return otp


# def verify_otp(user, otp):
#     if user.otp:
#         if int(user.otp) == int(otp):
#             user.otp = None
#             user.otp_timestamp = None
#             user.save()
#             return True
#     return False

class MessageError:
    """Class for check error messages"""
    def get_error_messages(self, serializer):
        """Method for return error messages if occure"""
        messages = []
        for msg in tuple(serializer.errors.values()):
            if type(msg) is list:
                messages.append(msg[0])
            else:
                for ele in msg.values():
                    messages.append(ele[0])
        return messages


def get_response_data(user):
    """ method for return user information """

    return {
        'email': user.email,
        'first_name': user.details.first_name,
        'last_name': user.details.last_name,
        # 'phone': '+' + str(user.details.phone.country_code) + ' ' + str(
        #     user.details.phone.national_number),
        'is_phone_verified': user.details.is_phone_verified,
        'is_email_verified': user.is_email_verified,
        'is_active': user.is_active,
        'signals': user.details.signals,
        'is_staff': user.is_staff,
        'username': user.username,
        'address': user.details.address,
        'dob': user.details.dob,
        'gender': user.details.gender,
        'connected_brokers': user.details.connected_brokers,
        'authentication_provider': user.authentication_provider,
        'is_two_factor_enabled': user.details.is_two_factor_enabled,
    }


GOOGLE_ID_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'
GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'

def generate_tokens_for_user(user):
    """
    Generate access and refresh tokens for the given user
    """
    serializer = TokenObtainPairSerializer()
    token_data = serializer.get_token(user)
    access_token = token_data.access_token
    refresh_token = token_data
    return access_token, refresh_token


def google_get_access_token(*, code, redirect_uri):
    data = {
        'code': code,
        'client_id': base.GOOGLE_OAUTH2_CLIENT_ID,
        'client_secret': base.GOOGLE_OAUTH2_CLIENT_SECRET,
        'redirect_uri': base.SOCIAL_AUTH_LOGIN_URL,
        'grant_type': 'authorization_code'
    }

    print("Sending data:", data)
    response = requests.post(base.GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=data)
    print("Received response:", response.json())

    if not response.ok:
        raise ValidationError('Failed to obtain access token from Google.')

    access_token = response.json()['access_token']
    return access_token



def google_get_user_info(*, access_token:  str) -> Dict[str, Any]:
    response = requests.get(
        GOOGLE_USER_INFO_URL,
        params={'access_token': access_token}
    )                   

    if not response.ok:
        raise ValidationError('Failed to obtain user info from Google.')

    return response.json()


def get_first_matching_attr(obj, *attrs, default=None):
    for attr in attrs:
        if hasattr(obj, attr):
            return getattr(obj, attr)

    return default


def get_error_message(exc) -> str:
    if hasattr(exc, 'message_dict'):
        return exc.message_dict
    error_msg = get_first_matching_attr(exc, 'message', 'messages')

    if isinstance(error_msg, list):
        error_msg = ', '.join(error_msg)

    if error_msg is None:
        error_msg = str(exc)

    return error_msg