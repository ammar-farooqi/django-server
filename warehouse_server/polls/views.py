from rest_framework.fields import REGEX_TYPE
from .serializers import MemantSerializer
from django.shortcuts import render
from .models import Memant
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
# Functions based api views

from django.http import HttpResponse, HttpResponse, JsonResponse, request
# Example without using Rest Framework utilities


def index(request):  # request is provided automatically when the function is called in urls file
    return HttpResponse("Hello, world. You're at the polls index." + request.method)


def hmlyl(request):
    return render(request, 'polls/hello.html')


def helloworld(request):
    return HttpResponse("I am hello world")


def detail(request, question_id):

    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


@api_view(['GET', 'POST'])
def Memant_list(request):
    if request.method == "GET":
        memants = Memant.objects.all()
        serialize = MemantSerializer(memants, many=True)
        return JsonResponse(serialize.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        memant = MemantSerializer(data=data)
        if memant.is_valid():
            memant.save()
            return JsonResponse(memant.data, status=201)

        return JsonResponse(memant.errors, status=400)


@csrf_exempt
def getOneMemant(request, pk):
    try:

        memant = Memant.objects.get(pk=pk)

    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serialize = MemantSerializer(memant)
        return JsonResponse(serialize.data, safe=False)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serialize = MemantSerializer(memant, data=data)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data, status=201)

        return JsonResponse(serialize.errors, status=400)

    elif request.method == "DELETE":
        memant.delete()
        return HttpResponse(status=200, content="done")

# Examples using REST FRAMEWORK


@api_view(['GET', 'POST'])
def Memant_list_rest(request):
    if request.method == "GET":
        memants = Memant.objects.all()
        serialize = MemantSerializer(memants, many=True)
        return Response(serialize.data)

    elif request.method == "POST":

        memant = MemantSerializer(data=request.data)
        if memant.is_valid():
            memant.save()
            return Response(memant.data, status=status.HTTP_201_CREATED)

        return Response(memant.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def getOneMemant_rest(request, pk):
    try:

        memant = Memant.objects.get(pk=pk)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialize = MemantSerializer(memant)
        return Response(serialize.data)

    elif request.method == "PUT":

        serialize = MemantSerializer(memant, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)

        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        memant.delete()
        return Response(status=status.HTTP_200_OK, content="done")
