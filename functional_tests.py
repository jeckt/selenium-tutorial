#!/usr/bin/env python

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:5000')

assert 'Flask' in browser.title

browser.quit()
