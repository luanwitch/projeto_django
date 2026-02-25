from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore

def django_logo(request):
    return render(request, "core/logo.html")
