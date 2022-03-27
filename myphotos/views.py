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

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})

def filter_location(request):
    if 'image' in request.GET and request.GET["image"]:
        location = request.GET.get("image")
        filtered_images = Image.filter_by_location(location)

        return render(request, 'location.html',{"pics": filtered_images})

    else:
        message = "You haven't searched for any location"
        return render(request, 'location.html',{"message":message})
