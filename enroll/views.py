from django.shortcuts import render,HttpResponseRedirect
from .forms import studentregistration
from .models import User
# Create your views here.

def add_show (request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm =studentregistration()
    else:
        fm = studentregistration()
    stud = User.objects.all()
    return  render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})


def delet_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = studentregistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = studentregistration(instance=pi)

    return render(request,'enroll/updatestudent.html',{'form':fm})


