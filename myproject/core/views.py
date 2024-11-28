from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def sample_get_view(request):
    return HttpResponse("Hello World",content_type="text/plain")   

@csrf_exempt
def sample1(request):
    name=request.GET.get("name","Chanakya")
    return JsonResponse({"request":f"Hello {name}"})

@csrf_exempt
def sample2(request,name):
    return JsonResponse({"request":f"Hello {name}"})

@csrf_exempt
def sample3(request):
    body=json.loads(request.body)
    name=body.get("name",None)
    gender=body.get("gender","Male")
    return JsonResponse({"request":f"Hello {name} is a {gender} "})