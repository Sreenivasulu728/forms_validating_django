from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *
def studentform(request):
    SFO=student()
    d={'SFO':SFO}
    if request.method=='POST':
        FD=student(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    return render(request,'validating.html',d)