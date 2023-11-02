from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def index(reqest):
    return render(reqest, "index.html")


def about(reqest):
    return render(reqest, "about.html")


def resume(request):
    return render(request, "resume.html")


def portfolio(request):
    return render(request, "portfolio.html")


def contact(request):
    return render(request, "contact.html")


def saveData(request):
    n = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            n = 'Data saved successfully '
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Email sending code here using Django's Email API
            send_mail(
                f'New Contact Form Submission - {subject}',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                'Surajthakur4808@gmail.com',
                ['Thakursuraj9340@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'contact.html', {'n': n})

    else:
        form = StudentForm()

    return render(request, 'contact.html')
