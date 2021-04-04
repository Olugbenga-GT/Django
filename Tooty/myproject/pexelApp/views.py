from django.shortcuts import render

# Create your views (or your functions here) here.

def sayHello(request):
    return render(request, "index.html")


