from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.shortcuts import reverse


# #-----------------------------------------------------------------------

class Progress(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    progress_char = models.CharField(max_length=100)

    class Meta():
        ordering = ['-id']

    def __str__(self):
        return self.name + ": " + str(self.progress)


class Image(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.pk

# #-----------------------------------------------------------------------


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    text = models.TextField()

    class Meta():
        ordering = ['-id']

    def __str__(self):
        return self.email

# #-----------------------------------------------------------------------


class Softwear(models.Model):
    softwear = models.CharField(max_length=100, blank=True, null=True)
    progress = models.ForeignKey(
        Progress, on_delete=models.SET_NULL, null=True)
    img = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta():
        ordering = ['-id']

    def __str__(self):
        return self.softwear

# -----------------------------------------------------------------------


class Project(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    imges = models.ManyToManyField(Image, null=True, blank=True)
    hosted_link = models.URLField()
    extra_description_link = models.URLField()
    github_link = models.URLField()
    progress = models.ForeignKey(
        Progress, on_delete=models.SET_NULL, null=True)
    tools = models.ManyToManyField(
        Softwear, related_name='sw_projects', blank=True)

    class Meta():
        ordering = ['-id']

    def __str__(self):
        return self.name

# -----------------------------------------------------------------------


class AdminModel(models.Model):
    """ User Profile Model """
    dob = models.DateField(auto_now_add=True)
    phone_no = models.IntegerField()
    softwears = models.ManyToManyField(Softwear)
    about = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    degree = models.CharField(max_length=100)
    age = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    cerificates = models.TextField(null=True, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    intrests = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        ''' Representation of instances '''
        return str(f"email:{self.user.email}  id: {self.pk}")


def progress_post_save_reciever(sender, instance, created, *args, **kwargs):
    if created:
        value = instance.progess


post_save.connect(progress_post_save_reciever, sender=Progress)
