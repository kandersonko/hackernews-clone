from snapshottest.django import TestCase

from graphene.test import Client

from hackernews.schema import schema

from .models import Link


class APITestCase(TestCase):
    
    def setUp(self):
        self.client = Client(schema)
        Link.objects.create(url="https://www.example.com/1", description="Link 1")
        Link.objects.create(url="https://www.example.com/2", description="Link 2")
        Link.objects.create(url="https://www.example.com/3", description="Link 3")
        Link.objects.create(url="https://www.example.com/4", description="Link 4")

    def test_all_links_resolver(self):
        self.assertMatchSnapshot(self.client.execute('''
        { links { id, url, description } }
        '''))

    def test_links_first_resolver(self):
         self.assertMatchSnapshot(self.client.execute('''
        { links(first: 2) { id, url, description } }
        '''))

    def test_links_skip_resolver(self):
         self.assertMatchSnapshot(self.client.execute('''
        { links(skip: 2) { id, url, description } }
        '''))