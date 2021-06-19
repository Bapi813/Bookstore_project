from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class CustomUsertest(TestCase):
	def test_create_user(self):
		User = get_user_model()
		user=User.objects.create_user(
			username='Xenos',
			email='Xenso@email.com',
			password='bapi1234',)

		self.assertEqual(user.username, 'Xenos')
		self.assertEqual(user.email, 'Xenso@email.com')
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)


	def test_create_Superuser(self):
		User=get_user_model()
		admin_user= User.objects.create_superuser(
			username='superadmin',
			email='superadmin@email.com',
			password='bapi1234',
			)

		self.assertEqual(admin_user.username, 'superadmin')
		self.assertEqual(admin_user.email, 'superadmin@email.com')
		self.assertTrue(admin_user.is_active)
		self.assertTrue(admin_user.is_staff)
		self.assertTrue(admin_user.is_superuser)
