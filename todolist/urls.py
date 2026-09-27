from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/',views.indexView,name='index'),
]
