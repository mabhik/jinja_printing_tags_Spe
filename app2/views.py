from django.shortcuts import render

# Create your views here.
def jinjaap21(request):
    a={'abhi':'ABHI'}
    return render(request, 'jinjaap21.html',context=a)