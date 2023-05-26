from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse



def student(request):
    SFO=studentform()
    d={'SFO':SFO}
    if request.method=='POST':
        FD=studentform(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))

    return render(request,'student.html',context=d)