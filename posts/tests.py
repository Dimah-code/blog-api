from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="testuser",
            email="test@gmail.com",
            password="secrete123",
        )
        cls.post = Post.objects.create(
            title='Post Title',
            body='Post Body',
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, 'Post Title')
        self.assertEqual(self.post.body, 'Post Body')
        self.assertEqual(str(self.post), 'Post Title')
        self.assertEqual(self.post.author.username, "testuser")


