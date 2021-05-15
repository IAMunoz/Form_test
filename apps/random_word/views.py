from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
    
    if request.method == "GET":
        counter = request.session.get('counter',0) + 1
        request.session['counter'] = counter
        random = get_random_string(length=14)
    context = {'random': random}
    return render(request,"random.html", context)

def generate(request):
    return redirect('/random_word')

def reset(request):
    request.session['counter'] = 0
    return redirect('/random_word')

