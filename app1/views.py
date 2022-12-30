from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'a':'abcd'}
    return render(request,'jinja.html',context=d)

def jinja2(request):
    d={'abcd':'ABCD'}
    return render(request, 'jinja2.html',d)

def jinja12(request):
    d={'new':'in 2022 only two days are there please study well'}
    return render(request,'jinja12.html',d)

def one1(request):
    a={'newyear':'wish you happy new year good morning'}
    return render(request,'one1.html',a)