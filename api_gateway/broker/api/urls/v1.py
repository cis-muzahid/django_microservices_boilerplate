from django.urls import path
from ..views import BrokerListView, BrokerCreateView,BrokerUpdateView,BrokerRetrieveView

app_name = 'api_broker_v1'

urlpatterns = [
    path('broker-list/', BrokerListView.as_view(),name="broker_list"),
    path('create/', BrokerCreateView.as_view(),
         name="create"),
    path('update/<int:pk>/', BrokerUpdateView.as_view(),
         name="update"),
    path('get/<int:pk>/', BrokerRetrieveView.as_view(),
         name="get")
]

