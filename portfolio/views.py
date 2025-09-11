import os
from django.http import HttpResponse
import mimetypes
from wsgiref.util import FileWrapper
from django.shortcuts import render, redirect, reverse
from portfolio.models import ContactModel
from portfolio.forms import ContactForm
from django.contrib import messages

from django.conf import settings
from django.template.loader import render_to_string

from django.core.mail import EmailMessage

from .models import *
from .utils import get_all_projects, get_all_experiences, load_markdown_content


# from .forms import ContactForm
def another_home(request):
    context = {}
    
    # Get projects from both database and markdown files
    db_projects = Project.objects.all()
    md_projects = get_all_projects()
    md_experiences = get_all_experiences()
    
    software_skills = Softwear.objects.all()
    contact_form = ContactForm(request.POST or None)
    
    context['db_projects'] = db_projects
    context['md_projects'] = md_projects
    context['md_experiences'] = md_experiences
    context['software_skills'] = software_skills
    context['form'] = contact_form

    
    if request.POST and contact_form.is_valid():
        if(settings.EMAIL_ENABLE):
            print("nothing")
            contact = contact_form.save()
            template = render_to_string('email_template.html', {
                                        'name': contact.name, 'email': contact.email, "message": contact.text, 'title': contact.title if contact.title else None})
            subject = f"{contact.name} Contacted you for Query !"
            message = template
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['parthishere1234@gmail.com',]
            mail = EmailMessage(subject, message, email_from, recipient_list)
            mail.send()
            messages.success(request, "Mail Sent Successfully")
            return redirect('portfolio:a-home')
        else:
            messages.error(request, "Email is disabled, please manually send email to parthishere1234@gmail.com!")
            return redirect('portfolio:a-home')
    elif request.POST:
        messages.error(request, "Please complete the captcha verification to send your message.")
        return redirect('portfolio:a-home')
    return render(request, 'another_home.html', context)

def cmd_home(request):
    context = {}
    projects = Project.objects.all()
    Softwear.objects.all()
    contact_form = ContactForm(request.POST or None)
    context['form'] = contact_form

    if request.POST and contact_form.is_valid():
        print("nothing")
        contact = contact_form.save()
        template = render_to_string('email_template.html', {
                                    'name': contact.name, 'email': contact.email, "message": contact.text, 'title': contact.title if contact.title else None})
        subject = f"{contact.name} Contacted you for Query !"
        message = template
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['parthishere1234@gmail.com',]
        mail = EmailMessage(subject, message, email_from, recipient_list)
        mail.send()
        messages.success(request, "Mail Sent Successfully")
        return redirect('portfolio:a-home')
    return render(request, 'cmd.html', context)


def home_view(request):
    context = {}
    contact_form = ContactForm(request.POST or None)
    context['form'] = contact_form

    if request.POST and contact_form.is_valid():
        print("nothing")
        contact = contact_form.save()
        template = render_to_string('email_template.html', {
                                    'name': contact.name, 'email': contact.email, "message": contact.text, 'title': contact.title if contact.title else None})
        subject = f"{contact.name} Contacted you for Query !"
        message = template
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['parthishere1234@gmail.com',]
        mail = EmailMessage(subject, message, email_from, recipient_list)
        mail.send()
        messages.success(request, "Mail Sent Successfully")
        return redirect('portfolio:a-home')
    return render(request, "home.html", context)


def change_theme(request):
    return redirect('portfolio:home')


def change_another(request):
    return redirect('portfolio:a-home')


def modern_home(request):
    context = {}
    
    # Get projects from both database and markdown files
    db_projects = Project.objects.all()
    md_projects = get_all_projects()
    md_experiences = get_all_experiences()
    
    software_skills = Softwear.objects.all()
    contact_form = ContactForm(request.POST or None)
    
    context['db_projects'] = db_projects
    context['md_projects'] = md_projects
    context['md_experiences'] = md_experiences
    context['software_skills'] = software_skills
    context['form'] = contact_form

    if request.POST and contact_form.is_valid():
        contact = contact_form.save()
        template = render_to_string('email_template.html', {
                                    'name': contact.name, 'email': contact.email, "message": contact.text, 'title': contact.title if contact.title else None})
        subject = f"{contact.name} Contacted you for Query !"
        message = template
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['parthishere1234@gmail.com',]
        mail = EmailMessage(subject, message, email_from, recipient_list)
        mail.send()
        messages.success(request, "Mail Sent Successfully")
        return redirect('portfolio:modern-home')
    return render(request, 'modern_home.html', context)


def download_pdf(request):
    filename = 'portfolio/Parth_Thakkar.pdf'
    wrapper = FileWrapper(open(filename, 'rb'))
    response = HttpResponse(
        wrapper, content_type=mimetypes.guess_type(filename)[0])
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = "attachment; filename=" + filename
    return response


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
