from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect

from api.models import *
from api.serializers import *

class GetSuportees(APIView):
  
  def get(self, request, format = None):
    allS = Suportee.objects.all()
    serializer = SuporteeSerializer(allS, many = True)
    return Response(serializer.data)