# tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
# from ..models import TimeZone
from users.models import TimeZone

CustomUser = get_user_model()

class CustomUserTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email="test@example.com", password="test123")
        self.time_zone = TimeZone.objects.create(name="UTC", code="UTC", offset="UTC+0")

    def test_custom_user_creation(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("test123"))
        self.assertFalse(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertEqual(str(self.user), "test@example.com- None- 1")

    def test_time_zone_str(self):
        self.assertEqual(str(self.time_zone), "UTC")
