# Generated by Django 5.0.4 on 2024-04-19 11:48

import django.db.models.deletion
import users.managers
import users.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('company_registration_no', models.CharField(max_length=255)),
                ('company_website', models.URLField()),
                ('company_logo', models.URLField()),
                ('industry', models.CharField(max_length=255)),
                ('legal_entity_type', models.CharField(max_length=255)),
                ('tax_id_number', models.CharField(max_length=255)),
                ('business_description', models.TextField()),
                ('primary_contact_name', models.CharField(max_length=255)),
                ('primary_contact_email', models.EmailField(max_length=254)),
                ('primary_contact_phone', models.CharField(max_length=20)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=15)),
                ('profit', models.DecimalField(decimal_places=2, max_digits=15)),
                ('assets', models.DecimalField(decimal_places=2, max_digits=15)),
                ('liabilities', models.DecimalField(decimal_places=2, max_digits=15)),
                ('social_media_profiles', models.TextField()),
                ('operating_locations', models.TextField()),
                ('legal_documents', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plan_name', models.CharField(max_length=255)),
                ('plan_type', models.CharField(max_length=100)),
                ('plan_description', models.CharField(max_length=255)),
                ('plan_monthly_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('plan_max_signals_monthly', models.IntegerField()),
                ('plan_unlimited_trade_parameters', models.BooleanField(default=False)),
                ('plan_unlimited_features', models.BooleanField(default=False)),
                ('plan_max_brokers', models.IntegerField()),
                ('plan_currency', models.CharField(max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeZone',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=20)),
                ('offset', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=60, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('authentication_provider', models.CharField(choices=[('Manual', 'manual'), ('Google', 'google')], default='Manual', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', users.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionInvoice',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_number', models.CharField(max_length=255, unique=True)),
                ('invoice_date', models.DateField()),
                ('due_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=3)),
                ('payment_method', models.CharField(max_length=100)),
                ('payment_status', models.CharField(max_length=100)),
                ('payment_date', models.DateTimeField()),
                ('bill_to_name', models.CharField(max_length=255)),
                ('bill_to_address', models.CharField(max_length=255)),
                ('bill_to_phone', models.CharField(max_length=20)),
                ('bill_to_email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.subscriptionplan')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserOtherDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, max_length=60, null=True)),
                ('phone', models.CharField(max_length=17, unique=True, verbose_name='phone number')),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='address')),
                ('is_two_factor_enabled', models.BooleanField(default=False)),
                ('signals', models.IntegerField(blank=True, default=0)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=users.models.upload_to, verbose_name='User photograph')),
                ('dob', models.DateField(null=True, verbose_name='Date Of Birth')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=3, null=True, verbose_name='Gender')),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('otp_is_active', models.BooleanField(default=False)),
                ('otp_timestamp', models.DateTimeField(blank=True, null=True)),
                ('connected_brokers', models.IntegerField(blank=True, default=0, null=True)),
                ('time_zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.timezone')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
