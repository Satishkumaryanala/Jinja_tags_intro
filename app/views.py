from django.shortcuts import render

# Create your views here.

def data_render(request):
    d={'name':'Satish kumar', 'course':'Python'}
    return render(request,'data_render.html',context=d)