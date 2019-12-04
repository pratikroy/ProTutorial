from django.db import models

# Create your models here.
class HomePage(models.Model):
    topic_name = models.CharField(max_length=255, unique=True, blank=False)
    topic_image = models.ImageField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_modefication = models.DateTimeField(auto_now=True)
    text_of_motivation = models.TextField(blank=True)
    book_recommendation = models.ImageField()

    def __str__(self):
        return self.topic_name
