from django.shortcuts import render

# Create your views(or your functions) here.

def display_html(request):
    context = {
        "message": "This shit is fucked up!!!"
    }
    return render(request, "index.html", context)


def call_mom(request):
    context = {
        "message": "Hey Momma, I'm feeling a little inebriated"
    }
    return render(request, "index.html", context)