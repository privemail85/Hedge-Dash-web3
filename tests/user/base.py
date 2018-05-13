from django.test import TestCase
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress


class UserBaseTests(TestCase):
    alice = None
    bob = None
    carmen = None

    def setUp(self):
        # Create sample users
        for idx, username in enumerate(['alice', 'bob', 'carmen']):
            user = User.objects.create_user(
                username=username, 
                email='%s@example.com' % username, 
                password='s3cr3t',
            )

            # Update phone number
            user.profile.phone_country_code = '1'
            user.profile.phone_number = '%s' % idx * 8
            user.profile.save()

            # Set email address as verified
            EmailAddress.objects.filter(user=user).update(verified=True)

            setattr(self, username, user)
