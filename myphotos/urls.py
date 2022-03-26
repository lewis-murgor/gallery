from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.images,name='images'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^image/(\d+)',views.image,name ='image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)