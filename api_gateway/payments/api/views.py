from api_gateway.core.views.services import ServiceGetAPIView,ServicePostAPIView, ServicePatchAPIView
from api_gateway.core.permissions import PrivateTokenAccessPermission
from api_gateway.services.repositories import payments
from rest_framework.permissions import IsAuthenticated
from users.permissions import RefreshTokenPermission

class TransactionListView(ServiceGetAPIView):
    api_verison = 'v1'
    repository_class = payments.PaymentRepository
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated, RefreshTokenPermission]

    def call_service(self, request, *args, **kwargs):
        return self.request.repository.payment_list(
            self.request.user.pk, self.request.data, self.request.headers)

