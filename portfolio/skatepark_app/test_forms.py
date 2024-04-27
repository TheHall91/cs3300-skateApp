from django.test import TestCase
from .models import Skatepark
from .forms import SkateparkForm
class FormTest(TestCase):
    def test_is_invalid(self):
        form = SkateparkForm(data={"name": "Skate", "location": "Parker", "difficulty": "Easy", "rating": 2.2})
        self.assertTrue(form.is_valid())

    def test_too_many_decimal_points(self):
        form = SkateparkForm(data={"name": "Skate", "location": "Parker", "difficulty": "Easy", "rating": 2.212341234})
        self.assertFalse(form.is_valid())
    
    def test_no_data_given(self):
        form = SkateparkForm(data={})
        self.assertFalse(form.is_valid())

