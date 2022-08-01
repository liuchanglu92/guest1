from django.contrib.auth.models import User
from django.test import TestCase
from django.http import  response
class LoginActionTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin','admin@mail,com','admin123')

    def tearDown(self):
        pass
    def test_add_admin(self):
        user = User.objects.get(username='admin')
        self.assertEqual(user.username,'admin')
        self.assertEqual(user.email,'admin@mail,com')

    def test_login_action_username_password_null(self):
        test_data = {'username':'','password':''}
        response = self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"username or password error",response.content)

    def test_login_action_username_password_error(self):
        test_date= {'username':'admin1','password':'123'}
        response = self.client.post('/login_action/',data=test_date)
        self.assertEqual(response.status_code,200)
        self.assertIn(b'username or password error',response.content)

    def test_login_success(self):
        test_data = {'username':'admin','password':'admin123456'}
        response = self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code,200)