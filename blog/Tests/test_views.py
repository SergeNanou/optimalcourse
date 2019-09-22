from django.test import TestCase
from django.shortcuts import render
from blog.models import *


class BlogPageTestCase(TestCase):

    def test_post_blog(self):
        # setup for create user
        
        
        p = Article.objects.create(titre='La vie de boss', 
                                   auteur='Adonis',
                                   contenu ='La vie est chic à Cergy'
                                    )
        publish = list(Article.objects.all().order_by ('-date').values())
        publish = publish[0]
        publish['photo'] = '/media/'+publish['photo']
        response = self.client.get('/edit/',{'publish':publish})
        self.assertEqual(response.status_code, 200)