from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home_page.html", {})

def login_view(request, *args, **kwargs):
	return render(request, "login_page.html", {})