from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile
from .factories import CustomUserFactory, ProfileFactory

User = get_user_model()


class CustomUserTests(TestCase):
    """
    Test cases for CustomUser model.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.user = CustomUserFactory()

    def test_create_user(self):
        """
        Test creating a new user.
        """
        self.assertTrue(isinstance(self.user, User))
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_admin)
        self.assertFalse(self.user.is_superuser)


class ProfileTests(TestCase):
    """
    Test cases for Profile model.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.profile = ProfileFactory()

    def test_profile_creation(self):
        """
        Test that a profile is created for a new user.
        """
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertTrue(isinstance(self.profile.user, User))

    def test_profile_str(self):
        """
        Test the string representation of the profile.
        """
        self.assertEqual(str(self.profile), f"{self.profile.user.username}'s profile")

    def test_get_profile_image_url(self):
        """
        Test the profile image URL method.
        """
        self.assertEqual(
            self.profile.get_profile_image_url(), "/static/images/default_profile.png"
        )
