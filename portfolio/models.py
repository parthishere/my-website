from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.shortcuts import reverse


#-----------------------------------------------------------------------
    
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    image = models.ImageField(upload_to='/tag_images')
    
    class Meta():
        app_label = 'portfoilo'
        ordering = ['-id']
        
    def __str__(self):
        return self.tag
    
# #-----------------------------------------------------------------------
    
# class Progress(models.Model):
#     progress = models.CharField(max_length=100)
    
#     class Meta():
#         app_label = 'portfoilo'
#         ordering = ['-id']
        
#     def __str__(self):
#         return self.progress
    
# #-----------------------------------------------------------------------
    
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    text = models.TextField()
    
    class Meta():
        ordering = [ '-id' ]
        
    def __str__(self):
        return self.email

# #-----------------------------------------------------------------------

# class Softwear(models.Model):
#     softwear = models.CharField(max_length=100)
#     value = models.IntegerField(max_length=100)
    
#     class Meta():
#         app_label = 'portfoilo'
#         ordering = ['-id']
        
#     def __str__(self):
#         return self.softwear

#-----------------------------------------------------------------------

class Projects(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    img = models.ImageField(upload_to='projects')
    description = models.TextField()
    tools = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    class Meta():
        app_label = 'portfoilo'
        ordering = ['-id']
    
    def __str__(self):
        return self.name
    
#-----------------------------------------------------------------------

# class UserProfileModel(models.Model):
#     """ User Profile Model """
#     user            = models.ForeignKey(User, on_delete=models.CASCADE)
#     dob             = models.DateField(auto_now_add=True)
#     phone_no        = models.IntegerField()
#     softwear        = models.ManyToManyField(Softwear)
#     about           = models.TextField(max_length=500,null=True, blank=True)
#     image           = models.ImageField(upload_to='profiles/', null=True, blank=True)
#     degree          = models.CharField(max_length=100)
#     Age             = models.IntegerField(blank=False, null=False)
#     city            = models.CharField(max_length=50)
#     cerificates     = models.TextField(null=True, blank=True)
#     tags            = models.ManyToManyField(Tag, blank=True)
#     intrests        = models.CharField(max_length=100, null=True, blank=True)
  
#     class Meta:
#         app_label = 'portfoilo'
#         ordering = [ '-id' ]

#     def __str__(self):
#         ''' Representation of instances '''
#         return str(f"email:{self.user.email}  id: {self.pk}")





    



# def user_post_save_reciever(sender, instance, created, *args, **kwargs):
#     if created:
#         UserProfileModel.objects.get_or_create(user=instance)

# post_save.connect(user_post_save_reciever, sender=User)