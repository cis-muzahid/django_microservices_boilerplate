from django.conf import settings
# from api_gateway.api_gateway import settings
from api_gateway.core.services.base.repository import RestRepository
from api_gateway.services.repositories.endpoints import services
from .endpoints.broker import BROKER_ENDPOINTS


class BrokerRepository(RestRepository):
    def __init__(self, version):
        super(BrokerRepository, self).__init__(version)
        self.repository_url = settings.BROKER_REPOSITORY_ENDPOINT
        self.endpoints = BROKER_ENDPOINTS

    # def pension_account_delete(self, user_id):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_PENSION_ACCOUNT_DELETE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url)

    def broker_list(self, user_id, data, headers):
        url = self.get_service_endpoint(
            services.BROKER_LIST_SERVICE, False)
        # breakpoint()
        url = self.get_absolute_url(url)
        return self.get(url, data, headers)

    def broker_create(self, user_id, data, headers):
        url = self.get_service_endpoint(
            services.BROKER_CREATE_SERVICE, False)
        url = self.get_absolute_url(url)
        return self.post(url, data, headers)

    def broker_update(self, user_id, data, headers):
        url = self.get_service_endpoint(
            services.BROKER_UPDATE_SERVICE, False)
        url = self.get_absolute_url(url.format(user_id))
        return self.patch(url, data, headers)

    def broker_retrieve(self, user_id, headers):
        url = self.get_service_endpoint(
            services.BROKER_RETRIEVE_SERVICE, False)
        # breakpoint()
        url = self.get_absolute_url(url.format(user_id))
        data = {}
        return self.get(url, data,  headers)

    def create_new_user(self, data):
        url = self.get_service_endpoint(
            services.BROKER_USER_CREATE_SERVICE, False)
        url = self.get_absolute_url(url)
        # data['create_date'] = data['create_date'].isoformat()
        # data['modify_date'] = data['modify_date'].isoformat()
        return self.post(url, data=data)

    def forgot_password(self, data, headers):
        url = self.get_service_endpoint(
            services.BROKER_USER_FORGOT_PASSWORD_SERVICE, False)
        url = self.get_absolute_url(url)
        # data['create_date'] = data['create_date'].isoformat()
        # data['modify_date'] = data['modify_date'].isoformat()
        return self.post(url, headers, data=data)

    def reset_password(self, data, headers):
        url = self.get_service_endpoint(
            services.BROKER_USER_RESET_PASSWORD_SERVICE, False)
        url = self.get_absolute_url(url)
        # data['create_date'] = data['create_date'].isoformat()
        # data['modify_date'] = data['modify_date'].isoformat()
        return self.post(url, headers, data=data)

    # def pension_account_delete(self, user_id):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_PENSION_ACCOUNT_DELETE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url)

    # def get_pension_lga_state_list(self, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_PENSION_LGA_STATE_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, params=params)

    # def get_pension_region_list(self, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_PENSION_REGION_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, params=params)

    # def get_pfa_list(self):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_PFA_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url)

    # def get_pension_country_list(self):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_PENSION_COUNTRY_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url)

    # def get_lga_list(self, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_LGA_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, params=params)

    # def get_location_type_list(self, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_LOCATION_TYPE_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, params=params)

    # def get_employer_list(self, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_EMPLOYER_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, params=params)     

    # def get_sector_of_employment_list(self):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_SECTOR_OF_EMPLOYMENT_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url)

    # def get_relationship_list(self):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_RELATIONSHIP_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url)

    # def get_airtime_network_list(self):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_AIRTIME_NETWORK_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url)

    # def get_wallet_balance(self, user_id):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_WALLET_ACCOUNT_BALANCE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url)

    # def get_agent_wallet_balance(self, user_id):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_AGENT_WALLET_ACCOUNT_BALANCE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url)

    # def change_wallet_pin(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_CHANGE_WALLET_PIN, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.put(url, data=data)

    # def get_user_wallet_balance(self, user_id):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_USER_WALLET_DETAILS, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url)

    # def get_wallet_transaction_chart(self, user_id):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_WALLET_TRANSACTION_CHART, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url)

    # def tranfer_wallet_balance_request(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_WALLET_ACCOUNT_BALANCE_TRANSFER_START, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url, data)

    # def tranfer_wallet_balance_request_complete(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_WALLET_ACCOUNT_BALANCE_TRANSFER_COMPLETE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url, data)

    # def get_user_tranfer_history(self, user_id, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_WALLET_ACCOUNT_BALANCE_TRANSFER_HISTORY, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url, params=params)

    # def get_tranfer_history_list(self, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_WALLET_TRANSACTION_HISTORY_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, params=params)

    # def get_tranfer_history_data(self, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_WALLET_TRANSACTION_HISTORY_DATA, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, params=params)

    # def custom_pot_money_transfer_request_complete(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_WALLET_CUSTOM_POT_ADD_MONEY_REQUEST_COMPLETE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url, data)

    # def create_subwallet_invite(self, user_id, invite_data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_CREATE_SUBWALLET, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url, invite_data)

    # def admin_reward_pot(self, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_ADMIN_REWARD_POT, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, params=params)

    # def subwallet_user_invites(self, user_id, status_id, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_SUBWALLLET_USER_INVITES, False)
    #     url = self.get_absolute_url(url.format(user_id, status_id))
    #     params.update({'status': status_id})
    #     return self.get(url, params=params)

    # def validate_subwallet_phonenumber(self, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_VALIDATE_SUBWALLET_PHONE, False)
    #     url = self.get_absolute_url(url)
    #     return self.post(url, data)

    # def reward_pots_wallet_transfer_complete(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_REWARDS_TRANSFER_WALLET_COMPLETE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url, data)

    # def investment_pots_wallet_transfer_complete(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_INVESTMENT_TRANSFER_WALLET_COMPLETE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url, data)

    # def admin_allusers_list(self, data, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_ADMIN_ALL_USERS_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, data=data, params=params)

    # def admin_allusers_download(self, data, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_ADMIN_ALL_USERS_DOWNLAOD, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, data=data, params=params)

    # def tanadi_users_list(self, data, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_TANADI_USERS_LIST, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, data=data, params=params)

    # def loan_pots_wallet_transfer_complete(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_LOAN_POT_WALLET_TRANSFER_COMPLETE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url, data)

    # def create_new_user(self, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_WALLET_USER_CREATE, False)
    #     url = self.get_absolute_url(url)
    #     data['create_date'] = data['create_date'].isoformat()
    #     data['modify_date'] = data['modify_date'].isoformat()
    #     return self.post(url, data=data)

    # def get_user_profile(self, user_id):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_GET_USER_PROFILE_DATA, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url)

    # def update_user_details(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_UPDATE_USER_DETAILS, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.put(url, data=data)

    # def view_taj_account(self, user_id):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_VIEW_TAJ_ACCOUNT, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url)

    # def update_taj_profile_image(self, user_id, files):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_UPDATE_TAJ_PROFILE_IMAGE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.put(url, files=files, data=None)

    # def update_tanadi_kyc_proof_image(self, user_id, files):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_UPDATE_TANADI_KYC_PROOF, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.put(url, files=files, data=None)

    # def admin_user_wallet_transaction_history(self, user_id, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_USER_WALLET_TRANSACTIONS_ADMIN, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url, params=params)

    # def user_recent_payouts_view(self, user_id, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_USER_RECENT_PAYOUTS, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url, params=params)

    # def transactions_with_phone_number_owner(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_TRANSACTIONS_WITH_PHONENUMBER_OWNER, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url, data=data)

    # def transactions_with_user(self, user_id, params, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_TRANSACTIONS_WITH_USER, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url, params=params, data=data)

    # def delete_tanadi_kyc_proof_image(self, user_id):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_DELETE_TANADI_KYC_PROOF, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.patch(url, data={})

    # def get_maintenance_fee(self, user_id, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_USER_MAINTENANCE_FEE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url, params=params)

    # def get_user_pension_bank_pin(self, user_id, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_USER_PENSION_BANK_PIN_DETAILS, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url, params=params)

    # def get_user_sms_fee(self, user_id, params):
    #     url = self.get_service_endpoint(services.SERVICE_USER_SMS_FEE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url, params=params)

    # def get_montly_sms_fee(self, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_MONTHLY_SMS_FEE, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, params=params)

    # def get_montly_maintenace_fee(self, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_MONTHLY_MAINTENANCE_FEE, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, params=params)

    # def get_monthly_ussd_fee(self, params):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_MONTHLY_USSD_FEE, False)
    #     url = self.get_absolute_url(url)
    #     return self.get(url, params=params)

    # def update_admin_wallet_fund(self, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_UPDATE_ADMIN_WALLET_BALANCE, False)
    #     url = self.get_absolute_url(url)
    #     return self.post(url, data=data)

    # def user_wallet_to_user_bank_transfer(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_USER_WALLET_TO_USER_BANK_TRANSFER, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url, data=data)

    # def user_bank_to_user_wallet_transfer(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_USER_BANK_TO_USER_WALLET_TRANSFER, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url, data=data)

    # def user_defaulted_fee(self, user_id):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_USER_DEFAULTED_FEE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.get(url)

    # def reset_transaction_pin(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_WALLET_RESET_TRANSACTION_PIN, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.put(url, data=data)

    # def admin_inactive_user_funds_transfer(self, user_id, data):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_ADMIN_INACTIVE_USER_FUNDS_TRANSFER, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.post(url, data=data)
    
    # def update_pension_profile_image(self, user_id, files):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_UPDATE_PENSION_PROFILE_IMAGE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.put(url, files=files, data=None)

        
    # def upload_pension_signature_image(self, user_id, files):
    #     url = self.get_service_endpoint(
    #         services.SERVICE_UPLOAD_PENSION_SIGNATURE_IMAGE, False)
    #     url = self.get_absolute_url(url.format(user_id))
    #     return self.put(url, files=files, data=None)


# class TajAccountRepository(RestRepository):

#     def __init__(self, version):
#         super(TajAccountRepository, self).__init__(version)
#         self.repository_url = settings.WALLET_REPOSITORY_ENDPOINT
#         self.endpoints = BROKER_ENDPOINTS

#     def create_update_taj_account(self, user_id, taj_account_data):
#         url = self.get_service_endpoint(
#             services.SERVICE_TAJ_ACCOUNT_CREATE_UPDATE, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.post(url, taj_account_data)

#     def tajaccount_change_status(self, account_id, data):
#         url = self.get_service_endpoint(
#             services.SERVICE_TAJ_ACCOUNT_STATUS_UPDATE, False)
#         url = self.get_absolute_url(url.format(account_id))
#         return self.patch(url, data=data)

#     def salary_account_rating(self, user_id, data):
#         url = self.get_service_endpoint(
#             services.SERVICE_SALARY_ACCOUNT_RATING, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.patch(url, data=data)

#     def get_tajaccount_all_list(self, params):
#         url = self.get_service_endpoint(
#             services.SERVICE_TAJ_ACCOUNT_ALL_LIST, False)
#         url = self.get_absolute_url(url)
#         return self.get(url, params=params)

#     def get_tajaccount_pending_list(self, params):
#         url = self.get_service_endpoint(
#             services.SERVICE_TAJ_ACCOUNT_PENDING_LIST, False)
#         url = self.get_absolute_url(url)
#         return self.get(url, params=params)

#     def update_taj_profile_image(self, user_id, action, files):
#         url = self.get_service_endpoint(
#             services.SERVICE_TAJ_PROFILE_SIGN_UPDATE_DELETE, False)
#         url = self.get_absolute_url(url.format(user_id, action))
#         return self.put(url, files=files, data={})


# class KYCDetailRepository(RestRepository):

#     def __init__(self, version):
#         super(KYCDetailRepository, self).__init__(version)
#         self.repository_url = settings.WALLET_REPOSITORY_ENDPOINT
#         self.endpoints = BROKER_ENDPOINTS

#     def create_update_kyc_details(self, user_id, taj_account_data):
#         url = self.get_service_endpoint(
#             services.SERVICE_KYC_DETAIL_CREATE_UPDATE, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.post(url, taj_account_data)

#     def get_kycdetail_all_list(self, params):
#         url = self.get_service_endpoint(
#             services.SERVICE_KYC_DETAIL_ALL_LIST, False)
#         url = self.get_absolute_url(url)
#         return self.get(url, params=params)

#     def get_kycdetail_pending_list(self, params):
#         url = self.get_service_endpoint(
#             services.SERVICE_KYC_DETAIL_PENDING_LIST, False)
#         url = self.get_absolute_url(url)
#         return self.get(url, params=params)

#     def kycdetail_change_status(self, kyc_id, data):
#         url = self.get_service_endpoint(
#             services.SERVICE_KYC_DETAIL_STATUS_UPDATE, False)
#         url = self.get_absolute_url(url.format(kyc_id))
#         return self.patch(url, data=data)

#     def view_kyc_detail(self, user_id):
#         url = self.get_service_endpoint(
#             services.SERVICE_VIEW_KYC_DETAIL, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.get(url)


# class BankRepository(RestRepository):
#     def __init__(self, version):
#         super(BankRepository, self).__init__(version)
#         self.repository_url = settings.WALLET_REPOSITORY_ENDPOINT
#         self.endpoints = BROKER_ENDPOINTS

#     def create_bank_account(self, bank, user_id, taj_account_data):
#         url = self.get_service_endpoint(
#             services.SERVICE_BANK_ACCOUNT_CREATE, False)
#         url = self.get_absolute_url(url.format(bank, user_id))
#         return self.post(url, taj_account_data)

#     def link_bank_account(self, bank, user_id, taj_account_data):
#         url = self.get_service_endpoint(
#             services.SERVICE_BANK_ACCOUNT_LINK, False)
#         url = self.get_absolute_url(url.format(bank, user_id))
#         return self.post(url, taj_account_data)

#     def get_bank_account_transaction_listing(self, params, data):
#         url = self.get_service_endpoint(
#             services.SERVICE_BANK_ACCOUNT_TRANSACTION_LISTING, False)
#         url = self.get_absolute_url(url)
#         return self.get(url, params=params, data=data)

#     def get_bank_account_transaction_data(self, params):
#         url = self.get_service_endpoint(
#             services.SERVICE_BANK_ACCOUNT_TRANSACTION_DATA, False)
#         url = self.get_absolute_url(url)
#         return self.get(url, params=params)

#     def admin_update_user_bank(self, user_id, data):
#         url = self.get_service_endpoint(
#             services.SERVICE_ADMIN_UPDATE_USER_BANK, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.patch(url, data=data)
        
#     def admin_change_user_bank(self, user_id, data):
#         url = self.get_service_endpoint(
#             services.SERVICE_ADMIN_CHANGE_USER_BANK, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.post(url, data=data)
    
#     def all_bank_list(self):
#         url = self.get_service_endpoint(
#             services.SERVICE_BANK_LIST, False)
#         url = self.get_absolute_url(url)
#         return self.get(url)


# class PensionAccountRepository(RestRepository):
#     def __init__(self, version):
#         super(PensionAccountRepository, self).__init__(version)
#         self.repository_url = settings.WALLET_REPOSITORY_ENDPOINT
#         self.endpoints = BROKER_ENDPOINTS
    
#     def create_update_user_pension_account(self, user_id, pension_account_data):
#         url = self.get_service_endpoint(
#             services.SERVICE_USER_PENSION_ACCOUNT_CREATE_UPDATE, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.post(url, pension_account_data)

#     def user_pension_account_change_status(self, pension_id, data):
#         url = self.get_service_endpoint(
#             services.SERVICE_USER_PENSION_ACCOUNT_STATUS_UPDATE, False)
#         url = self.get_absolute_url(url.format(pension_id))
#         return self.patch(url, data=data)

#     def get_pension_account_all_list(self, params):
#         url = self.get_service_endpoint(
#             services.SERVICE_PENSION_ACCOUNT_ALL_LIST, False)
#         url = self.get_absolute_url(url)
#         return self.get(url, params=params)

#     def get_pension_provider_list(self, user_id, params):
#         url = self.get_service_endpoint(
#             services.SERVICE_PENSION_PROVIDER_LIST, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.get(url, params=params)
        
#     def get_user_pension_detail(self, user_id, params):
#         url = self.get_service_endpoint(
#             services.SERVICE_USER_PENSION_ACCOUNT_DETAIL, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.get(url, params=params)

#     def get_pension_account_pending_list(self, params):
#         url = self.get_service_endpoint(
#             services.SERVICE_PENSION_ACCOUNT_PENDING_LIST, False)
#         url = self.get_absolute_url(url)
#         return self.get(url, params=params)

#     def create_premium_pension_account(self, user_id, premium_pension_data):
#         url = self.get_service_endpoint(
#             services.SERVICE_CREATE_PREMIUM_PENSION_ACCOUNT, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.post(url, premium_pension_data)

#     def premium_account_change_status(self, account_id, data):
#         url = self.get_service_endpoint(
#             services.SERVICE_PREMIUM_ACCOUNT_STATUS_UPDATE, False)
#         url = self.get_absolute_url(url.format(account_id))
#         return self.patch(url, data=data)

#     def get_user_pension_account(self, params):
#         url = self.get_service_endpoint(
#             services.SERVICE_USER_PENSION_ACCOUNT, False)
#         url = self.get_absolute_url(url.format(params))
#         print(url)
#         return self.get(url)

# class PensionRepository(RestRepository):
#     def __init__(self, version):
#         super(PensionRepository, self).__init__(version)
#         self.repository_url = settings.WALLET_REPOSITORY_ENDPOINT
#         self.endpoints = BROKER_ENDPOINTS

#     def create_pension_account(self,provider, user_id, pension_data):
#         # import pdb; pdb.set_trace()
#         url = self.get_service_endpoint(
#             services.SERVICE_PENSION_ACCOUNT_CREATE, False)
#         url = self.get_absolute_url(url.format(provider, user_id))
#         return self.post(url, pension_data)


#     def create_pension_provider(self, pension_provider, user_id, provider_account_data):
#         url = self.get_service_endpoint(
#             services.SERVICE_PENSION_PROVIDER_CREATE, False)
#         url = self.get_absolute_url(url)
#         return self.post(url, provider_account_data)

#     def link_pension_account(self, user_id, pension_account_data):
#         url = self.get_service_endpoint(
#             services.SERVICE_PENSION_ACCOUNT_LINK, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.post(url, pension_account_data)


# class AirtimeRepository(RestRepository):
#     def __init__(self, version):
#         super(AirtimeRepository, self).__init__(version)
#         self.repository_url = settings.WALLET_REPOSITORY_ENDPOINT
#         self.endpoints = BROKER_ENDPOINTS

#     def get_network_all_lists(self):
#         url = self.get_service_endpoint(
#             services.SERVICE_AIRTIME_NETWORK_ALL_LIST, False)
#         url = self.get_absolute_url(url)
#         return self.get(url)

#     def purchase_airtime(self, user_id, data):
#         url = self.get_service_endpoint(
#             services.SERVICE_USER_PURCHASE_AIRTIME, False)
#         url = self.get_absolute_url(url.format(user_id))
#         return self.post(url, data)


# class BasicSettingsRepository(RestRepository):
#     def __init__(self, version):
#         super(BasicSettingsRepository, self).__init__(version)
#         self.repository_url = settings.WALLET_REPOSITORY_ENDPOINT
#         self.endpoints = BROKER_ENDPOINTS

#     def create_update_basic_settings(self, data):
#         url = self.get_service_endpoint(
#             services.SERVICE_BASIC_SETTINGS_CREATE_UPDATE, False)
#         url = self.get_absolute_url(url)
#         return self.post(url, data)

#     def create_update_bank_fee(self, data):
#         url = self.get_service_endpoint(
#             services.SERVICE_BANK_FEE_CREATE_UPDATE, False)
#         url = self.get_absolute_url(url)
#         return self.post(url, data)
    
#     def get_basic_setting_all_lists(self):
#         url = self.get_service_endpoint(
#             services.SERVICE_BASIC_SETTING_ALL_LIST, False)
#         url = self.get_absolute_url(url)
#         return self.get(url)
