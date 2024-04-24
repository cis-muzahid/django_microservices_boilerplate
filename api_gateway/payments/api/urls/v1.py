app_name = 'api_loans_v1'

from django.urls import path
from ..views import TransactionListView

urlpatterns = [
    path('payment/list/', TransactionListView.as_view(), name='payment_list'),

]
