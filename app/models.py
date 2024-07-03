from django.db import models

# Create your models here.
class React(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    message = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

