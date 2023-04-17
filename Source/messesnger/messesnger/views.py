from django.http import HttpResponse
from django.shortcuts import render


def starting(request):
    return render(request, 'Homepage/Starting.html')