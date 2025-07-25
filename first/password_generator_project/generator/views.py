from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    lst = list(range(6, 15))
    return render(request, "generator/home.html", {'lst': lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    special = request.GET.get('special')
    if uppercase:
        char += [chr(i) for i in range(65, 91)]
    if numbers:
        char += [chr(i) for i in range(48, 58)]
    if special:
        char += [chr(i) for i in range(33, 48)]
        char += [chr(i) for i in range(58, 65)]
        char += [chr(i) for i in range(91, 97)]
        char += [chr(i) for i in range(123, 127)]

    psw = ''
    for i in range(length):
        psw += random.choice(char)
    return render(request, "generator/password.html", {'password': psw})
