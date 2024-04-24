from django.conf import settings
# from api_gateway.api_gateway import settings
from api_gateway.core.services.base.repository import RestRepository
from api_gateway.services.repositories.endpoints import services
from .endpoints.payement_endpoint import PAYMENTS_ENDPOINTS


class PaymentRepository(RestRepository):
    def __init__(self, version):
        super(PaymentRepository, self).__init__(version)
        self.repository_url = settings.PAYEMENT_REPOSITORY_ENDPOINT
        self.endpoints = PAYMENTS_ENDPOINTS

    # def pension_account_delete(self, user_id):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_PENSION_ACCOUNT_DELETE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url)

    def payment_list(self, user_id, data, headers):
        url = self.get_service_endpoint(
            services.PAYMENT_LIST_SERVICE, False)
        # breakpoint()
        url = self.get_absolute_url(url)
        return self.get(url, data, headers)

    def payment_create(self, user_id, data, headers):
        url = self.get_service_endpoint(
            services.PAYMENT_CREATE_SERVICE, False)
        url = self.get_absolute_url(url)
        return self.post(url, data, headers)

    def payment_update(self, user_id, data, headers):
        url = self.get_service_endpoint(
            services.PAYMENT_UPDATE_SERVICE, False)
        url = self.get_absolute_url(url.format(user_id))
        return self.patch(url, data, headers)

    def payment_retrieve(self, user_id, headers):
        url = self.get_service_endpoint(
            services.BROKER_RETRIEVE_SERVICE, False)
        # breakpoint()
        url = self.get_absolute_url(url.format(user_id))
        data = {}
        return self.get(url, data,  headers)

    def create_new_user(self, data):
        url = self.get_service_endpoint(
            services.PAYMENT_USER_CREATE_SERVICE, False)
        url = self.get_absolute_url(url)
        # data['create_date'] = data['create_date'].isoformat()
        # data['modify_date'] = data['modify_date'].isoformat()
        return self.post(url, data=data)

    def forgot_password(self, data, headers):
        url = self.get_service_endpoint(
            services.PAYMENT_USER_FORGOT_PASSWORD_SERVICE, False)
        url = self.get_absolute_url(url)
        # data['create_date'] = data['create_date'].isoformat()
        # data['modify_date'] = data['modify_date'].isoformat()
        return self.post(url, headers, data=data)

    def reset_password(self, data, headers):
        url = self.get_service_endpoint(
            services.PAYMENT_USER_RESET_PASSWORD_SERVICE, False)
        url = self.get_absolute_url(url)
        # data['create_date'] = data['create_date'].isoformat()
        # data['modify_date'] = data['modify_date'].isoformat()
        return self.post(url, headers, data=data)