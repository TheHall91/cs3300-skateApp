from django.db import models
from django.urls import reverse
# Create your models here.

class Skatepark(models.Model):

#List of choices for major value in database, human readable name
    DIFFICULTY = (
    ('1', 'Beginner'),
    ('2', 'Easy'),
    ('3', 'Medium'),
    ('4', 'Hard'),
    ('5', 'Extreme'),
)
    name = models.CharField(max_length=200)
    Location = models.CharField("Location:", max_length=200)
    difficulty = models.CharField(max_length=200, choices=DIFFICULTY, blank = False)

    def __str__(self):
        return self.name

#Returns the URL to access a particular instance of MyModelName.
#if you define this method then Django will automatically
# add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

class Review(models.Model): 
    title = models.CharField("Review Title:", max_length=200)
    review = models.CharField("Review:", max_length=400)
    park = models.ForeignKey(Skatepark, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title

#Returns the URL to access a particular instance of MyModelName.
#if you define this method then Django will automatically
# add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])