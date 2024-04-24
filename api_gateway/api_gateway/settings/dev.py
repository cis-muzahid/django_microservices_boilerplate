from .base import *
import os
# Database Configurations

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#        'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'OPTIONS': {
#             'options': f"-c search_path={os.environ.get('DB_SCHEMA')}"
#         },
#         'NAME':os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD':os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST'),
#     }
# }

# Email Configurations.
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')

# Broker Repository
BROKER_REPOSITORY_ENDPOINT = os.environ.get('BROKER_REPOSITORY_ENDPOINT')

# Logging Configuration
if not os.path.exists('logs/errors'):
    os.makedirs('logs/errors')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logs/errors/error_{date}.log'.format(date=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'users': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'api_gateway': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
