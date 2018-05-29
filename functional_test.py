import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(10)

	def tearDown(self):
		self.browser.quit()

	def test_creating_a_new_list(self):
		# Edith has heard about cool new online to-do app. She goes
		# to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header = self.browser.find_element_by_tag_name('h1')
		self.assertIn('To-Do', header.text)

		# She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item')

		# She types "Buy peacock feathers" into a test box (Edith's hobby
		# is tying fly-fishing lures)
		inputbox.send_keys("Buy peacock feathers")

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in the to-do list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		import time
		time.sleep(10)
		self.assertIn(
			'1: Buy peacock feathers',
			[row.text for row in rows]
		)

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)

		# The page updates again, and now shows both items on her list

		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some 
		# explanatory test to that effect
		self.fail('Finish the test!')

		# She visits the URL - her to-do list is still there.

		# Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main()

