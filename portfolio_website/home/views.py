from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        send_mail(
                'New Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {desc}',
                'abhitayusharma42@gmail.com',  # Replace with your email address
                ['abhitayusharma42@gmail.com'],  # Replace with the recipient email address(es)
                fail_silently=False,
        )
        contact = Contact(name=name,email=email,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
