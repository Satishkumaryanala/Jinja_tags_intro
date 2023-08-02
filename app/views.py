from django.shortcuts import render

# Create your views here.

def data_render_loop(request):
    d={'name':'satish kumar', 'age':20, 'hobbies':['badminton','volleybal','listeninig music']}
    return render(request,'data_render_loop.html',context=d)

def urlnavigation(request):
    d={'name':'Satish kumar'}
    return render(request,'urlnavigation.html',context=d)