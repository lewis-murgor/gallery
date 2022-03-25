from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404

# Create your views here.
def images(request):

    return render(request, 'photos.html')
