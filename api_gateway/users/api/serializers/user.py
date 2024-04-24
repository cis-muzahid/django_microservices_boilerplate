from rest_framework import serializers
from users.models import CustomUser, UserOtherDetails
from django.contrib.auth.hashers import check_password
# from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
# from .utils import send_and_return_otp, generate_otp
from django.utils import timezone
# from django.contrib.auth import authenticate, login
from api_gateway.services.repositories import broker, payments
# from phonenumber_field.serializerfields import PhoneNumberField


class UserOtherDetailSerializer(serializers.ModelSerializer):
    address = serializers.CharField(label='Address', required=False)
    # phone = serializers.CharField(label='Phone No.', required=False)
    # phone = PhoneNumberField()
    first_name = serializers.CharField(label='First Name', required=False)
    last_name = serializers.CharField(label='Last Name', required=False)
    gender = serializers.CharField(label='Last Name', required=False)
    dob = serializers.DateField(required=False)
    # country = serializers.IntegerField(label='Country', required=True)

    class Meta:
        model = UserOtherDetails
        fields = ("address", "phone", "first_name", "last_name", "dob",
                  "gender",'time_zone')


    # def validate_country(self, value):
    #     if not Country.objects.filter(id=value).exists():
    #         raise serializers.ValidationError("Invalid Country")
    #     country = Country.objects.get(id=value)
    #     return country

class RegisterUserSerializer(serializers.ModelSerializer):
    """
    Serializer class for user registration.

    This serializer is used for registering a new user in the database.

    Attributes:
        Meta: Specifies the model and fields to include/exclude.
    """

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'confirm_email', 'confirm_password',
                  'username', 'user_other_detail')
    username = serializers.CharField(label='Username', required=True)
    # last_name = serializers.CharField(label='Last Name', required=True)
    # email = serializers.CharField(label='Email', required=False)
    email = serializers.EmailField(label='Email', required=False)
    password = serializers.CharField(label='Password', required=True)
    # phone = serializers.CharField(label='Phone No.', required=True)
    # dial_code = serializers.CharField(label='Dial Code', required=True)
    user_other_detail = UserOtherDetailSerializer()
    confirm_email = serializers.CharField(label='Confirm Email',
                                          required=False)
    confirm_password = serializers.CharField(label='Confirm Password',
                                             required=True)
    # captcha_value = serializers.CharField(label='Captcha Value', required=True)

    def validate_email(self, value):
        if value:
            if CustomUser.objects.filter(email=value):
                raise serializers.ValidationError("email already used")
        return value

    def validate(self, data):
        password = data.get('password', None)
        confirm_password = data.get('confirm_password', None)
        email = data.get('email')
        confirm_email = data.get('confirm_email')

        if password != confirm_password:
            raise serializers.ValidationError("password and confirm_password"
                                              "does not match")
        if email:
            if email != confirm_email:
                raise serializers.ValidationError("Email and Confirm email"
                                                  " does not match")
        return data

    def create(self, validated_data):
        """
        Create and return a new user instance.

        Args:
            validated_data (dict): Validated user data.

        Returns:
            CustomUser: The newly created user instance.
        """
        try:
            if validated_data.get('confirm_email'):
                validated_data.pop('confirm_email')
            validated_data.pop('confirm_password')
            
            user_other_detail = validated_data.pop('user_other_detail')
            # user_other_detail = validated_data.pop('time_zone')
            print(validated_data, "VALIDATED")
            user = super().create(validated_data)
            user.set_password(validated_data['password'])
            user.is_active = True
            user.save()
            other_detail = UserOtherDetails.objects.create(user=user, **user_other_detail)
            otp = other_detail.generate_otp()
            print(otp)
            # otp_timestamp = timezone.now()
            # other_detail.otp_timestamp = otp_timestamp.isoformat()
            other_detail.dob = user.details.dob.isoformat()
            other_detail.save()
            validated_data.pop('password')
            self.broadcast_user_create(validated_data)
            return user
        except Exception as excp:
            # users_logger.info(f"{timezone.now()} => {excp}")
            print(excp)
            raise serializers.ValidationError(
                {'status': 'failed',
                 'data': None,
                 'message': "Failed to create account"})


    # -----------for test cases--------------
    # def create(self, validated_data):
    #     """
    #         Override the default create method to handle additional logic for user creation,
    #         especially for test cases.

    #         Args:
    #             validated_data (dict): Validated user data.

    #         Returns:
    #             CustomUser: The newly created user instance.
    #     """
    #     try:
    #         if validated_data.get('confirm_email'):
    #             validated_data.pop('confirm_email')
    #         validated_data.pop('confirm_password')
            
    #         user_other_detail = validated_data.pop('user_other_detail')
    #         user = super().create(validated_data)
    #         user.set_password(validated_data['password'])
    #         user.is_active = True
    #         user.save()
    #         other_detail = UserOtherDetails.objects.create(user=user, **user_other_detail)
    #         otp = other_detail.generate_otp()
    #         other_detail.dob = user.details.dob.isoformat()
    #         other_detail.save()
    #         validated_data.pop('password')
    #         print("Before broadcasting:", validated_data)
    #         if user.username == "nony":  
    #             self.broadcast_user_create(validated_data)
            
    #         return user
    #     except Exception as excp:
    #         print(excp)
    #         raise serializers.ValidationError(
    #             {'status': 'failed',
    #             'data': None,
    #             'message': "Failed to create account"})


    def broadcast_user_create(self, instance):
        # instance.pop("otp_timestamp")
        # data = instance.toDict()
        data = instance
        # data['otp_timestamp'] = data['otp_timestamp'].isoformat()
        # data['dob'] = data['dob'].isoformat()
        broker_repository = broker.BrokerRepository('v1')
        response = broker_repository.create_new_user(data)
        payment_repository = payments.PaymentRepository('v1')
        response = payment_repository.create_new_user(data)
        # account_create_update(data)
        # breakpoint()
        return response
        # return data


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer class for user authentication.

    This serializer is used for authenticating users based on email and password.

    Attributes:
        Meta: Specifies the model and fields to include.
    """

    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        """
        Validate user credentials and generate access and refresh tokens.

        Args:
            attrs (dict): Input attributes containing email and password.

        Returns:
            dict: Validated attributes containing access and refresh tokens.
        """
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = CustomUser.objects.filter(email=email).first()

        if not user:
            raise serializers.ValidationError(
                'No user found with the provided email, try again')

        if not check_password(password, user.password):
            raise serializers.ValidationError('Invalid credentials, try again')

        if not user.is_active:
            raise serializers.ValidationError(
                'Account disabled, contact admin')

        if not user.is_email_verified:
            user.details.generate_otp()
            raise serializers.ValidationError('Please verify your email')

        refresh = RefreshToken.for_user(user)
        attrs['access'] = str(refresh.access_token)
        attrs['refresh'] = str(refresh)
        attrs.pop("email")
        attrs.pop("password")
        return attrs


class VerifyOtpSerializer(serializers.Serializer):
    """
    Serializer for verifying OTP for email verification.

    Attributes:
        email (EmailField): The email of the user.
        otp (IntegerField): The OTP entered by the user.

    Methods:
        validate(attrs): Validates the email and OTP entered by the user.
            Args:
                attrs (dict): The attributes to be validated.
            Returns:
                dict: The validated data.
            Raises:
                ValidationError: If the OTP is incorrect.
    """
    email = serializers.EmailField()
    otp = serializers.IntegerField()

    def validate(self, attrs):

        email = attrs['email']
        otp = attrs['otp']
        user = CustomUser.objects.filter(email=email).first()
        if not user.details.verify_otp(otp):
            raise serializers.ValidationError("Wrong Otp please try again")
        user.is_email_verified = True
        user.save()
        validated_data = super().validate(attrs)
        return validated_data


class LogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        print(self.token)
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
            # self.token.blacklist()
        except TokenError:
            raise serializers.ValidationError(
                {"refresh": ['Token is expired or invalid']})


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'id')


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(label='Email', required=True)

    def validate(self, data):
        email = data.get('email', None)

        if email:
            if not CustomUser.objects.filter(email=email):
                raise serializers.ValidationError(
                    """Oops, this email does not exist on our records.
                        Please try again or Sign Up.""")
        return data


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(label='Email', required=True)
    otp = serializers.IntegerField(label='Otp', required=True)
    new_password = serializers.CharField(label='Password', required=True)
    confirm_new_password = serializers.CharField(label='Confirm Password',
                                                 required=True)

    def validate_email(self, email):
        if not CustomUser.objects.filter(email=email):
            raise serializers.ValidationError("Invalid email")
        return email

    def validate(self, data):
        new_password = data.get('new_password')
        confirm_new_password = data.get('confirm_new_password')
        if new_password != confirm_new_password:
            raise serializers.ValidationError("Password and confirm password "
                                              "does not match.")
        return data

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_email_verified', 'authentication_provider')