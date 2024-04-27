from selenium import webdriver
from .models import Skatepark
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time



class TestPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe')
    
    def tearDown(self):
        self.browser.close()
    
    def test_login_selenium(self):
        alert = self.browser.find_element_by_class_name('navbar-nav')
        self.assertEquals(alert.find_element_by_tag_name('a').text, 'Login')
        time.sleep(20)