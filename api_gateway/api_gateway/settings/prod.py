from .base import *

# Debug Mode
DEBUG = False
print('DEBUG', DEBUG)

# Database Configurations
DATABASES = {
       'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'options': f"-c search_path={os.environ.get('DB_SCHEMA')}"
        },
        'NAME':os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD':os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
    }
}

# Email Configurations.
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')

# Broker Repository
BROKER_REPOSITORY_ENDPOINT = os.environ.get('BROKER_REPOSITORY_ENDPOINT')

# S3 Storage
AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.environ.get('AWS_S3_SECRET_ACCESS_KEY')
AWS_S3_STORAGE_BUCKET_NAME = os.environ.get('AWS_S3_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')

# Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
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
        's3': {
            'level': 'ERROR',
            'class': 'api_gateway.common.log_handler.S3LogHandler',
            'bucket_name': 'AWS_S3_STORAGE_BUCKET_NAME',
            'key': 'error.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['s3', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'users': {
            'handlers': ['s3', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'api_gateway': {
            'handlers': ['s3', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
