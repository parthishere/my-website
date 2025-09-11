from django.shortcuts import render, redirect, reverse
from portfolio.models import ContactModel
from portfolio.forms import ContactForm
from django.contrib import messages

from django.conf import settings
from django.template.loader import render_to_string

from django.core.mail import EmailMessage

# def contact_form(request):
#     context = {}
#     title = None
#     contact_form = ContactForm(request.POST or None)
    
#     if request.POST and contact_form.is_valid():
#         contact = contact_form.save()
#         if title:
#             title = contact.title
#         template = render_to_string('app/email_template.html', {'name': contact.name, 'email':contact.email, "message": contact.message, 'title':title})
#         subject = f"{contact.name} Contacted you for Query !"
#         message = template
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = ['parthishere1234@gmail.com',]
#         mail = EmailMessage(subject, message, email_from, recipient_list)
#         mail.send()
#         messages.success(request, "Sent Successfully")
#         return redirect('')
#     return render(request, "home.html", context)