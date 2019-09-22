from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from blog.models import *



# test for LoginTest page  
class LogInTest(TestCase):
    # setup test
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret',
            'email': 'connect@yahoo.fr'}
        User.objects.create_user(**self.credentials)
    def test_register(self):
        # send register data
        response = self.client.post('/register/',
                                    self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
    def test_login(self):
        # send login data
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        
        
        response = self.client.post('/user_login/',
                                    self.credentials, follow=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        
        self.credentials_0 = {
            'username': 'testuse',
            'password': 'secret'}
        response_0 = self.client.post('/user_login/',
                                        self.credentials_0, follow=True)
        self.assertEqual(response_0.status_code, 200)
    def test_logout(self):
        # send login data
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        response = self.client.post('/user_login/',
                                    self.credentials, follow=True)
        # Log out
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('reception'))
        self.assertEqual(response.status_code, 200)
class loginTestCase(TestCase):
    def test_login_pge(self):
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)


