from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from .models import Skatepark
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time



class TestPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe')
        
        service = Service(executable_path='./chromedriver.exe')
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    
    def tearDown(self):
        self.browser.close()
    
    def test_login_selenium(self):
        alert = self.browser.find_element_by_class_name('navbar-nav')
        self.assertEquals(alert.find_element_by_tag_name('a').text, 'Login')
        time.sleep(20)