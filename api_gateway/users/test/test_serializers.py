# tests.py
from django.test import TestCase
from users.api.serializers.user import RegisterUserSerializer
from users.models import TimeZone,CustomUser,UserOtherDetails


class RegisterUserSerializerTestCase(TestCase):

    def setUp(self):
        self.time_zone = TimeZone.objects.create(id=1, name='UTC', code='UTC', offset='UTC+0')
        self.valid_data = {
            'email': 'test@example.com',
            'password': 'test123',
            'confirm_password': 'test123',
            'confirm_email': 'test@example.com',
            'username': 'testuser',
            'user_other_detail': {
                'first_name': 'John',
                'last_name': 'Doe',
                'phone': '1234567890',
                'dob': '1990-01-01',
                'gender': 'M',
                'time_zone': self.time_zone.id  
            }
        }       

        self.invalid_data_password = {
            'email': 'test@example.com',
            'confirm_email': 'test@example.com',
            'password': 'test123',
            'confirm_password': 'test1234',
            'username': 'testuser',
            'user_other_detail': {
                'first_name': 'John',
                'last_name': 'Doe',
                'phone': '1234567890',
                'dob': '1990-01-01',
                'gender': 'M',
                'time_zone': self.time_zone.id
            }
        }

        self.invalid_data_email = {
            'email': 'test@example.com',
            'password': 'test123',
            'confirm_password': 'test123',
            'username': 'testuser',
            'confirm_email': 'test@example.com',
            'user_other_detail': {
                'first_name': 'John',
                'last_name': 'Doe',
                'phone': '1234567890',
                'dob': '1990-01-01',
                'gender': 'M',
                'time_zone': self.time_zone.id
            }
        }

    def test_valid_serializer(self):
        serializer = RegisterUserSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, self.valid_data['email'])
        self.assertEqual(user.username, self.valid_data['username'])

    def test_invalid_password(self):
        serializer = RegisterUserSerializer(data=self.invalid_data_password)
        is_valid = serializer.is_valid()
        self.assertFalse(is_valid)
        for data in serializer.errors['non_field_errors']:
            self.assertIn('password and confirm_password does not match', data)


    def test_invalid_email_confirmation(self):
        
        serializer = RegisterUserSerializer(data=self.invalid_data_email)
        self.assertFalse(serializer.is_valid())
        self.assertIn('Email and Confirm email does not match', serializer.errors['non_field_errors'])

    def test_email_already_used(self):
        CustomUser.objects.create(email='test@example.com', password='test123')
        serializer = RegisterUserSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email already used', serializer.errors['email'][0])