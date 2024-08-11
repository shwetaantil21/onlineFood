from django.shortcuts import HttpResponse, render

# Create views here


def home(request):
    return render(request, "home.html")
