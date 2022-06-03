from django.shortcuts import render, redirect, reverse
from portfolio.models import ContactModel
from portfolio.forms import ContactForm
from django.contrib import messages

from django.conf import settings
from django.template.loader import render_to_string

from django.core.mail import EmailMessage


# from .forms import ContactForm


def home_view(request):
    context = {}
    title = None
    contact_form = ContactForm(request.POST or None)
    context['form'] = contact_form
    if request.POST and contact_form.is_valid():
        print("nothing")
        contact = contact_form.save()
        if title:
            title = contact.title
        template = render_to_string('email_template.html', {'name': contact.name, 'email':contact.email, "message": contact.text, 'title':title})
        subject = f"{contact.name} Contacted you for Query !"
        message = template
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['parthishere1234@gmail.com',]
        mail = EmailMessage(subject, message, email_from, recipient_list)
        mail.send()
        messages.success(request, "Sent Successfully")
        return redirect('profile:home')
    return render(request, "home.html", context)
    
# @login_required(login_url='accounts:login')
# def contact_us_view(request):
#     context = {}
#     contact_form = ContactForm(request.POST or None)
#     if contact_form.is_valid():
#         context['form'] = contact_form
#         email = request.user.email
#         print(request.user.email)
#         instance = contact_form.save()
#         instance.email = email
        
#         instance.save()
        
#         send_mail(
#         instance.title,
#         instance.text,
#         settings.EMAIL_HOST_USER,
#         ['parthishere1234@gmail.com'],
#         fail_silently=False,
#         )
        
#         return redirect('contact_us_congo')
        
#     context['form'] = contact_form
#     return render(request, 'contact-us.htm', context=context)
