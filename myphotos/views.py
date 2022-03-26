from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.
def images(request):
    photos = Image.objects.all()

    return render(request, 'photos.html',{"photos":photos})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any name"
        return render(request, 'search.html',{"message":message})
