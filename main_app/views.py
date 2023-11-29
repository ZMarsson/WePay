from django.shortcuts import render
from users.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate


# Create your views here.
def home(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def service(request):
    return render(request,"services.html")


def contact(request):
    return render(request,"contact.html")


def how_it_works(request):
    return render(request,"how-it-works.html")


def blog(request):
    return render(request,"blog.html")


def blog_details(request):
    return render(request,"blog=details.html")


def faq(request):
    return render(request,"faq.html")


def terms_and_conditions(request):
    return render(request,"terms.html")


def privacy_policy(request):
    return render(request,"privacy-policy.html")


def legal(request):
    return render(request,'legal.html')


