from django.test import TestCase
from model_bakery import baker
from posts.models import Post
from django.utils.formats import date_format
from http import HTTPStatus


class DetailPageTest(TestCase):
    def setUp(self) -> None:
        self.post = baker.make(Post)
     
    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())
        
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'posts/detail.html') 
        
    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())
        
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        formatted_date = date_format(self.post.created_at, "N j, Y, P")
        self.assertContains(response, formatted_date)