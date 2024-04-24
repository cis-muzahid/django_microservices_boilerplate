from rest_framework import generics
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from api_gateway.core.views.services import ServiceGetAPIView, ServicePostAPIView, ServicePutAPIView, ServicePatchAPIView
from api_gateway.core.permissions import PrivateTokenAccessPermission, StaffTokenAccessPermission, PublicTokenAccessPermission, AgentAccessPermission, PublicPrivateTokenAccessPermission, DeactivatedUserAccessPermission
from api_gateway.services.repositories import broker
from rest_framework.permissions import IsAuthenticated
from users.permissions import RefreshTokenPermission
# from app.models import SiteConfig


class BrokerListView(ServiceGetAPIView):
    api_verison = 'v1'
    repository_class = broker.BrokerRepository
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated, RefreshTokenPermission]

    def call_service(self, request, *args, **kwargs):
        return self.request.repository.broker_list(
            self.request.user.pk, self.request.data, self.request.headers)


class BrokerCreateView(ServicePostAPIView):
    api_verison = 'v1'
    repository_class = broker.BrokerRepository
    permission_classes = [IsAuthenticated, RefreshTokenPermission]

    def call_service(self, request, *args, **kwargs):
        # breakpoint()
        return self.request.repository.broker_create(
            self.request.user.pk, self.request.data, self.request.headers)


class BrokerRetrieveView(ServiceGetAPIView):
    api_verison = 'v1'
    repository_class = broker.BrokerRepository
    permission_classes = [IsAuthenticated, RefreshTokenPermission]

    def call_service(self, request, *args, **kwargs):
        return self.request.repository.broker_retrieve(
            self.kwargs.get('pk'), self.request.headers)
            # self.request.user.pk)


class BrokerUpdateView(ServicePutAPIView):
    api_verison = 'v1'
    repository_class = broker.BrokerRepository
    permission_classes = [IsAuthenticated, RefreshTokenPermission]

    def call_service(self, request, *args, **kwargs):
        return self.request.repository.broker_update(
            self.kwargs.get('pk'), self.request.data, self.request.headers)


# class BrokerDeleteView(ServicePostAPIView):
#     api_verison = 'v1'
#     repository_class = broker.BrokerRepository
#     # permission_classes = (PrivateTokenAccessPermission,)

#     def call_service(self, request, *args, **kwargs):
#         # breakpoint()
#         return self.request.repository.broker_delete(
#             self.request.user.pk, self.request.data)