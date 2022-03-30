from django.test import TestCase
from .models import Post


class HogeTest(TestCase):
    def test_hoge(self):
        post = Post()
        self.assertIsNotNone(post.created_date)
        print('testです')
