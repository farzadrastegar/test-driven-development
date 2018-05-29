from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_uses_home_template(self):
		request = HttpRequest()

		response = home_page(request)

		expected_content = render_to_string('home.html')
		self.assertEqual(response.content.decode('utf8'), expected_content)

	def test_home_page_can_store_post_request(self):
		post_str = 'new item'
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = post_str

		response = home_page(request)
		
		expected_content = render_to_string(
			'home.html',
			{'new_item_text': post_str}
		)
		self.assertEqual(response.content.decode('utf8'), expected_content)


