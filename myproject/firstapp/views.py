from django.shortcuts import render,get_object_or_404, get_list_or_404
from .models import Person
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage



def index(request):
    data=Person.objects.all()
    return render(request,'index.html',{'data':data})

def display(request):
        name=request.POST.get('t1')
        email=request.POST.get('t2')
        obj=Person(name=name,email=email)
        obj.save()
        return HttpResponseRedirect('/index')

def delete(request,pid=0):
    id = get_object_or_404(Person,pk=pid)
    obj = id.delete()
    return HttpResponseRedirect('/index')

def update_now(request,pid=0):
    id = get_object_or_404(Person,pk=pid)
    context = {
        'id':id
    }
    return render(request,'update_now.html',{'id':id})

def update(request,pid=0):
    id=Person.objects.filter(pk=pid)
    name = request.POST.get('name')
    email = request.POST.get('email')
    obj = id.update(name=name,email=email)
    return HttpResponseRedirect('/index')

