from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Scottie heard about a cool new to-do app and
        # and Googled for the URL
        self.browser.get('http://localhost:8000')

        # He notices the page title and header say's 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is asked to add a to-do item immediately.

        # he types "Buy peacock feathers" into a text box (Scottie's hobby
        # is tying fly-fishing lures)

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting him to add another item. He
        # enters "Use peacock feathers to make a fly" (Scottie is very methodical)

        # The page updates again, and now shows both items on her list

        # Scottie wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.

        # He visits that URL - his to-do list is still there.

        # Satisfied, he goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
