from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name': 'Shaik Allabakash'}
    return render(request,'loop.html',d)

 
