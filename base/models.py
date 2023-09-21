from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Image(models.Model):
    project = models.ForeignKey('Project', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name
