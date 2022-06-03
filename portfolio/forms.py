from django import forms

from .models import ContactModel

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'title', 'text']
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
 
        self.fields['email'].lable='Enter Email'
        

        self.fields['name'].lable='Enter Name'
        

        self.fields['title'].lable='Enter Title'
        self.fields['title'].required=False
        
        self.fields['text'].label = "Enter Message"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form form-control'