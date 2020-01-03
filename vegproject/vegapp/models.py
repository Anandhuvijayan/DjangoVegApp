from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_heading = models.CharField(max_length=100)
    blog_text = models.CharField(max_length=200)
    date = models.DateTimeField('date')
    blog_image = models.ImageField()


    def __str__(self):
        return self.blog_heading

class Responseform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MyForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=100)
    feedback = models.CharField(max_length=100)

    def __str__(self):
        return self.name
