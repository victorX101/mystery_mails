from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import EmailForm


# Create your views here.

def Index(request):
    if (request.method == 'POST'):
        form = EmailForm(request.POST)
        if form.is_valid():
            to = form.cleaned_data['to']
            subject = form.cleaned_data['subject']
            msg = form.cleaned_data['message']
            k = send_mail("[no-reply]" + subject,"Hi there,\nSomewhene wants to give you an anonymous message\n-------------------\n\n" + msg + "\n\n-------------------\nRegards\nMYSTERY MAILS SERVICES\n",settings.EMAIL_HOST_USER,[to],fail_silently=False)
            if(k == True):
                content = {
                    'msg': 'Thanks for Your Patience :)\nYour message has been deleivered successfully'
                }
                return render(request,'mmails\message.html',content)
            else:
                content = {
                    'msg' : 'Sorry an error occured :\ \n Please Try again'
                }
                return render(request,'mmails\message.html',content)
        else:
            form = form()
    else:
        form = EmailForm()
        content = {
         'form' : form,
        }
        return render(request,'mmails/index.html',content)


