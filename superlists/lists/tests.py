import re

from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve

from .views import home_page
from .models import Item


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        observed_html = re.sub(csrf_regex, '', response.content.decode())
        expected_html = render_to_string('home.html')

        self.assertEqual(observed_html, expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, '신규 작업 아이템')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

        # self.assertIn('신규 작업 아이템', response.content.decode())
        #
        # csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        # observed_html = re.sub(csrf_regex, '', response.content.decode())
        # expected_html = render_to_string(
        #     'home.html',
        #     {'new_item_text': '신규 작업 아이템'},
        # )
        # self.assertEqual(observed_html, expected_html)

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.save()

        second_itme = Item()
        second_itme.text = '두 번째 아이템'
        second_itme.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(second_saved_item.text, '두 번째 아이템')
