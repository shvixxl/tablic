from django.test import TestCase

from .models import User


class UserModelTest(TestCase):
    """Tests for Custom User model"""

    def test_user_fields(self):
        """Test Custom User fields"""
        user = User.objects.create(
            username="username",
            email="email@mail.com",
            password="qwerty",
        )

        self.assertEqual(user.username, 'username')
        self.assertEqual(user.email, 'email@mail.com')
