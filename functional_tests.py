#!/usr/bin/env python

import unittest
from selenium import webdriver

class FunctionalTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_flask_in_browser_title(self):
        self.browser.get('http://localhost:5000')
        assert 'Flask' in self.browser.title

if __name__ == '__main__':
    unittest.main()
