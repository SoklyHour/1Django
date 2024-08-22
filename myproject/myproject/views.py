from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello World! I am Home.")

def about(request):
    return HttpResponse("My about page.")