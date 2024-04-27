from django.test import TestCase
from .models import Skater, Skatepark
from django.contrib.auth import get_user_model
# Create your tests here.



class TheTestClass(TestCase):
    # Set up
    def setUp(self):
       Skatepark.objects.create(name='Woodland Park Skatepark', location='Woodland Park, CO', rating=4.2)
       Skater.objects.create(username='testuser')
       
    def test_does_home_page_load(self):
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 404)

    def test_is_user_created(self):
        skater = Skater.objects.filter(username='testuser')
        self.assertTrue(skater.exists())

    def test_leave_difficulty_empty(self):
        skatepark = Skatepark.objects.filter(name='Woodland Park Skatepark')
        self.assertEqual(skatepark.name, "Woodland Park Skatepark")
        
    def test_name_set_correctly(self):
        skatepark = Skatepark.objects.get(name='Woodland Park Skatepark')
        self.assertEqual(skatepark.name, "Woodland Park Skatepark")