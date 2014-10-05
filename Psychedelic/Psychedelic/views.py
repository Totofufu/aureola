from django.shortcuts import render
from django.http import Http404,HttpResponseBadRequest,\
                    HttpResponseRedirect,HttpResponse


def loadIndex(request):
  return render(request, 'home.html')

def supporteePage(request):
  return render(request, 'supportee_profile.html')

def supporterPage(request):
  return render(request, 'supporter_profile.html')

def createSupportee(request):
  return render(request, 'create_supportee.html')

def createSupporter(request):
  return render(request, 'create_supporter.html')

def loginPage(request):
  return render(request, 'login.html')

def aboutPage(request):
  return render(request, 'about.html')