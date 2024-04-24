
from django.urls import path,include
app_name = 'api_v1'

urlpatterns = [
    path('auth/', include('users.api.urls.v1', namespace='users_auth')),
    path('broker/', include('broker.api.urls.v1', namespace='broker_auth')),
    path('payments/', include('payments.api.urls.v1', namespace='payments')),
]
