from django.shortcuts import render
from django.core.mail import mail_admins, send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# from .forms import ContactForm



class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, *args, **kwargs):
        context =  super(HomeView, self).get_context_data(*args, **kwargs)
        context['sit'] = 'sit'
        return context
    
    
    
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
