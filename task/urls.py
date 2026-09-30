from django.urls import path
import task
from task import views

urlpatterns = [
  path('',views.indexView,name='index'),
  path('edit/<int:task_id>',views.editView,name='edit'),
  path('delete/<int:task_id>',views.deleteView,name='delete'),
  path('toggle/<int:task_id>',views.toggleView,name='toggle'),
]