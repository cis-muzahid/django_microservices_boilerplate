from django.contrib.auth import get_user_model
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions
from rest_framework.exceptions import APIException
from django.conf import settings


class PrivateTokenAccessPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = _('You dont have permission to perform this action!')

    def has_permission(self, request, view):
        '''
        Returns True if the user for the given HttpRequest
        has permission to view at least one page in the admin
        site. Defaults to requiring both User.is_active
        and User.is_staff to be True.
        '''
        _ = self.message
        if request.user.is_anonymous or request.user.is_appuser or not request.user.is_active:
            return False
        return True


class PublicTokenAccessPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = _('You dont have permission to perform this action.')

    def has_permission(self, request, view):
        '''
        Returns True if the user for the given HttpRequest
        has permission to view at least one page in the admin
        site. Defaults to requiring both User.is_active
        and User.is_staff to be True.
        '''
        _ = self.message
        if request.user.is_anonymous or not request.user.is_active:
            return False
        return True


class PublicPrivateTokenAccessPermission(permissions.BasePermission):
    """
    Custom permission to all the users of an object to edit it.
    """
    message = _('Public Private Token Access Permission violated')

    def has_permission(self, request, view):
        '''
        Returns True if the user for the given HttpRequest
        has permission to view at least one page in the admin
        site. Defaults to requiring both User.is_active
        and User.is_staff to be True.
        '''
        _ = self.message
        if request.user.is_anonymous:
            return False
        return True



class StaffTokenAccessPermission(permissions.BasePermission):

    message = _('You dont have permission to perform this action!')

    def has_permission(self, request, view):
        '''
        Returns True if the user for the given HttpRequest
        has permission to view at least one page in the admin
        site. Defaults to requiring both User.is_active
        and User.is_staff to be True.
        '''
        _ = self.message
        if request.user.is_anonymous or not request.user.is_staff or not request.user.is_active:
            return False
        return True


class AdminCashierWithdrawalPermission(permissions.BasePermission):
    message = _('You do not have permission to perform this action!')

    def has_permission(self, request, view):
        if request.user.is_anonymous or not request.user.is_active:
            return False

        # Check for admin, cashier, or withdrawal approver roles
        return request.user.is_staff or request.user.is_cashier or request.user.is_withdrawal_approver or request.user.is_senior_cashier

class NotCashierException(APIException):
    status_code = 112
    default_detail = _('Cashier profile is deactivated.')
    default_code = 'cashier_deactivated'
    
class NotWithdrawalApproverException(APIException):
    status_code = 112
    default_detail = _('Withdrawal approver profile is deactivated.')
    default_code = 'withdrawal_approver_deactivated'

class NotAgentException(APIException):
    status_code = 112
    default_detail = _('Agent profile is deactivated.')
    default_code = 'agent_deactivated'


class CashierAccessPermission(permissions.BasePermission):
    message = _('Cashier profile is deactivated.')
    def has_permission(self, request, view):
        '''
        Returns True if the user for the given HttpRequest
        has permission to view at least one page in the admin
        site. Defaults to requiring both User.is_active
        and User.is_staff to be True.
        '''
        _ = self.message
        if request.user.is_anonymous or not request.user.is_cashier:
            raise NotCashierException
        return True

class WithdrawalApproverAccessPermission(permissions.BasePermission):
    message = _('Cashier profile is deactivated.')
    def has_permission(self, request, view):
        '''
        Returns True if the user for the given HttpRequest
        has permission to view at least one page in the admin
        site. Defaults to requiring both User.is_active
        and User.is_staff to be True.
        '''
        _ = self.message
        if request.user.is_anonymous or not request.user.is_withdrawal_approver:
            raise NotWithdrawalApproverException
        return True

class AgentAccessPermission(permissions.BasePermission):

    message = _('Agent profile is deactivated.')

    def has_permission(self, request, view):
        '''
        Returns True if the user for the given HttpRequest
        has permission to view at least one page in the admin
        site. Defaults to requiring both User.is_active
        and User.is_staff to be True.
        '''
        _ = self.message
        if request.user.is_anonymous or not request.user.is_agent:
            raise NotAgentException
        return True


class UssdIpPermission(permissions.BasePermission):

    message = _('IP not Allowed.')

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def has_permission(self, request, view):
        '''
        Returns True if the user for the given HttpRequest
        has permission to view at least one page in the admin
        site. Defaults to requiring both User.is_active
        and User.is_staff to be True.
        '''
        _ = self.message
        ip = self.get_client_ip(request)
        if ip in settings.EWALLMOB_USSD_IP or '*' in settings.EWALLMOB_USSD_IP:
            return True
        return False


class DeactivatedUserAccessPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = _('Your account has been suspended, contact us to reactivate it...')

    def has_permission(self, request, view):
        '''
        Returns True if the user for the given HttpRequest
        has permission to view at least one page in the admin
        site. Defaults to requiring both User.user_active to be True.
        '''
        _ = self.message
        if not request.user.user_active:
            return False
        return True

# `class UssdIpPermission(permissions.BasePermission):

#     message = _('IP not Allowed.')

#     def get_client_ip(self, request):
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         return ip

#     def has_permission(self, request, view):
#         '''
#         Returns True if the user for the given HttpRequest
#         has permission to view at least one page in the admin
#         site. Defaults to requiring both User.is_active
#         and User.is_staff to be True.
#         '''
#         _ = self.message
#         ip = self.get_client_ip(request)
#         if settings.EWALLMOB_USSD_IP == ip:
#             return True
#         return False`