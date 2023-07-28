from django.shortcuts import render

# Create your views here.

def jinja_tags(request):
    d={'a':1000,'b':2000}
    return render(request,'jinja_tags.html',context=d)