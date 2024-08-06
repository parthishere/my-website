from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.shortcuts import reverse





class Image(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.pk


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    text = models.TextField()

    class Meta():
        ordering = ['-id']

    def __str__(self):
        return self.email



class Skills(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    percent = models.IntegerField()

    class Meta():
        ordering = ['-id']

    def __str__(self):
        return self.name



class Project(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    thumbnail = models.ForeignKey(
        Image, on_delete=models.SET_NULL, null=True, blank=True, related_name="projects_tumb")
    more_imges = models.ManyToManyField(
        Image, null=True, blank=True, related_name="projects_sub_img")
    hosted_link = models.URLField()
    extra_description_link = models.URLField()
    github_link = models.URLField()
    
    small_project = models.BooleanField(default=False)

    class Meta():
        ordering = ['-id']

    def __str__(self):
        return self.name




class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials')
    
# -----------------------------------------------------------------------



class About(models.Model):

    description = models.TextField()
    dob = models.DateField(auto_now_add=True)
    website = models.URLField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    about = models.TextField()
    
    project_worked_on = models.IntegerField()
    skill = models.ManyToManyField(Skills)
    

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


