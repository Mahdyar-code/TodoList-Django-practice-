from django.shortcuts import render
import task
# Create your views here.
def indexView(request):
    return  render(request,'task/index.html')
