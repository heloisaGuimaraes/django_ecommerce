from django.http import HttpResponse
from django.shortcuts import render


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
    context = {
        "title": "Contact page",
        "content": "Welcome to contact page!"
    }
    return render (request, "contact/view.html", context)