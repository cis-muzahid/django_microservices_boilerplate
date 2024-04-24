
import random
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission
# from django.utils import timezone
# from django_countries.fields import CountryField
from .managers import CustomUserManager
from django.utils import timezone
# import datetime
# from datetime import datetime, timedelta
# from cities_light.models import Country
from datetime import datetime
# from phonenumber_field.modelfields import PhoneNumberField



GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]


# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class TimeStampedModel(models.Model):
    """TimeStampedModel model for created and modified date."""

    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        """Meta class."""

        abstract = True

class CustomUser(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """Using email instead of username."""

    PROVIDER = (
        ("Manual", "manual"),
        ("Google", "google"),
    )

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60, null=True, blank=True)
    # email = models.CharField(max_length=255, null=True, blank=True,
    #                          unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, verbose_name=_('groups'),
                                    blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission,
                                              verbose_name=_('user permissions'),
                                              blank=True,
                                              related_name='customuser_set')
    authentication_provider = models.CharField(max_length=20, choices=PROVIDER,
                                               default="Manual")
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        """Str method to return ContactInfo name."""
        return '{}- {}- {}'.format(self.email, self.username, self.id)

    def save(self, *args, **kwargs):
        if 'pbkdf2_sha256' not in self.password:
            self.set_password(self.password)

        return super(CustomUser, self).save(*args, **kwargs)


class UserOtherDetails(TimeStampedModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                related_name='details', null=True, blank=True)
    first_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(_('phone number'),
                             max_length=17, unique=True)
    # phone = PhoneNumberField(blank=True)
    is_phone_verified = models.BooleanField(default=False)
    address = models.CharField(('address'), max_length=500, blank=True,
                               null=True)
    is_two_factor_enabled = models.BooleanField(default=False)
    signals = models.IntegerField(blank=True, default=0)
    profile_picture = models.ImageField(_('User photograph'),
                                        upload_to=upload_to, null=True,
                                        blank=True)

    dob = models.DateField(_('Date Of Birth'), null=True)
    gender = models.CharField(_('Gender'), max_length=3,
                              choices=GENDER_CHOICES, null=True)
    # country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True,
    #                             null=True, default=224)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_is_active = models.BooleanField(default=False)
    otp_timestamp = models.DateTimeField(null=True, blank=True)
    # otp_attempts = models.IntegerField(default=0)  # Track OTP verification attempts
    connected_brokers = models.IntegerField(null=True, blank=True, default=0)
    time_zone = models.ForeignKey('TimeZone', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def _get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def _set_full_name(self, combined_name):
        self.first_name, self.last_name = combined_name.split(' ', 1)

    def generate_otp(self):
        # otp = random.randint(100000, 999999)
        otp = ''.join(random.choices('0123456789', k=6))
        print(otp)
        self.otp = otp
        # self.otp_timestamp = datetime.now().isoformat()
        self.otp_timestamp = timezone.now()
        self.save()
        return self.otp

    def verify_otp(self, otp):
        if self.otp:
            if int(self.otp) == int(otp):
                self.otp = None
                self.otp_timestamp = None
                self.save()
                return True
        return False

    full_name = property(_get_full_name)

    @property
    def get_gender(self):
        gender = None
        for g in GENDER_CHOICES:
            if g[0] == self.gender:
                gender = g[1]
                break
        return gender


class TimeZone(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    offset = models.CharField(max_length=10)

    def __str__(self):
        return self.name



class SubscriptionPlan(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=255)
    plan_type = models.CharField(max_length=100)
    plan_description = models.CharField(max_length=255)
    plan_monthly_cost = models.DecimalField(max_digits=10, decimal_places=2)
    plan_max_signals_monthly = models.IntegerField()
    plan_unlimited_trade_parameters = models.BooleanField(default=False)
    plan_unlimited_features = models.BooleanField(default=False)
    plan_max_brokers = models.IntegerField()
    plan_currency = models.CharField(max_length=3)  # Assuming currency codes are 3 characters long (e.g., USD, INR)

    def __str__(self):
        return self.plan_name


class SubscriptionInvoice(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    # company_id = models.IntegerField()  # Assuming this refers to the ID of the company model
    invoice_number = models.CharField(max_length=255, unique=True)
    invoice_date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)  # Assuming currency codes are 3 characters long (e.g., USD, INR)
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    payment_date = models.DateTimeField()
    bill_to_name = models.CharField(max_length=255)
    bill_to_address = models.CharField(max_length=255)
    bill_to_phone = models.CharField(max_length=20)
    bill_to_email = models.EmailField()

    def __str__(self):
        return f"Invoice #{self.invoice_number} for {self.user.username} - {self.plan.plan_name}"


class CompanyDetails(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    company_registration_no = models.CharField(max_length=255)
    company_website = models.URLField()
    company_logo = models.URLField()
    industry = models.CharField(max_length=255)
    legal_entity_type = models.CharField(max_length=255)
    tax_id_number = models.CharField(max_length=255)
    business_description = models.TextField()
    primary_contact_name = models.CharField(max_length=255)
    primary_contact_email = models.EmailField()
    primary_contact_phone = models.CharField(max_length=20)
    revenue = models.DecimalField(max_digits=15, decimal_places=2)
    profit = models.DecimalField(max_digits=15, decimal_places=2)
    assets = models.DecimalField(max_digits=15, decimal_places=2)
    liabilities = models.DecimalField(max_digits=15, decimal_places=2)
    social_media_profiles = models.TextField()
    operating_locations = models.TextField()
    legal_documents = models.TextField()

    def __str__(self):
        return self.company_name


class Newsletter(TimeStampedModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
