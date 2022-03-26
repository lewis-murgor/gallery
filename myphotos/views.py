from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.
def images(request):
    photos = Image.objects.all()

    return render(request, 'photos.html',{"photos":photos})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
