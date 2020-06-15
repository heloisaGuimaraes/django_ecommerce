from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    context = {
        "title" : "Main page",
        "content": "Welcome to main page!"
    }
    return render(request, "home_page.html", context)

def about_page (request):
    context = {
        "title": "About page",
        "content": "Welcome to about page!"
    }
    return render(request, "about/view.html", context)

def contact_page (request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact page",
        "content": "Welcome to contact page!", 
        "form": contact_form
    }
    
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        
    return render (request, "contact/view.html", context)