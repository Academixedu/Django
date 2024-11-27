from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

def sample_get_view(request):
    return HttpResponse("Hello World",content_type="text/plain")   

def sample1(request):
    return JsonResponse({"message":"Hello JSON"}) 

def sample2(request):
    return JsonResponse({"message":"Hello JSON"}) 

def sample_text_view(request):
    content = """
    Welcome to our Django app!

    we are Learning Django

    Thank you for visiting!
    """
    return HttpResponse(content, content_type="text/plain")

def new(request):
    content = """
    Welcome to our Django app!

    we are Learning Django

    Thank you for visiting!
    
    """
    return JsonResponse({"message": content})

