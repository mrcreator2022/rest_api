from django.shortcuts import render
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view(['GET'])
# def hello_word(request):
#     return Response({'msg':'hello world'})

# @api_view(['POST'])
# def hello_word(request):
#     if request.method == "POST":
#        print(request.data)
#        return Response({'msg':'hello world post req'})


@api_view(['GET','POST'])
def hello_word(request):
    if request.method == "GET":
      return Response({'msg':'hello world Get Method'})

    if request.method == "POST":
      print('request.data')
      return Response({'msg':'hello world Post Method','data':request.data})