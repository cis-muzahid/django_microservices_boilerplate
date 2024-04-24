from . import services
BROKER_ENDPOINTS = {
    'v1': {
        services.BROKER_LIST_SERVICE: r'api/v1/broker/broker-list/',
        services.BROKER_CREATE_SERVICE: r'api/v1/broker/create/',
        services.BROKER_RETRIEVE_SERVICE: r'api/v1/broker/get/{}/',
        services.BROKER_UPDATE_SERVICE: r'api/v1/broker/update/{}/',
        services.BROKER_USER_CREATE_SERVICE: r'api/v1/broker/user-create/',
        services.BROKER_USER_FORGOT_PASSWORD_SERVICE: r'api/v1/broker/forgot-password/',
        services.BROKER_USER_RESET_PASSWORD_SERVICE: r'api/v1/broker/reset-password/'
    },
}

