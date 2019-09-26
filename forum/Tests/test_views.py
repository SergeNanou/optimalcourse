from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from blog.models import *
from forum.models import *

# Create your tests here.
# test for ForumTest page  
class ForumTest(TestCase):
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
        p = Article.objects.create(titre='La vie de boss', 
                                   auteur='Adonis',
                                   contenu ='La vie est chic à Cergy'
                                    )
        publis = list(Article.objects.all().values())
        publish = publis[0]['photo']
        publish = '/media/'+publish
        contenu = publis[0]['contenu']
        text = contenu[0:225]
        titre = publis[0]['titre']
        response = self.client.post('/index/',{'publish':publish,
                                        'contenu':contenu, 
                                        'titre':titre,
                                        'text':text})
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
    def test_help_ent(self):
        # setup of text
        p = Quest_ans.objects.create(sujet_h='Test sur forum',
                                     message_h='Salut la team',
                                     email_h='affoumounanou@yahoo.fr',
                                     phone_h='07450232'
                                    )
        publish_h = list(Quest_ans.objects.all().order_by('-created_at_h').values())
        response_0 = self.client.get('/help_ent/',
                                        {'publish_h':publish_h})
        response = self.client.get('/help_ent/')
        self.assertEqual(response_0.status_code, 302)
