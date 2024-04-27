from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client
#test if user can create skatepark when logged in
class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user', email='email@e.com',  password='password')
    
    def test_correct_password(self):
        response = self.client.post('/login/', {'username': 'user', 'password': 'password'})
        self.assertEqual(response.status_code, 302)

    def test_incorrect_password(self):
        response = self.client.post('/login/', {'username': 'user', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 200)

    
    def test_user_must_be_logged_in(self):
        
        response = self.client.post('/login/', {'username': 'user', 'password': 'password'})
        #self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('create-skatepark'))
        self.assertEqual(response.status_code, 200)