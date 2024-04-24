from django.contrib import admin
from users.models import (CustomUser, UserOtherDetails, SubscriptionPlan,
                          SubscriptionInvoice, Newsletter,TimeZone,CompanyDetails)


admin.site.register(CustomUser)
admin.site.register(UserOtherDetails)
admin.site.register(SubscriptionPlan)
admin.site.register(SubscriptionInvoice)
admin.site.register(Newsletter)
admin.site.register(TimeZone)