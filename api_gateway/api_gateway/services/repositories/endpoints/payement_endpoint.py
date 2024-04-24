from . import services

PAYMENTS_ENDPOINTS = {
    'v1': {
        services.PAYMENT_LIST_SERVICE: r'api/v1/payments/payment/list/',
        services.PAYMENT_CREATE_SERVICE: r'api/v1/payments/create-payment',
        services.PAYMENT_RETRIEVE_SERVICE: r'api/v1/payments/delete-payment/',
        services.PAYMENT_UPDATE_SERVICE: r'api/v1/payments/payment/update-payment',
        services.PAYMENT_USER_CREATE_SERVICE:r'api/v1/payments/create-user/',
        services.PAYMENT_USER_FORGOT_PASSWORD_SERVICE: r'api/v1/payments/forgot-password/',
        services.PAYMENT_USER_RESET_PASSWORD_SERVICE: r'api/v1/payments/reset-password/'

    },
}