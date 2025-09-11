from django import forms
from captcha.fields import CaptchaField

from .models import ContactModel

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'title', 'text']
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
 
        self.fields['email'].label='Enter Email'
        self.fields['name'].label='Enter Name'
        self.fields['title'].label='Enter Title'
        self.fields['title'].required=False
        self.fields['text'].label = "Enter Message"
        
        for visible in self.visible_fields():
            if visible.name != 'captcha':
                visible.field.widget.attrs['class'] = 'form form-control'