from pathlib import Path
import os
from sqlite3 import adapters
from api_gateway.settings import *
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env_vars'))

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-wa()jor%^@4jb_4s%&3#i#2ebqgn^%+vw47tzx1^(al3$m)$mb'
SECRET_KEY=os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
print('DEBUG', DEBUG)
ALLOWED_HOSTS = ['*', '192.168.2.21', '192.168.1.176']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APP = [
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    'rest_framework',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
 
]
LOCAL_APPS = [
    'users',
]
INSTALLED_APPS += THIRD_PARTY_APP + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware',


]

ROOT_URLCONF = 'api_gateway.urls'
AUTH_USER_MODEL = 'users.CustomUser'

SOCIAL_AUTH_LOGIN_URL = 'http://localhost:3000/google'
LOGIN_REDIRECT_URL = 'http://localhost:3000'
LOGOUT_REDIRECT_URL = 'http://127.0.0.1:8000/accounts/google/login/'
GOOGLE_REDIRECT_URL = 'http://localhost:3000/google'
DASHBOARD_BASE_ROUTE = 'http://localhost:3000'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
    ]


SITE_ID = 3
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}
# GOOGLE_OAUTH2_CLIENT_ID =os.environ.get('GOOGLE_OAUTH2_CLIENT_ID')
# GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET')


# GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'ADAPTER': 'api_gateway.adapters.CustomGoogleOAuth2Adapter',
    },
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': os.path.join(BASE_DIR, 'templates'),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]
WSGI_APPLICATION = 'api_gateway.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.BasicAuthentication',
    #     # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'api_gateway.core.views.renderers.ApiRenderer',
    ),
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CONFIG_DIR = os.path.join(Path(BASE_DIR), 'config')
JWT_PRIVATE_KEY_PATH = os.path.join(CONFIG_DIR, 'jwt_key')
JWT_PUBLIC_KEY_PATH = os.path.join(CONFIG_DIR, 'jwt_key.pub')

if (not os.path.exists(JWT_PRIVATE_KEY_PATH)) or (not os.path.exists(JWT_PUBLIC_KEY_PATH)):

    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(JWT_PRIVATE_KEY_PATH, 'w') as pk:
        pk.write(pem.decode())

    public_key = private_key.public_key()
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(JWT_PUBLIC_KEY_PATH, 'w') as pk:
        pk.write(pem_public.decode())
    print('PUBLIC/PRIVATE keys Generated!')

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=15),  # "exp" (Expiration Time) Claim
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),  # "exp" (Expiration Time) Claim

    'ALGORITHM': 'RS256',  # 'alg' (Algorithm Used) specified in header

    'SIGNING_KEY': open(JWT_PRIVATE_KEY_PATH).read(),
    'VERIFYING_KEY': open(JWT_PUBLIC_KEY_PATH).read(),

    'AUDIENCE': None,  # "aud" (Audience) Claim
    'ISSUER': None,  # "iss" (Issuer) Claim

    'USER_ID_CLAIM': 'user_id',  # The field name to use for identifying user
    'USER_ID_FIELD': 'id',  # The field in the DB which will be filled in USER_ID_CLAIM

    'JTI_CLAIM': 'jti',  # A token’s unique identifier

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ROTATE_REFRESH_TOKENS': False,
}
if DEBUG:
    from . import dev
else:
    from . import prod